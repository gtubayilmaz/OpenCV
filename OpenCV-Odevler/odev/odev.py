import cv2

path = "video.mp4"
cap = cv2.VideoCapture(path)

frame_count = 0

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    frame_count += 1
    cv2.imshow("Video", frame)

    key = cv2.waitKey(25) & 0xFF

    if key == ord("t"):
        filename = f"frame_{frame_count}.png"
        cv2.imwrite(filename, frame)
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()