# app/utils/logging.py

import logging
import os

def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Logging initialized")

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
