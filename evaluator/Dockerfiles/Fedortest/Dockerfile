FROM fedora

RUN dnf install python3.7 pipenv sudo git -y && \
git clone https://github.com/ZachAndrews98/Docker-Automation.git

CMD cd Docker-Automation && \
pipenv install && \
pipenv run python3 main.py --command
