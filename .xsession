
if [ -r /etc/profile.d/apps-bin-path.sh ] ; then
	source /etc/profile.d/apps-bin-path.sh
fi

exec i3
