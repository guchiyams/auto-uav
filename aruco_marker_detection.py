import cv2
import numpy as np
import time  # Import the time module

# Load the predefined dictionary for ArUco markers
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()  # Corrected parameter creation

# Start video capture (0 for default camera, or replace with your video path)
cap = cv2.VideoCapture(0)

# Ensure the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream or file")
    exit()

# Initialize FPS counter
fps = 0
fps_counter = 0
start_time = time.time()  # Record the start time

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab frame")
        break

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the markers in the frame
    corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # If markers are detected, draw them on the frame
    if ids is not None:
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)

    # Increment the frame counter
    fps_counter += 1

    # Calculate and display FPS every second
    if time.time() - start_time >= 1:  # Update every 1 second
        fps = fps_counter
        fps_counter = 0  # Reset the frame counter
        start_time = time.time()  # Reset the start time

    # Display the FPS on the frame
    cv2.putText(frame, f'FPS: {fps}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with detected markers and FPS
    cv2.imshow('ArUco Marker Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()


