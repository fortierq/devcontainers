FROM python:3.10-alpine

RUN adduser -s /bin/ash -S user && \
    apk add --update --no-cache curl git

USER user
ENV PATH /home/user/.local/bin:$PATH
RUN curl -SL https://install.python-poetry.org | python3 -
