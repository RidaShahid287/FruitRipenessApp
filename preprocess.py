import os
import numpy as np
import cv2   # Import OpenCV

# Function to load and preprocess images from dataset
def load_dataset(folder):
    images = []
    labels = []

    for label in ["Ripe", "Unripe"]:
        path = os.path.join(folder, label)
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            if img_path.lower().endswith(('.png', '.jpg', '.jpeg')):  # Ensure it's an image
                
                # Read the image using OpenCV
                img = cv2.imread(img_path)
                
                if img is None:
                    print(f"Skipping {img_path}, unable to read.")
                    continue

                # Convert to RGB (since OpenCV loads in BGR format)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Resize image to 100x100
                img = cv2.resize(img, (100, 100))

                # Normalize pixel values (0-1)
                img = img / 255.0

                images.append(img)
                labels.append(1 if label == "Ripe" else 0)  # 1 = Ripe, 0 = Unripe

    return np.array(images), np.array(labels)

# Debugging - Run this script alone to check dataset loading
if __name__ == "__main__":
    X, y = load_dataset("dataset/")
    print(f"Dataset Loaded: {len(X)} images")
    print(f"Labels Distribution: {np.bincount(y)}")
