FROM ocaml/opam:alpine

RUN opam init && \
    opam update && \
    opam install ocaml-lsp-server ocamlformat ocamlformat-rpc
