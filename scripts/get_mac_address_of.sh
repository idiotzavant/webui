#!/bin/bash
#

eth=$1
ret=$(ifconfig $eth 2>/dev/null | grep HWaddr | awk '{print $5}')
echo -n $ret
