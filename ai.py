import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import scipy
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import logging
import datetime
import os

# Quien lo lea es un guapete

def check_garbage_patch():
    logging.basicConfig(filename='check-{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d')), level=logging.INFO)
    # Load the trained model
    model = keras.models.load_model('garbage_classifier.h5')
    directory_path = input("Enter the path to the directory containing the images: ")
    for file_name in os.listdir(directory_path):
        # check if file is an image
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            # Preprocess the image
            img_path = os.path.join(directory_path, file_name)
            img = image.load_img(img_path, target_size=(64, 64))
            img_tensor = image.img_to_array(img)
            img_tensor = np.expand_dims(img_tensor, axis=0)
            img_tensor /= 255.

            # Use the model to predict if the image is a garbage patch
            prediction = model.predict(img_tensor)

            # Print the result
            if prediction >= 0.5:
                print("The image {} is a garbage patch.".format(file_name))
            else:
                print("The image {} is not a garbage patch.".format(file_name))
            # Log the results in a single line
            logging.info("Checked image: {} (Prediction: {}) - {}".format(img_path, str(prediction[0][0]), "This image is a garbage patch." if prediction >= 0.5 else "This image is not a garbage patch."))

def train_AI():
    # Load images from a directory
    train_dir = "C:/Users/Sergio/Downloads/h/JPGs"
    val_dir = "C:/Users/Sergio/Downloads/h/JPGs"
    train_datagen = ImageDataGenerator(rescale=1./255)
    val_datagen = ImageDataGenerator(rescale=1./255)
    
    training_set = train_datagen.flow_from_directory(
        './JPGs',
        target_size=(480,360),
        color_mode='grayscale',
        class_mode='binary')
    
    val_set = val_datagen.flow_from_directory(
        './JPGs',
        target_size=(480,360),
        color_mode='grayscale',
        class_mode='binary')

    # Create the model
    model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(480, 360, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
    ])
    # Compile the model
    model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
    # Train the model
    model.fit(training_set, epochs=10, validation_data=val_set)
    model.save('garbage_classifier.h5')

def main():
    prompt = input("Enter 1 to train AI or 2 to check for garbage patch: ")

    if prompt == "1":
        # Logging learn action
        log_file = "learn-" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        logging.basicConfig(filename=log_file, level=logging.INFO)
        logging.info("Training AI started at: " + str(datetime.datetime.now()))
        train_AI()
        logging.info("Training AI completed at: " + str(datetime.datetime.now()))
    elif prompt == "2":
        # Logging check action
        log_file = "check-" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        logging.basicConfig(filename=log_file, level=logging.INFO)
        logging.info("Checking for garbage patch started at: " + str(datetime.datetime.now()))
        check_garbage_patch()
        logging.info("Checking for garbage patch completed at: " + str(datetime.now()))
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
