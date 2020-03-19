import commands
if __name__ == "__main__":
    print "Hello"
    re=commands.getstatusoutput("for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev | grep ttyUSB);\
         do udevadm info -q property --export -p `dirname $sysdevpath` |\
         grep --color=never  'DEVNAME\|ID_SERIAL_SHORT';done")
    print re