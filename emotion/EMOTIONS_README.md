# Emotion Display System

This system allows you to easily display emotions on the OLED screen using image files instead of hardcoded bitmaps.

## 📁 Folder Structure

```
emotion/
├── emotions/           # Emotion animations folder
│   ├── happy/         # Each emotion has its own folder
│   │   ├── frame0.png
│   │   ├── frame1.png
│   │   └── ...
│   ├── angry/
│   ├── sad/
│   └── ...
├── emotion_loader.py  # Loads emotions from folders
├── oled_display.py   # Displays on OLED screen
└── main.py          # Main application
```

## 🚀 Quick Start

### Basic Usage

```python
from oled_display import OLEDDisplay
from emotion_loader import EmotionLoader

# Initialize
display = OLEDDisplay()
loader = EmotionLoader()

# Display a single frame
happy_frames = loader.get_emotion("happy")
display.display_image(happy_frames[0])

# Display an animation
display.display_animation(happy_frames, fps=20, loop=2)
```

## 📝 How It Works

### 1. EmotionLoader Class

The `EmotionLoader` automatically scans the `emotions/` folder and loads all emotion animations:

```python
loader = EmotionLoader()

# Get all available emotions
emotions = loader.get_emotion_names()
print(emotions)  # ['happy', 'angry', 'sad', 'excited', ...]

# Get frames for a specific emotion
frames = loader.get_emotion("happy")

# Check if emotion exists
if loader.has_emotion("happy"):
    # Do something
```

### 2. OLEDDisplay Class

Enhanced with new methods to display images and animations:

```python
display = OLEDDisplay()

# Display a single image
display.display_image(image)

# Display an animation
display.display_animation(frames, fps=30, loop=1)

# Legacy bitmap support still works
display.display_bitmap(bitmap_array)
```

## ✨ Adding New Emotions

Adding a new emotion is super easy - just create a new folder!

1. Create a folder in `emotions/` with your emotion name:
   ```
   emotions/my_new_emotion/
   ```

2. Add your frame images (PNG format recommended):
   ```
   emotions/my_new_emotion/
   ├── frame0.png
   ├── frame1.png
   ├── frame2.png
   └── ...
   ```

3. The frames will be automatically loaded in alphabetical/numerical order

4. Use it in your code:
   ```python
   frames = loader.get_emotion("my_new_emotion")
   display.display_animation(frames, fps=20, loop=1)
   ```

## 🎨 Image Requirements

- **Format**: PNG (recommended), or any PIL-supported format
- **Size**: Any size (will be auto-resized to 128x64 for the OLED)
- **Color**: Any (will be auto-converted to 1-bit black/white)
- **Naming**: Frames should be named in order (frame0.png, frame1.png, etc.)

## 🎬 Animation Control

The `display_animation()` method accepts these parameters:

- `frames`: List of PIL Image objects
- `fps`: Frames per second (default: 30)
- `loop`: Number of times to loop (default: 1, use 0 for infinite)

```python
# Play once at 30 fps
display.display_animation(frames, fps=30, loop=1)

# Play 3 times at 20 fps
display.display_animation(frames, fps=20, loop=3)

# Loop forever at 15 fps
display.display_animation(frames, fps=15, loop=0)
```

## 📚 Examples

See `example_usage.py` for complete examples including:
- Simple single frame display
- Animation playback
- Multiple emotion sequences
- Custom emotion stories

## 🔄 Migration from Bitmaps

If you have old code using bitmaps:

**Old way (bitmaps.py):**
```python
import bitmaps
display.display_bitmap(bitmaps.happy_bitmap)
```

**New way (emotion loader):**
```python
from emotion_loader import EmotionLoader
loader = EmotionLoader()
frames = loader.get_emotion("happy")
display.display_image(frames[0])  # Single frame
# OR
display.display_animation(frames, fps=20, loop=1)  # Animation
```

## 💡 Tips

1. **Frame naming**: Use consistent naming like `frame0.png`, `frame1.png` for proper ordering
2. **Performance**: Fewer frames = faster loading, but smoother animations need more frames
3. **File size**: OLED is only 128x64 pixels, so high-resolution images aren't necessary
4. **Testing**: Use `example_usage.py` to test new emotions before using them in your main app

## 🐛 Troubleshooting

**"No emotions found!"**
- Make sure the `emotions/` folder exists
- Check that emotion folders contain .png files

**Animation looks choppy:**
- Try adjusting the `fps` parameter
- Ensure you have enough frames for smooth motion

**Emotion not loading:**
- Check the folder name matches exactly (case-sensitive)
- Verify PNG files are not corrupted
- Check console output for error messages

