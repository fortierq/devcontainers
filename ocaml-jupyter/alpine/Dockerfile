FROM qfortier/ocaml:alpine

USER root

RUN usermod --login user opam
RUN ln -s /home/opam /home/user

USER user

RUN opam update && \
    opam install ocaml-lsp-server ocamlformat ocamlformat-rpc
