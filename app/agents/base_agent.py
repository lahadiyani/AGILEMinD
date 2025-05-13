from app.monitoring.logger import get_agent_logger

logger = get_agent_logger("BaseAgent", "base_agent.log")

class BaseAgent:
    """
    Kelas dasar untuk semua agen dalam sistem.
    
    Kelas ini menyediakan struktur dan fungsionalitas dasar yang harus dimiliki oleh semua agen,
    termasuk pembuatan prompt, interaksi dengan LLM, manajemen memori, dan pemrosesan respons.
    """
    
    def __init__(self, name, description=None, prompt=None, llm=None, memory=None, tools=None, logging_enabled=True):
        """
        Inisialisasi instance BaseAgent baru.
        
        Args:
            name (str): Nama agen
            description (str, opsional): Deskripsi tujuan agen
            prompt (str, opsional): Template prompt untuk agen
            llm (opsional): Instance model bahasa
            memory (opsional): Sistem memori untuk menyimpan interaksi
            tools (list, opsional): Daftar alat yang tersedia untuk agen
            logging_enabled (bool): Menentukan apakah logging diaktifkan
        """
        self.name = name
        self.description = description or ""
        self.prompt = prompt
        self.llm = llm
        self.memory = memory
        self.tools = tools or []
        
        # Setup logger
        if logging_enabled:
            self.logger = logging.getLogger(__name__)
            logging.basicConfig(level=logging.INFO)

    def log(self, message):
        """Log pesan jika logging diaktifkan."""
        if hasattr(self, 'logger'):
            self.logger.info(f"[{self.name}] {message}")

    def validate(self):
        """Validasi konfigurasi agen sebelum dijalankan."""
        if not self.prompt:
            raise ValueError("Prompt not configured.")
        if not self.llm:
            raise ValueError("LLM instance not configured.")
        
    def build_prompt(self, input_text):
        """
        Membangun prompt dengan mengganti placeholder dengan teks input.
        
        Args:
            input_text (str): Teks input yang akan dimasukkan ke dalam template prompt
            
        Returns:
            str: Prompt yang telah diformat
        """
        if not self.prompt:
            raise ValueError("Prompt not configured.")
        return self.prompt.replace("{input}", input_text)

    def call_llm(self, prompt):
        """
        Memanggil model bahasa dengan prompt yang diberikan.
        
        Args:
            prompt (str): Prompt yang akan dikirim ke model bahasa
            
        Returns:
            str: Respons dari model bahasa
        """
        if not self.llm:
            raise ValueError("LLM instance not configured.")
        self.log(f"Calling LLM with prompt: {prompt}")
        return self.llm.generate(prompt)

    def postprocess(self, response):
        """
        Memproses respons dari model bahasa.
        
        Args:
            response (str): Respons mentah dari model bahasa
            
        Returns:
            str: Respons yang telah diproses
        """
        self.log(f"Raw response from LLM: {response}")
        return response  # Bisa di-custom sesuai kebutuhan

    def remember(self, input_text, output_text):
        """
        Menyimpan interaksi dalam memori jika sistem memori dikonfigurasi.
        
        Args:
            input_text (str): Teks input dari interaksi
            output_text (str): Teks output dari interaksi
        """
        if self.memory:
            self.memory.save(input_text, output_text)
            self.log("Interaction saved in memory.")

    def run(self, input_text):
        """
        Menjalankan alur kerja lengkap agen.
        
        Metode ini:
        1. Membangun prompt
        2. Memanggil model bahasa
        3. Menyimpan interaksi dalam memori
        4. Memproses respons
        
        Args:
            input_text (str): Teks input yang akan diproses
            
        Returns:
            str: Respons yang telah diproses
        """
        try:
            self.validate()  # Validasi konfigurasi agen sebelum menjalankan
            self.log(f"Running agent with input: {input_text}")
            prompt = self.build_prompt(input_text)
            response = self.call_llm(prompt)
            self.remember(input_text, response)
            return self.postprocess(response)
        except Exception as e:
            self.log(f"Error occurred: {e}")
            raise  # Meneruskan error jika terjadi masalah dalam eksekusi
