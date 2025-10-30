from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# --- Dummy Offline Medicine Database ---
medicine_data = {
    # --- Active Medicines (70) ---
    "paracetamol": {"MolecularWeight": 151.16, "LogP": 0.91, "HBondDonorCount": 2, "HBondAcceptorCount": 3},
    "ibuprofen": {"MolecularWeight": 206.28, "LogP": 3.5, "HBondDonorCount": 1, "HBondAcceptorCount": 2},
    "amoxicillin": {"MolecularWeight": 365.4, "LogP": 1.6, "HBondDonorCount": 4, "HBondAcceptorCount": 6},
    "caffeine": {"MolecularWeight": 194.19, "LogP": -0.07, "HBondDonorCount": 0, "HBondAcceptorCount": 2},
    "aspirin": {"MolecularWeight": 180.16, "LogP": 1.2, "HBondDonorCount": 1, "HBondAcceptorCount": 3},
    "acetaminophen": {"MolecularWeight": 151.16, "LogP": 0.5, "HBondDonorCount": 2, "HBondAcceptorCount": 3},
    "cetirizine": {"MolecularWeight": 388.89, "LogP": 3.2, "HBondDonorCount": 2, "HBondAcceptorCount": 5},
    "loratadine": {"MolecularWeight": 382.89, "LogP": 4.5, "HBondDonorCount": 1, "HBondAcceptorCount": 4},
    "ranitidine": {"MolecularWeight": 314.41, "LogP": 0.9, "HBondDonorCount": 2, "HBondAcceptorCount": 5},
    "omeprazole": {"MolecularWeight": 345.42, "LogP": 2.2, "HBondDonorCount": 1, "HBondAcceptorCount": 4},
    "metformin": {"MolecularWeight": 129.16, "LogP": -1.4, "HBondDonorCount": 3, "HBondAcceptorCount": 5},
    "atenolol": {"MolecularWeight": 266.34, "LogP": 0.16, "HBondDonorCount": 3, "HBondAcceptorCount": 4},
    "amlodipine": {"MolecularWeight": 408.88, "LogP": 3.0, "HBondDonorCount": 2, "HBondAcceptorCount": 5},
    "losartan": {"MolecularWeight": 422.91, "LogP": 4.1, "HBondDonorCount": 2, "HBondAcceptorCount": 5},
    "atorvastatin": {"MolecularWeight": 558.64, "LogP": 4.1, "HBondDonorCount": 3, "HBondAcceptorCount": 6},
    "simvastatin": {"MolecularWeight": 418.57, "LogP": 4.7, "HBondDonorCount": 1, "HBondAcceptorCount": 5},
    "rosuvastatin": {"MolecularWeight": 481.54, "LogP": 2.8, "HBondDonorCount": 2, "HBondAcceptorCount": 7},
    "azithromycin": {"MolecularWeight": 748.98, "LogP": 3.1, "HBondDonorCount": 5, "HBondAcceptorCount": 14},
    "ciprofloxacin": {"MolecularWeight": 331.34, "LogP": 1.3, "HBondDonorCount": 2, "HBondAcceptorCount": 6},
    "levofloxacin": {"MolecularWeight": 361.37, "LogP": -0.4, "HBondDonorCount": 2, "HBondAcceptorCount": 6},
    "clarithromycin": {"MolecularWeight": 747.96, "LogP": 3.2, "HBondDonorCount": 3, "HBondAcceptorCount": 13},
    "erythromycin": {"MolecularWeight": 733.93, "LogP": 3.1, "HBondDonorCount": 5, "HBondAcceptorCount": 13},
    "fluconazole": {"MolecularWeight": 306.27, "LogP": 0.5, "HBondDonorCount": 1, "HBondAcceptorCount": 7},
    "ketoconazole": {"MolecularWeight": 531.43, "LogP": 4.3, "HBondDonorCount": 2, "HBondAcceptorCount": 7},
    "itraconazole": {"MolecularWeight": 705.64, "LogP": 5.7, "HBondDonorCount": 1, "HBondAcceptorCount": 8},
    "clopidogrel": {"MolecularWeight": 321.82, "LogP": 3.2, "HBondDonorCount": 0, "HBondAcceptorCount": 5},
    "metoprolol": {"MolecularWeight": 267.36, "LogP": 1.9, "HBondDonorCount": 2, "HBondAcceptorCount": 4},
    "propranolol": {"MolecularWeight": 259.34, "LogP": 3.0, "HBondDonorCount": 2, "HBondAcceptorCount": 3},
    "furosemide": {"MolecularWeight": 330.74, "LogP": 2.0, "HBondDonorCount": 2, "HBondAcceptorCount": 5},
    "spironolactone": {"MolecularWeight": 416.57, "LogP": 2.8, "HBondDonorCount": 1, "HBondAcceptorCount": 5},
    "hydrochlorothiazide": {"MolecularWeight": 297.73, "LogP": -0.1, "HBondDonorCount": 2, "HBondAcceptorCount": 8},
    "prednisone": {"MolecularWeight": 358.43, "LogP": 1.6, "HBondDonorCount": 2, "HBondAcceptorCount": 5},
    "dexamethasone": {"MolecularWeight": 392.46, "LogP": 1.8, "HBondDonorCount": 2, "HBondAcceptorCount": 6},
    "betamethasone": {"MolecularWeight": 392.46, "LogP": 1.8, "HBondDonorCount": 2, "HBondAcceptorCount": 6},
    "insulin": {"MolecularWeight": 5808, "LogP": -3.0, "HBondDonorCount": 30, "HBondAcceptorCount": 40},
    "salbutamol": {"MolecularWeight": 239.31, "LogP": 0.3, "HBondDonorCount": 3, "HBondAcceptorCount": 4},
    "montelukast": {"MolecularWeight": 586.2, "LogP": 4.2, "HBondDonorCount": 2, "HBondAcceptorCount": 7},
    "theophylline": {"MolecularWeight": 180.16, "LogP": 0.5, "HBondDonorCount": 1, "HBondAcceptorCount": 3},
    "carbamazepine": {"MolecularWeight": 236.27, "LogP": 2.5, "HBondDonorCount": 1, "HBondAcceptorCount": 2},
    "valproic_acid": {"MolecularWeight": 144.21, "LogP": 2.7, "HBondDonorCount": 1, "HBondAcceptorCount": 2},
    "lamotrigine": {"MolecularWeight": 256.09, "LogP": 1.9, "HBondDonorCount": 2, "HBondAcceptorCount": 4},
    "sertraline": {"MolecularWeight": 306.23, "LogP": 3.3, "HBondDonorCount": 1, "HBondAcceptorCount": 2},
    "fluoxetine": {"MolecularWeight": 309.33, "LogP": 4.1, "HBondDonorCount": 1, "HBondAcceptorCount": 3},
    "paroxetine": {"MolecularWeight": 329.38, "LogP": 3.2, "HBondDonorCount": 1, "HBondAcceptorCount": 4},
    "citalopram": {"MolecularWeight": 324.39, "LogP": 3.5, "HBondDonorCount": 1, "HBondAcceptorCount": 3},
    "escitalopram": {"MolecularWeight": 324.39, "LogP": 3.3, "HBondDonorCount": 1, "HBondAcceptorCount": 3},
    "venlafaxine": {"MolecularWeight": 277.4, "LogP": 3.0, "HBondDonorCount": 1, "HBondAcceptorCount": 4},
    "bupropion": {"MolecularWeight": 239.74, "LogP": 3.0, "HBondDonorCount": 0, "HBondAcceptorCount": 3},
    "tramadol": {"MolecularWeight": 263.38, "LogP": 2.4, "HBondDonorCount": 1, "HBondAcceptorCount": 3},
    "codeine": {"MolecularWeight": 299.36, "LogP": 1.2, "HBondDonorCount": 2, "HBondAcceptorCount": 4},
    "morphine": {"MolecularWeight": 285.34, "LogP": 0.9, "HBondDonorCount": 3, "HBondAcceptorCount": 6},
    "hydroxychloroquine": {"MolecularWeight": 335.87, "LogP": 3.8, "HBondDonorCount": 2, "HBondAcceptorCount": 4},
    "chloroquine": {"MolecularWeight": 319.87, "LogP": 4.2, "HBondDonorCount": 1, "HBondAcceptorCount": 3},
    "quinine": {"MolecularWeight": 324.43, "LogP": 2.9, "HBondDonorCount": 1, "HBondAcceptorCount": 5},
    "albendazole": {"MolecularWeight": 265.33, "LogP": 3.3, "HBondDonorCount": 2, "HBondAcceptorCount": 3},
    "ivermectin": {"MolecularWeight": 875.1, "LogP": 4.8, "HBondDonorCount": 5, "HBondAcceptorCount": 10},
    "artemether": {"MolecularWeight": 298.37, "LogP": 3.4, "HBondDonorCount": 0, "HBondAcceptorCount": 5},
    "lumefantrine": {"MolecularWeight": 528.9, "LogP": 5.0, "HBondDonorCount": 1, "HBondAcceptorCount": 4},
    "azathioprine": {"MolecularWeight": 277.3, "LogP": 0.5, "HBondDonorCount": 1, "HBondAcceptorCount": 5},
    "mycophenolate": {"MolecularWeight": 320.34, "LogP": 3.6, "HBondDonorCount": 2, "HBondAcceptorCount": 5},
    "cyclosporine": {"MolecularWeight": 1202.6, "LogP": 3.9, "HBondDonorCount": 12, "HBondAcceptorCount": 16},
    "tacrolimus": {"MolecularWeight": 804.0, "LogP": 3.6, "HBondDonorCount": 6, "HBondAcceptorCount": 12},
    "sirolimus": {"MolecularWeight": 914.2, "LogP": 4.0, "HBondDonorCount": 5, "HBondAcceptorCount": 12},
    "acyclovir": {"MolecularWeight": 225.2, "LogP": -1.6, "HBondDonorCount": 3, "HBondAcceptorCount": 7},
    "valacyclovir": {"MolecularWeight": 324.34, "LogP": -1.5, "HBondDonorCount": 4, "HBondAcceptorCount": 9},
    "oseltamivir": {"MolecularWeight": 312.4, "LogP": 1.2, "HBondDonorCount": 2, "HBondAcceptorCount": 6},
    "remdesivir": {"MolecularWeight": 602.6, "LogP": 3.2, "HBondDonorCount": 4, "HBondAcceptorCount": 10},

    # --- Inactive Medicines (30) ---
    "bismuth_subsalicylate": {"MolecularWeight": 362.09, "LogP": 7.2, "HBondDonorCount": 0, "HBondAcceptorCount": 3},
    "heparin": {"MolecularWeight": 15000, "LogP": -4.0, "HBondDonorCount": 20, "HBondAcceptorCount": 30},
    "vancomycin": {"MolecularWeight": 1449.3, "LogP": -3.1, "HBondDonorCount": 19, "HBondAcceptorCount": 24},
    "colistin": {"MolecularWeight": 1155.4, "LogP": 6.5, "HBondDonorCount": 10, "HBondAcceptorCount": 17},
    "amphotericin_b": {"MolecularWeight": 924.1, "LogP": 6.7, "HBondDonorCount": 7, "HBondAcceptorCount": 14},
    "interferon_alpha": {"MolecularWeight": 19000, "LogP": -5.0, "HBondDonorCount": 50, "HBondAcceptorCount": 70},
    "etanercept": {"MolecularWeight": 150000, "LogP": -6.0, "HBondDonorCount": 100, "HBondAcceptorCount": 150},
    "adalimumab": {"MolecularWeight": 148000, "LogP": -5.5, "HBondDonorCount": 98, "HBondAcceptorCount": 160},
    "trastuzumab": {"MolecularWeight": 145000, "LogP": -5.8, "HBondDonorCount": 95, "HBondAcceptorCount": 150},
    "bevacizumab": {"MolecularWeight": 149000, "LogP": -5.6, "HBondDonorCount": 100, "HBondAcceptorCount": 155},
    "rituximab": {"MolecularWeight": 143000, "LogP": -5.7, "HBondDonorCount": 90, "HBondAcceptorCount": 140},
    "insulin_glargine": {"MolecularWeight": 6063, "LogP": -3.0, "HBondDonorCount": 35, "HBondAcceptorCount": 45},
    "pegfilgrastim": {"MolecularWeight": 18800, "LogP": -4.5, "HBondDonorCount": 60, "HBondAcceptorCount": 80},
    "epoetin_alpha": {"MolecularWeight": 30400, "LogP": -4.0, "HBondDonorCount": 60, "HBondAcceptorCount": 80},
    "somatotropin": {"MolecularWeight": 22124, "LogP": -3.2, "HBondDonorCount": 40, "HBondAcceptorCount": 60},
    "filgrastim": {"MolecularWeight": 18700, "LogP": -4.3, "HBondDonorCount": 55, "HBondAcceptorCount": 75},
    "interleukin_2": {"MolecularWeight": 15500, "LogP": -3.8, "HBondDonorCount": 48, "HBondAcceptorCount": 65},
    "infliximab": {"MolecularWeight": 149000, "LogP": -5.6, "HBondDonorCount": 90, "HBondAcceptorCount": 150},
    "golimumab": {"MolecularWeight": 147000, "LogP": -5.7, "HBondDonorCount": 95, "HBondAcceptorCount": 150},
    "ustekinumab": {"MolecularWeight": 148000, "LogP": -5.5, "HBondDonorCount": 100, "HBondAcceptorCount": 155},
    "secukinumab": {"MolecularWeight": 146000, "LogP": -5.4, "HBondDonorCount": 92, "HBondAcceptorCount": 150},
    "omalizumab": {"MolecularWeight": 145000, "LogP": -5.6, "HBondDonorCount": 90, "HBondAcceptorCount": 140},
    "dupilumab": {"MolecularWeight": 147000, "LogP": -5.7, "HBondDonorCount": 100, "HBondAcceptorCount": 150},
    "ranibizumab": {"MolecularWeight": 48000, "LogP": -4.9, "HBondDonorCount": 60, "HBondAcceptorCount": 70},
    "omaline": {"MolecularWeight": 900, "LogP": 6.2, "HBondDonorCount": 9, "HBondAcceptorCount": 13},
    "protamine": {"MolecularWeight": 5100, "LogP": -3.4, "HBondDonorCount": 25, "HBondAcceptorCount": 30},
    "streptokinase": {"MolecularWeight": 47000, "LogP": -3.7, "HBondDonorCount": 50, "HBondAcceptorCount": 70},
    "alteplase": {"MolecularWeight": 59000, "LogP": -4.0, "HBondDonorCount": 60, "HBondAcceptorCount": 75},
    "tenecteplase": {"MolecularWeight": 58000, "LogP": -4.1, "HBondDonorCount": 62, "HBondAcceptorCount": 78},
    "abciximab": {"MolecularWeight": 47000, "LogP": -5.2, "HBondDonorCount": 80, "HBondAcceptorCount": 100},
    "basiliximab": {"MolecularWeight": 145000, "LogP": -5.5, "HBondDonorCount": 95, "HBondAcceptorCount": 140},
}


# --- Lipinski Rule Predictor ---
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


# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search_medicine():
    try:
        data = request.get_json()
        medicine_name = data.get('medicine_name', '').strip().lower()
        
        if not medicine_name:
            return jsonify({'success': False, 'error': 'Please enter a medicine name'}), 400

        if medicine_name in medicine_data:
            props = medicine_data[medicine_name]
            time.sleep(0.3)
            return jsonify({
                'success': True,
                'data': {
                    'molecular_weight': props['MolecularWeight'],
                    'logp': props['LogP'],
                    'h_donors': props['HBondDonorCount'],
                    'h_acceptors': props['HBondAcceptorCount']
                }
            })
        else:
            return jsonify({'success': False, 'error': f'Medicine \"{medicine_name}\" not found in local database'}), 404

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        molecular_weight = float(data.get('molecular_weight', 0))
        logp = float(data.get('logp', 0))
        h_donors = int(data.get('h_donors', 0))
        h_acceptors = int(data.get('h_acceptors', 0))

        result, confidence = lipinski_predict(molecular_weight, logp, h_donors, h_acceptors)

        return jsonify({
            'success': True,
            'prediction': result,
            'confidence': f"{confidence:.1f}%"
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    print("✅ Flask Drug Discovery App (Offline Mode) is starting...")
    app.run(host='0.0.0.0', port=5000, debug=True)
