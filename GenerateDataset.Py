import os
import glob
import numpy as np
import matplotlib.pyplot as plt

# Set the base directory
base_dir = 'path/to/files'

# Get a list of all the files in the base directory
files = glob.glob(os.path.join(base_dir, '*'))

# Initialize an empty list to store the data
data = []

# Loop through the files
for file in files:
    # Check the file extension
    if file.endswith('.jpg'):
        # Load the image and store it in the data list
        image = plt.imread(file)
        data.append(image)
    elif file.endswith('.mp3'):
        # Load the audio and store it in the data list
        audio, sr = librosa.load(file)
        data.append(audio)
    elif file.endswith('.mp4'):
        # Load the video and store it in the data list
        video = cv2.VideoCapture(file)
        success, image = video.read()
        while success:
            data.append(image)
            success, image = video.read()

# Convert the data list to a NumPy array
data = np.array(data)

# Do something with the data, such as splitting it into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# This code will loop through all the files in the base directory, check the file extension, and load the data into a list depending on the type of file it is. You can then use the data list to create a NumPy array and perform any further preprocessing or data manipulation as needed.

#Note that this is just a basic example, and you may need to modify the code depending on your specific requirements and the structure of your dataset.
