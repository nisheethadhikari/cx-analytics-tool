# CX Analytics Tool

A secure, modular Streamlit-based tool for dynamic customer experience analytics across formats.

## ✅ Features
- Upload CSV or Excel data
- Auto-analyze SLA %, backlog, and KPI trends
- Compute weighted risk scores
- Password-protected access
- Modular, scalable codebase

## 🛠 Folder Structure
```
cx-analytics-tool/
├── src/
│   ├── app.py
│   ├── auth/
│   ├── ui/
│   ├── logic/
│   ├── data/
│   └── utils/
├── requirements.txt
├── .streamlit/
└── README.md
```

## 🚀 How to Run Locally
```bash
git clone https://github.com/YOUR_USERNAME/cx-analytics-tool.git
cd cx-analytics-tool
pip install -r requirements.txt
streamlit run src/app.py
```

## 🔒 Access Control
The app prompts for a password before loading. Update it in `src/auth/login.py`.

## 🌐 Deployment (Streamlit Cloud)
1. Push to public GitHub repo
2. Go to https://streamlit.io/cloud
3. Deploy your app using path `src/app.py`

---

**Note:** For test purposes only. Not for handling regulated or sensitive PII without securing backend and encryption.
