import os
import time
import threading
import logging
from datetime import datetime
from threading import Lock

BASE_LOG_ROOT = os.path.join(os.path.dirname(__file__), "logs")
ARCHIVE_DIR = os.path.join(os.path.dirname(__file__), "archived")

os.makedirs(ARCHIVE_DIR, exist_ok=True)

log_lock = Lock()

logger = logging.getLogger("LogCleaner")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def archive_and_clear_logs():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d")
        archive_file_name = f"log_{timestamp}.txt"
        archive_path = os.path.join(ARCHIVE_DIR, archive_file_name)

        with log_lock:
            with open(archive_path, "a", encoding="utf-8") as archive:
                archive.write(f"\n\n=== LOG ARCHIVE @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")

                # Scan semua subfolder di logs/
                if not os.path.exists(BASE_LOG_ROOT):
                    logger.warning(f"Log root folder tidak ditemukan: {BASE_LOG_ROOT}")
                    return

                for subfolder in os.listdir(BASE_LOG_ROOT):
                    subfolder_path = os.path.join(BASE_LOG_ROOT, subfolder)
                    if not os.path.isdir(subfolder_path):
                        continue

                    logs_to_process = [f for f in os.listdir(subfolder_path) if f.endswith(".log")]

                    for log_file in logs_to_process:
                        log_path = os.path.join(subfolder_path, log_file)

                        if os.path.getsize(log_path) > 0:
                            with open(log_path, "r", encoding="utf-8") as lf:
                                archive.write(f"\n--- {log_file} from {subfolder} ---\n")
                                archive.write(lf.read())

                            # Clear log file setelah diarsipkan
                            open(log_path, "w").close()

        logger.info(f"Archived and cleared logs for {timestamp}")

    except Exception as e:
        logger.error(f"LogCleaner Error: {e}", exc_info=True)

def start_scheduler(interval_minutes=10):
    def run():
        while True:
            archive_and_clear_logs()
            time.sleep(interval_minutes * 60)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
