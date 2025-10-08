import os
from PIL import Image
from typing import List, Dict

class EmotionLoader:
    def __init__(self, emotions_dir="emotions"):
        self.emotions_dir = emotions_dir
        self.emotions = {}
        self.load_all_emotions()
    
    def load_all_emotions(self):
        """Load all emotions from the emotions directory"""
        if not os.path.exists(self.emotions_dir):
            print(f"Warning: Emotions directory '{self.emotions_dir}' not found")
            return
        
        # Get all subdirectories (each represents an emotion)
        emotion_folders = [f for f in os.listdir(self.emotions_dir) 
                          if os.path.isdir(os.path.join(self.emotions_dir, f))]
        
        for emotion_name in emotion_folders:
            self.emotions[emotion_name] = self.load_emotion_frames(emotion_name)
        
        print(f"Loaded {len(self.emotions)} emotions: {list(self.emotions.keys())}")
    
    def load_emotion_frames(self, emotion_name: str) -> List[Image.Image]:
        """Load all frames for a specific emotion"""
        emotion_path = os.path.join(self.emotions_dir, emotion_name)
        frames = []
        
        # Get all PNG files in the emotion folder
        frame_files = sorted([f for f in os.listdir(emotion_path) if f.endswith('.png')])
        
        for frame_file in frame_files:
            frame_path = os.path.join(emotion_path, frame_file)
            try:
                img = Image.open(frame_path)
                # Convert to 1-bit (black and white) for OLED display
                img = img.convert('1')
                frames.append(img)
            except Exception as e:
                print(f"Error loading frame {frame_path}: {e}")
        
        print(f"  - {emotion_name}: {len(frames)} frames")
        return frames
    
    def get_emotion(self, emotion_name: str) -> List[Image.Image]:
        """Get frames for a specific emotion"""
        if emotion_name not in self.emotions:
            print(f"Warning: Emotion '{emotion_name}' not found")
            return []
        return self.emotions[emotion_name]
    
    def get_emotion_names(self) -> List[str]:
        """Get list of all available emotion names"""
        return list(self.emotions.keys())
    
    def has_emotion(self, emotion_name: str) -> bool:
        """Check if an emotion exists"""
        return emotion_name in self.emotions

