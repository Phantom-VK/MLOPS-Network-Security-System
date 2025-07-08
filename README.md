# 🛡️ Phishing Website Detection

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![AWS](https://img.shields.io/badge/AWS-EC2%20|%20ECR-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-blue)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-informational)
![Dagshub](https://img.shields.io/badge/Dagshub-Remote%20Tracking-lightgrey)

## 🚀 Project: End-to-End Modular ML Pipeline for Detecting Phishing Websites

This project builds a scalable and modular machine learning pipeline to detect phishing websites based on URL and network-based features. It uses a production-grade architecture where each ML lifecycle stage is isolated and implemented as a separate component, enabling reuse, testing, and seamless CI/CD deployment to the cloud.

## [Dagshub](https://dagshub.com/Phantom-VK/MLOPS-Network-Security-System)

---

## 🔍 Problem Statement

Phishing websites are a common cyber threat. This ML system is trained on over **10,000+ website entries** and **30 extracted features** to predict if a website is **legitimate or phishing**.

---

## 🧱 Project Architecture

- **Data Ingestion**
- **Data Validation**
- **Data Transformation**
- **Model Training**
- **Model Evaluation**
- **Model Pusher**
- **API Deployment (FastAPI)**
- **CI/CD via GitHub Actions to AWS EC2**

---

## 🛠️ Tech Stack

| Tool               | Purpose                                         |
| ------------------ | ----------------------------------------------- |
| **Python**         | Core programming language                       |
| **Pandas/Numpy**   | Data preprocessing                              |
| **Scikit-learn**   | ML models and evaluation metrics                |
| **FastAPI**        | Serve model as REST API                         |
| **Docker**         | Containerization                                |
| **GitHub Actions** | CI/CD pipeline for build/test/deploy automation |
| **AWS EC2 & ECR**  | Hosting and container registry                  |
| **MLflow**         | Experiment tracking                             |
| **Dagshub**        | Remote tracking (optional)                      |

---

## ⚙️ Core Libraries

```
python-dotenv, pandas, numpy, scikit-learn, dill, pyyaml, fastapi,
uvicorn, pymongo, mlflow, dagshub, certifi, setuptools, scipy
```

---

## 🧠 Dataset Overview

- **Rows:** 10,000+
- **Target:** `Result` (1 = phishing, -1 = legitimate)
- **Columns:** 30 engineered network/URL features

| Feature Examples    | Type    |
| ------------------- | ------- |
| `having_IP_Address` | Numeric |
| `URL_Length`        | Numeric |
| `SSLfinal_State`    | Numeric |
| `Page_Rank`         | Numeric |
| `Abnormal_URL`      | Numeric |
| `Google_Index`      | Numeric |

---

## 🔁 CI/CD Pipeline (GitHub Actions)

- **CI Stage**: Code linting, Unit testing
- **CD Stage**: Docker image build ➝ Push to ECR ➝ Deploy on EC2 via self-hosted runner
- **Auto Deploy**: Every push to `main` triggers full deployment

---

## 🌐 API Access

Once deployed, the FastAPI app is accessible at:

```
http://<EC2-Public-IP>:8080/docs
```

Use `/predict` endpoint to make POST requests with website features.
Use `/train` endpoint to run the pipeline.

---

## 📁 Folder Structure (Simplified)

```
📦 MLOPS-Network-Security-System
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── setup.py
├── README.md
├── .github/
│   └── workflows/
│       └── main.yml
├── networksecurity/
│   ├── __init__.py
│   ├── cloud/
│   │   └── s3_syncer.py
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── constant/
│   ├── entity/
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── batch_prediction.py
│   └── utils/
│       ├── file_utils/
│       └── ml_utils/
├── data_schema/
├── prediction_output/
├── final_model/
├── notebooks/
├── templates/
├── valid_data/
├── temp_network_data/
├── Artifacts/
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   └── model_trainer/

```

---

## 📦 Deployment Notes

- Project is containerized with **Docker**
- **ECR** is used as container registry
- GitHub Actions runner on EC2 handles deployment
- ML model tracked with **MLflow** (local or remote)

---

## 👨‍💻 Author

**Vikramaditya** — Final Year IT Student passionate about Computers and Programming.
This project is a part of my ML studies and course by Krish Naik Sir.

---
