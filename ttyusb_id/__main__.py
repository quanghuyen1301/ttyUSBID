import sys
import commands
def find_in( s, first, last):
    try:
        start = s.index( first ) + len( first ) 
        if last =="":
            end = len(s)
        else:
            end = s.index( last, start ) 
        return s[start:end]
    except ValueError:
        return ""
def tty2id(tty_serials,ttyUSB):
    if ttyUSB.find('tty') != -1:
        for tty_serial in tty_serials:
            if tty_serial.find(ttyUSB) != -1:
                re= find_in(tty_serial,"ID_SERIAL_SHORT='","'")
                if re != "" :return re
    return ttyUSB
def id2tty(tty_serials,ttyUSB):
    if ttyUSB.find('tty') == -1:
        for tty_serial in tty_serials:
            if tty_serial.find(ttyUSB) != -1:
                re= find_in(tty_serial,"/dev/","'")
                if re != "" :return re
    return ttyUSB
def list_ttyusb(tty_serials,tty_dmesgs):
    ttyUSBID = []
    re = []
    for tty_dmesg in reversed(tty_dmesgs):
        ttyUSB = find_in(tty_dmesg," to ","")
        if (ttyUSB !="") and (ttyUSB.find('tty') != -1) and ((ttyUSB in ttyUSBID) == False):
            id = tty2id(tty_serials,ttyUSB)
            if id != ttyUSB:
                ttyUSBID.append(ttyUSB)
                re.append("[%s] %s %s" %(find_in(tty_dmesg,"[","]"),ttyUSB,id))
    return re
def get_ttydata():
    tty_serial=commands.getstatusoutput("for i in $(find /sys/bus/usb/devices/usb*/ -name dev | grep --color=never ttyUSB);\
         do udevadm info -q property --export -p `dirname $i` |\
         grep --color=never  'DEVNAME\|ID_SERIAL_SHORT';done")
    tty_dmesg=commands.getstatusoutput("dmesg | grep 'to ttyUSB'")
    return tty_serial[1].split("DEVNAME="),tty_dmesg[1].replace("\r","").split("\n")
def get_ttydata_ssh(host="root@localhost",hostpass="root",hostprom="~",timeout=1*60):
    import pexpect
    tty = pexpect.spawn ("ssh -o 'StrictHostKeyChecking no' %s" %(host) ,timeout=4*timeout)
    #tty.logfile_read = sys.stdout
    if tty.expect(["password",pexpect.EOF,pexpect.TIMEOUT],timeout=timeout) !=0:
        return "",""
    tty.sendline(hostpass)
    if tty.expect([hostprom,pexpect.EOF,pexpect.TIMEOUT],timeout=timeout) !=0:
        return "",""
    tty.sendline("bash")
    tty.sendline("for i in $(find /sys/bus/usb/devices/usb*/ -name dev | grep --color=never ttyUSB); \
            do udevadm info -q property --export -p `dirname $i` | \
            grep --color=never  'DEVNAME\|ID_SERIAL_SHORT';done;echo -n __DONE__;echo -n __DONE__")
    if tty.expect(["__DONE____DONE__"],timeout=timeout) !=0:
        return "",""
    tty_serial = tty.before.split("DEVNAME=")
    tty.sendline("dmesg | grep --color=never 'to ttyUSB';echo -n __DONE__;echo -n __DONE__")
    if tty.expect(["__DONE____DONE__"],timeout=timeout) !=0:
        return "",""
    tty_dmesg = tty.before.replace("\r","").split("\n")
    return tty_serial,tty_dmesg
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        tty_serials,tty_dmesgs = get_ttydata_ssh(sys.argv[1],sys.argv[2])
    else:
    	tty_serials,tty_dmesgs = get_ttydata()
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        re = list_ttyusb(tty_serials,tty_dmesgs)
        for e in re:
            print e
    if len(sys.argv) == 2 :
        ttyUSB=sys.argv[1]
        if sys.argv[1].find('tty') == -1:
            re = id2tty(tty_serials,ttyUSB)
        else:
            re = tty2id(tty_serials,ttyUSB)
        print re
    if len(sys.argv) >= 4 :
        ttyUSB=sys.argv[3]
        if sys.argv[1].find('tty') == -1:
            re = id2tty(tty_serials,ttyUSB)
        else:
            re = tty2id(tty_serials,ttyUSB)
        print re
