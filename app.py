from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

model = None
feature_names = ['molecular_weight', 'logp', 'h_donors', 'h_acceptors']

def generate_dataset():
    np.random.seed(42)
    n_samples = 500
    
    molecular_weight = np.random.uniform(150, 600, n_samples)
    logp = np.random.uniform(-2, 6, n_samples)
    h_donors = np.random.randint(0, 8, n_samples)
    h_acceptors = np.random.randint(0, 12, n_samples)
    
    activity = []
    for i in range(n_samples):
        score = 0
        
        if 200 <= molecular_weight[i] <= 500:
            score += 1
        if 0 <= logp[i] <= 5:
            score += 1
        if h_donors[i] <= 5:
            score += 1
        if h_acceptors[i] <= 10:
            score += 1
        
        if score >= 3:
            activity.append(1)
        else:
            activity.append(0)
    
    activity = np.array(activity)
    noise_indices = np.random.choice(n_samples, size=int(0.15 * n_samples), replace=False)
    activity[noise_indices] = 1 - activity[noise_indices]
    
    df = pd.DataFrame({
        'molecular_weight': molecular_weight,
        'logp': logp,
        'h_donors': h_donors,
        'h_acceptors': h_acceptors,
        'activity': activity
    })
    
    return df

def train_model():
    global model
    
    df = generate_dataset()
    
    X = df[feature_names]
    y = df['activity']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    print(f"Model trained successfully with accuracy: {accuracy:.2%}")
    
    return accuracy

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    global model
    
    if model is None:
        print("Model not initialized. Training model...")
        train_model()
    
    try:
        data = request.get_json()
        
        molecular_weight = float(data.get('molecular_weight', 0))
        logp = float(data.get('logp', 0))
        h_donors = int(data.get('h_donors', 0))
        h_acceptors = int(data.get('h_acceptors', 0))
        
        features = np.array([[molecular_weight, logp, h_donors, h_acceptors]])
        
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]
        
        result = "Active Drug" if prediction == 1 else "Inactive Drug"
        confidence = max(probability) * 100
        
        return jsonify({
            'success': True,
            'prediction': result,
            'confidence': f"{confidence:.1f}%"
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    print("Training the drug discovery prediction model...")
    train_model()
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
