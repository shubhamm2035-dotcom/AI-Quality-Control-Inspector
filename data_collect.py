import cv2
import os

# 1. Create folders for the dataset (if they don't already exist)
os.makedirs("dataset/good", exist_ok=True)
os.makedirs("dataset/defective", exist_ok=True)

# 2. Count existing files to prevent overwriting when saving new images
good_count = len(os.listdir("dataset/good"))
defective_count = len(os.listdir("dataset/defective"))

# 3. Initialize the camera (0 is usually the default built-in webcam)
cap = cv2.VideoCapture(0)

print("--- Data Collection Started ---")
print("Press 'g' -> To save a Good product image")
print("Press 'd' -> To save a Defective product image")
print("Press 'q' -> To quit the program")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to access the camera!")
        break

    # Display live instructions and image counts on the video frame
    cv2.putText(frame, f"Good: {good_count} | Defective: {defective_count}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "Press 'g' for Good | 'd' for Defect | 'q' to Quit", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show the live video feed in a window
    cv2.imshow("Data Collection for Quality Control", frame)

    # Capture keyboard input 
    key = cv2.waitKey(1) & 0xFF

    if key == ord('g'):
        # Save the frame to the 'good' folder when 'g' is pressed
        filename = f"dataset/good/good_{good_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        good_count += 1
        
    elif key == ord('d'):
        # Save the frame to the 'defective' folder when 'd' is pressed
        filename = f"dataset/defective/defective_{defective_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        defective_count += 1
        
    elif key == ord('q'):
        # Exit the loop when 'q' is pressed
        print("Closing the program...")
        break

# Release the camera hardware and close all OpenCV windows safely
cap.release()
cv2.destroyAllWindows()
