from fastapi import FastAPI
from app import node_manager, logger

app = FastAPI()

@app.post('/node/start')
def start_node():
    try:
        result = node_manager.start_node()
        logger.log_action('start', result)
        return result
    except Exception as e:
        logger.log_error('start', str(e))
        return {'error': str(e)}
    
@app.post('/node/stop')
def stop_node():
    try:
        result = node_manager.stop_node()
        logger.log_action('stop', result)
        return result
    except Exception as e:
        logger.log_error('stop', str(e))
        return {'error': str(e)}
    
@app.get('/node/status')
def get_status():
    try:
        result = node_manager.node_status()
        logger.log_action('status', result)
        return result
    except Exception as e:
        logger.log_error('status', str(e))
        return {'error': str(e)}
    