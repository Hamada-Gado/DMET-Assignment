import cv2
import glob

frames = sorted(
    glob.glob("frames/*.jpg"), key=lambda x: int(x.split("/frame")[1].split(".")[0])
)

for i, filename in enumerate(frames):
    img = cv2.imread(filename)
    cv2.putText(
        img,
        f"Frame {i}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    cv2.imshow("frame", img)

    if cv2.waitKey(0) == ord("q"):
        break
