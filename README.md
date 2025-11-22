# CX Analytics Tool

This is a modular, secure, and extensible CX analytics platform. Upload case/ticket data and receive metrics, risks, and insights in real time.

## Run Locally
```bash
pip install -r requirements.txt
streamlit run src/app.py
```

## Build & Run with Docker
```bash
docker build -t cx-analytics .
docker run -p 8501:8501 cx-analytics
```