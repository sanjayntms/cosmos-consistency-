
# 🌍 Azure Cosmos DB Consistency Demo (Flask + Python)

This project demonstrates different **consistency models** in Azure Cosmos DB using a Python Flask web interface. It allows you to choose a consistency level (Strong, Bounded Staleness, Session, Consistent Prefix, Eventual) and interact with Cosmos DB accordingly.

---

## 🚀 Features

- Web UI to read/write messages to Cosmos DB
- Select consistency level dynamically
- Multi-region Cosmos DB support
- One-click deploy to Azure VM via GitHub Actions
- GitHub Secrets for secure credential handling

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py               # Flask application
│   ├── cosmos_client.py      # Cosmos DB logic
│   └── templates/
│       └── index.html        # HTML UI
├── requirements.txt          # Python dependencies
├── .github/
│   └── workflows/
│       └── deploy-vm.yml     # Azure VM deploy workflow
└── README.md
```

---

## 🧪 Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set environment variables

Create a `.env` file inside the `app/` directory:

```env
COSMOS_ENDPOINT=your_cosmos_db_endpoint
COSMOS_KEY=your_cosmos_db_key
COSMOS_DB=consistency-demo-db
COSMOS_CONTAINER=messages
```

### 3. Start the app

```bash
cd app
python main.py
```

Open your browser at [http://localhost:5000](http://localhost:5000)

---

## ☁️ Deploy to Azure VM with GitHub Actions

### 🔐 Required GitHub Secrets

Go to **Repo → Settings → Secrets → Actions**, and add:

| Secret Name         | Description                           |
|---------------------|---------------------------------------|
| `AZURE_CREDENTIALS` | Output from `az ad sp create-for-rbac` |
| `VM_PASSWORD`       | Admin password for Azure VM login     |
| `COSMOS_ENDPOINT`   | Azure Cosmos DB endpoint URI          |
| `COSMOS_KEY`        | Cosmos DB access key                  |

---

### ▶️ Run Deployment

Go to the **Actions** tab on GitHub → Select `Deploy Flask Cosmos App to Azure VM` → Click **Run workflow**.

When done, the app will be available at:

```
http://<vm-public-ip>:5000
```

Port 5000 is opened automatically in the workflow.

---

## 🧹 Cleanup Azure Resources

To remove the deployed VM and resource group:

```bash
az group delete --name cosmos-consistency-rg --yes --no-wait
```

---

## 📄 License

MIT License
