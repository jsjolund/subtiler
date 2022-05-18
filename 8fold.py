import svgwrite
from tile import Tile
from math import sqrt, cos, acos, sin, pi

image = svgwrite.Drawing('test.svg', size=(600, 600))


def draw(tiles, force_color=None):
    if type(tiles) is Tile:
        tiles = [tiles]
    for tile in tiles:
        color = 'white'
        match tile.name:
            case 'T1': color = 'yellow'
            case 'T2': color = 'lightblue'
            case 'T3': color = 'green'
            case 'T4': color = 'red'
        if force_color != None:
            color = force_color
        path = tile.transform()
        image.add(image.polygon(path, id=tile.name, stroke='black', stroke_width='0.01px',
                                fill=color, transform="translate(200,200),scale(100)"))


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
T1 = T1.v_tra(-dx-0.5, -dy-0.5)  # Mid point at origin
T1r = T1.cpy().l_rot(theta)
T1scl = (T1r[4][1]-T1r[0][1])/(sqrt(2)+1+dx +
                               1+1+sqrt(2)+sqrt(1-(sqrt(2)/2)**2))

T2 = Tile('T2', [(0, dy), (2, dy), (dx+2, 0)])
T2 = T2.v_tra(0, -dy)  # Left bottom at origin
T2r = T2.cpy().l_rot(theta).l_flipX()
T2scl = (T2r[0][1]-T2r[1][1])/(sqrt(1-(sqrt(2)/2)**2)*2)

T3 = Tile('T3', [(0, 1), (1, 0), (1, 1)])
T3 = T3.v_tra(0, -1)  # Left bottom at origin
T3scl = 1/(1+sqrt(2)+1+1+1+sqrt(2)+1)

T4 = Tile('T4', [(0, dy), (dx, 0), (dx+1, 0), (1, dy)])
T4 = T4.v_tra(0, -dy)  # Left bottom at origin
T4scl = dy/((1+dy*2)*2+dy)

T1s = []
T1s.append(T2.cpy().l_tra(T1r[7]).l_scl(T1scl))
T1s.append(T3.cpy().l_tra(T1r[0]).l_scl(T1scl).l_rot(3*pi/4))
T1s.append(T4.cpy().l_tra(T1s[-1][2]).l_scl(T1scl).l_rot(pi/2))
T1s.append(T4.cpy().l_tra(T1s[-1][2]).l_scl(T1scl).l_flipY())
T1s.append(T4.cpy().l_tra(T1s[-1][3]).l_scl(T1scl).l_flipY())
T1s.append(T4.cpy().l_tra(T1s[-1][0]).l_scl(T1scl).l_flipY().l_flipX())
T1s.append(T3.cpy().l_tra(T1s[-1][3]).l_scl(T1scl).l_flipY().l_flipX().l_rot(pi/4))
T1s.append(T3.cpy().l_tra(T1s[-1][0]).l_scl(T1scl).l_flipY().l_rot(pi/4))
T1s.append(T3.cpy().l_tra(T1s[-1][2]).l_scl(T1scl).l_flipY().l_flipX().l_rot(pi/4))
T1s.append(T2.cpy().l_tra(T1s[-1][1]).l_scl(T1scl).l_rot(-pi/4))
T1s.append(T3.cpy().l_tra(T1s[-1][2]).l_scl(T1scl).l_flipX())
T1s.append(T3.cpy().l_tra(T1s[-1][1]).l_scl(T1scl).l_flipY())
T1s.append(T3.cpy().l_tra(T1s[3][1]).l_scl(T1scl).l_rot(-pi/2))
T1s.append(T3.cpy().l_tra(T1s[-1][1]).l_scl(T1scl).l_rot(pi/2))
T1s.extend([t.cpy().g_rot(pi/2) for t in T1s])
T1s.extend([t.cpy().g_rot(pi) for t in T1s])
T1s.extend([t.cpy().g_rot(-pi/2) for t in T1s])
T1s.append(T1.cpy().l_scl(T1scl))
T1s = [t.cpy().g_rot(-theta) for t in T1s]

T2s = []
T2s.append(T2.cpy().l_tra(T2r[0]).l_scl(T2scl))
T2s.append(T2.cpy().l_tra(T2s[-1][1]).l_scl(T2scl))
T2s.append(T2.cpy().l_tra(T2s[-1][2]).l_scl(T2scl).l_flipY().l_flipX())
T2s.append(T2.cpy().l_tra(T2s[-1][1]).l_scl(T2scl))
T2s.append(T3.cpy().l_tra(T2s[-1][1]).l_scl(T2scl).l_rot(pi/4))
T2s.append(T3.cpy().l_tra(T2s[-1][0]).l_scl(T2scl).l_flipX().l_rot(pi/4))
T2s.append(T3.cpy().l_tra(T2s[1][1]).l_scl(T2scl).l_flipX().l_rot(pi/4))
T2s.append(T3.cpy().l_tra(T2s[-1][1]).l_scl(T2scl).l_flipX().l_rot(pi/4))

T3s = []
T3s.append(T4.cpy().l_tra(T3[0]).l_scl(T3scl))
T3s.append(T3.cpy().l_tra(T3s[-1][3]).l_scl(T3scl).l_flipX().l_rot(pi/4))
T3s.append(T4.cpy().l_tra(T3s[-1][2]).l_scl(T3scl).l_flipX())
T3s.append(T4.cpy().l_tra(T3s[-1][3]).l_scl(T3scl).l_flipX())
T3s.append(T3.cpy().l_tra(T3s[0][1]).l_scl(T3scl))
T3s.append(T3.cpy().l_tra(T3s[-1][1]).l_scl(T3scl).l_rot(pi/2))
T3s.append(T3.cpy().l_tra(T3s[-1][0]).l_scl(T3scl))
T3s.append(T3.cpy().l_tra(T3s[-2][1]).l_scl(T3scl).l_rot(-pi/2))
T3s.append(T3.cpy().l_tra(T3s[-1][2]).l_scl(T3scl).l_rot(pi/2))
T3s.append(T3.cpy().l_tra(T3s[-1][1]).l_scl(T3scl).l_rot(3*pi/2))
T3s.append(T4.cpy().l_tra(T3s[-1][1]).l_scl(T3scl))
T3s.append(T4.cpy().l_tra(T3s[-1][0]).l_scl(T3scl).l_flipX().l_rot(pi/2))
T3s.append(T3.cpy().l_tra(T3s[-2][2]).l_scl(T3scl).l_flipY())
T3s.append(T3.cpy().l_tra(T3s[-1][1]).l_scl(T3scl).l_flipX())
T3s.append(T1.cpy().l_tra(T3s[9][0]).l_tra(T1[2][0]*T3scl, (T3s[9][2][1]-T3s[9][0][1])/2).l_scl(T3scl))
T3s.append(T3.cpy().l_tra(T3s[-1][0]).l_scl(T3scl).l_flipY())
T3s.append(T4.cpy().l_tra(T3[2]).l_scl(T3scl).l_flipY())
T3s.append(T3.cpy().l_tra(T3s[-1][3]).l_scl(T3scl).l_flipX().l_flipY().l_rot(pi/4))
T3s.append(T3.cpy().l_tra(T3s[-2][1]).l_scl(T3scl).l_flipY())
T3s.extend([t.cpy().g_tra(T3[1]).g_flipX().g_rot(-pi/2) for t in T3s])
T3s.append(T3.cpy().l_tra(T3s[12][1]).l_scl(T3scl))

T4s = []
T4s.append(T4.cpy().l_tra(T4[0]).l_scl(T4scl))
T4s.append(T3.cpy().l_tra(T4s[-1][3]).l_scl(T4scl).l_flipX().l_rot(pi/4))
T4s.append(T3.cpy().l_tra(T4s[0][1]).l_scl(T4scl))
T4s.append(T1.cpy().l_tra(T4s[-1][1]).l_tra(T1[2][0]*T4scl, (T4s[-1][2][1]-T4s[-1][1][1])/2).l_scl(T4scl))
T4s.append(T3.cpy().l_tra(T4s[-1][0]).l_scl(T4scl).l_rot(pi/4))
T4s.append(T4.cpy().l_tra(T4s[-1][2]).l_scl(T4scl))
T4s.append(T3.cpy().l_tra(T4s[-1][3]).l_scl(T4scl).l_flipY().l_flipX())
T4s.append(T4.cpy().l_tra(T4s[3][3]).l_scl(T4scl))
T4s.extend([t.cpy().g_tra(T4s[-1][3]) for t in T4s])
T4s.pop(-1)
T4s.append(T3.cpy().l_tra(T4s[7][1]).l_scl(T4scl))
T4s.append(T3.cpy().l_tra(T4s[-1][2]).l_scl(T4scl).l_flipY().l_rot(-pi/2))
T4s.append(T4.cpy().l_tra(T4s[-1][2]).l_scl(T4scl))
T4s.append(T4.cpy().l_tra(T4s[3][7]).l_scl(T4scl))
T4s.extend([t.cpy().g_tra(T4s[-1][1]) for t in T4s])
T4s.pop(-1)
T4s.append(T3.cpy().l_tra(T4s[4][0]).l_scl(T4scl).l_flipX().l_rot(pi/4))
T4s.append(T3.cpy().l_tra(T4s[-1][2]).l_scl(T4scl).l_rot(pi/4))
T4s.append(T4.cpy().l_tra(T4s[-1][2]).l_scl(T4scl))
T4s.append(T4.cpy().l_tra(T4s[-1][3]).l_scl(T4scl))
T4s.append(T4.cpy().l_tra(T4s[-1][3]).l_scl(T4scl))
T4s.append(T3.cpy().l_tra(T4s[-1][3]).l_scl(T4scl).l_flipX().l_rot(pi/4))
T4s.append(T3.cpy().l_tra(T4s[-1][2]).l_scl(T4scl).l_rot(pi/4))
T4s.append(T4.cpy().l_tra(T4s[-1][2]).l_scl(T4scl))

draw(T1s)
draw(T2s)
draw(T3s)
draw(T4s)

image.save()
