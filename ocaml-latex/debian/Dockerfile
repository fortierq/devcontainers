FROM qfortier/ocaml-jupyter:debian

USER root

RUN apt update -y --allow-releaseinfo-change && \
    apt install -y texlive python3-pygments build-essential imagemagick && \
    mkdir /workspaces && chown -R opam /workspaces && \
    grep -v PDF /etc/ImageMagick-6/policy.xml > /tmp/policy.xml && \
    rm /etc/ImageMagick-6/policy.xml && \
    mv /tmp/policy.xml /etc/ImageMagick-6/policy.xml

USER opam
