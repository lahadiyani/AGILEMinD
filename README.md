# AGILEMinD - Starter Framework AI Agent

![logo](app/static/assets/icon.jpg)

**AGILEMinD** adalah sebuah framework starter modular yang bisa kamu kustomisasi untuk membangun dan menjalankan AI Agent (seperti `Researcher`, `Planner`, dan `Coder`) berbasis Python, Flask, dan LangChain. Cocok untuk membangun prototipe AGI atau alat bantu AI dengan sistem orchestrator, memory, tools, dan vectorstore.

---

## 🚀 Fitur Unggulan

* ✅ Menggunakan Application Factory Pattern (Flask)
* ✅ AI Agent Modular Setiap agent bisa dikembangkan secara terpisah dan dikombinasikan melalui orchestrator.
* ✅ Mendukung Prompt Engineering Prompt disimpan dalam file template, mudah disesuaikan.
* ✅ Terintegrasi dengan LangChain
* ✅ Mendukung FAISS & ElasticSearch untuk vector database
* ✅ MySQL untuk data relasional terstruktur
* ✅ Custom (HTML, CSS, JavaScript native)
* ✅ Siap untuk CI/CD & containerization (Docker)

---

## 🔧 Persyaratan

Install terlebih dahulu:

* Python 3.10+
* MySQL Server (lokal atau via Docker)
* ElasticSearch (versi 8 ke atas)
* FAISS (`faiss-cpu` atau `faiss-gpu`)
* Docker (opsional namun direkomendasikan)

---

## 📦 Instalasi

1. Clone repository:

```bash
git clone https://github.com/lahadiyani/AGILEMinD.git
cd AGILEMinD
```

2. Buat virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # atau .\.venv\Scripts\Activate untuk Windows
```

3. Pesiapan Sebelum Menginstall module

jika anda menggunakan sistem operasi linux pastikan `mariadb-connector-c-devel` dan `pkg-config` sudah terinstall pada komputer anda, jika belum anda bisa menginstallnya terlebih dahulu.

untuk RedHat, Fedora


```sh
sudo dnf install mysql-devel mariadb-connector-c-devel pkg-config
```

untuk debian dan turunan nya (ubuntu, mint, xubuntu)

```sh
sudo apt update
sudo apt install mysql-devel python3-dev default-libmysqlclient-dev build-essential pkg-config
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Konfigurasi `.env`:

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

6. Jalankan migrasi database (jika menggunakan SQLAlchemy):

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

7. Jalankan server:

```bash
yarn install
yarn run start
```

---

## 🧠 Menjalankan AI Agent

Buka:

```
http://localhost:5000/
```

---

## 🐳 Jalankan via Docker

```bash
docker-compose up --build
```

---

## 🧪 Pengujian

```bash
pytest tests/
```

---

## 📌 Roadmap (Rencana Pengembangan)

* [ ] Integrasi WebSocket untuk feedback agent secara real-time
* [ ] Sistem RAG bawaan
* [ ] Dukungan multiple backend memory (FAISS, Elastic)

---

## Cara Membangun AGI dengan AGILEMinD

[Tutorial bahasa Indonesia](documentation/tutorial.md)
[Tutorial dalam Bahasa Inggris](documentation/tutorial_eng.md)

---

## 📄 Lisensi

Lisensi MIT

---

## 👨‍💻 Pengembang

Saya mengembangkan framework ini untuk mempermudah proses membangun Semi AGI, didorong oleh semangat untuk menulis kode yang modular, fleksibel, dan berkelanjutan.

## 🤝 Kontribusi dan Kontak

Email: [lahadiyani@gmail.com](mailto:lahadiyani@gmail.com)
