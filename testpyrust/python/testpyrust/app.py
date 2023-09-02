import uvicorn
from fastapi import FastAPI

from testpyrust.utils.fake import show_sum, show_diff

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/run/sum")
async def run_sum():
    return {"message": f"show_sum(1,2) = {show_sum(1,2)}"}

@app.get("/run/diff")
async def run_diff():
    return {"message": f"show_diff(1,2) = {show_diff(1,2)}"}

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)  # Modify host and port as needed

if __name__ == '__main__':
    main()