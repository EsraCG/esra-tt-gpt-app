# Rabobank GPT Assignment – Esra

## Use Case

An FAQ assistant that allows users to ask natural language questions related to Rabobank and get AI-generated answers using Azure GPT-4o.

- A FastAPI backend that connects to Azure OpenAI GPT-4o
- A simple HTML/JavaScript frontend that interacts with the backend
- AI integration with prompt input and real-time response
- Secure key management using a local `.env` file


## AI Integration

- Model: GPT-4o
- Provider: Azure OpenAI
- Endpoint: via RESTful API (`/ask`)
- Prompt structure: Simple one-shot prompt with system + user roles
- Local `.env` file used to store the Azure API key securely

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/esra-tt-gpt-app.git
cd esra-tt-gpt-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the project root

```
AZURE_OPENAI_KEY=your_actual_azure_key_here
```

### 5. Run the FastAPI backend

```bash
uvicorn src.api.main:app --reload --host 127.0.0.1 --port 8000
```

### 6. Open the frontend

Double-click `frontend/index.html` or open it in a browser.

---

## Folder Structure

```
project/
├── src/
│   ├── api/
│   │   └── main.py
│   ├── services/
│   │   └── ai_service.py
├── frontend/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── .env (local only, not in GitHub)
```

---

## Deployment Notes

Due to a subscription issue with the `robapplicant@outlook.com` Azure account ("no subscriptions found"), full deployment could not be completed.

However, the app is fully containerized and deployment-ready:
- `Dockerfile` included and tested locally
- Prepared for push to Azure Container Registry
- Ready to deploy via Azure Web App for Containers

---

## Improvements with More Time

- Deploy both frontend and backend to Azure (App Service + Static Web App)
- Add streaming AI responses
- Allow prompt categories (Payments, Mortgages, etc.)
- Add basic auth and rate limiting
- Improve frontend styling and user flow

---

## Submission Summary

- [x] FastAPI backend with Azure GPT-4o integration
- [x] Functional frontend (vanilla HTML/JS)
- [x] Clean code structure with modular services
- [x] Secure key handling in local `.env`
- [x] Docker-ready project
- [x] GitHub repo pushed

