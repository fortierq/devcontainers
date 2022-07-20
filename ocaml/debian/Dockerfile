FROM ocaml/opam:debian

USER root

RUN apt update && \
    apt install -y python3-dev libffi-dev python3-pip g++ bash pkg-config libzmq3-dev libgmp-dev zlib1g-dev && \
    usermod --login user opam

USER user

RUN opam update && \
    opam install ocaml-lsp-server ocamlformat ocamlformat-rpc

ENV PATH="/home/user/.local/bin:${PATH}"

RUN pip3 install wheel jupyter && \
    opam install -y jupyter && \
    eval $(opam env) && \
    opam exec -- ocaml-jupyter-opam-genspec && \
    /home/opam/.local/bin/jupyter kernelspec install --user --name ocaml-jupyter "$(opam var share)/jupyter"
