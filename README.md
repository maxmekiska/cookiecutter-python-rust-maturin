# Python on steroids

Maturin Python Rust Mix template.

## Build via Maturin

- create a vitual env: `python -m venev env`
- activate env: `.\env\Scripts\activate`
- pip install maturin
- run `maturin new --mixed <your path\nameOfYourLibrary>`
- test via: 
    - `maturin develop` or
    - `maturin build --interpreter python` + `pip install .`


## Build as a Microservice

- `docker build -t my-microservice .`
- `docker run -d -p 8000:8000 --name your-flask-app-container my-microservice`