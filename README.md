---
title: Kidney Guard AI
emoji: 🛡️
colorFrom: indigo
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---

# 🏥 Kidney Guard AI: Deep Learning CT Scan Classifier

Kidney Guard AI is a professional medical imaging application designed for the automated classification of kidney CT scans. This project demonstrates a production-grade machine learning pipeline, from experimentation to containerized deployment.

## 🚀 Key Features
*   **Automated Classification**: High-accuracy detection of **Normal** vs. **Tumor** states.
*   **Production Pipeline**: Implements a modular architecture with data ingestion, model preparation, training, and evaluation.
*   **Seamless Monitoring**: Integrated with **MLflow** and **DagsHub** for experiment tracking and version control.
*   **Premium Web Dashboard**: A user-friendly, responsive interface for instant diagnostic feedback.
*   **Cloud Deployment**: Hosted on **Hugging Face Spaces** using **Docker**.

## 🛠️ Technology Stack & Tools
*   **Deep Learning**: TensorFlow, Keras (VGG16 Architecture)
*   **API Framework**: FastAPI
*   **Containerization**: Docker
*   **Experiment Tracking**: [MLflow](https://mlflow.org/) (Hosted on DagsHub)
*   **Data/Model Versioning**: [DVC](https://dvc.org/) (Data Version Control)
*   **Project Management**: [DagsHub](https://dagshub.com/)
*   **Deployment**: Hugging Face Spaces

## 📈 Experiment Tracking (MLflow + DagsHub)
This project uses **MLflow** to track metrics, parameters, and models. All experiments are logged remotely to **DagsHub**, providing a centralized dashboard for performance analysis.
- **Tracking URI**: `https://dagshub.com/Rahii123/Kidney_disease_classification.mlflow`
- **DVC Integration**: Large datasets and model artifacts are managed via DVC and stored on DagsHub's remote storage.

## 📋 Pipeline Workflow (Modular Approach)
1.  **Data Ingestion**: Automated data downloading and extraction.
2.  **Prepare Base Model**: Initialization and modification of the VGG16 architecture.
3.  **Model Training**: Training the model with data augmentation and checkpointing.
4.  **Model Evaluation**: Performance analysis and remote logging to MLflow.

## 💻 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rahii123/Kidney_disease_classification.git
   cd Kidney_disease_classification
   ```

2. **Setup environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   # Or using uvicorn
   uvicorn app:app --reload
   ```

---
**Author**: Raheel Nadeem
**Contact**: rahiiiraja123@gmail.com
**DagsHub Repository**: [View Project on DagsHub](https://dagshub.com/Rahii123/Kidney_disease_classification)
