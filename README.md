# Computer Vision projects
#L1

Welcome to my repository of computer vision projects! This collection showcases various techniques and applications of computer vision using OpenCV and other relevant libraries. Below are the details of each project included in this repository.

## Project 1: Moving Object Detection using OpenCV

### Description
This project involves detecting moving objects in a video stream using OpenCV. The technique is based on frame differencing and background subtraction to identify changes in the scene. The program captures the first frame and compares it with subsequent frames to detect motion.

### Features
- Frame differencing
- Background subtraction
- Contour detection
- Real-time motion detection

### Requirements
- OpenCV
- NumPy
- imutils

---

## Project 2: Advanced Face Detection and Tracking

### Description
This project focuses on detecting and tracking faces in real-time using advanced techniques. It uses Haar cascades for face detection and processes a video file to identify and highlight faces in each frame.

### Features
- Face detection using Haar cascades
- Real-time face tracking in a video file

### Requirements
- OpenCV
- Haar cascade XML file

---

## Project 3: Object Detection and Tracking based on Colour

### Description
This project involves color calibration using HSV values and object tracking in a video file. The GUI allows the user to adjust the HSV values to filter specific colors and detect objects of that color in real-time.

### Features
- Color calibration using HSV sliders
- Object tracking in a video file based on calibrated color
- Screenshot functionality

### Requirements
- OpenCV
- NumPy
- Tkinter
- PIL
- imutils
- pyautogui

---

## Project 4: Face Recognition with OpenCV

### Description
This project demonstrates a basic face recognition system using OpenCV. The project is divided into two main parts: data creation and face recognition.
#### Data Creation:
The data creation script captures 30 images of a person's face and saves them in a specified directory.
#### Face Recognition:
The face recognition script trains a face recognition model using the collected dataset and then uses the webcam to recognize faces in real-time.

### Features
- Face detection using Haar cascades
- Face recognition using LBPH

### Requirements
- OpenCV
- NumPy
- OS

---

## Project 5: Face Emotion Recognition

### Description
This project demonstrates how to recognize emotions from facial expressions using the `facial_emotion_recognition` library. The project includes two main functionalities:
1. Real-time emotion recognition from a webcam feed.
2. Emotion recognition from an IP camera stream.

### Features
- **Real-time Emotion Detection:** Identify and display emotions from live video captured via webcam.
- **IP Camera Integration:** Stream video from an IP camera and perform emotion recognition.
- **Emotion Visualization:** Overlay recognized emotions on the video feed for easy interpretation.
- **Adjustable Video Feed:** Resize and adjust the video feed for better visibility and performance.
- **Simple Exit Options:** Exit the application using keyboard shortcuts (`Esc` for webcam feed and `q` for IP camera stream).


### Requirements
- OpenCV
- NumPy
- Torch
- Torchvision
- facial_emotion_recognition

---

### Prerequisites
Ensure you have Python and pip installed on your system. You need to install the required libraries.

---

Feel free to explore each project and provide feedback. Contributions are welcome!😊
