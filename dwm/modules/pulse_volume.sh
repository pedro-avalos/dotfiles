#!/usr/bin/env sh
# File: pulse_volume.sh

pulse_volume() {
	STATUS=$( pamixer --get-mute )
	VOL=$( pamixer --get-volume )

	printf -- "%s" "${SEPL}"
	if [ "${STATUS}" = "true" ] ; then 
		printf -- "MUTE"
	else
		printf -- "VOL %s%%" "${VOL}"
	fi
	printf -- "%s" "${SEPR}"
}

pulse_volume

# vim: ft=sh
