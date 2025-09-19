# ⚡ ZapStore

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/) ![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat&logo=fastapi) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) [![GitHub issues](https://img.shields.io/github/issues/ritesh-tiwary/zap-store)](https://github.com/ritesh-tiwary/zap-store/issues) [![GitHub stars](https://img.shields.io/github/stars/ritesh-tiwary/zap-store)](https://github.com/ritesh-tiwary/zap-store/stargazers)

Blazing-fast, flexible Firestore APIs powered by FastAPI. **ZapStore** allows you to create, fetch, and manage documents in any Firestore collection — **no fixed schema** required.

---

## 🔥 Features

* ⚡ **FastAPI**-based backend for rapid API development
* 📦 Dynamic collections with flexible document structure
* 🔑 Google **Firestore** integration (serverless NoSQL database)
* 🌍 Cloud-ready and container-friendly
* 🛠️ Lightweight, simple, and open-source

---

## 🚀 Quickstart

### 1️⃣ Clone the repo

```bash
git clone https://github.com/ritesh-tiwary/zap-store.git
cd zap-store
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Firestore credentials

**Option 1: JSON file**

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"
```

**Option 2: JSON content in `.env`**

```ini
GOOGLE_APPLICATION_CREDENTIALS_JSON='{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "xxxxxx",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "your-service-account@project.iam.gserviceaccount.com",
  "client_id": "xxxxxx",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/..."
}'
```

### 4️⃣ Run the app

```bash
uvicorn main:app --reload
```

---

## 🛠️ API Endpoints

### Create a document in a collection

```http
POST /collections/{collection_name}
```

**Body:** JSON representing the document (dynamic schema) \
**Response:**

```json
{
  "message": "Document created successfully",
  "id": "<doc_id>"
}
```

### Fetch all documents from a collection

```http
GET /collections/{collection_name}
```

**Response:**

```json
{
  "count": 2,
  "items": [
    {"id": "abc123", "username": "ritesh", "role": "admin"},
    {"id": "def456", "username": "alice", "role": "user"}
  ]
}
```

---

## 💡 Example Usage

**Create a user document**

```bash
curl -X POST "http://127.0.0.1:8000/collections/users" \
  -H "Content-Type: application/json" \
  -d '{"username":"ritesh","role":"admin"}'
```

**Fetch all users**

```bash
curl "http://127.0.0.1:8000/collections/users"
```

---

## 🏗️ Project Structure

```css
zap-store/
 ├── main.py
 ├── requirements.txt
 ├── Dockerfile
 ├── .gitignore
 ├── README.md
 └── LICENSE
```

---

## ☁️ Deploy to the Cloud

```bash
curl -fsSL https://railway.com/install.sh | sh
echo "export RAILWAY_TOKEN=your_token" >> ~/.bashrc
source ~/.bashrc

railway login --browserless
railway whoami   # check current user
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Please follow the [GitHub flow](https://guides.github.com/introduction/flow/) when submitting PRs.

---

## 📜 License
MIT **[License](LICENSE)** © 2025 – Made with ❤️ by the **⚡ ZapStore** community.
