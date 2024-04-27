from PIL import Image, ImageDraw, ImageFont
from io import TextIOWrapper
import argparse
import math
# https://www.youtube.com/watch?v=2fZBLPk-T2Y
parser = argparse.ArgumentParser(description="Simple CLI to create ASCII art")
parser.add_argument("--in_f", help="The input filepath")
parser.add_argument("--out", help="The output filepath")
parser.add_argument("--sf", type=float, default=0.2, help="The scale factor", required=False)
parser.add_argument("--charset", default="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ", help="The charset used", required=False)
parser.add_argument("--font", default='C:\\Windows\\Fonts\\lucon.ttf', help="The font", required=False)
parser.add_argument("--font_size", type=int, default=15, help="The font size", required=False)
parser.add_argument("--density_algorithm", choices=["Average", "Luminance"], default="Average", help="How to calculate the density", required=False)
args = parser.parse_args()

def calculate_density(RGB: tuple[int, int, int]) -> int:
    R, G, B = RGB
    if args.density_algorithm == "Average": return int((R + G + B) // 3)
    if args.density_algorithm == "Luminance": return int((0.2126*R + 0.7152*G + 0.0722*B))

try:
    chars: str = args.charset[::-1]
    charLength: int = len(chars)
    interval: float = charLength/256
    scaleFactor: float = args.sf
    oneCharWidth: int = 10
    oneCharHeight: int = 18

    def getChar(inputInt: int) -> str:
        return chars[math.floor(inputInt*interval)]

    text_file: TextIOWrapper = open(args.out + ".txt", "w")
    im: Image = Image.open(args.in_f)
    fnt: ImageFont.FreeTypeFont = ImageFont.truetype(args.font, args.font_size)
    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = im.size
    pix = im.load()
    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
    d = ImageDraw.Draw(outputImage)
    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = calculate_density(pix[j, i])
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font=fnt, fill=(r, g, b))
        text_file.write('\n')
    outputImage.save(args.out)
finally:
    outputImage.close()
    im.close()
    text_file.close()