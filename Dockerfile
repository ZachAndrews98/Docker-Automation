FROM debian:bullseye

ENV PROJECT_DIR=/home/

ENV COMP_DIR=/root/.local/share

WORKDIR ${PROJECT_DIR}

VOLUME ${PROJECT_DIR} ${COMP_DIR}

RUN apt-get update && apt-get upgrade -y && apt-get install sudo -y

