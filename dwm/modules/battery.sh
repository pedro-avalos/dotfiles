#!/usr/bin/env sh

battery() {
		if [ -d /sys/class/power_supply/BAT0 ] ; then
				CAPACITY=$( cat /sys/class/power_supply/BAT0/capacity )
				STATUS=$( cat /sys/class/power_supply/BAT0/status )
				printf -- "%s" "${SEPL}"
				printf -- "BAT %s%% %s" "${CAPACITY}" "${STATUS}"
				printf -- "%s" "${SEPR}"
		else
				printf -- ""
		fi
}

battery
