from fastapi import FastAPI, Request, Header, HTTPException, Depends
from app import node_manager
from app.logger import log_action, log_error

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

app = FastAPI()

API_KEY = 'super_secret_key'


@app.get("/")
def read_root():
    return {"message": "Welcome to Node Agent Microserver"}

@app.post('/node/start')
async def start_node(request: Request, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        config = await request.json() if await request.body() else {}
        result = node_manager.start_node(config)
        log_action('start', result)
        return result
    except Exception as e:
        log_error('start', str(e))
        return {'error': str(e)}
    
@app.post('/node/stop')
def stop_node(_: str = Depends(verify_api_key)):
    try:
        result = node_manager.stop_node()
        log_action('stop', result)
        return result
    except Exception as e:
        log_error('stop', str(e))
        return {'error': str(e)}
    
@app.get('/node/status')
def get_status(_: str = Depends(verify_api_key)):
    try:
        result = node_manager.node_status()
        log_action('status', result)
        return result
    except Exception as e:
        log_error('status', str(e))
        return {'error': str(e)}
    