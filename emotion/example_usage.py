"""
Example usage of the emotion display system

This file demonstrates various ways to use emotions from the emotions/ folder
"""

from oled_display import OLEDDisplay
from emotion_loader import EmotionLoader
import time

def example_simple_display():
    """Display a single frame from an emotion"""
    display = OLEDDisplay()
    loader = EmotionLoader()
    
    # Display first frame of happy emotion
    happy_frames = loader.get_emotion("happy")
    if happy_frames:
        display.display_image(happy_frames[0])
        print("Displaying happy emotion (first frame)")

def example_animation():
    """Display an animated emotion"""
    display = OLEDDisplay()
    loader = EmotionLoader()
    
    # Play bootup animation once at 30 fps
    bootup_frames = loader.get_emotion("bootup")
    if bootup_frames:
        print(f"Playing bootup animation ({len(bootup_frames)} frames)")
        display.display_animation(bootup_frames, fps=30, loop=1)

def example_multiple_emotions():
    """Cycle through multiple emotions"""
    display = OLEDDisplay()
    loader = EmotionLoader()
    
    emotions_to_show = ["happy", "excited", "neutral", "sad", "angry"]
    
    for emotion_name in emotions_to_show:
        if loader.has_emotion(emotion_name):
            print(f"Showing {emotion_name}...")
            frames = loader.get_emotion(emotion_name)
            # Play each emotion for 2 loops at 20 fps
            display.display_animation(frames, fps=20, loop=2)
            time.sleep(0.5)  # Brief pause between emotions
        else:
            print(f"Emotion '{emotion_name}' not found, skipping")

def example_custom_sequence():
    """Create a custom sequence of emotions"""
    display = OLEDDisplay()
    loader = EmotionLoader()
    
    # Create a story: bootup -> happy -> excited -> blink
    sequence = [
        ("bootup", 30, 1),    # (emotion_name, fps, loops)
        ("happy", 20, 2),
        ("excited", 25, 3),
        ("blink", 20, 1),
    ]
    
    for emotion_name, fps, loops in sequence:
        if loader.has_emotion(emotion_name):
            print(f"Playing {emotion_name} at {fps}fps, {loops} loop(s)")
            frames = loader.get_emotion(emotion_name)
            display.display_animation(frames, fps=fps, loop=loops)
        else:
            print(f"Warning: {emotion_name} not found")

def list_all_emotions():
    """List all available emotions and their frame counts"""
    loader = EmotionLoader()
    
    print("\n=== Available Emotions ===")
    for emotion_name in loader.get_emotion_names():
        frames = loader.get_emotion(emotion_name)
        print(f"  {emotion_name}: {len(frames)} frames")
    print("========================\n")

if __name__ == "__main__":
    # List available emotions
    list_all_emotions()
    
    # Choose which example to run:
    # example_simple_display()
    # example_animation()
    # example_multiple_emotions()
    # example_custom_sequence()

