from oled_display import OLEDDisplay
from emotion_loader import EmotionLoader
import time

def main():
    display = OLEDDisplay()
    emotion_loader = EmotionLoader()
    
    # Get available emotions
    emotions = emotion_loader.get_emotion_names()
    if not emotions:
        print("No emotions found!")
        return
    
    print(f"Available emotions: {emotions}")
    print(f"Total: {len(emotions)} emotions")
    print("\nStarting emotion display loop...")
    print("Press Ctrl+C to stop\n")
    
    try:
        # Infinite loop to continuously cycle through all emotions
        while True:
            for emotion_name in sorted(emotions):  # Sort for consistent order
                frames = emotion_loader.get_emotion(emotion_name)
                
                if not frames:
                    print(f"⚠️  Skipping {emotion_name} - no frames loaded")
                    continue
                
                # Display emotion info
                print(f"▶️  Playing: {emotion_name} ({len(frames)} frames)")
                
                # Play the animation
                # Adjust FPS based on number of frames for smooth playback
                fps = 30 if len(frames) > 50 else 20
                display.display_animation(frames, fps=fps, loop=1)
                
                # Brief pause between emotions
                time.sleep(0.3)
            
            print("\n🔄 Completed one full cycle. Restarting...\n")
            time.sleep(1)  # Pause before restarting the cycle
    
    except KeyboardInterrupt:
        print("\n\n✋ Stopped by user")
        display.clear()
        print("Display cleared. Goodbye!")

if __name__ == "__main__":
    main()
