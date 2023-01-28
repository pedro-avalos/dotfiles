#!/usr/bin/env bash
# File: print_colors.sh
# Author: Pedro Avalos

for cmd in sgr0 bold ; do
  tput ${cmd}
  for i in $(seq 0 7) ; do
    for j in $(seq 0 7) ; do
      tput setaf "${i}" ; tput setab "${j}" ; echo -n " ${i},${j} "
    done
    tput sgr0 ; echo ; tput ${cmd}
  done
done
