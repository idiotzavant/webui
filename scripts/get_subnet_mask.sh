#!/bin/bash
#

mode=$(grep -v ^# /etc/network/interfaces | grep enp0s8 | grep -i iface | awk '{print $4}')
if [[ "$mode" = 'static' ]];then
    ret=$(sed -n '/^#beginstatic_/,/^#endstatic_/{/^#/!{/^\$/!p}}' /etc/network/interfaces | grep netmask | awk '{print $2}')
    echo -n $ret
else
    echo -n '255.255.255.0'
fi
