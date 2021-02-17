from PIL import Image, ImageDraw
import math

im = Image.new("RGBA", (500,500), (0,0,0,255)) # intialising the image class
draw = ImageDraw.Draw(im) # Getting ready

slices = int(input("how many pizza slices would you like \n"))

x1 = 150
y1 = 150
x2 = 400
y2 = 400
ang = 0
xCor = 0
yCor = 0
constAng = 360 / slices
a = (x2 - x1) / 2
b = (y2 - y1) / 2
rad = math.radians(ang)
mid = ((x1 + x2) / 2, (y1 + y2) / 2)

dist = lambda a, b, rad: a * b / math.sqrt((b * math.cos(rad)) ** 2 + (a * math.sin(rad)) ** 2)
point = lambda distance, mid, rad, ang: (mid[0] + math.cos(rad) * distance, mid[1] - math.sin(rad) * distance)

draw.ellipse(
(x1,y1,x2,y2),
outline = (0,255,0)
)

for i in range(slices + 1):
    distance = dist(a, b, rad)
    tempPoint = point(distance, mid, rad, ang)

    draw.line(
        (mid, tempPoint),
        fill = (0,255,0)
    )

    rad = math.radians(ang)
    ang += constAng


im.save("image.png", quality = 100)

