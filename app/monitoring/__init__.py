from app.monitoring.logger import get_agent_logger
from app.monitoring.log_cleaner import start_scheduler

# Mulai penghapusan log tiap 10 menit
start_scheduler(interval_minutes=30)