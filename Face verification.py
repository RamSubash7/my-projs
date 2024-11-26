import cv2
import numpy as np
from deepface import DeepFace
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to select image file
def select_image1():
    file_path = filedialog.askopenfilename(title="Select the First Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image1_entry.delete(0, tk.END)
        image1_entry.insert(0, file_path)

# Function to select second image file
def select_image2():
    file_path = filedialog.askopenfilename(title="Select the Second Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image2_entry.delete(0, tk.END)
        image2_entry.insert(0, file_path)

# Function to verify faces using DeepFace
def verify_faces():
    # Get image paths from the entry fields
    image1_path = image1_entry.get()
    image2_path = image2_entry.get()

    # Load images
    try:
        img1 = cv2.imread(image1_path)
        img2 = cv2.imread(image2_path)
        
        if img1 is None or img2 is None:
            raise ValueError("One or both images not found.")
        
        # Verify faces using DeepFace
        result = DeepFace.verify(img1, img2, model_name="Facenet")
        
        # Extract results
        match = result['verified']
        distance = result['distance']
        threshold = result['threshold']
        
        # Display the result
        if match:
            result_label.config(text=f"Match found! Distance: {distance:.3f}, Threshold: {threshold:.3f}")
        else:
            result_label.config(text=f"No match. Distance: {distance:.3f}, Threshold: {threshold:.3f}")
    
    except Exception as e:
        # Handle any exceptions (e.g., invalid file paths, DeepFace errors)
        messagebox.showerror("Error", f"Error during face verification: {str(e)}")
        result_label.config(text="Error occurred. Please try again.")

# Set up the tkinter window
window = tk.Tk()
window.title("Face Verification Tool")

# Labels and input fields for image paths
image1_label = tk.Label(window, text="Select First Image:")
image1_label.grid(row=0, column=0, padx=10, pady=5)
image1_entry = tk.Entry(window, width=40)
image1_entry.grid(row=0, column=1, padx=10, pady=5)
image1_button = tk.Button(window, text="Browse", command=select_image1)
image1_button.grid(row=0, column=2, padx=10, pady=5)

image2_label = tk.Label(window, text="Select Second Image:")
image2_label.grid(row=1, column=0, padx=10, pady=5)
image2_entry = tk.Entry(window, width=40)
image2_entry.grid(row=1, column=1, padx=10, pady=5)
image2_button = tk.Button(window, text="Browse", command=select_image2)
image2_button.grid(row=1, column=2, padx=10, pady=5)

# Button to trigger face verification
verify_button = tk.Button(window, text="Verify Faces", command=verify_faces)
verify_button.grid(row=2, column=0, columnspan=3, pady=10)

# Label to display result
result_label = tk.Label(window, text="Verification Result: ", wraplength=400)
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Start the tkinter main loop
window.mainloop()
