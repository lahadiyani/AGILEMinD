Berikut terjemahan ke dalam Bahasa Inggris dengan gaya dokumentasi proyek yang profesional:

---

# AGILEMinD - Starter Framework for AI Agents

![logo](../app/static/assets/icon.jpg)

**AGILEMinD** is a modular starter framework that you can customize to build and run AI Agents (such as `Researcher`, `Planner`, and `Coder`) based on Python, Flask, and LangChain. Ideal for building AGI prototypes or AI-powered assistant tools with orchestrator systems, memory, tools, and vectorstore integrations.

---

## 🚀 Key Features

* ✅ Utilizes the Application Factory Pattern (Flask)
* ✅ Modular AI Agent – Each agent can be developed independently and integrated via the orchestrator
* ✅ Supports Prompt Engineering – Prompts are stored in templates for easy customization
* ✅ Integrated with LangChain
* ✅ Supports FAISS & ElasticSearch as vector databases
* ✅ MySQL for structured relational data
* ✅ Custom UI (HTML, CSS, native JavaScript)
* ✅ Ready for CI/CD & containerization (Docker)

---

## 🔧 Requirements

Ensure the following are installed:

* Python 3.10+
* MySQL Server (local or via Docker)
* ElasticSearch (version 8 or above)
* FAISS (`faiss-cpu` or `faiss-gpu`)
* Docker (optional but recommended)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/lahadiyani/AGILEMinD.git
cd AGILEMinD
```

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\Activate on Windows
```

3. Pre-installation Setup

If you're using Linux, make sure `mariadb-connector-c-devel` and `pkg-config` are installed. If not, install them first.

For RedHat or Fedora:

```sh
sudo dnf install mysql-devel mariadb-connector-c-devel pkg-config
```

For Debian-based systems (Ubuntu, Mint, Xubuntu):

```sh
sudo apt update
sudo apt install mysql-devel python3-dev default-libmysqlclient-dev build-essential pkg-config
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Configure `.env`:

```env
FLASK_APP=main.py
FLASK_ENV=development
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_NAME=ai_agent_db
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/ai_agent_db
ELASTICSEARCH_HOST=http://localhost:9200
OPENAI_API_KEY=your-openai-api-key
```

6. Run database migration (if using SQLAlchemy):

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

7. Start the server:

```bash
yarn install
yarn run start
```

---

## 🧠 Running the AI Agent

Open:

```
http://localhost:5000/
```

---

## 🐳 Running via Docker

```bash
docker-compose up --build
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📌 Roadmap

* [ ] WebSocket integration for real-time agent feedback
* [ ] Built-in RAG system
* [ ] Support for multiple memory backends (FAISS, Elastic)

---

## How to Build AGI with AGILEMinD

[Indonesian Tutorial](documentation/tutorial.md)
[English Tutorial](documentation/tutorial_eng.md)

---

## 📄 License

MIT License

---

## 👨‍💻 Developer

I developed this framework to simplify the process of building semi-AGI systems, driven by a passion for writing modular, flexible, and maintainable code.

## 🤝 Contributions & Contact

Email: [lahadiyani@gmail.com](mailto:lahadiyani@gmail.com)