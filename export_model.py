"""
use this script to export and save any model to the 'model' directory (change the path to your prefered one)

Remember that we are using a pre-trained model. If you want a custom trained model, then you will have to train it 
yourself and then export using the code below. 
"""
import os
import tensorflow as tf # used for exporting and importing a model
from tensorflow.keras.applications import MobileNetV2 # a pre trained model

# Load the MobileNetV2 model (without the top classification layer, for feature extraction)
model_to_save = MobileNetV2(weights='imagenet', include_top=True, input_shape=(224, 224, 3))

# Define a directory where you want to save the model
save_path = 'model/'

# Create the directory if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Save the model
# tf.saved_model.save(model_to_save, save_path)
tf.saved_model.save(
    model_to_save, 
    save_path
)