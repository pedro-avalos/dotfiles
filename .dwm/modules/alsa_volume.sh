#!/usr/bin/env sh

alsa_volume() {
		STATUS=$( amixer sget Master | tail -n1 | sed -r "s/.*\[(.*)\]/\1/" )
		VOL=$( amixer sget Master | tail -n1 | sed -r "s/.*\[(.*)%\].*/\1/" )

		printf -- "%s" "${SEPL}"
		if [ "${STATUS}" = "off" ] ; then
				printf -- "MUTE"
		else
				printf -- "VOL %s%%" "${VOL}"
		fi
		printf -- "%s" "${SEPR}"
}

alsa_volume
