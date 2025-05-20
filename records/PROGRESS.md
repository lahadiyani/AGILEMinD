# Progress & Notes Tracker (app/)

Catatan dan tracking perubahan, fitur, serta file penting di folder `app/`.

---

## 📁 Struktur & Fitur Utama

- **agents/**  
  - BaseAgent, custom agents, registry, manager, utils  
  - [x] Modular agent system  
  - [x] Registry & dynamic agent loading

- **chains/**  
  - BaseChain, custom chains, registry, builder, hooks, utils  
  - [x] Modular chain system  
  - [x] Hooks & monitoring  
  - [x] Chain registry

- **llms/**  
  - BaseLLM, PollinationsLLM, OpenAILLM, registry  
  - [x] Unified LLM interface  
  - [x] Pollinations & OpenAI support  
  - [x] Image/text generation via PollinationsLLM

- **memory/**  
  - FaissStore, ElasticsearchStore, ChromaStore, factory  
  - [x] Pluggable vector store  
  - [x] Factory for memory backend

- **monitoring/**  
  - Logger, log_cleaner, __init__  
  - [x] Per-agent/chain logging  
  - [x] Log rotation/archiving

- **loaders/**  
  - BaseLoader, registry, builder, custom/pdf_loader, utils  
  - [x] Modular document loaders  
  - [x] PDF loader  
  - [x] Loader registry

- **tools/**  
  - pollination.py, ...  
  - [x] Pollinations API integration

- **controllers/**  
  - BaseController, AgentController  
  - [x] API endpoints for agent orchestration

- **routes/**  
  - agents_route, base_route, __init__  
  - [x] API & web routes

- **extension.py**  
  - [x] Flask extension setup

- **templates/**  
  - base.html  
  - [x] Main UI

- **static/**  
  - css/, js/, assets/  
  - [x] Tailwind, scripts.js, icons

---

## 📝 Progress Log

- [x] Modular agent, chain, and LLM architecture
- [x] Pollinations LLM: text & image generation
- [x] Loader system with PDF support
- [x] Pluggable memory (faiss, elasticsearch, chroma)
- [x] Logging & log cleaning
- [x] Frontend: agent/model selection, markdown rendering
- [x] API: model listing, agent orchestration
- [ ] Add more loaders (e.g. docx, txt)
- [ ] Add more chains and agent types
- [ ] Add tests for all modules
- [ ] Improve error handling and validation

---

## 📌 Catatan

- Semua modul utama sudah terhubung via registry/factory.
- Untuk menambah agent/chain/loader/llm baru, cukup daftarkan di registry masing-masing.
- LLM dan memory backend bisa diganti lewat env/config.
- Log progress ini bisa diupdate manual setiap ada perubahan signifikan.

---
