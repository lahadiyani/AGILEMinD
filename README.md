# AGILEMinD - AI Agent Framework Starter

![logo](app/static/assets/icon.jpg)

**AGILEMinD** is a modular starter framework that you can customize to build and run AI Agents (such as `Researcher`, `Planner`, and `Coder`) based on Python, Flask, and LangChain. Perfect for building AGI prototypes or AI tooling with orchestrator, memory, tools, and vectorstore systems.

---

## 🚀 Key Features

- ✅ Application Factory Pattern (Flask)
- ✅ Modular AI Agents Each agent can be developed separately and combined with the orchestrator.
- ✅ Prompt Engineering Friendly Prompts are stored in template files, easy to customize.
- ✅ Integrated with LangChain
- ✅ FAISS & ElasticSearch support for vector database
- ✅ MySQL for structured relational data
- ✅ Lightweight Web UI (HTML, CSS, native JS)
- ✅ Ready for CI/CD & containerization (Docker)

---

## 🔧 Requirements

Install first:

- Python 3.10+
- MySQL Server (local or Docker)
- ElasticSearch (v8+)
- FAISS (via `faiss-cpu` or `faiss-gpu`)
- Docker (optional but recommended)

---

## 📦 Installation

1. Clone repository:
```bash
git clone https://github.com/lahadiyani/AGILEMinD.git
cd AGILEMinD
```

2. Create virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure `.env`:

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

5. Run database migration (if using SQLAlchemy):

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

6. Run server:

```bash
yarn install
yarn run start
```

---

## 🧠 Running AI Agents

Visit:

```
http://localhost:5000/
```

---

## 🐳 Run via Docker

```bash
docker-compose up --build
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📌 Roadmap (TODO)

* [ ] WebSocket integration for live agent feedback
* [ ] GUI interface for prompt & memory editing
* [ ] Built-in RAG system
* [ ] Multiple memory backend switch (FAISS, Elastic)
* [ ] Auth & Role-Based Access

---

## How To Create AGI with AGILEMinD

[Tutorial bahasa indonesia](documentation/tutorial.md)
[English Tutorial](documentation/tutorial_eng.md)

---

## 📄 License

MIT License

---

## 👨‍💻 Author

I developed this framework to make it easier for me to build Semi AGI, driven by my passion for modular, flexible, and sustainable code.

## �� Contribute and Me
