from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from langserve import add_routes
from app.chatbot import chain, HF_flan_t5, Home_dolly_2

app = FastAPI(title="Retrieval App")

@app.get("/", tags=["Home"])
async def get():
    return HTMLResponse(open("app/index.html", "r").read())

add_routes(app, chain)

add_routes(app, HF_flan_t5)

add_routes(app, Home_dolly_2)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
