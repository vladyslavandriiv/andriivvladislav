import logging
import os
import time
from datetime import datetime

# Створення папки logs, якщо не існує
if not os.path.exists("logs"):
    os.makedirs("logs")

# Налаштування логера
log_file = os.path.join("logs", "task_log.log")
logging.basicConfig(
    filename=log_file,
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_logger_task():
    start_time = time.time()
    duration = 60  # 1 хвилина
    interval = 5   # кожні 5 секунд

    while True:
        elapsed = time.time() - start_time
        if elapsed >= duration:
            break
        logging.info(f"Program running for {int(elapsed)} seconds. Current time: {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(interval)

    logging.error("Task completed")

# Виконання функції
run_logger_task()


