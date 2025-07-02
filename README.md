## End-to-End Modular ML Pipeline for Detecting Phishing Websites
This project aims to build a scalable and modular Machine Learning pipeline to detect phishing websites based on network and URL features. The pipeline follows a clean modular structure using component-based architecture for each stage of the ML lifecycle — from ingestion to deployment.

The goal is to enable production-ready deployment of phishing detection as an API service, leveraging FastAPI, Docker, Cloud deployment, and CI/CD workflows via GitHub Actions.


## Core Dependencies
```
python-dotenv~=1.1.1
pandas~=2.3.0
numpy~=2.3.1
pymongo~=4.13.2
pymongo[srv]==3.12
certifi~=2025.6.15
setuptools~=80.9.0
NetworkSecurity~=0.0.1
scikit-learn~=1.7.0
dill
pyyaml
scipy~=1.16.0
```

## Deployment Stack

| Tool                         | Purpose                                   |
| ---------------------------- | ----------------------------------------- |
| **FastAPI**                  | Serve the ML model via REST API           |
| **Uvicorn**                  | ASGI server for high-performance serving  |
| **Docker**                   | Containerize the entire project           |
| **GitHub Actions**           | Automate CI/CD for testing and deployment |
| **Cloud (e.g., AWS/Render)** | Host the API securely and scalably        |
