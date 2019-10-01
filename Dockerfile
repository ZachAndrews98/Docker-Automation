FROM alpine:latest

ENV PROJECT_DIR=/home/

ENV COMP_DIR=/root/.local/share

WORKDIR ${PROJECT_DIR}

VOLUME ${PROJECT_DIR} ${COMP_DIR}

RUN apk add --no-cache bash

