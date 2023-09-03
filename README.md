# Python on steroids

Maturin Python Rust Mix template.

## Build via Maturin

- create a vitual env: `python -m venev env`
- activate env: `.\env\Scripts\activate`
- pip install maturin
- run `maturin new --mixed <your path\nameOfYourLibrary>`
- test via: 
    - `maturin develop`
    - `maturin build --interpreter python` + `pip install .`


