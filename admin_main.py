from fastapi import FastAPI
import uvicorn
from endpoints import router


app = FastAPI()
app.include_router(router)

uvicorn.run(app, host="127.0.0.1", port=8001)