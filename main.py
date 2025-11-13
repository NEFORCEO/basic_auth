

from client.app.lifespan import start_app
from client.app.run import main
from router.router import router
from datetime import datetime
from loger.logging import logger

from fastapi import FastAPI, Request, Response


app = FastAPI(lifespan=start_app)
app.include_router(router=router)

@app.middleware('http')
async def log_routers(request: Request, call_next) -> Response:
    start_time = datetime.now()
    
    logger.info(f"request: {request.method}, url: {request.url}")
    response = await call_next(request)
    
    duration = (datetime.now() - start_time).total_seconds()
    logger.info(f"answer: {response.status_code} | time: {duration:.2f}s")
    
    return response
    

if __name__ == "__main__":
    main.run()
    



