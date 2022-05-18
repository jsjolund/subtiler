import svgwrite
from math import sqrt, cos, acos, sin, pi


def flipX(vec):
    return [(v[0], -v[1]) for v in vec]


def flipY(vec):
    return [(-v[0], v[1]) for v in vec]


def rotCW(vec):
    return [(-v[1], v[0]) for v in vec]


def rotCCW(vec):
    return [(v[1], -v[0]) for v in vec]


def rot(vec, t):
    return [(v[0]*cos(t)-v[1]*sin(t), v[0]*sin(t)+v[1]*cos(t)) for v in vec]


def scl(vec, s):
    return [(v[0]*s, v[1]*s) for v in vec]


def tra(vec, p):
    return [(v[0]+p[0], v[1]+p[1]) for v in vec]


image = svgwrite.Drawing('test.svg', size=(300, 300))
alpha = 100


def draw(path):
    path = scl(path, alpha)
    image.add(image.polygon(path, id='polygon', stroke="black", fill="white"))


dx = cos(pi/4)
dy = sin(pi/4)
print(dx)
print(dy)

# Tilt of T1, T2
xa = 2+dx
ya = dy
xb = 2
yb = 0
theta = -acos((xa*xb+ya*yb)/(sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))

T1 = [(dx+1, 0), (dx*2+1, dy), (dx*2+1, dy+1),
      (dx+1, dy*2+1), (dx, dy*2+1), (0, dy+1), (0, dy), (dx, 0)]
T1 = tra(T1, (-dx-0.5, -dy-0.5))  # Mid point at origin
T1r = rot(T1, theta)
T1scl = (T1r[0][1]-T1r[4][1])/(sqrt(2)+1+dx +
                               1+1+sqrt(2)+sqrt(1-(sqrt(2)/2)**2))

T2 = [(0, dy), (2, dy), (dx+2, 0)]
T2 = tra(T2, (0, -dy))  # Left bottom at origin
T2r = flipX(rot(T2, -theta))
T2scl = (T2r[0][1]-T2r[1][1])/(sqrt(1-(sqrt(2)/2)**2)*2)

T3 = [(0, 1), (1, 0), (1, 1)]
T3 = tra(T3, (0, -1))  # Left bottom at origin
T3scl = 1/(1+sqrt(2)+1+1+1+sqrt(2)+1)

T4 = [(0, dy), (dx, 0), (dx+1, 0), (1, dy)]
T4 = tra(T4, (0, -dy))  # Left bottom at origin
T4scl = dy/((1+dy*2)*2+dy)

# draw(T1)
# draw(T2)
# draw(T3)
# draw(T4)

# draw(T1r)
# draw(scl(T2, T1scl))
# draw(scl(T3, T1scl))
# draw(scl(T4, T1scl))

# draw(T2r)
# draw(scl(T2, T2scl))
# draw(scl(T3, T2scl))

# draw(T3)
# draw(scl(T1, T3scl))
# draw(scl(T3, T3scl))
# draw(scl(T4, T3scl))

draw(T4)
draw(scl(T1, T4scl))
draw(scl(T3, T4scl))
draw(scl(T4, T4scl))

image.save()
