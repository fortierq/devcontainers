FROM qfortier/poetry:alpine

USER root
RUN apk add build-base linux-headers libffi-dev

USER user
WORKDIR /home/user
COPY pyproject.toml .
RUN poetry install
