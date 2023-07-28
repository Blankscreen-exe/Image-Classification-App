import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Load the MobileNetV2 model
# This is the model we saved using the export_model.py script
model = tf.saved_model.load('./model')

# Helper function to preprocess the image for the model
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB') # Remove alpha channel
    image = image.resize((224, 224))  # Resize to match MobileNetV2 input size
    image = np.array(image)  # Convert to numpy array
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)  # Normalize according to MobileNetV2
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Helper function to get the prediction label
def get_prediction_label(predictions):
    predictions = predictions.numpy() # Convert to numpy array
    label = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)
    return label[0][0][1]

# Tkinter GUI
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        # Update the image path label
        image_path_label.configure(text="" + file_path)
        
        img = Image.open(file_path)
        img.thumbnail((300, 250))  # Resize for display
        img = ImageTk.PhotoImage(img)
        image_label.configure(image=img)
        image_label.image = img

        # Preprocess the image
        image = preprocess_image(file_path)

        # Make a prediction
        predictions = model(image)
        prediction_label = get_prediction_label(predictions)

        # Update the prediction text
        prediction_label = prediction_label.replace("_", " ").capitalize()
        result_label.configure(text=prediction_label)

# Create the main Tkinter window
root = tk.Tk()
root.title("Image Classification App")

# window size
root.geometry("400x400")

# Descriptive Text
text_desc = tk.Label(root, text="⚡️Image Classification App ⚡️", font=("Helvetica", 13, 'bold'), fg="#149EF0")
text_desc.pack(pady=5, padx=0)

# Button to browse image
browse_button = tk.Button(root, text="Browse Image", command=browse_image, bg="#149EF0", fg="white")
browse_button.pack(pady=2)

# Descriptive Text
text_desc = tk.Label(root, text="Acceptable image formats: .png, .jpg, .jpeg", font=("Helvetica", 10))
text_desc.pack(pady=0, padx=0)

# Image path label
image_path_label = tk.Label(root, font=("Helvetica", 10), fg="#979797")
image_path_label.pack(pady=0)

# Image display
image_label = tk.Label(root)
image_label.pack()

# Result text box
result_label = tk.Label(root, text="Results Will Appear Here", font=("Helvetica", 12, 'bold'), bg="#CEE3F8", fg="#149EF0", padx=500, pady=0)
result_label.pack(pady=2)

# Start the Tkinter event loop
root.mainloop()
