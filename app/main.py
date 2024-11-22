from fastapi import FastAPI
from loguru import logger
from contextlib import asynccontextmanager


# The function get_data goes into the folder personnal_info and get the .txt file my_info.txt and return the content of the file
def get_data():
    with open("app/personnal_info/my_info.txt") as f:
        return f.read()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: You can add initialization code here
    logger.info("Starting the application")

    yield  # Here the FastAPI application runs

    # Shutdown: You can add cleanup code here if needed
    print("Shutting down the application")


app = FastAPI(lifespan=lifespan)


@app.post("/form")
def form():
    data = get_data()
    logger.info(data)
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
