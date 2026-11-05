from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def server_status() -> str:
    return "Server is running successfully. Github actions are working fine."
