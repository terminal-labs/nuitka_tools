export DEBIAN_FRONTEND=noninteractive

apt-get update -y
apt-get install zstd -y
apt-get install linux-headers-$(uname -r) -y
apt-get upgrade -y

apt-get install build-essential -y

apt-get install dkms -y

apt-get install curl wget -y
apt-get install zip unzip -y
apt-get install checkinstall pkg-config -y
apt-get install openssl libssl-dev libssl-doc -y 
apt-get install libreadline-dev libncursesw5-dev libxml2-dev libffi-dev libyaml-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev liblzma-dev libb2-dev -y
apt-get install build-essential zlib1g-dev libbz2-dev liblzma-dev libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev libgdbm-dev liblzma-dev lzma lzma-dev libgdbm-dev -y
apt-get install libpng-dev libfreetype6-dev -y

apt-get install ccache -y

apt-get install python3 python3-pip python3-venv python3-dev -y

su vagrant << EOF

cd /home/vagrant
python3 -m venv venv
. venv/bin/activate
pip install patchelf nuitka
EOF
