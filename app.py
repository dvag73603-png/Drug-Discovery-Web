from flask import Flask, render_template, request, jsonify

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
