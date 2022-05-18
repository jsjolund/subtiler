import svgwrite
from copy import deepcopy
from math import sqrt, cos, acos, sin, pi


class Tile:
    def __init__(self, name, vec):
        self.vec = vec
        self.name = name

    def flipX(self):
        res = [(v[0], -v[1]) for v in self.vec]
        return Tile(self.name, res)

    def flipY(self):
        res = [(-v[0], v[1]) for v in self.vec]
        return Tile(self.name, res)

    def rotCW(self):
        res = [(-v[1], v[0]) for v in self.vec]
        return Tile(self.name, res)

    def rotCCW(self):
        res = [(v[1], -v[0]) for v in self.vec]
        return Tile(self.name, res)

    def rot(self, t):
        res = [(v[0]*cos(t)-v[1]*sin(t), v[0]*sin(t)+v[1]*cos(t))
               for v in self.vec]
        return Tile(self.name, res)

    def scl(self, s):
        res = [(v[0]*s, v[1]*s) for v in self.vec]
        return Tile(self.name, res)

    def tra(self, px, py=0):
        if type(px) is tuple:
            py = px[1]
            px = px[0]
        res = [(v[0]+px, v[1]+py) for v in self.vec]
        return Tile(self.name, res)

    def __getitem__(self, key):
        return deepcopy(self.vec[key])


image = svgwrite.Drawing('test.svg', size=(600, 600))
tile_scl = 100


def draw(tiles):
    if type(tiles) is Tile:
        tiles = [tiles]
    for tile in tiles:
        color = 'white'
        match tile.name:
            case 'T1': color = 'white'
            case 'T2': color = 'blue'
            case 'T3': color = 'green'
            case 'T4': color = 'red'
        path = tile.scl(tile_scl).vec
        image.add(image.polygon(path, id=tile.name,
                  stroke='black', fill=color, transform=f"translate(200,200)"))


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
T1 = T1.tra(-dx-0.5, -dy-0.5)  # Mid point at origin
T1r = T1.rot(theta)
T1scl = (T1r[4][1]-T1r[0][1])/(sqrt(2)+1+dx +
                               1+1+sqrt(2)+sqrt(1-(sqrt(2)/2)**2))

T2 = Tile('T2', [(0, dy), (2, dy), (dx+2, 0)])
T2 = T2.tra(0, -dy)  # Left bottom at origin
T2r = T2.rot(-theta).flipX()
T2scl = (T2r[0][1]-T2r[1][1])/(sqrt(1-(sqrt(2)/2)**2)*2)

T3 = Tile('T3', [(0, 1), (1, 0), (1, 1)])
T3 = T3.tra(0, -1)  # Left bottom at origin
T3scl = 1/(1+sqrt(2)+1+1+1+sqrt(2)+1)

T4 = Tile('T4', [(0, dy), (dx, 0), (dx+1, 0), (1, dy)])
T4 = T4.tra(0, -dy)  # Left bottom at origin
T4scl = dy/((1+dy*2)*2+dy)

t1 = T1.scl(T1scl)
t2 = T2.scl(T1scl)
t3 = T3.scl(T1scl)
t4 = T4.scl(T1scl)
T1s = []
T1s.append(t2.tra(T1r[7]))
T1s.append(t3.rot(pi/4).rotCW().tra(T1r[0]))
T1s.append(t4.rotCW().tra(T1s[-1][2]))
T1s.append(t4.flipY().tra(T1s[-1][2]))
T1s.append(t4.flipY().tra(T1s[-1][3]))
T1s.append(t4.flipY().flipX().tra(T1s[-1][0]))
T1s.append(t3.rot(pi/4).flipY().flipX().tra(T1s[-1][3]))
T1s.append(t3.rot(pi/4).flipY().tra(T1s[-1][0]))
T1s.append(t3.rot(pi/4).flipY().flipX().tra(T1s[-1][2]))
T1s.append(t2.rot(-pi/4).tra(T1s[-1][1]))
T1s.append(t3.flipX().tra(T1s[-1][2]))
T1s.append(t3.flipY().tra(T1s[-1][1]))
T1s.append(t3.rotCCW().tra(T1s[3][1]))
T1s.append(t3.rotCW().tra(T1s[-1][1]))
T1s.extend([t.rot(pi/2) for t in T1s])
T1s.extend([t.rot(pi) for t in T1s])
T1s.append(t1)
# T1s = [t.rot(-theta) for t in T1s]
draw(T1s)

# draw(T2r)
# draw(T2.scl(T2scl))
# draw(T3.scl(T2scl))

# draw(T3)
# draw(T1.scl(T3scl))
# draw(T3.scl(T3scl))
# draw(T4.scl(T3scl))

# draw(T4)
# draw(T1.scl(T4scl))
# draw(T3.scl(T4scl))
# draw(T4.scl(T4scl))


image.save()
