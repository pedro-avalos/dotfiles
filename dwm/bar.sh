#!/usr/bin/env sh
# bar.sh

LOC=$( readlink -f "$0" )
DIR=$( dirname "${LOC}" )

export SEPL=" ["
export SEPR="] "

# Source modules
. "${DIR}/modules/battery.sh"
. "${DIR}/modules/nm_network.sh"

# Run these updates in parallel
parallelize() {
	while true; do
		nm_network &
		sleep 5s
	done
}
parallelize &

# Update status bar
while true ; do
	top=""
	top="${top}$( battery )"
	top="${top}${__NM_NETWORK__}"

	xsetroot -name "${top}"
	sleep 1s
done

# vim: ft=sh
