import os
import time
import threading
from datetime import datetime

AGENT_LOG_DIR = os.path.join(os.path.dirname(__file__), "agents")
ARCHIVE_DIR = os.path.join(os.path.dirname(__file__), "archived")

# Pastikan folder arsip ada
os.makedirs(ARCHIVE_DIR, exist_ok=True)

def archive_and_clear_logs():
    try:
        logs_to_process = [f for f in os.listdir(AGENT_LOG_DIR) if f.endswith(".log")]
        timestamp = datetime.now().strftime("%Y-%m-%d")

        # Tentukan nama file arsip berdasarkan tanggal
        archive_file_name = f"log_{timestamp}.txt"
        archive_path = os.path.join(ARCHIVE_DIR, archive_file_name)

        with open(archive_path, "a", encoding="utf-8") as archive:
            archive.write(f"\n\n=== LOG ARCHIVE @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")

            for log_file in logs_to_process:
                log_path = os.path.join(AGENT_LOG_DIR, log_file)

                # Baca isinya kalau ada
                if os.path.getsize(log_path) > 0:
                    with open(log_path, "r", encoding="utf-8") as lf:
                        archive.write(f"\n--- {log_file} ---\n")
                        archive.write(lf.read())

                    # Kosongkan log-nya
                    open(log_path, "w").close()

    except Exception as e:
        print(f"LogCleaner Error: {e}")

def start_scheduler(interval_minutes=10):
    def run():
        while True:
            archive_and_clear_logs()
            time.sleep(interval_minutes * 60)
    
    thread = threading.Thread(target=run, daemon=True)
    thread.start()
