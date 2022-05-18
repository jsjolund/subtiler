import svgwrite
from math import sqrt, cos, acos, sin, pi


def rot(t, vec):
    return [(v[0]*cos(t)-v[1]*sin(t), v[0]*sin(t)+v[1]*cos(t)) for v in vec]


def scl(s, vec):
    return [(v[0]*s, v[1]*s) for v in vec]


def tra(p, vec):
    return [(v[0]+p[0], v[1]+p[1]) for v in vec]


image = svgwrite.Drawing('test.svg', size=(300, 300))
alpha = 100


def draw(path):
    path = scl(alpha, path)
    image.add(image.polygon(path, id='polygon', stroke="black", fill="white"))


dx = cos(pi/4)
dy = sin(pi/4)
xa = 2+dx
ya = dy
xb = 2
yb = 0
theta = -acos((xa*xb+ya*yb)/(sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))


T1 = [(dx+1, 0), (dx*2+1, dy), (dx*2+1, dy+1),
      (dx+1, dy*2+1), (dx, dy*2+1), (0, dy+1), (0, dy), (dx, 0)]
T1 = tra((-dx-0.5, -dy-0.5), T1)
T2 = [(0, dy), (2, dy), (dx+2, 0)]
T3 = [(0, 1), (1, 0), (1, 1)]
T4 = [(0, dy), (dx, 0), (dx+1, 0), (1, dy)]


T1r = rot(theta, T1)
T1DivScl = (T1r[0][1]-T1r[4][1])/(sqrt(2)+1+dx +
                                  1+1+sqrt(2)+sqrt(1-(sqrt(2)/2)**2))
draw(T1r)

draw(scl(T1DivScl, T2))
draw(scl(T1DivScl, T3))
draw(scl(T1DivScl, T4))


image.save()
