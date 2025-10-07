# Emotion Face Display 

This is a modular Python application to display animated emotion faces (e.g., happy, angry) on an OLED display. It is designed to run primarily on Raspberry Pi with SSD1306 OLED displays, but can be adapted for PC environments with simulation.


## Structure
    ├── emotion/
    │   ├── bitmaps.py       # Contains byte arrays representing different emotion faces as bitmaps
    │   ├── oled_display.py  # Manages OLED display initialization and rendering bitmaps to the screen
    │   ├── input_handler.py # Handles user input for switching between different emotion faces
    │   ├── main.py          # Main entry point, coordinates display and input handler to switch faces interactivel
    │   ├── requirements.txt # Specifies Python dependencies and versions
    ├── README.md        # General information 


## Installation Steps

### 1. Connect the OLED display

Connect the display pins as shown:
- GND → Ground  
- VCC → 3.3V  
- SCL → GPIO3 (Pin 5)  
- SDA → GPIO2 (Pin 3)

![Display connections](./image/connections.jpeg)

### 2. Upgrade Raspberry Pi firmware and reboot

```bash
sudo apt-get update
sudo apt-get -y upgrade
sudo reboot
```

### 3. Install Python pip and upgrade setuptools

```bash
sudo apt-get install python3-pip
sudo apt install --upgrade python3-setuptools
```

### 4. Create a Python virtual environment

This is required on Raspberry Pi OS Bookworm and later.

```bash
sudo apt install python3-venv
python3 -m venv stats_env --system-site-packages
source stats_env/bin/activate
```

### 5. Verify I2C device connection

To check whether the OLED display is connected and recognized, run:

```bash
sudo i2cdetect -y 1
```

Look for the address 3c in the output grid, which is the default I2C address for the SSD1306 OLED display.

Example output:

```bash
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00: -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

> If the address `3c` does not appear, double-check your wiring and ensure that I2C is enabled (next step).

### 6. Enable I2C interface if needed:

```bash
sudo raspi-config
```

Navigate to:
- 3 Interfacing Options
- I5 I2C
- Select Yes to enable
- Select OK and then Finish

Reboot the Raspberry Pi if prompted.

### 7. Install Required System Libraries for Building Python Packages

Make sure you are inside the `stats_env` virtual environment.

```bash
source stats_env/bin/activate
```

Then install development libraries needed to build packages like pygame and Pillow:

```bash
sudo apt-get install build-essential libfreetype6-dev libjpeg-dev \
pkg-config python3-dev libffi-dev libsdl2-dev libsdl2-image-dev \
libsdl2-mixer-dev libsdl2-ttf-dev
```

### 8. Install Project Python Dependencies

Inside the activated virtual environment, run:

```bash
pip install -r requirements.txt
```

This will install:
- adafruit-blinka (CircuitPython compatibility layer)
- adafruit-circuitpython-ssd1306 (OLED driver)
- Pillow (Python image processing library)
- pygame (for input and display simulation)
- keyboard (keyboard input library)

### 9. Download and Run the project code

Exit the virtual environment:

```bash
deactivate
```

Install git if needed:

```bash
sudo apt-get install git
```

Clone the repository:

```bash
git clone https://github.com/.git
```

Re-enter the virtual environment and change directory:

```bash
source venv/bin/activate
cd emotion
```

Run the main application:

```bash
python3 main.py
```

Troubleshooting
- If keyboard events do not register: You may need to run with sudo:

```bash
sudo python3 main.py
```

- If installation of pygame or Pillow fails, ensure step 7 libraries are installed and try reinstalling.
- The OLED display must use SSD1306 controller. SH1106 is incompatible.

## Usage Notes
- The program displays a happy face initially.
- Press the spacebar to switch to the angry face.
- The display updates continuously until the program stops.

## Additional Resources

- [Adafruit Blinka](https://github.com/adafruit/Adafruit_Blinka)  
- [CircuitPython SSD1306](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306)  

