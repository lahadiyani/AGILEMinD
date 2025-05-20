# 📌 Core Goals & Design Principles for Each Folder (`app/`)

Panduan tujuan utama dan prinsip desain untuk setiap folder di dalam `app/` agar pengembangan AI Agent modular, mudah, dan terukur.

---

## agents/
**Goal:**  
Menyediakan sistem agent yang modular, extensible, dan mudah diregistrasi.  
- Setiap agent harus dapat diinisialisasi, dijalankan, dan dihubungkan dengan LLM, memory, dan tools.
- Mendukung registry, validasi, dan pipeline multi-agent.

---

## chains/
**Goal:**  
Mendukung pembuatan workflow/logic berantai (chain) yang fleksibel.  
- Chain dapat mengorkestrasi satu atau lebih agent.
- Mendukung hooks, monitoring, registry, dan builder untuk custom workflow.

---

## llms/
**Goal:**  
Abstraksi dan integrasi berbagai Large Language Model (LLM) secara seragam.  
- Semua LLM (OpenAI, Pollinations, dsb) harus memiliki interface yang konsisten (`generate`, `generate_image`).
- Mudah menambah/registrasi LLM baru.

---

## memory/
**Goal:**  
Menyediakan backend memory (vector store) yang pluggable untuk agent/chain.  
- Mendukung FAISS, Elasticsearch, Chroma, dsb.
- Mudah switching backend via config/env.

---

## monitoring/
**Goal:**  
Logging, monitoring, dan audit trail untuk semua aktivitas agent/chain.  
- Mendukung log per agent/chain, log cleaner, dan integrasi monitoring eksternal.

---

## loaders/
**Goal:**  
Loader dokumen modular untuk berbagai format (PDF, txt, dsb).  
- Loader harus mudah diregistrasi dan digunakan di pipeline agent/chain.
- Mendukung validasi dan logging.

---

## tools/
**Goal:**  
Integrasi API eksternal dan utilitas (misal: Pollinations, search, dsb) sebagai "alat" yang bisa dipakai agent/chain.  
- Mudah menambah tool baru dan menghubungkannya ke agent.

---

## controllers/
**Goal:**  
Mengatur logic request/response antara frontend, API, dan core logic agent/chain.  
- Bersih, terpisah dari logic agent/chain.

---

## routes/
**Goal:**  
Routing API dan web, terstruktur dan mudah dikembangkan.  
- Mendukung RESTful API dan endpoint modular.

---

## templates/
**Goal:**  
Template HTML untuk UI, mudah dikustomisasi dan terintegrasi dengan backend.

---

## static/
**Goal:**  
Resource statis (CSS, JS, assets) untuk UI/UX yang modern dan responsif.

---

## extension.py
**Goal:**  
Inisialisasi ekstensi Flask (SQLAlchemy, Migrate, dsb) secara terpusat.

---

## Prinsip Umum
- **Modular:** Setiap komponen bisa dikembangkan/ditukar tanpa mengubah core lain.
- **Extensible:** Mudah menambah agent, chain, llm, memory, loader, dsb.
- **Configurable:** Semua backend dan parameter utama bisa diatur via config/env.
- **Testable:** Setiap modul mudah di-test secara terpisah.
- **Logging:** Semua aksi penting terekam untuk debugging dan audit.

---
