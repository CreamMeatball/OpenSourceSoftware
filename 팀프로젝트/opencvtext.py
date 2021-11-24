"""
Tesseract - OCR 프로그램 중 하나, 다양한 운영체제에서 사용할 수 있는 엔진, 무료 소프트웨어

이미지에 있는 텍스트 추출 과정
1. Tesseract-OCR 설치
2. Python에서 Tesseract 사용하기
"""
from PIL import Image
import pytesseract
from gtts import gTTS

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open("news3.jpg"), lang="kor")
print(text)
print(text.replace(" ", ""))

# gtext = "안녕하세요"
tts = gTTS(text, lang='ko')
tts.save("news.mp3")

with open("news.txt", "w", encoding="utf8") as f:
    f.write(text)
    f.write("\n\n\n")
    f.write(text.replace(" ", ""))