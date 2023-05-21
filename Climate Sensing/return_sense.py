		


	import sdcard
	import uos

	# Assign chip select (CS) pin (and start it high)
	cs = machine.Pin(7, machine.Pin.OUT)

	# Intialize SPI peripheral 
	spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(23),
                  mosi=machine.Pin(9),
                  miso=machine.Pin(10))

	# Initialize SD card
	sd = sdcard.SDCard(spi, cs)

	# filesystem
	vfs = uos.VfsFat(sd)
	uos.mount(vfs, "/sd")

	# Create file 
	with open("/sd/.txt", "w") as file:
   	 
