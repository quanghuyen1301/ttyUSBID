# ttyUSBID
List | Sort | Converter ttyUSB id to serial number
## Install
	$git clone https://github.com/quanghuyen1301/ttyUSBID.git
	$cd ttyUSBID 
	$pip install .
## List ttyUSB id and serial number Sort by kernel mount ttyUSB
	$python -m ttyUSBID
	TIME TTYUSB SERIAL
	[2644609.259334] ttyUSB5 FTHK9JP9  --> New device
	[2644606.689701] ttyUSB4 FTBELQCK
	[2467077.574854] ttyUSB8 A10179GG
	[2467002.839031] ttyUSB9 AC01X49W
	[1865270.430936] ttyUSB7 AM00F4EM
	[1805605.119032] ttyUSB1 A6018654
	[1365036.902674] ttyUSB3 FTAWCC3C
	[1365022.519438] ttyUSB2 FTAXN4DG
	[1365016.055157] ttyUSB0 FTAXMM1E
## Converter ttyUSB id to serial number
	$python -m ttyUSBID ttyUSB0
	FTAXMM1E
## Converter serial number to ttyUSB id
	$python -m ttyUSBID FTAXMM1E
	ttyUSB0
## Open ttyUSB via serial number
	$minicom -D /dev/`python -m ttyUSBID FTAXMM1E`
	$kermit -c -y .kermit_`python -m ttyUSBID FTAXMM1E`
