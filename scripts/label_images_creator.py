import cv2
import os
import numpy as np

# Define the input video path
input_video_path = '../hackathon-info/videos/Devasandra_Sgnl_JN_FIX_1_time_2024-05-14T07_30_02_000.mp4'
output_folder = '../hackathon-info/label_images'
frame_interval = 100  # Extract every 50th frame
motion_threshold = 500000  # Threshold for detecting motion

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the input video
cap = cv2.VideoCapture(input_video_path)

# Get the properties of the input video
frame_index = 0
saved_frame_count = 0
last_frame = None

# Loop through the video frames
success, frame = cap.read()

while success:
    if frame_index % frame_interval == 0:
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if last_frame is not None:
            # Calculate the absolute difference between the current frame and the last frame
            frame_diff = cv2.absdiff(gray_frame, last_frame)
            # Calculate the sum of the absolute differences
            diff_sum = np.sum(frame_diff)

            if diff_sum > motion_threshold:
                # Save the frame as an image if motion is detected
                output_image_path = os.path.join(output_folder, f'frame_{frame_index}.jpg')
                cv2.imwrite(output_image_path, frame)
                saved_frame_count += 1

        # Update the last frame
        last_frame = gray_frame

    frame_index += 1
    success, frame = cap.read()

# Release the resources
cap.release()
cv2.destroyAllWindows()

print(f"Extracted {saved_frame_count} frames with motion and saved to '{output_folder}' folder.")
