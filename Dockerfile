FROM archlinux/base

ENV PROJECT_DIR=/home/

ENV COMP_DIR=/root/.local/share

WORKDIR ${PROJECT_DIR}

VOLUME ${PROJECT_DIR} ${COMP_DIR}

RUN pacman -Sy && pacman -S --noconfirm base

