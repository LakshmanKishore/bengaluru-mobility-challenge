import cv2

# Target FPS for the output video (e.g., 10 FPS)
target_fps = 10

BASE_PATH = "../hackathon-info"

# Open the video file (assuming it's the 1 FPS video)
cap = cv2.VideoCapture(f'{BASE_PATH}/processed_videos/reduced_one_fps_full.mp4')

# Get original video width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and filename for the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Adjust codec if needed
out = cv2.VideoWriter("reduced_video_duration_from_one_fps.mp4", fourcc, target_fps, (width, height))

# List to store frames for 1 second
frames_buffer = []

while True:
  # Capture frame-by-frame
  ret, frame = cap.read()

  if not ret:
    print("No more frames captured!")
    break

  # Append frame to buffer
  frames_buffer.append(frame)

  # Check if buffer has enough frames for 1 second
  if len(frames_buffer) == target_fps:
    # Write all frames in the buffer to the output video
    for frame_to_write in frames_buffer:
      out.write(frame_to_write)
    # Clear the buffer for the next second
    frames_buffer = []

# Write any remaining frames in the buffer
if frames_buffer:
  for frame_to_write in frames_buffer:
    out.write(frame_to_write)

# Release capture and writer
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video processing complete!")
