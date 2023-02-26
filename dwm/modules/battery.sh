#!/usr/bin/env sh
# File: battery.sh

battery() {
	CAPACITY=$( cat /sys/class/power_supply/BAT0/capacity )
	STATUS=$( cat /sys/class/power_supply/BAT0/status )

	printf -- "%s" "${SEPL}"
	printf -- "BAT %s%% %s" "${CAPACITY}" "${STATUS}"
	printf -- "%s" "${SEPR}"
}

battery

# vim: ft=sh
