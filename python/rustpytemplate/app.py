import uvicorn
from fastapi import FastAPI
from rustpytemplate.utils.fake import show_diff, show_sum

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/run/sum/{a}/{b}")
async def run_sum(a: int, b: int):
    return {"message": f"show_sum({a},{b}) = {show_sum(a,b)}"}


@app.get("/run/diff/{a}/{b}")
async def run_diff(a: int, b: int):
    return {"message": f"show_diff({a},{b}) = {show_diff(a,b)}"}


def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
