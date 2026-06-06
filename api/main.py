from fastapi import FastAPI
from pydantic import BaseModel

from rag.query_engine import ask

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


@app.post("/query", response_model=QueryResponse)
def query_docs(request: QueryRequest):

    result = ask(request.query)

    return QueryResponse(
        answer=result["answer"],
        sources=result["sources"]
    )