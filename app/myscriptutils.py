import subprocess

def testcall():
    proc = subprocess.Popen(['/home/siem/webui/scripts/test.sh'],stdout=subprocess.PIPE)

def do_staticnetworking(ipaddr,subnetmask,gateway,dns1,dns2):
    proc = subprocess.Popen(['/home/siem/webui/scripts/staticnetworking.sh',ipaddr,subnetmask,gateway,dns1,dns2],stdout=subprocess.PIPE)

def get_ip_mode():
    proc = subprocess.Popen(['/home/siem/webui/scripts/get_ip_mode.sh'],stdout=subprocess.PIPE)
    x = list(proc.stdout)
    ret = x[0].strip()
    return ret

def get_ipaddr():
    proc = subprocess.Popen(['/home/siem/webui/scripts/get_ipaddr.sh'],stdout=subprocess.PIPE)
    x = list(proc.stdout)
    ret = x[0].strip()
    return ret

def get_subnet_mask():
    proc = subprocess.Popen(['/home/siem/webui/scripts/get_subnet_mask.sh'],stdout=subprocess.PIPE)
    x = list(proc.stdout)
    ret = x[0].strip()
    return ret

def get_defaultgwaddr():
    proc = subprocess.Popen(['/home/siem/webui/scripts/get_defaultgwaddr.sh'],stdout=subprocess.PIPE)
    x = list(proc.stdout)
    ret = x[0].strip()
    return ret

def get_dnsservers():
    proc = subprocess.Popen(['/home/siem/webui/scripts/get_dnsservers.sh'],stdout=subprocess.PIPE)
    x = list(proc.stdout)
    ret = x[0].strip()
    return ret.split(' ')

def uptime():  
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return '{} seconds'.format(uptime_seconds)

def get_mac_address_of(eth):
    try:
        proc = subprocess.Popen(['/home/siem/webui/scripts/get_mac_address_of.sh',eth],stdout=subprocess.PIPE)
        x = list(proc.stdout)
        ret = x[0].strip()
        return ret
    except:
        return "not found"
