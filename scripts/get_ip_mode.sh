#!/bin/bash
#

mode=$(grep -v ^# /etc/network/interfaces | grep enp0s8 | grep -i iface | awk '{print $4}')
echo -n $mode
