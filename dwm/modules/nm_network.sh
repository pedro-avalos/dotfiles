#!/usr/bin/env sh
# File: nm_network.sh

nm_network() {
	CONNAME=$( nmcli -a | grep 'Wired connection' | awk -F: '{print $1}' )
	if [ "${CONNAME}" = "" ] ; then
		CONNAME=$( nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -c 5- )
	fi

	export __NM_NETWORK__="${SEPL}NET ${CONNAME}${SEPR}"
}

nm_network
