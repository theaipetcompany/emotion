import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image
import time

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
        """Display a bitmap from byte array (legacy support)"""
        img = self.bytes_to_image(bitmap)
        self.oled.image(img)
        self.oled.show()
    
    def display_image(self, image):
        """Display a PIL Image directly"""
        # Resize image to fit OLED if needed
        if image.size != (self.width, self.height):
            image = image.resize((self.width, self.height))
        
        # Ensure image is in 1-bit mode
        if image.mode != '1':
            image = image.convert('1')
        
        self.oled.image(image)
        self.oled.show()
    
    def display_animation(self, frames, fps=30, loop=1):
        """
        Display an animation from a list of PIL Images
        
        Args:
            frames: List of PIL Image objects
            fps: Frames per second
            loop: Number of times to loop the animation (0 for infinite)
        """
        if not frames:
            print("No frames to display")
            return
        
        frame_delay = 1.0 / fps
        loops = 0
        
        while True:
            for frame in frames:
                self.display_image(frame)
                time.sleep(frame_delay)
            
            loops += 1
            if loop > 0 and loops >= loop:
                break

    def clear(self):
        self.oled.fill(0)
        self.oled.show()
