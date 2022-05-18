import svgwrite
from math import sqrt, cos, acos, sin, pi

image = svgwrite.Drawing('test.svg', size=(300, 300))
scl = 100

dx = cos(pi/4)
dy = sin(pi/4)
T1 = [(dx, 0), (dx+1, 0), (dx*2+1, dy), (dx*2+1, dy+1), (dx+1, dy*2+1), (dx, dy*2+1), (0, dy+1), (0, dy)]
T2 = [(0, dy), (2, dy), (dx+2, 0)]
T3 = [(0, 1), (1, 0), (1, 1)]
T4 = [(0, dy), (dx, 0), (dx+1, 0), (1, dy)]


xa = 2+dx
ya = dy
xb = 2
yb = 0
alpha = acos((xa*xb+ya*yb)/(sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))*180/pi

path = T1
# path = [(el[0]*scl, el[1]*scl) for el in path]
image.add(image.polygon(path, id='polygon', stroke="black", fill="white", transform=f"rotate({-alpha})"))

# path = T2
# path = [(el[0]*scl, el[1]*scl) for el in path]
# image.add(image.polygon(path, id='polygon', stroke="black", fill="white"))

# path = T3
# path = [(el[0]*scl, el[1]*scl) for el in path]
# image.add(image.polygon(path, id='polygon', stroke="black", fill="white"))

# path = T4
# path = [(el[0]*scl, el[1]*scl) for el in path]
# image.add(image.polygon(path, id='polygon', stroke="black", fill="white"))


image.save()
