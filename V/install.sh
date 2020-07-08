dnf install -y git gcc make

cd /usr/local/src

git clone https://github.com/vlang/v

cd v

make

./v symlink

reboot