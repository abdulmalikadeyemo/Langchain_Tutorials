# Install langserve using "pip install langserve[all]"

from fastapi import FastAPI
from langserve import add_routes
import uvicorn
from app import chain


#1. Create the app definition
app = FastAPI(
    title="First Langchain Deployment",
    version="1.0",
    description="A deployment for our text translation application"
)

#2. Add the chain to the route
add_routes(
    app,
    chain,
    path="/translate"
)


if __name__=="__main__":

    uvicorn.run(app, host="localhost", port=8000)

