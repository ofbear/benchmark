dnf install -y gcc pcre openssl*

cd /usr/local/src

curl https://nim-lang.org/choosenim/init.sh -sSf | sh

export PATH=$HOME/.nimble/bin:$PATH

choosenim update stable