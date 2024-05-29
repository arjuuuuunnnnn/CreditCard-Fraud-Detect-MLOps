import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logss = "logs"
log_filepath = os.path.join(logss, "logs.log")
os.makedirs(logss, exist_ok=True)

logging.basicConfig(
        level= logging.INFO,
        format= logging_str,

        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler(sys.stdout)
            ]
        )

logger = logging.getLogger("MLOpsLogger")
