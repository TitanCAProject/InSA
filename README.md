#### 1. Tool Information

* **Tool Name:** InSA
* **Repository / URL:** [InSA](https://github.com/TitanCAProject/InSA)

#### 2. Authors and Contact

* **Main Author(s):** Jinfeng Jiang

#### 3. Overview

This tool uses a pre-trained machine learning model to analyze source code snippets and predict the base severity level of potential security vulnerabilities. It vectorizes code input, applies a trained classifier, and maps the prediction to a human-readable severity label using a label encoder.

#### 4. Installation

1. Ensure Python 3.8+ is installed.
2. Install required dependencies:pip install joblib scikit-learn
3. Place the following files in the same directory (or update paths accordingly):
    * baseSeverity.joblib
    * baseSeverity_vectorizer.joblib
    * baseSeverity_label_encoder.joblib
    * demo.py


#### 5. Usage

1. In `demo.py`, make sure `model_dir` points to the folder containing:
   - `baseSeverity.joblib`
   - `baseSeverity_vectorizer.joblib`
   - `baseSeverity_label_encoder.joblib`

2. Replace the `example_code` string with the **vulnerable function** (or code snippet) you want to evaluate.

3. Run the script:
```bash
python demo.py
```

The script will vectorize the provided code snippet, run the classifier, decode the predicted class label, and print the result.

#### 6. Input and Output Format

* **Input format:** A single code snippet.
* **Output format:** A single severity label printed to standard output. Possible labels: CRITICAL, HIGH, MEDIUM, LOW. 
Example output: 
```
Prediction: CRITICAL.
```
