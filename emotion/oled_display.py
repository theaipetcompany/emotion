import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image

class OLEDDisplay:
    def __init__(self, width=128, height=64):
        self.width = width
        self.height = height
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = SSD1306_I2C(self.width, self.height, self.i2c)
        self.clear()

    def bytes_to_image(self, byte_array):
        img = Image.new("1", (self.width, self.height))
        bytes_per_row = self.width // 8
        pixels = img.load()
        for y in range(self.height):
            for byte_index in range(bytes_per_row):
                byte = byte_array[y * bytes_per_row + byte_index]
                for bit in range(8):
                    x = byte_index * 8 + (7 - bit)
                    if x < self.width:
                        val = (byte >> bit) & 1
                        pixels[x, y] = 255 * val
        return img

    def display_bitmap(self, bitmap):
        img = self.bytes_to_image(bitmap)
        self.oled.image(img)
        self.oled.show()

    def clear(self):
        self.oled.fill(0)
        self.oled.show()
