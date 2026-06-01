# ModelMentor ML

A lightweight Flask-based machine learning utility project for tabular data analysis and preprocessing. The project provides REST APIs for dataset summarization, outlier detection, and reusable preprocessing pipelines using Pandas and Scikit-learn.

## Features

* Flask-based backend architecture
* REST API endpoints for ML utilities
* Dataset statistical summary generation
* IQR-based outlier detection
* Scikit-learn preprocessing pipeline support
* Modular project structure
* Easy local setup and deployment

---

# Tech Stack

* **Backend:** Python, Flask
* **Data Processing:** Pandas, NumPy
* **Machine Learning Utilities:** Scikit-learn
* **Frontend:** HTML, CSS, JavaScript

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/modelmentor_ml.git
cd modelmentor_ml
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Project

Start the Flask development server:

```bash
python run.py
```

Server will run at:

```bash
http://127.0.0.1:5000/
```

## Dataset Summary

Generate statistical summary of tabular data.

### Endpoint

```http
POST /api/ml/describe
```

### Request Body

```json
{
  "records": [
    {
      "age": 22,
      "salary": 45000
    },
    {
      "age": 25,
      "salary": 52000
    }
  ]
}
```

### Features

* Row and column count
* Data types
* Missing value percentage
* Statistical summary

---

## Outlier Detection (IQR Method)

Detect outliers using the Interquartile Range method.

### Endpoint

```http
POST /api/ml/outliers-iqr
```

### Request Body

```json
{
  "records": [
    {
      "salary": 45000
    },
    {
      "salary": 1000000
    }
  ],
  "column": "salary"
}
```

### Response

```json
{
  "column": "salary",
  "outlier_row_indices": [1]
}
```

---

# Machine Learning Utilities

The `tabular.py` module includes reusable ML preprocessing helpers:

* DataFrame conversion
* Dataset description generation
* IQR-based outlier detection
* Scikit-learn preprocessing pipeline creation

### Example Pipeline Features

* Missing value imputation
* Feature scaling
* One-hot encoding for categorical variables

---

# Future Improvements

* Model training API
* CSV file upload support
* Data visualization dashboard
* Feature engineering utilities
* Authentication system
* Deployment using Docker

---

# Requirements

```txt
flask>=3.0.0
pandas>=2.2.0
numpy>=1.26.0
scikit-learn>=1.4.0
```

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# License

This project is open-source and available under the MIT License.

---

# Author

Developed as part of a machine learning and Flask-based web application project.


### Netlify Link

link : model-mentor-ml.netlify.app
