dnf -y install python36

alternatives --config python

2

update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1