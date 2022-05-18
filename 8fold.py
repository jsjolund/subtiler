import svgwrite
from copy import deepcopy
from math import sqrt, cos, acos, sin, pi
from matrix import Matrix3


class Tile:
    def __init__(self, name, vec, locl=Matrix3(), glob=Matrix3()):
        self.vec = vec
        self.name = name
        self.local = locl
        self.glob = glob

    def vtra(self, px, py=0):
        if type(px) is tuple:
            py = px[1]
            px = px[0]
        res = [(v[0]+px, v[1]+py) for v in self.vec]
        return Tile(self.name, res)

    def mul(self, vec, mat):
        new_vec = []
        for v in vec:
            new_vec.append((v[0] * mat.val[0] + v[1] * mat.val[3] + mat.val[6],
                            v[0] * mat.val[1] + v[1] * mat.val[4] + mat.val[7]))
        return new_vec

    def transform(self):
        tra_vec = self.mul(self.vec, self.local)
        tra_vec = self.mul(tra_vec, self.glob)
        return tra_vec

    def flipX(self):
        self.local.flipX()
        return self

    def flipY(self):
        self.local.flipY()
        return self

    def rot(self, t):
        self.local.rot(t)
        return self

    def scl(self, s):
        self.local.scl(s)
        return self

    def tra(self, x, y=0):
        if type(x) is tuple:
            y = x[1]
            x = x[0]
        self.local.tra(x, y)
        return self

    def cpy(self):
        return Tile(self.name, deepcopy(self.vec), self.local.cpy(), self.glob.cpy())

    def __getitem__(self, key):
        return self.transform()[key]


image = svgwrite.Drawing('test.svg', size=(600, 600))


def draw(tiles):
    if type(tiles) is Tile:
        tiles = [tiles]
    for tile in tiles:
        color = 'white'
        match tile.name:
            case 'T1': color = 'yellow'
            case 'T2': color = 'blue'
            case 'T3': color = 'green'
            case 'T4': color = 'red'
        path = tile.transform()
        image.add(image.polygon(path, id=tile.name, stroke='black', stroke_width='0.01px',
                                fill=color, transform="translate(200,200),scale(100)"))
        # fill=color))


dx = cos(pi/4)
dy = sin(pi/4)

# Tilt of T1, T2
xa = 2+dx
ya = dy
xb = 2
yb = 0
theta = -acos((xa*xb+ya*yb)/(sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))

T1 = Tile('T1', [(dx+1, 0), (dx*2+1, dy), (dx*2+1, dy+1),
                 (dx+1, dy*2+1), (dx, dy*2+1), (0, dy+1), (0, dy), (dx, 0)])
T1 = T1.vtra(-dx-0.5, -dy-0.5)  # Mid point at origin
T1r = T1.cpy().rot(theta)
T1scl = (T1r[4][1]-T1r[0][1])/(sqrt(2)+1+dx +
                               1+1+sqrt(2)+sqrt(1-(sqrt(2)/2)**2))

T2 = Tile('T2', [(0, dy), (2, dy), (dx+2, 0)])
T2 = T2.vtra(0, -dy)  # Left bottom at origin
T2r = T2.cpy().rot(theta).flipX()
T2scl = (T2r[0][1]-T2r[1][1])/(sqrt(1-(sqrt(2)/2)**2)*2)

T3 = Tile('T3', [(0, 1), (1, 0), (1, 1)])
T3 = T3.vtra(0, -1)  # Left bottom at origin
T3scl = 1/(1+sqrt(2)+1+1+1+sqrt(2)+1)

T4 = Tile('T4', [(0, dy), (dx, 0), (dx+1, 0), (1, dy)])
T4 = T4.vtra(0, -dy)  # Left bottom at origin
T4scl = dy/((1+dy*2)*2+dy)

# draw(T1)
# draw(T1r)
# draw(T2)
# draw(T2r)
# draw(T3)
# draw(T4)

# print(T1scl)
# print(T2scl)
# print(T3scl)
# print(T4scl)

T1s = []
T1s.append(T2.cpy().tra(T1r[7]).scl(T1scl))
T1s.append(T3.cpy().tra(T1r[0]).scl(T1scl).rot(3*pi/4))
T1s.append(T4.cpy().tra(T1s[-1][2]).scl(T1scl).rot(pi/2))
T1s.append(T4.cpy().tra(T1s[-1][2]).scl(T1scl).flipY())
T1s.append(T4.cpy().tra(T1s[-1][3]).scl(T1scl).flipY())
T1s.append(T4.cpy().tra(T1s[-1][0]).scl(T1scl).flipY().flipX())
T1s.append(T3.cpy().tra(T1s[-1][3]).scl(T1scl).flipY().flipX().rot(pi/4))
T1s.append(T3.cpy().tra(T1s[-1][0]).scl(T1scl).flipY().rot(pi/4))
T1s.append(T3.cpy().tra(T1s[-1][2]).scl(T1scl).flipY().flipX().rot(pi/4))
T1s.append(T2.cpy().tra(T1s[-1][1]).scl(T1scl).rot(-pi/4))
T1s.append(T3.cpy().tra(T1s[-1][2]).scl(T1scl).flipX())
T1s.append(T3.cpy().tra(T1s[-1][1]).scl(T1scl).flipY())
T1s.append(T3.cpy().tra(T1s[3][1]).scl(T1scl).rot(-pi/2))
T1s.append(T3.cpy().tra(T1s[-1][1]).scl(T1scl).rot(pi/2))

T1s2 = []
for t in T1s:
    t1 = t.cpy()
    t2 = t.cpy()
    t3 = t.cpy()
    t1.glob.rot(pi/2)
    t2.glob.rot(pi)
    t3.glob.rot(-pi/2)
    T1s2.extend([t1, t2, t3])
T1s.extend(T1s2)
T1s.append(T1.cpy().scl(T1scl))
for t in T1s:
    t.glob.rot(-theta)

draw(T1s)

# # draw(T2r)
# # draw(T2.scl(T2scl))
# # draw(T3.scl(T2scl))

# # draw(T3)
# # draw(T1.scl(T3scl))
# # draw(T3.scl(T3scl))
# # draw(T4.scl(T3scl))

# # draw(T4)
# # draw(T1.scl(T4scl))
# # draw(T3.scl(T4scl))
# # draw(T4.scl(T4scl))


image.save()
