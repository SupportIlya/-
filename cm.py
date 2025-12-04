from loguru import logger
import sys

logger.add("logs/app.log", rotation="500 MB", retention="10 days")
logger.add(sys.stderr, level="INFO")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    logger.info(f"{request.method} {request.url.path} {response.status_code} ({process_time:.2f}s)")
    return response