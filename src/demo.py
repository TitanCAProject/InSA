import joblib
import os

model_dir = "Path/To/Your/Model/Directory" 
model_path = os.path.join(model_dir, "baseSeverity.joblib")
vectorizer_path = os.path.join(model_dir, "baseSeverity_vectorizer.joblib")
label_encoder_path = os.path.join(model_dir, "baseSeverity_label_encoder.joblib")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)
label_encoder = joblib.load(label_encoder_path)

example_code = """
void example_function() {
    char buffer[10];
    gets(buffer);  // Unsafe function
}
"""

X_example = vectorizer.transform([example_code])

y_pred = model.predict(X_example)

predicted_label = label_encoder.inverse_transform(y_pred)

print("Prediction: ", predicted_label[0])
