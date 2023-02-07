from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki,search_wiki

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi, this is a wikipedia API. Call /search or /fetch"}

@app.get("/search/{word}")
async def search(word: str):
    """Page to search in wikipedia"""

    result = search_wiki(word)
    return {"Entries": result}

@app.get("/fetch/{word}")
async def fetch(word: str):
    """Page to fetch description in wikipedia"""

    result = wiki(word)
    return {"Result": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
