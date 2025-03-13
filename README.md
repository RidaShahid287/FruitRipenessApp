🍎 Fruit Ripeness Classifier
This project is a Fruit Ripeness Classifier that uses TensorFlow, Tkinter, and SQLite to predict whether a fruit (e.g., Tomato) is Ripe or Unripe based on an uploaded image.

📌 Features
✔ Graphical User Interface (GUI) to upload an image and get a prediction.
✔ Trained CNN Model (fruit_classifier.h5) to classify fruit ripeness.
✔ SQLite Database for user authentication (Login System).

📌 Project Requirements
✅ System Requirements
Operating System: Windows 10/11
Python Version: 3.10 (TensorFlow does not support Python 3.11)
PIP Version: Latest (upgrade required)

📌 Installation Guide (From Scratch)

🔹 Step 1: Install Python 3.10
Download Python 3.10 from Python Official Site
During installation, check: ✅ Add Python to PATH
Verify Python installation:
❗ Run this command:
python --version

Upgrade pip:
❗ Run this command:
python -m pip install --upgrade pip

🔹 Step 2: Clone the Repository
If Git is installed, clone the project from GitHub:
❗ Run this command:
git clone https://github.com/yourusername/FruitRipenessApp.git
cd FruitRipenessApp
If Git is NOT installed, download the project manually from GitHub.

🔹 Step 3: Create & Activate a Virtual Environment
Create a virtual environment:
❗ Run this command:
python -m venv fruit_env

Activate the virtual environment:
Windows:
❗ Run this command:
fruit_env\Scripts\activate

Mac/Linux:
❗ Run this command:
source fruit_env/bin/activate

🔹 Step 4: Install Required Dependencies
Run the following command to install TensorFlow, Tkinter, and other required packages:
❗ Run this command:
pip install -r requirements.txt

🔹 Step 5: Train the Model (If Not Provided)
If the model fruit_classifier.h5 is not available, train it using:
❗ Run this command:
python train_model.py
This will create and save the model in the models/ directory.

🔹 Step 6: Setting Up the Database
Ensure SQLite is installed (comes pre-installed with Python).
Create the SQLite database:
❗ Run this command:
python main.py
(This will generate fruit_classifier.db in the project folder.)
View the database using DB Browser for SQLite:
Download DB Browser for SQLite here
Open fruit_classifier.db to see the users' table.

🔹 Step 7: Run the GUI Application
To start the application:
❗ Run this command:
python main.py
This will launch a GUI where you can upload an image to classify it as Ripe or Unripe.

🔹 Project Structure
FruitRipenessApp/
├── __pycache__/               # Compiled Python files
├── .git/                      # Git repository metadata
├── database/                  # Database-related files
├── dataset/                   # Dataset for training and testing
├── fruit_env/                 # Virtual environment (should be excluded from Git)
├── images/                    # Folder for storing fruit images
├── models/                    # Machine learning models
│   ├── fruit_classifier.h5    # Trained model file
│   └── test/                  # Model testing files
├── .gitattributes             # Git LFS attributes (if any)
├── .gitignore                 # Git ignore file to exclude unnecessary files
├── all-files.txt              # List of all repository files
├── classify.py                # Script to classify fruit images
├── fruit_classifier.db        # Database file
├── main.py                    # Main entry point for the application
├── preprocess.py              # Preprocessing script for dataset
├── README.md                  # Project documentation
├── requirements.txt           # Dependencies and packages needed
└── train_model.py             # Script to train the fruit classifier model


📌 Technologies Used
Python 3.10
TensorFlow (Deep Learning Model)
Keras (CNN Model)
Pillow (Image Processing)
Tkinter (GUI)
SQLite (Database for user login)

HAPPY CODING!!!
