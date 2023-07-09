FROM texlive/texlive:latest

RUN apt update -y --allow-releaseinfo-change && \
    apt install -y imagemagick openssh-server && \
    mkdir /workspaces && \
    grep -v PDF /etc/ImageMagick-6/policy.xml > /tmp/policy.xml && \
    rm /etc/ImageMagick-6/policy.xml && \
    mv /tmp/policy.xml /etc/ImageMagick-6/policy.xml

RUN apt-get -y install python3-pip

RUN apt-get install -y sudo && \
    useradd -ms /bin/bash -G sudo user && \
    echo 'user:user' | chpasswd && \
    chown -R user /workspaces

USER user
