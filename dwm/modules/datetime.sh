#!/usr/bin/env sh
# File: datetime.sh

datetime() {
	printf -- "%s" "${SEPL}"
	printf -- "DAT %s" "$( date "+%Y-%m-%d (%a) %H:%M" )"
	printf -- "%s" "${SEPR}"
}

datetime

# vim: ft=sh
