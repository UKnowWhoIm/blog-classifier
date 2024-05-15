FROM ollama/ollama

COPY install-model.sh /tmp/install-model.sh

WORKDIR /tmp

RUN chmod +x install-model.sh \
    && ./install-model.sh
