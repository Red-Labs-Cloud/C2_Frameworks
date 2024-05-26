#!/bin/bash




function install_ansible {
  # Update package lists
  sudo apt update

  # Install required dependencies
  sudo apt install -y apt-transport-https python3-pip

  # Add Ansible repository
  echo "deb http://ppa.ansible.com/debian bullseye stable" | sudo tee /etc/apt/sources.list.d/ansible.list

  # Import signing key
  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD754CE36E

  # Update package lists again
  sudo apt update

  # Install Ansible
  sudo apt install -y ansible

  echo "Ansible installation complete!"
}

# Call the function
install_ansible