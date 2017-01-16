# -*- mode: ruby -*-
# vi: set ft=ruby :

# Usage:
#
# $ vagrant up
# $ vagrant ssh
# $ cd /vagrant/
# $ make devserver
#
# Then, use a browser to visit http://localhost:8000/
#
Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-16.04"

  ENV['LC_ALL']="en_US.UTF-8"
  
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    locale-gen en_US.UTF-8
    apt-get update
    apt-get install -y python-pip
    pip install pelican markdown ghp-import
  SHELL
end

