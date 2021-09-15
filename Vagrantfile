# -*- mode: ruby -*-
# vi: set ft=ruby :

# Usage:
#
# $ vagrant up
# $ vagrant ssh
# $ cd /vagrant/
# $ make serve
#
# Then, use a browser to visit http://localhost:1313/
#
Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-21.04"

  ENV['LC_ALL']="en_US.UTF-8"
  
  config.vm.network "forwarded_port", guest: 1313, host: 1313

  config.vm.provision "shell", inline: <<-SHELL
    locale-gen en_US.UTF-8
    apt-get update
    apt-get install -y make hugo python3-pip
    pip3 install requests
  SHELL
end

