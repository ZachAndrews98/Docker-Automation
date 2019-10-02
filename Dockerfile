FROM alpine:latest

ENV PROJECT_DIR=/home/

ENV COMP_DIR=/root/.local/share

WORKDIR ${PROJECT_DIR}

VOLUME ${PROJECT_DIR} ${COMP_DIR}

ADD pkgmgrTest.sh /home/test/pkgmgrTest.sh

RUN apk add --no-cache bash

