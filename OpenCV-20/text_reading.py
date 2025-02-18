from PIL import Image
import pytesseract

# resmi acmak icin:
img = Image.open("text.png")
# resimden metin okuma
text = pytesseract.image_to_string(img,lang="tur")
print(text)