from fastapi import FastAPI
from fastapi.responses import JSONResponse
from service import get_hello_message

app = FastAPI()

@app.get("/api/hello")
async def hello():
    message = get_hello_message()
    return JSONResponse(status_code=200, content=message)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=3000)