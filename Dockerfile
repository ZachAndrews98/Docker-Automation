FROM archlinux/base

ENV PROJECT_DIR=/home/

ENV COMP_DIR=/root/.local/share

WORKDIR ${PROJECT_DIR}

VOLUME ${PROJECT_DIR} ${COMP_DIR}

ADD pkgmgrTest.sh /home/test/pkgmgrTest.sh

RUN pacman -Sy && pacman -S --noconfirm base

