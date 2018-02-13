#!/bin/bash
#

enp0s8_ipaddr=$(ip addr show enp0s8 | grep 'inet '|awk '{print $2}'|cut -d'/' -f1) >/dev/null
echo -n $enp0s8_ipaddr

