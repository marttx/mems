from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")
top_text = input("Введите верхний текст")
bottom_text = input("Введите нижний текст")
print(top_text, bottom_text)
print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
imageNumber = int(input("введите номер картинки"))
if imageNumber==1:
    imagefile = "Кот в ресторане.png"
elif imageNumber==2:
    imagefile = "Кот в очках.png"
image = Image.open(imagefile)
width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=50)
text = draw.textbbox((0,0),top_text, font)
draw.text(((width-text[2])/2,10),top_text, font=font, fill="black")
text = draw.textbbox((0,0),bottom_text, font)
draw.text(((width-text[2])/2, height-text[3]-10),bottom_text, font=font, fill="black")
image.save("New_file.jpg")
