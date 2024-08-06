'''
Script to extract first few seconds of the video with target fps
'''
# Import cv2
import cv2
from datetime import datetime

BASE_PATH = "../hackathon-info"

# cap = cv2.VideoCapture(f'{BASE_PATH}/processed_videos/first_minute.mp4')
# cap = cv2.VideoCapture(f'{BASE_PATH}/videos/Devasandra_Sgnl_JN_FIX_1_time_2024-05-14T07_30_02_000.mp4')
cap = cv2.VideoCapture(f'{BASE_PATH}/videos/Stn_HD_1_time_2024-05-14T07_30_02_001.mp4')
desired_fps = 2
number_of_seconds = 5

output_path = f'{BASE_PATH}/processed_videos/stn_hd_1_first_{number_of_seconds}_seconds_with_{desired_fps}_fps.mp4'

original_fps = cap.get(cv2.CAP_PROP_FPS)

print("Original FPS: ", original_fps)


fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use appropriate codec based on desired output format
out = cv2.VideoWriter(output_path, fourcc, desired_fps, (int(cap.get(3)), int(cap.get(4))))

# Print start time
start_time = datetime.now()
print("Start time: ", start_time)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret or frame_count > number_of_seconds * original_fps:
        break
    frame_count += 1

    # Process only every Nth frame to achieve desired frame rate
    if frame_count % int(original_fps/desired_fps) == 0:
        print("Frame count: ", frame_count)
        out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

end_time = datetime.now()
print("End time: ", end_time)

print("Elapsed time: ", end_time - start_time)
print("output_path: ", output_path)
print("Done!")
