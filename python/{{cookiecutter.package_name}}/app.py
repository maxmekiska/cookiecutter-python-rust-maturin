from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from {{cookiecutter.package_name}}.observer.tracker import track
from {{cookiecutter.package_name}}.utils.fake import show_diff, show_sum

app = FastAPI()


# Configure CORS settings to allow requests from all origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)


@app.get("/")
async def read_root():
    track.info("successful startup, standby for requests")
    return {"message": "Hello, World!"}


@app.get("/heartbeat/")
def heartbeat():
    track.info("heartbeat check requested")
    return {
        f'Micro Service Alive at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}'
    }


@app.get("/run/sum/{a}/{b}")
async def run_sum(a: int, b: int):
    track.info(f"SUM endpoint received request with params: {a}, {b}")
    return {"message": f"show_sum({a},{b}) = {show_sum(a,b)}"}


@app.get("/run/diff/{a}/{b}")
async def run_diff(a: int, b: int):
    track.info(f"DIFF endpoint received request with params: {a}, {b}")
    return {"message": f"show_diff({a},{b}) = {show_diff(a,b)}"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
