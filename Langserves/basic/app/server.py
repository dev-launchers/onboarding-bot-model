from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from langserve import add_routes
from app.chatbot import chain

app = FastAPI(title="Retrieval App")

@app.get("/", tags=["Home"])
async def get():
    return HTMLResponse(open("app/index.html", "r").read())

add_routes(app, chain)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
