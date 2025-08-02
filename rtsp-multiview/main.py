import cv2
import numpy as np
from config import RTSP_STREAMS

def get_cap(stream):
    cap = cv2.VideoCapture(stream)
    if not cap.isOpened():
        print(f"Failed to open stream: {stream}")
    return cap

caps = [get_cap(url) for url in RTSP_STREAMS]

while True:
    frames = []
    for cap in caps:
        ret, frame = cap.read()
        if not ret or frame is None:
            frame = np.zeros((480, 640, 3), dtype=np.uint8)
        else:
            frame = cv2.resize(frame, (640, 360))
        frames.append(frame)

    if len(frames) == 4:
        top = np.hstack((frames[0], frames[1]))
        bottom = np.hstack((frames[2], frames[3]))
        combined = np.vstack((top, bottom))
        cv2.imshow("4-Cam Feed", combined)
    else:
        cv2.imshow("4-Cam Feed", np.zeros((720, 1280, 3), dtype=np.uint8))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

for cap in caps:
    cap.release()
cv2.destroyAllWindows()