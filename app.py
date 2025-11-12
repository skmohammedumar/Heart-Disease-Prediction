from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, template_folder='templates')

# Load all models + scaler
with open("all_models.pkl", "rb") as f:
    models = pickle.load(f)

scaler = models["scaler"]

# Models that require scaling
scale_required = ["KNN", "LogisticRegression", "SVM"]

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form["age"]),
            float(request.form["sex"]),
            float(request.form["cp"]),
            float(request.form["trestbps"]),
            float(request.form["chol"]),
            float(request.form["fbs"]),
            float(request.form["restecg"]),
            float(request.form["thalach"]),
            float(request.form["exang"]),
            float(request.form["oldpeak"]),
            float(request.form["slope"]),
            float(request.form["ca"]),
            float(request.form["thal"])
        ]

        final_features = np.array(features).reshape(1, -1)

        selected_model = request.form["model_select"]
        model = models[selected_model]

        if selected_model in scale_required:
            final_features = scaler.transform(final_features)

        pred = model.predict(final_features)[0]

        result = "Heart Disease Detected" if pred == 1 else "No Heart Disease"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)
