import cv2
import glob

SIZE = (1920, 1080)
FPS = 30

cap = cv2.VideoWriter("90framesVod.mp4", cv2.VideoWriter_fourcc(*"mp4v"), FPS, SIZE)
frames = sorted(
    glob.glob("frames/*.jpg"), key=lambda x: int(x.split("/frame")[1].split(".")[0])
)

print(f"Number of frames: {len(frames)}")
for filename in frames:
    img = cv2.imread(filename)
    cap.write(img)

cap.release()
print("Done")
