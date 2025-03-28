import logging
import os

log_folder = "log"
log_file_path = os.path.join(log_folder, "server.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger()