import cv2
import os
import glob
from colour import Color

SIZE = (1920, 1080)
FPS = 5
ID = "55-3969"
PATH = "15frames/"

os.makedirs(PATH, exist_ok=True)

output_frames = slice(19, 79, 4)

cap = cv2.VideoWriter("15framesVod.mp4", cv2.VideoWriter_fourcc(*"mp4v"), FPS, SIZE)
frames = sorted(
    glob.glob("frames/*.jpg"), key=lambda x: int(x.split("/frame")[1].split(".")[0])
)

print(f"Number of frames: {len(frames)}")
print(f"Number of output frames: {len(frames[output_frames])}")

x = SIZE[0] // 2 - 300
y = 50
dy = 48

colors = list(Color("violet").range_to(Color("red"), len(frames[output_frames])))
for i, filename in enumerate(frames[output_frames]):
    img = cv2.imread(filename)
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

    cv2.imwrite(f"{PATH}/frame{i}.jpg", img)

    cap.write(img)

    y += dy

cap.release()
print("Done")
