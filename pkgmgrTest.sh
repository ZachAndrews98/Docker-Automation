#!/bin/bash

# checks for existance of individual package managers

which apt &>/dev/null # silent run of which command -> no output, no errors
if [[ $? == 0 ]]; then
	echo $password | sudo apt-get update
	echo $password | sudo apt-get upgrade -y
	echo $password | sudo apt-get install docker.io -y
else
	echo "apt not installed"
fi

which apk &>/dev/null
if [[ $? == 0 ]]; then
	apk add docker
else
	echo "apk not installed"
fi

which yum &>/dev/null
if [[ $? == 0 ]]; then
	echo "yum installed"
else
	echo "yum not installed"
fi

which pacman &>/dev/null
if [[ $? == 0 ]]; then
	echo $password | sudo pacman -Sy
	sudo pacman -S docker --noconfirm
else
	echo "pacman not installed"
fi

sudo usermod -aG docker $USER


docker run --rm hello-world &>/dev/null
echo $?
if [[ $? == 0 ]] || [[ $? == 126 ]]; then
	echo Docker Installed.
else
	echo Something Went Wrong.
fi
docker rmi hello-world &>/dev/null
echo $?


echo Please Reboot Your System.
