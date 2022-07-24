FROM qfortier/ocaml:alpine

USER root 

RUN apk --update add texlive openssh

RUN mkdir /workspaces && chown -R opam /workspaces/

USER opam
