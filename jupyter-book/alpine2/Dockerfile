FROM qfortier/poetry:alpine

USER root
RUN apk add build-base linux-headers libffi-dev
COPY pyproject.toml /home/user/
RUN chown -R user /home/user

USER user
WORKDIR /home/user
RUN poetry add jupyter-book
