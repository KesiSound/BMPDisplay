#RAN BEFORE START:
#FOR DISPLAY:
# sudo python -m pip install --upgrade pip setuptools wheel
# git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
# cd Adafruit_Python_SSD1306
# sudo python setup.py install
#FOR BMP280:
# sudo pip3 install adafruit-circuitpython-bmp280

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
import board
import digitalio
import busio
import adafruit_bmp280
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280.sea_level_pressure = 1013.25



# Raspberry Pi pin configuration:
RST = 24

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_address=0x3D)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
top = padding
bottom = height-padding

#Load default font
font = ImageFont.load_default()
test = ":("
while True:
   temperature = bmp280.temperature
   pressure = bmp280.temperature
   altitude = bmp280.altitude
   # Write two lines of text.
   draw.rectangle((0,0,width,height), outline=0, fill=0)
   draw.text((padding, -2),    'Temperature: ',  font=font, fill=455)
   draw.text((75, -2), str(temperature) , font=font, fill=255)
   draw.text((padding, 8),   'Altitude: ',   font=font, fill=455)
   draw.text((55, 8), str(altitude) , font=font, fill=255)
   draw.text((padding, 18),    'Pressure: ',  font=font, fill=255)
   draw.text((55, 18), str(pressure) , font=font, fill=255)

   # Display image.
   disp.image(image)
   disp.display()
   time.sleep(1)




