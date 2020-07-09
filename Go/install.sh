dnf install -y tar

cd /usr/local/src

curl -L -O https://dl.google.com/go/go1.14.4.linux-amd64.tar.gz

tar -C /usr/local -xf go1.14.4.linux-amd64.tar.gz

echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bash_profile

echo 'export GOPATH=$HOME/go' >> ~/.bash_profile

echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bash_profile
