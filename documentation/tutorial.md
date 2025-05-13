# Tutorial AGILEMinD Framework: Membuat Journal Searcher AI

## Gambaran Umum
AGILEMinD adalah framework fleksibel untuk membangun AI agent yang dapat menangani berbagai tugas melalui antarmuka terpadu. Tutorial ini akan memandu Anda membuat Journal Searcher AI yang dapat mencari dan menganalisis makalah akademik.

## Prasyarat
- Python 3.8+
- Flask
- Pemahaman dasar Python dan REST API
- Akses ke API makalah akademik (misalnya arXiv, Semantic Scholar)

## Struktur Proyek
```
app/
├── controllers/
│   └── journal_controller.py
├── services/
│   ├── journal_service.py
│   └── prompt_service.py
├── tools/
│   └── journal_search.py
├── prompts/
│   └── journal_searcher_prompts.txt
└── static/
    └── js/
        └── journal_scripts.js
```

## Langkah 1: Membuat Journal Search Tool
Pertama, buat tool untuk berinteraksi dengan API makalah akademik.

```python
# app/tools/journal_search.py
import requests
from typing import Dict, List, Optional

class JournalSearchTool:
    def __init__(self):
        self.base_url = "https://api.semanticscholar.org/v1"
        self.headers = {
            "Accept": "application/json"
        }

    def search_papers(self, query: str, limit: int = 5) -> Dict:
        """Mencari makalah akademik menggunakan query."""
        try:
            response = requests.get(
                f"{self.base_url}/paper/search",
                params={"query": query, "limit": limit},
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"Error saat mencari makalah: {str(e)}"}

    def get_paper_details(self, paper_id: str) -> Dict:
        """Mendapatkan informasi detail tentang makalah tertentu."""
        try:
            response = requests.get(
                f"{self.base_url}/paper/{paper_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"Error saat mendapatkan detail makalah: {str(e)}"}
```

## Langkah 2: Membuat Template Prompt
Buat template prompt untuk Journal Searcher AI.

```text
# app/prompts/journal_searcher_prompts.txt
Anda adalah Journal Searcher AI, khusus dalam mencari dan menganalisis makalah akademik. Tugas Anda adalah:

1. Mencari makalah yang relevan berdasarkan query pengguna
2. Menganalisis dan merangkum temuan utama
3. Memberikan wawasan dan koneksi antar makalah
4. Menyarankan arah penelitian terkait

Format respons Anda sebagai berikut:

# Hasil Pencarian
- Daftar makalah relevan dengan judul dan penulis

# Temuan Utama
- Ringkasan temuan utama dari makalah-makalah

# Analisis
- Analisis kritis terhadap penelitian
- Koneksi antar makalah yang berbeda

# Arah Masa Depan
- Saran untuk penelitian lebih lanjut
- Topik terkait untuk dieksplorasi

Harap berikan temuan penelitian yang komprehensif dan terstruktur dengan baik.
```

## Langkah 3: Membuat Journal Service
Buat service untuk menangani logika bisnis.

```python
# app/services/journal_service.py
from app.tools.journal_search import JournalSearchTool
from app.services.prompt_service import PromptService

class JournalService:
    def __init__(self):
        self.search_tool = JournalSearchTool()
        self.prompt_service = PromptService()

    def search_journals(self, query: str, model: Optional[str] = None) -> Dict:
        """Mencari dan menganalisis makalah akademik."""
        try:
            # Mendapatkan hasil pencarian
            search_results = self.search_tool.search_papers(query)
            if "error" in search_results:
                return {"status": "error", "error": search_results["error"]}

            # Mendapatkan prompt dasar
            base_prompt = self.prompt_service.get_prompt("journal_searcher")
            
            # Memformat prompt dengan hasil pencarian
            formatted_prompt = f"{base_prompt}\n\nHasil Pencarian:\n{search_results}"
            
            # Menghasilkan analisis menggunakan Pollinations API
            analysis = generate_text(formatted_prompt, model)
            
            return {
                "status": "success",
                "search_results": search_results,
                "analysis": analysis
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
```

## Langkah 4: Membuat Controller
Buat controller untuk menangani permintaan HTTP.

```python
# app/controllers/journal_controller.py
from flask import current_app
from app.services.journal_service import JournalService

class JournalController:
    def __init__(self):
        self.journal_service = JournalService()

    def search_journals(self, query: str, model: Optional[str] = None) -> Dict:
        """Menangani permintaan pencarian jurnal."""
        try:
            result = self.journal_service.search_journals(query, model)
            return result
        except Exception as e:
            current_app.logger.error(f"Error dalam pencarian jurnal: {e}")
            return {"status": "error", "error": str(e)}
```

## Langkah 5: Menambahkan JavaScript Frontend
Buat antarmuka frontend untuk Journal Searcher.

```javascript
// app/static/js/journal_scripts.js
function searchJournals() {
    const query = document.getElementById('search-input').value;
    const model = document.getElementById('model-select').value;

    if (!query) {
        document.getElementById('search-output').innerHTML = 
            '<p class="text-red-500">❌ Mohon masukkan query pencarian</p>';
        return;
    }

    // Tampilkan status loading
    document.getElementById('search-output').innerHTML = 
        '<p class="text-gray-500">⏳ Mencari jurnal...</p>';

    // Siapkan data permintaan
    const requestData = {
        query: query,
        model: model
    };

    fetch('/api/journals/search', {
        method: 'POST',
        body: JSON.stringify(requestData),
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'error') {
            document.getElementById('search-output').innerHTML = 
                `<p class="text-red-500">❌ Error: ${data.error}</p>`;
            return;
        }

        // Format dan tampilkan hasil
        const formattedResults = formatJournalResults(data);
        document.getElementById('search-output').innerHTML = formattedResults;
    })
    .catch(error => {
        document.getElementById('search-output').innerHTML = 
            `<p class="text-red-500">❌ Error: ${error}</p>`;
    });
}

function formatJournalResults(data) {
    const { search_results, analysis } = data;
    
    return `
        <div class="space-y-6">
            <div class="search-results">
                <h3 class="text-lg font-semibold mb-2">Hasil Pencarian</h3>
                ${formatSearchResults(search_results)}
            </div>
            
            <div class="analysis">
                <h3 class="text-lg font-semibold mb-2">Analisis</h3>
                <div class="markdown-content">
                    ${formatResponse(analysis)}
                </div>
            </div>
        </div>
    `;
}
```

## Langkah 6: Menambahkan Routes
Tambahkan routes yang diperlukan ke aplikasi Flask Anda.

```python
# app/routes/journal_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.journal_controller import JournalController

journal_bp = Blueprint('journal', __name__)
journal_controller = JournalController()

@journal_bp.route('/api/journals/search', methods=['POST'])
def search_journals():
    data = request.get_json()
    query = data.get('query')
    model = data.get('model')
    
    if not query:
        return jsonify({"status": "error", "error": "Query diperlukan"}), 400
        
    result = journal_controller.search_journals(query, model)
    return jsonify(result)
```

## Contoh Penggunaan

1. Jalankan aplikasi Flask:
```bash
flask run
```

2. Akses antarmuka Journal Searcher di `http://localhost:5000`

3. Masukkan query pencarian, misalnya:
```
"aplikasi machine learning dalam kesehatan"
```

4. Journal Searcher akan:
   - Mencari makalah yang relevan
   - Menganalisis temuan
   - Memberikan ringkasan terstruktur
   - Menyarankan arah penelitian terkait

## Tips Kustomisasi

1. **Menambah Fitur Baru**
   - Perluas kelas `JournalSearchTool` untuk mendukung lebih banyak API
   - Tambahkan metode baru ke `JournalService` untuk berbagai jenis analisis
   - Buat template prompt baru untuk kasus penggunaan tertentu

2. **Meningkatkan Hasil**
   - Implementasikan caching untuk makalah yang sering dicari
   - Tambahkan filter untuk tanggal publikasi, jurnal, dll.
   - Sertakan analisis sitasi dan metrik dampak

3. **Meningkatkan UI**
   - Tambahkan visualisasi untuk hubungan antar makalah
   - Implementasikan sistem rekomendasi makalah
   - Tambahkan fungsi ekspor untuk hasil pencarian

## Praktik Terbaik

1. **Penanganan Error**
   - Selalu implementasikan penanganan error yang tepat dalam panggilan API
   - Berikan pesan error yang bermakna kepada pengguna
   - Catat error untuk debugging

2. **Performa**
   - Cache respons API jika memungkinkan
   - Implementasikan pagination untuk set hasil besar
   - Gunakan operasi async untuk tugas yang memakan waktu lama

3. **Keamanan**
   - Validasi semua input pengguna
   - Implementasikan rate limiting untuk panggilan API
   - Amankan API key dan data sensitif

## Kesimpulan
Framework AGILEMinD menyediakan fondasi fleksibel untuk membangun AI agent. Dengan mengikuti tutorial ini, Anda telah membuat Journal Searcher AI yang dapat membantu peneliti mencari dan menganalisis makalah akademik. Anda dapat mengembangkannya lebih lanjut dengan menambah fitur, meningkatkan analisis, atau mengintegrasikan dengan API tambahan.
