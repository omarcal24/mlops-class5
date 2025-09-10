from fastapi import FastAPI

app = FastAPI()

@app.get()
async def root_call():
    return "Hello"

