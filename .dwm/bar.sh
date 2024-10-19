#!/usr/bin/env sh
# Heavily inspired by: https://github.com/joestandring/dwm-bar

LOC=$( readlink -f "$0" )
DIR=$( dirname "${LOC}" )

export SEPL=" ["
export SEPR="] "

# Source modules
. "${DIR}/modules/battery.sh"
. "${DIR}/modules/nm_network.sh"
. "${DIR}/modules/datetime.sh"
. "${DIR}/modules/alsa_volume.sh"

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

		BATT=$( battery )
		if [ -n "${BATT}" ] ; then
				top="${top}${BATT}"
		fi

		top="${top}$( alsa_volume )"
		top="${top}$( datetime )"
		top="${top}${__NM_NETWORK__}"

		xsetroot -name "${top}"
		sleep 1s
done
