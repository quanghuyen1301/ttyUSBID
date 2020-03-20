# ttyUSBID
Local/ssh List | Sort | Converter ttyUSB id to serial number
## Install
	$git clone https://github.com/quanghuyen1301/ttyUSBID.git
	$cd ttyUSBID 
	$pip install .
## List ttyUSB id and serial number Sort by kernel mount ttyUSB
	$python -m ttyUSBID
	[1805605.119032] ttyUSB1 A6018654
	[1365036.902674] ttyUSB3 FTAWCC3C
	[1365022.519438] ttyUSB2 FTAXN4DG
	[1365016.055157] ttyUSB0 FTAXMM1E
## List ttyUSB id and serial via ssh
	$python -m ttyUSBID <user@hostip> <password>
	$python -m ttyUSBID root@localhost root
	[1805605.119032] ttyUSB1 A6018654
	[1365036.902674] ttyUSB3 FTAWCC3C
	[1365022.519438] ttyUSB2 FTAXN4DG
	[1365016.055157] ttyUSB0 FTAXMM1E

	
## Converter ttyUSB id to serial number
	$python -m ttyUSBID ttyUSB0
	FTAXMM1E
## Converter ttyUSB serial number to id
	$python -m ttyUSBID FTAXMM1E
	ttyUSB0
## Converter ttyUSB serial number via ssh
	$python -m ttyUSBID <user@hostip> <password> [ttyUSB0|FTAXMM1E]
	ttyUSB0
## Open ttyUSB via serial number
	$minicom -D /dev/``python -m ttyUSBID FTAXMM1E``
