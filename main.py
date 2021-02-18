from PIL import Image, ImageDraw
import math

im = Image.new("RGBA", (500,500), (0,0,0,255)) # Intialising the image class
draw = ImageDraw.Draw(im) # Getting ready

slices = int(input("how many pizza slices would you like \n")) # Asking the user

x1 = 119 # Determining where the circe should be
y1 = 125 # The same as above
x2 = 369
y2 = 375
ang = 0 # A variable to keep track of were the last slice were made
constAng = 360 / slices # How big each slice have to be
a = (x2 - x1) / 2 # The vertical radius
b = (y2 - y1) / 2 # The horisontal radius
rad = math.radians(ang) # Converting angle to radians cause python math
mid = ((x1 + x2) / 2, (y1 + y2) / 2) # Finding the center of the circle

dist = lambda a, b, rad: a * b / math.sqrt((b * math.cos(rad)) ** 2 + (a * math.sin(rad)) ** 2) # The distance from the center of the circle the circle at a specific angle
point = lambda distance, mid, rad, ang: (mid[0] + math.cos(rad) * distance, mid[1] - math.sin(rad) * distance) # Using trigonomitri to get the corodinats of the edge of the circle

draw.ellipse( # Draws the ellipse
(x1,y1,x2,y2), # sets the corodinatsof the ellipse
outline = (0,255,0) # makes it green
)

for i in range(slices): # Start the loop
    distance = dist(a, b, rad) # Run the dist funktion to get the distance to the edge
    tempPoint = point(distance, mid, rad, ang) # Runs the point funktion to get the corodinats of the edge

    draw.line( # Draws the line
        (mid, tempPoint), # The corodinats of the line
        fill = (0,255,0) # Making it gren
    )

    ang += constAng # making the angle bigger sa the next slice is ready to be cut
    rad = math.radians(ang) # convertin the angle to radians


im.save("image.png", quality = 100) # Saving the image
