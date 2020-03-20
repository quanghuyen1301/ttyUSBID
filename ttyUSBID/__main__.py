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
def get_ttydata():
    tty_serial=commands.getstatusoutput("for i in $(find /sys/bus/usb/devices/usb*/ -name dev | grep ttyUSB);\
         do udevadm info -q property --export -p `dirname $i` |\
         grep --color=never  'DEVNAME\|ID_SERIAL_SHORT';done")
    tty_dmesg=commands.getstatusoutput("dmesg | grep 'to ttyUSB'")
    return tty_serial[1].split("DEVNAME="),tty_dmesg[1].split("\n")
if __name__ == "__main__":
    tty_serials,tty_dmesgs = get_ttydata()
    if len(sys.argv) == 1 :
        print "TIME TTYUSB SERIAL"
        ttyUSBID=[]
        for tty_dmesg in reversed(tty_dmesgs):
            ttyUSB=find_in(tty_dmesg," to ","")
            if (ttyUSB !="") and (ttyUSB.find('tty') != -1) and ((ttyUSB in ttyUSBID) == False):
                id = tty2id(tty_serials,ttyUSB)
                if id != ttyUSB:
                    ttyUSBID.append(ttyUSB)
                    print "[%s] %s %s" %(find_in(tty_dmesg,"[","]"),ttyUSB,id)
    if len(sys.argv) >= 2 :
        ttyUSB=sys.argv[1]
        if sys.argv[1].find('tty') == -1:
            re = id2tty(tty_serials,ttyUSB)
        else:
            re = tty2id(tty_serials,ttyUSB)
        print re