FROM pypy

ENV HOME /root

# Define working directory.
WORKDIR /root

# Cloning and install dependencies
RUN \
    git clone https://github.com/GustavoDinizMonteiro/network-of-favors.git && \
    pipenv install

EXPOSE 5000/tcp

# Define working directory.
WORKDIR /root/network-of-favors