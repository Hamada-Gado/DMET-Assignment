import cv2
import os
import glob
from colour import Color

SIZE = (1920, 1080)
FPS = 5
ID = "55-3969"
PATH = "5FPS/"

os.makedirs(PATH, exist_ok=True)


cap = cv2.VideoWriter(f"{PATH}/vod.mp4", cv2.VideoWriter_fourcc(*"mp4v"), FPS, SIZE)
frames = sorted(
    glob.glob("frames/*.jpg"), key=lambda x: int(x.split("/frame")[1].split(".")[0])
)

print(f"Number of frames: {len(frames)}")

x = SIZE[0] // 2 - 300
y = 50
dy = 48

counter = 0
colors = list(Color("violet").range_to(Color("red"), len(frames)))
for i, filename in enumerate(frames):
    img = cv2.imread(filename)
    if i % 6 != 0:
        continue

    cv2.putText(
        img,
        f"ID: {ID}",
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        list(map(lambda x: x * 255, colors[i].rgb)),
        3,
        cv2.LINE_AA,
    )

    cv2.imwrite(f"{PATH}/frame{counter}.jpg", img)

    cap.write(img)

    y += dy
    counter += 1

cap.release()
print(f"Number of output frames: {counter}")
print("Done")
