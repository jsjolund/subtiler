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
            case 'T1': color = '#FE52F0'
            case 'T2': color = '#FE52F0'
            case 'T3': color = '#FE6152'
            case 'T4': color = '#B752FE'
        if force_color != None:
            color = force_color
        path = tile.transform()
        image.add(image.polygon(path, id=tile.name, stroke='black', stroke_width='0.002px',
                                fill=color, transform="translate(300,300),scale(230)"))


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
T1r = T1.cpy().rot(theta).push()
T1scl = (T1r[4][1]-T1r[0][1])/(sqrt(2)+1+dx +
                               1+1+sqrt(2)+sqrt(1-(sqrt(2)/2)**2))

T2 = Tile('T2', [(0, dy), (2, dy), (dx+2, 0)])
T2 = T2.v_tra(0, -dy)  # Left bottom at origin
T2r = T2.cpy().rot(theta).flipX().push()
T2scl = (T2r[0][1]-T2r[1][1])/(sqrt(1-(sqrt(2)/2)**2)*2)

T3 = Tile('T3', [(0, 1), (1, 0), (1, 1)])
T3 = T3.v_tra(0, -1)  # Left bottom at origin
T3scl = 1/(1+sqrt(2)+1+1+1+sqrt(2)+1)

T4 = Tile('T4', [(0, dy), (dx, 0), (dx+1, 0), (1, dy)])
T4 = T4.v_tra(0, -dy)  # Left bottom at origin
T4scl = dy/((1+dy*2)*2+dy)

T1s = []
T1s.append(T2.cpy().tra(T1r[7]).scl(T1scl).push())
T1s.append(T3.cpy().tra(T1r[0]).scl(T1scl).rot(3*pi/4).push())
T1s.append(T4.cpy().tra(T1s[-1][2]).scl(T1scl).rot(pi/2).push())
T1s.append(T4.cpy().tra(T1s[-1][2]).scl(T1scl).flipY().push())
T1s.append(T4.cpy().tra(T1s[-1][3]).scl(T1scl).flipY().push())
T1s.append(T4.cpy().tra(T1s[-1][0]).scl(T1scl).flipY().flipX().push())
T1s.append(T3.cpy().tra(T1s[-1][3]).scl(T1scl).flipY().flipX().rot(pi/4).push())
T1s.append(T3.cpy().tra(T1s[-1][0]).scl(T1scl).flipY().rot(pi/4).push())
T1s.append(T3.cpy().tra(T1s[-1][2]).scl(T1scl).flipY().flipX().rot(pi/4).push())
T1s.append(T2.cpy().tra(T1s[-1][1]).scl(T1scl).rot(-pi/4).push())
T1s.append(T3.cpy().tra(T1s[-1][2]).scl(T1scl).flipX().push())
T1s.append(T3.cpy().tra(T1s[-1][1]).scl(T1scl).flipY().push())
T1s.append(T3.cpy().tra(T1s[3][1]).scl(T1scl).rot(-pi/2).push())
T1s.append(T3.cpy().tra(T1s[-1][1]).scl(T1scl).rot(pi/2).push())
T1s.extend([t.cpy().rot(pi/2).push() for t in T1s])
T1s.extend([t.cpy().rot(pi).push() for t in T1s])
T1s.append(T1.cpy().scl(T1scl).push())
T1s = [t.cpy().rot(-theta).push() for t in T1s]

T2s = []
T2s.append(T2.cpy().tra(T2r[0]).scl(T2scl).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2scl).push())
T2s.append(T2.cpy().tra(T2s[-1][2]).scl(T2scl).flipY().flipX().push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2scl).push())
T2s.append(T3.cpy().tra(T2s[-1][1]).scl(T2scl).rot(pi/4).push())
T2s.append(T3.cpy().tra(T2s[-1][0]).scl(T2scl).flipX().rot(pi/4).push())
T2s.append(T3.cpy().tra(T2s[1][1]).scl(T2scl).flipX().rot(pi/4).push())
T2s.append(T3.cpy().tra(T2s[-1][1]).scl(T2scl).flipX().rot(pi/4).push())
T2s.append(T2.cpy().tra(T2s[-3][2]).scl(T2scl).rot(pi/4).push())
T2s = [t.cpy().flipX().rot(-theta).push() for t in T2s]

T3s = []
T3s.append(T4.cpy().tra(T3[0]).scl(T3scl).push())
T3s.append(T3.cpy().tra(T3s[-1][3]).scl(T3scl).flipX().rot(pi/4).push())
T3s.append(T4.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().push())
T3s.append(T4.cpy().tra(T3s[-1][3]).scl(T3scl).flipX().push())
T3s.append(T3.cpy().tra(T3s[0][1]).scl(T3scl).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3scl).rot(pi/2).push())
T3s.append(T3.cpy().tra(T3s[-1][0]).scl(T3scl).push())
T3s.append(T3.cpy().tra(T3s[-2][1]).scl(T3scl).rot(-pi/2).push())
T3s.append(T3.cpy().tra(T3s[-1][2]).scl(T3scl).rot(pi/2).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3scl).rot(3*pi/2).push())
T3s.append(T4.cpy().tra(T3s[-1][1]).scl(T3scl).push())
T3s.append(T4.cpy().tra(T3s[-1][0]).scl(T3scl).flipX().rot(pi/2).push())
T3s.append(T3.cpy().tra(T3s[-2][2]).scl(T3scl).flipY().push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3scl).flipX().push())
T3s.append(T1.cpy().tra(T3s[9][0]).tra(T1[2][0]*T3scl, (T3s[9][2][1]-T3s[9][0][1])/2).scl(T3scl).push())
T3s.append(T3.cpy().tra(T3s[-1][0]).scl(T3scl).flipY().push())
T3s.append(T4.cpy().tra(T3[2]).scl(T3scl).flipY().push())
T3s.append(T3.cpy().tra(T3s[-1][3]).scl(T3scl).flipX().flipY().rot(pi/4).push())
T3s.append(T3.cpy().tra(T3s[-2][1]).scl(T3scl).flipY().push())
T3s.extend([t.cpy().tra(T3[1]).flipX().rot(-pi/2).push() for t in T3s])
T3s.append(T3.cpy().tra(T3s[12][1]).scl(T3scl).push())

T4s = []
T4s.append(T4.cpy().tra(T4[0]).scl(T4scl).push())
T4s.append(T3.cpy().tra(T4s[-1][3]).scl(T4scl).flipX().rot(pi/4).push())
T4s.append(T3.cpy().tra(T4s[0][1]).scl(T4scl).push())
T4s.append(T1.cpy().tra(T4s[-1][1]).tra(T1[2][0]*T4scl, (T4s[-1][2][1]-T4s[-1][1][1])/2).scl(T4scl).push())
T4s.append(T3.cpy().tra(T4s[-1][0]).scl(T4scl).rot(pi/4).push())
T4s.append(T4.cpy().tra(T4s[-1][2]).scl(T4scl).push())
T4s.append(T3.cpy().tra(T4s[-1][3]).scl(T4scl).flipY().flipX().push())
T4s.append(T4.cpy().tra(T4s[3][3]).scl(T4scl).push())
T4s.extend([t.cpy().tra(T4s[-1][3]).push() for t in T4s])
T4s.pop(-1)
T4s.append(T3.cpy().tra(T4s[7][1]).scl(T4scl).push())
T4s.append(T3.cpy().tra(T4s[-1][2]).scl(T4scl).flipY().rot(-pi/2).push())
T4s.append(T4.cpy().tra(T4s[-1][2]).scl(T4scl).push())
T4s.append(T4.cpy().tra(T4s[3][7]).scl(T4scl).push())
T4s.extend([t.cpy().tra(T4s[-1][1]).push() for t in T4s])
T4s.pop(-1)
T4s.append(T3.cpy().tra(T4s[4][0]).scl(T4scl).flipX().rot(pi/4).push())
T4s.append(T3.cpy().tra(T4s[-1][2]).scl(T4scl).rot(pi/4).push())
T4s.append(T4.cpy().tra(T4s[-1][2]).scl(T4scl).push())
T4s.append(T4.cpy().tra(T4s[-1][3]).scl(T4scl).push())
T4s.append(T4.cpy().tra(T4s[-1][3]).scl(T4scl).push())
T4s.append(T3.cpy().tra(T4s[-1][3]).scl(T4scl).flipX().rot(pi/4).push())
T4s.append(T3.cpy().tra(T4s[-1][2]).scl(T4scl).rot(pi/4).push())
T4s.append(T4.cpy().tra(T4s[-1][2]).scl(T4scl).push())


iterations = 1
base_tile = T1s

Tr = [t for t in base_tile]
for i in range(0, iterations):
    Ti = []
    for t in Tr:
        match t.name:
            case 'T1': Ts = T1s
            case 'T2': Ts = T2s
            case 'T3': Ts = T3s
            case 'T4': Ts = T4s
        for ts in Ts:
            tc = ts.cpy()
            tc.transforms.extend(t.transforms)
            Ti.append(tc)
    Tr = Ti
draw(Tr)

# draw(T1)
# draw(T2)
# draw(T3)
# draw(T4)
# draw(T1s)
# draw(T2s)
# draw(T3s)
# draw(T4s)

image.save()
