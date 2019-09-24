# Zachary Andrews
## Fall 2019 Senior Comprehensive Project

### Notes

`sed '1!d' /etc/os-release` -> gets name of distro.

**Debian (not jessie)**-

*appear to not need `-get`*

```
apt-get update

apt-get upgrade

apt-get install docker.io
```

**Alpine**-

```
apk add --no-cache docker
```

**Arch (pacman)**-

```
pacman -Sy

pacman -S docker
```

#### Process (rough)-

1. determine OS
	- linux -> determine base system & package manager, see above. **alt - `which <package manager name>` -> no output -> not package manager**
	- mac -> homebrew -> sudo chown root:wheel $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
sudo chmod u+s $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
	- windows -> bitadmin, choco -> **More Research Necessary**
