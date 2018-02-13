#!/bin/bash
#

if [ $# -lt 4 ];then
    echo "not enough params"
    exit 1
fi

address=$1
netmask=$2
gateway=$3
shift
shift
shift
dnsservers="$@"

sudo sed -i '/^#beginstatic_/,/^#endstatic_/{/^#/!{/^\$/!d}}' /etc/network/interfaces
sudo sed -i '/^#beginstatic_/d' /etc/network/interfaces
sudo sed -i '/^#endstatic_/d' /etc/network/interfaces

sudo sed -i '/enp0s8/d' /etc/network/interfaces

cat << EOF > /tmp/tmp1.output
#beginstatic_enp0s8
auto enp0s8
iface enp0s8 inet static
address ${address}
netmask ${netmask}
gateway ${gateway}
dns-nameservers ${dnsservers}
#endstatic_enp0s8
EOF

cat /tmp/tmp1.output | sudo tee --append /etc/network/interfaces >/dev/null
