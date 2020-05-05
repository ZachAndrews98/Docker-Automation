# BEGIN GENERATED CONTENTS
FROM debian:bullseye

ADD ./ project/

RUN apt update && apt upgrade -y && \
apt install python3 nodejs ruby-full default-jdk golang gcc -y

CMD cd ./project 
# END GENERATED CONTENTS
