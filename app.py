from flask import Flask, render_template, request, jsonify
import requests
import time

app = Flask(__name__)


# --- Function: Lipinski's Rule of Five Predictor ---
def lipinski_predict(molecular_weight, logp, h_donors, h_acceptors):
    rules = {
        "Molecular Weight": molecular_weight <= 500,
        "LogP": logp <= 5,
        "Hydrogen Donors": h_donors <= 5,
        "Hydrogen Acceptors": h_acceptors <= 10
    }

    satisfied_rules = sum(rules.values())
    confidence = (satisfied_rules / 4) * 100

    if satisfied_rules >= 3:
        return "Active Drug", confidence
    else:
        return "Inactive Drug", confidence


# --- Flask Routes ---
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search_medicine():
    try:
        data = request.get_json()
        medicine_name = data.get('medicine_name', '').strip()
        
        if not medicine_name:
            return jsonify({'success': False, 'error': 'Please enter a medicine name'}), 400
        
        base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
        properties = ['MolecularWeight', 'XLogP', 'HBondDonorCount', 'HBondAcceptorCount']
        
        url = f"{base_url}/compound/name/{medicine_name}/property/{','.join(properties)}/JSON"
        
        response = requests.get(url, timeout=10)
        time.sleep(0.2)
        
        if response.status_code == 200:
            data = response.json()
            props = data['PropertyTable']['Properties'][0]
            
            return jsonify({
                'success': True,
                'data': {
                    'molecular_weight': props.get('MolecularWeight', 0),
                    'logp': props.get('XLogP', 0),
                    'h_donors': props.get('HBondDonorCount', 0),
                    'h_acceptors': props.get('HBondAcceptorCount', 0)
                }
            })
        elif response.status_code == 404:
            return jsonify({'success': False, 'error': f'Medicine "{medicine_name}" not found in database'}), 404
        else:
            return jsonify({'success': False, 'error': 'Unable to fetch data. Please try again.'}), 500
            
    except requests.exceptions.Timeout:
        return jsonify({'success': False, 'error': 'Request timed out. Please try again.'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error: {str(e)}'}), 500


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        molecular_weight = float(data.get('molecular_weight', 0))
        logp = float(data.get('logp', 0))
        h_donors = int(data.get('h_donors', 0))
        h_acceptors = int(data.get('h_acceptors', 0))

        result, confidence = lipinski_predict(molecular_weight, logp, h_donors,
                                              h_acceptors)

        return jsonify({
            'success': True,
            'prediction': result,
            'confidence': f"{confidence:.1f}%"
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    print("✅ Flask Drug Discovery App (Lipinski Rule) is starting...")
    app.run(host='0.0.0.0', port=5000, debug=True)
