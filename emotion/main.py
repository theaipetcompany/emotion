from oled_display import OLEDDisplay
from emotion_loader import EmotionLoader
from input_handler import InputHandler

def main():
    display = OLEDDisplay()
    emotion_loader = EmotionLoader()
    input_handler = InputHandler()
    
    # Get available emotions
    emotions = emotion_loader.get_emotion_names()
    if not emotions:
        print("No emotions found!")
        return
    
    print(f"Available emotions: {emotions}")
    
    # Display happy emotion animation
    if emotion_loader.has_emotion("happy"):
        print("Displaying 'happy' emotion animation")
        print("Press SPACE to switch to next emotion")
        happy_frames = emotion_loader.get_emotion("happy")
        # Display first frame and wait
        display.display_image(happy_frames[0])
    else:
        print("'happy' emotion not found")
        return
    
    input_handler.wait_for_space()
    
    # Display angry emotion animation
    if emotion_loader.has_emotion("angry"):
        print("Displaying 'angry' emotion animation")
        print("Animation will loop 2 times")
        angry_frames = emotion_loader.get_emotion("angry")
        display.display_animation(angry_frames, fps=15, loop=2)
        print("Animation complete!")
    else:
        print("'angry' emotion not found")

if __name__ == "__main__":
    main()
