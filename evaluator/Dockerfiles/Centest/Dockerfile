FROM centos

RUN yum update -y && \
yum install python3 python3-pip git sudo -y && \
pip3 install pipenv && \
git clone https://github.com/ZachAndrews98/Docker-Automation.git

CMD cd Docker-Automation && \
pipenv --python /usr/bin/python3 && \
pipenv install && \
pipenv run python3 main.py --command
