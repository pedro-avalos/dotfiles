#!/usr/bin/env bash

i3status --config ~/.config/i3/i3status.conf | while :
do
	read line
	# Add language
	LG=$(setxkbmap -query | awk '/layout/{print $2}')
	dat="[{ \"name\": \"language\", \"full_text\": \"KB ${LG}\" },"
	echo "${line/[/$dat}" || exit 1
done
