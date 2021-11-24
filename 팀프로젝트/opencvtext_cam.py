import cv2
from PIL import Image
import pytesseract
import time

cap = cv2.VideoCapture(0)  # 0: default camera

while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        # 프레임 출력
        cv2.imshow('Camera Window', frame)

        # ESC를 누르면 캡처
        key = cv2.waitKey(1) & 0xFF
        if (key == 27):
            return_value, image = cap.read()
            cv2.imwrite("opencv.jpg", image)
            time.sleep(1)

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            text = pytesseract.image_to_string(Image.open("opencv.jpg"), lang="kor")

            print(text.replace(" ", ""))
            break

cap.release()
cv2.destroyAllWindows()