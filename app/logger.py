import logging
from datetime import datetime

LOG_FILE = 'logs/node_agent.log'

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_action(action, result):
    logging.info(f'{action} -> {result}')

def log_error(action, error):
    logging.error(f'{action} FAILED ->{ error}')
