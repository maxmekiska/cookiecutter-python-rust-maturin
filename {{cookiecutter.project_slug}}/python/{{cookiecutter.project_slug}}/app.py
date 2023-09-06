from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from {{cookiecutter.project_slug}}.observer.tracker import track
from {{cookiecutter.project_slug}}.utils.fake import show_diff, show_sum
from {{cookiecutter.project_slug}}.schemas.models import SumRequest, DiffRequest

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

@app.get("/run/sum/")
async def run_sum(request: SumRequest):
    track.info(f"SUM endpoint received request with params: {request.a}, {request.b}")
    return {"message": f"show_sum({request.a}, {request.b}) = {show_sum(request.a, request.b)}"}

@app.get("/run/diff/")
async def run_diff(request: DiffRequest):
    track.info(f"DIFF endpoint received request with params: {request.a}, {request.b}")
    return {"message": f"show_diff({request.a}, {request.b}) = {show_diff(request.a, request.b)}"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
