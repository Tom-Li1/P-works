from PIL import Image

ascii_chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")   #用来替代像素的字符集合...

def get_chars(r, g, b, alpha = 256):
    global ascii_chars
    if alpha == 0:
        return ' '
    length = len(ascii_chars)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = alpha / length                 #将256个像素均分给字符...
    return ascii_chars[int(gray/unit)]



imagePath = r"C:\Users\win10\Pictures\2-1P926160P2553.png"
outPutHeight = 70
outPutWidth = 100


img = Image.open(imagePath)
img = img.resize((outPutWidth, outPutHeight))


txt = ""
for y in range(outPutHeight):
    for x in range(outPutWidth):
        txt += get_chars(*img.getpixel((x, y)))
    txt += '\n'

print(txt)
input()