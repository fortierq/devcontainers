FROM alpine

RUN apk add --update --no-cache libffi-dev gmp-dev ocaml opam && \
    adduser -s /bin/ash -S user

USER user

RUN opam init && \
    opam update && \
    opam install ocaml-lsp-server ocamlformat ocamlformat-rpc
