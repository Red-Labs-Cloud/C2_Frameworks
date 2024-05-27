



adduser debian
usermod -aG sudo debian

vi /etc/systemd/system/cobaltc2.service



sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw allow 500,4500/udp