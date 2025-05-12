# AGILEMinD - AI Agent Framework Starter

![logo](app/static/assets/icon.jpg)

**AGILEMinD** adalah starter framework modular yang bisa anda customisasi untuk membangun dan menjalankan AI Agents (seperti `Researcher`, `Planner`, dan `Coder`) berbasis Python, Flask, dan LangChain. Cocok untuk membangun prototype AGI atau AI tooling dengan sistem orchestrator, memory, tools, dan vectorstore.

---

## 🚀 Fitur Utama

- ✅ Application Factory Pattern (Flask)
- ✅ Modular AI Agents Setiap agent bisa dikembangkan terpisah dan digabung dengan orchestrator.
- ✅ Prompt Engineering Friendly Prompt disimpan dalam template file, mudah dikustomisasi.
- ✅ Terintegrasi dengan LangChain
- ✅ Dukungan FAISS & ElasticSearch untuk vector database
- ✅ MySQL untuk structured relational data
- ✅ UI Web ringan (HTML, CSS, JS native)
- ✅ Siap untuk CI/CD & containerization (Docker)

---

## 🔧 Requirements

Install terlebih dahulu:

- Python 3.10+
- MySQL Server (local or Docker)
- ElasticSearch (v8+)
- FAISS (via `faiss-cpu` or `faiss-gpu`)
- Docker (optional but recommended)

---

## 📦 Instalasi

1. Clone repository:
```bash
git clone https://github.com/your-org/agilemind.git
cd agilemind
````

2. Buat virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Konfigurasikan `.env`:

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

5. Jalankan database migration (jika menggunakan SQLAlchemy):

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

6. Jalankan server:

```bash
python main.py
```

# Terminal 2 - Tailwind CLI
```bash
yarn dev:css
```

---

## 🧠 Menjalankan AI Agents

Kunjungi:

```
http://localhost:5000/
```

---

## 🐳 Jalankan via Docker

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

* [ ] Integrasi WebSocket untuk live agent feedback
* [ ] GUI interface untuk prompt & memory edit
* [ ] RAG system built-in
* [ ] Multiple memory backend switch (FAISS, Elastic)
* [ ] Auth & Role-Based Access

---

## 📄 Lisensi

MIT License

---

## 👨‍💻 Author

Framework ini saya kembangkan untuk memudahkan saya dalam membangun Semi AGI dengan alasan lainnya karena kecintaan saya terhadap kode yang modular, fleksibel, dan berkelanjutan.

## 😊 Contribute and Me
