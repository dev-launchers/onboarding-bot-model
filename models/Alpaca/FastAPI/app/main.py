#¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ ¨¨¨¨¨ #
#           Library            #
#_____ _____ _____ _____ _____ #

# General Libraries
import ssl
from model_pipeline import generate_text_from

# FastAPI requierements
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse

# Debug
ssl._create_default_https_context = ssl._create_unverified_context

# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#       FastAPI describe        #
# ______________________________#

app = FastAPI(
    timeout=1800, # temps de calcul max à 30 min (60s x 30)
    title="👾 Alpaca API",
    summary="Alpaca API: A question/answer LLM.",
    description="""
                ## Alpaca API: A question/answer LLM.
                * This API uses a Large Language Model to answer questions easily.
                """,
    version="0.0.1",
    contact={
        "name": "Gauthier Rammault",
        "url": "https://www.linkedin.com/in/gauthier-rammault/",
    },
    terms_of_service="https://devlaunchers.org/page/terms-and-conditions",
    openapi_tags= [
        {
            "name": "Home",
            "description": "👾 Alpaca API homepage."
        },
        {
            "name": "Question",
            "description": "👾 Alpaca API with POST or GET method."
        }
    ]
)

# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#       FastAPI run app.       #
# ______________________________#

with open("index.html", "r") as html_file:
    # Lire le contenu du fichier HTML dans une variable texte
    html = html_file.read()

@app.get("/", tags=["Home"])
async def get():
    return HTMLResponse(html)

@app.post("/question/", tags=["Question"])
async def question(input_text: str = ""):
    result = generate_text_from(input_text)
    return "Answer: {}".format(result)