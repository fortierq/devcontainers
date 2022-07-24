FROM python:3.10

RUN apt update && useradd -ms /bin/bash user

USER user
ENV PATH /home/user/.local/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN echo "poetry shell" >> /home/user/.bashrc
