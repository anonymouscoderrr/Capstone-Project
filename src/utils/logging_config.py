import logging
from pathlib import Path

# Create a folder to store log files if it doesn't already exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Name of the log file
LOG_FILE = LOG_DIR / "api.log"

# Configure how logging should work
logging.basicConfig(
    level=logging.INFO,  # Save INFO messages and anything more important
    format="%(asctime)s | %(levelname)s | %(message)s",  # Log format
    handlers=[
        logging.FileHandler(LOG_FILE),  # Save logs to a file
        logging.StreamHandler()         # Also print logs in the terminal
    ]
)

# Create a logger that the API can use
logger = logging.getLogger("road_maintenance_api")