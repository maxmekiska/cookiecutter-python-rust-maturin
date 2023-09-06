# Cookiecutter Python Rust Maturin Template

Please run the following commands to use this template:

- `pip install cookiecutter`
- `cookicuter https://github.com/maxmekiska/cookiecutter-python-rust-maturin`

## Overview

Enhanced maturin python rust template. The template supports two main modes:

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

You can still run the library in microservice mode via the command: `micro-launch`

## Build as a Microservice

- `docker build -t my-microservice .`
- `docker run -d -p 8000:8000 --name test-service my-microservice`

### Send example requests via curl

`/heartbeat/`
```
curl http://127.0.0.1:8000/heartbeat/
```

`/run/sum/`
```
curl -X 'POST' \
  'http://localhost:8000/run/sum/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "a": 1,
  "b": 2
}'
```


`/run/diff/`
```
curl -X 'POST' \
  'http://localhost:8000/run/diff/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "a": 2,
  "b": 1
}'
```

## Format and Test via tox

- install tox via: `pip install tox`
- run tox via: `tox`


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