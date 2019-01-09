FROM pypy:3

ENV HOME /root

# Define working directory.
WORKDIR /root

# Cloning and install dependencies
RUN \
    git clone https://github.com/GustavoDinizMonteiro/network-of-favors.git && \
    (cd network-of-favors && pip3 install)

EXPOSE 5000/tcp

# Define working directory.
WORKDIR /root/network-of-favors