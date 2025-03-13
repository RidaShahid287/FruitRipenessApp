import numpy as np
import cv2  # Import OpenCV
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("models/fruit_classifier.h5")

# Function to classify an image
def classify_image(image_path):
    try:
        # Read image using OpenCV
        img = cv2.imread(image_path)

        if img is None:
            return "Error: Cannot read image."

        # Convert to RGB format (since OpenCV loads in BGR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Resize image to match model input size
        img = cv2.resize(img, (100, 100))

        # Normalize (convert pixel values to range 0-1)
        img = img / 255.0

        # Expand dimensions to match model input shape
        img = np.expand_dims(img, axis=0)

        # Predict using the model
        prediction = model.predict(img)[0][0]

        # Interpret results
        return "Ripe" if prediction > 0.3 else "Unripe"

    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return "Error"
