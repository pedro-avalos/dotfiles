#!/usr/bin/env bash

# See https://documentation.ubuntu.com/lxd/en/latest/howto/network_bridge_firewalld/#prevent-connectivity-issues-with-lxd-and-docker
sudo iptables  -I DOCKER-USER -i lxdbr0 -j ACCEPT
sudo ip6tables -I DOCKER-USER -i lxdbr0 -j ACCEPT
sudo iptables  -I DOCKER-USER -o lxdbr0 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo ip6tables -I DOCKER-USER -o lxdbr0 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
