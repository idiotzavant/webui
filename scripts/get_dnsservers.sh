#!/bin/bash
#

ret=$(grep -v ^# /etc/resolv.conf | grep '^nameserver' | awk '{print $2}'|tr '\n' ' ')
echo -n $ret
