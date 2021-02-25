# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import digitalio
import busio
import board
from adafruit_epd.epd import Adafruit_EPD
from adafruit_epd.il0373 import Adafruit_IL0373
from adafruit_epd.il91874 import Adafruit_IL91874  # pylint: disable=unused-import
from adafruit_epd.il0398 import Adafruit_IL0398  # pylint: disable=unused-import
from adafruit_epd.ssd1608 import Adafruit_SSD1608  # pylint: disable=unused-import
from adafruit_epd.ssd1675 import Adafruit_SSD1675  # pylint: disable=unused-import

# create the spi device and pins we will need
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.D12)
dc = digitalio.DigitalInOut(board.D11)
srcs = digitalio.DigitalInOut(board.D10)  # can be None to use internal memory
rst = digitalio.DigitalInOut(board.D9)  # can be None to not use this pin
busy = digitalio.DigitalInOut(board.D5)  # can be None to not use this pin

# give them all to our driver
print("Creating display")
# display = Adafruit_SSD1608(200, 200, spi,        # 1.54" HD mono display
# display = Adafruit_SSD1675(122, 250, spi,        # 2.13" HD mono display
# display = Adafruit_IL91874(176, 264, spi,        # 2.7" Tri-color display
# display = Adafruit_IL0373(152, 152, spi,         # 1.54" Tri-color display
# display = Adafruit_IL0373(128, 296, spi,         # 2.9" Tri-color display
# display = Adafruit_IL0398(400, 300, spi,         # 4.2" Tri-color display
display = Adafruit_IL0373(
    104,
    212,
    spi,  # 2.13" Tri-color display
    cs_pin=ecs,
    dc_pin=dc,
    sramcs_pin=srcs,
    rst_pin=rst,
    busy_pin=busy,
)

# IF YOU HAVE A FLEXIBLE DISPLAY (2.13" or 2.9") uncomment these lines!
# display.set_black_buffer(1, False)
# display.set_color_buffer(1, False)

display.rotation = 1

# clear the buffer
print("Clear buffer")
display.fill(Adafruit_EPD.WHITE)
display.pixel(10, 100, Adafruit_EPD.BLACK)

print("Draw Rectangles")
display.fill_rect(5, 5, 10, 10, Adafruit_EPD.RED)
display.rect(0, 0, 20, 30, Adafruit_EPD.BLACK)

print("Draw lines")
display.line(0, 0, display.width - 1, display.height - 1, Adafruit_EPD.BLACK)
display.line(0, display.height - 1, display.width - 1, 0, Adafruit_EPD.RED)

print("Draw text")
display.text("hello world", 25, 10, Adafruit_EPD.BLACK)
display.display()
