FROM ubuntu

RUN apt update && apt upgrade -y && \
apt install python3.7 python3-pip git sudo -y && \
pip3 install pipenv && \
git clone https://github.com/ZachAndrews98/Docker-Automation.git

CMD cd Docker-Automation && \
export LANG=C.UTF-8 && \
pipenv --python /usr/bin/python3.7 && \
pipenv install && \
pipenv run python3 main.py --command
