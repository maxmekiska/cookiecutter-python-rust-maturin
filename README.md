# Python on Steroids

Enhanced maturin python rust mix template. The template supports two modes:

1. python library mode
2. microservice mode

Both modes can be used with no changes.

## Run as a library

- install maturin via: `pip install maturin`
- Either:
    - development mode
        - build package in development mode via: `maturin develop`
    - build wheel
        - build package wheel via: `maturin build --interpreter python`
        - `pip install .`

## Build as a Microservice

- `docker build -t my-microservice .`
- `docker run -d -p 8000:8000 --name your-flask-app-container my-microservice`



## Appendix

#### Core was build via Maturin

- create a vitual env: `python -m venev env`
- activate env: `.\env\Scripts\activate`
- pip install maturin
- run `maturin new --mixed <your path\nameOfYourLibrary>`
- test via either:
    - development mode
        - build package in development mode via: `maturin develop`
    - build wheel
        - build package wheel via: `maturin build --interpreter python`
        - `pip install .`