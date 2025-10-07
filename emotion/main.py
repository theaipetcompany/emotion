import bitmaps
from oled_display import OLEDDisplay
from input_handler import InputHandler

def main():
    display = OLEDDisplay()
    input_handler = InputHandler()

    display.display_bitmap(bitmaps.happy_bitmap)
    print("Press SPACE to switch to angry face")

    input_handler.wait_for_space()

    display.display_bitmap(bitmaps.angry_bitmap)
    print("Switched to angry face")

if __name__ == "__main__":
    main()
