#!/usr/bin/env sh
# This script fixes some weird bluetooth issues I have on my desktop.

sudo rmmod btusb
sudo rmmod btintel

sudo modprobe btintel
sudo modprobe btusb
