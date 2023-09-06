FROM python:{{cookiecutter.python_version}}-slim AS builder


RUN apt-get update && apt-get install -y build-essential curl

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o rustup.sh && sh rustup.sh -y

WORKDIR /microservice

ENV PATH="${PATH}:/root/.cargo/bin"
ENV RUST_BACKTRACE=full



COPY . .

RUN pip install maturin
RUN maturin build --release
RUN pip install .


CMD ["micro-launch"]
