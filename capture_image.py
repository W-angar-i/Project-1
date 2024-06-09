import cv2

def capture_and_display_image():
    # Open a connection to the default camera (usually the first camera detected by the system)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        cap.release()
        return

    # Display the captured frame
    cv2.imshow('Captured Image', frame)

    # Wait for a key press to close the image window
    cv2.waitKey(0)
        

    # Release the camera and close any open windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_display_image()
