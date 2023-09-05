# Python on Steroids Template

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
- `docker run -d -p 8000:8000 --name test-service my-microservice`

### Send example requests via curl

`/heartbeat/`
```
curl http://127.0.0.1:8000/heartbeat/
```

`/run/sum/{a}/{b}`
```
curl http://127.0.0.1:8000/run/sum/5/7
```


`/run/diff/{a}/{b}`
```
curl http://127.0.0.1:8000/run/diff/5/7
```



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