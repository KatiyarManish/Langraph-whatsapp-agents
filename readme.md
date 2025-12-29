# 🚀 LangGraph Watcher – Multi-Agent Automation with WhatsApp Alerts

A **production-style LangGraph multi-agent system** that automatically monitors:

- LangChain blogs  
- LangGraph GitHub releases  

and sends **real-time WhatsApp notifications** when something new is published.

Built step-by-step using **LangGraph, Python, GitHub Actions, and Twilio**, with proper state handling, diffing, and optional LLM summarization.

---

## ✨ Features

- 🧠 **Multi-agent LangGraph workflow**
- 🔍 Detects **new blogs / releases** (no duplicates)
- 💾 Persistent memory using SQLite
- 📱 WhatsApp notifications (FREE Twilio sandbox)
- 🔐 Secure secrets via `.env` and GitHub Secrets
- ⏰ Auto-run every 6 hours using GitHub Actions
- 🧩 Clean, modular, production-style codebase

---

## 🏗️ Architecture

Fetch Agent
↓
Diff Agent (DB check)
↓
Classifier Agent
↓
Notify Agent (WhatsApp)

yaml
Copy code

Each step is an **independent LangGraph node (agent)**.

---

## 📁 Project Structure

langgraph-watcher/
│
├── agents/
│ ├── fetch_agent.py # Fetch blogs & releases
│ ├── diff_agent.py # Detect new items
│ ├── classify_agent.py # Blog / Release tagging
│ └── notify_agent.py # WhatsApp notification
│
├── db.py # SQLite state management
├── graph.py # LangGraph definition
├── main.py # Entry point
├── requirements.txt
├── .env # (ignored, local only)
├── tracker.db # (auto-created, ignored)
└── .github/
└── workflows/
└── langgraph-watcher.yml

yaml
Copy code

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **LangGraph**
- **Requests + BeautifulSoup**
- **SQLite**
- **Twilio WhatsApp Sandbox**
- **GitHub Actions (FREE automation)**

---

## 🧪 Local Setup (Step-by-Step)

### 1️⃣ Clone the repo

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2️⃣ Create virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Create .env file (local only)
env
Copy code
TWILIO_SID=ACxxxxxxxxxxxxxxxx
TWILIO_AUTH=xxxxxxxxxxxxxxxx
TO_WHATSAPP=whatsapp:+91XXXXXXXXXX
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxx
⚠️ .env is ignored via .gitignore

5️⃣ Run locally
bash
Copy code
python main.py
📱 WhatsApp message will be sent only if a new update is detected.

📱 WhatsApp Setup (FREE)
This project uses Twilio WhatsApp Sandbox (no money, no card).

Steps:
Create account: https://www.twilio.com/try-twilio

Enable WhatsApp Sandbox

Send join <sandbox-code> to +1 415 523 8886

Copy Account SID & Auth Token

That’s it 🎉

⏰ GitHub Actions (Auto-Run)
The workflow runs:

⏱️ Every 6 hours automatically

▶️ Or manually via Run workflow

Secrets required (Repo → Settings → Secrets → Actions):
Secret Name	Description
TWILIO_SID	Twilio Account SID
TWILIO_AUTH	Twilio Auth Token
TO_WHATSAPP	Your WhatsApp number
GITHUB_TOKEN	GitHub Personal Access Token

🔐 Security
.env, tracker.db, venv/ are ignored

Secrets are stored securely in GitHub Actions

No credentials are committed to the repo

🚀 Example WhatsApp Alert
makefile
Copy code
🚀 Release New Update

Title: LangGraph v0.x
Source: LangGraph Release

Link:
https://github.com/langchain-ai/langgraph/releases/...
📌 Why This Project Matters
This is not a simple script.

It demonstrates:

Agentic architecture

State & memory handling

API auth & rate-limit safety

Real-world notification automation

Cloud scheduling (CI/CD style)

Perfect for:

Resume

Portfolio

Client demo

Learning LangGraph deeply

🛠️ Future Improvements
🧠 LLM summarizer agent (local / OpenAI)

⚠️ Breaking-change detector

📊 Streamlit dashboard

🔌 MCP tool integration

📦 Vector DB for historical analysis

❤️ Credits
Built with curiosity, debugging, and zero paid tools.
Inspired by real-world agentic AI workflows.

📜 License
MIT License – use, learn, modify freely.

yaml
Copy code

---

### ✅ Git Push
1️⃣ `README.md` file banao  
2️⃣ Ye content paste karo  
3️⃣ `git add README.md`
4️⃣ `git commit -m "Add project README"`
5️⃣ `git push`

---