from math import sqrt, cos, acos, sin, pi
from tile import Tile

alpha = 2*pi/8
dx = cos(alpha)
dy = sin(alpha)

# Prototile T1
T1 = Tile('T1', [(dx+1, 0), (dx*2+1, dy), (dx*2+1, dy+1),
                 (dx+1, dy*2+1), (dx, dy*2+1), (0, dy+1), (0, dy), (dx, 0)])
T1.vec = [(v[0]-dx-0.5, v[1]-dy-0.5) for v in T1.vec]  # Mid point at origin

# Prototile T2
T2 = Tile('T2', [(0, dy), (2, dy), (dx+2, 0)])
T2.vec = [(v[0], v[1]-dy) for v in T2.vec]  # Left bottom at origin

# Prototile T3
T3 = Tile('T3', [(0, 1), (1, 0), (1, 1)])
T3.vec = [(v[0], v[1]-1) for v in T3.vec]  # Left bottom at origin

# Prototile T4
T4 = Tile('T4', [(0, dy), (dx, 0), (dx+1, 0), (1, dy)])
T4.vec = [(v[0], v[1]-dy) for v in T4.vec]  # Left bottom at origin

# Rotation of T1, T2
xa = 2+dx
ya = dy
xb = 2
yb = 0
theta = -acos((xa*xb+ya*yb)/(sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))

# Rotated prototile T1, T2
T1r = T1.cpy().rot(theta).push()
T2r = T2.cpy().rot(theta).flipX().push()

# Scaling of substitution elements
T1.scale = (T1r[4][1]-T1r[0][1])/(dx+2*sqrt(2)+1/sqrt(2)+3)
T2.scale = T1.scale
T3.scale = 1/(5+2*sqrt(2))
T4.scale = T3.scale

T1s = []
T1s.append(T2.cpy().tra(T1r[7]).scl(T1.scale).push())
T1s.append(T3.cpy().tra(T1r[0]).scl(T1.scale).rot(3*pi/4).push())
T1s.append(T4.cpy().tra(T1s[-1][2]).scl(T1.scale).rot(pi/2).push())
T1s.append(T4.cpy().tra(T1s[-1][2]).scl(T1.scale).flipY().push())
T1s.append(T4.cpy().tra(T1s[-1][3]).scl(T1.scale).flipY().push())
T1s.append(T4.cpy().tra(T1s[-1][0]).scl(T1.scale).flipY().flipX().push())
T1s.append(T3.cpy().tra(T1s[-1][3]).scl(T1.scale).flipY().flipX().rot(pi/4).push())
T1s.append(T3.cpy().tra(T1s[-1][0]).scl(T1.scale).flipY().rot(pi/4).push())
T1s.append(T3.cpy().tra(T1s[-1][2]).scl(T1.scale).flipY().flipX().rot(pi/4).push())
T1s.append(T2.cpy().tra(T1s[-1][1]).scl(T1.scale).rot(-pi/4).push())
T1s.append(T3.cpy().tra(T1s[-1][2]).scl(T1.scale).flipX().push())
T1s.append(T3.cpy().tra(T1s[-1][1]).scl(T1.scale).flipY().push())
T1s.append(T3.cpy().tra(T1s[3][1]).scl(T1.scale).rot(-pi/2).push())
T1s.append(T3.cpy().tra(T1s[-1][1]).scl(T1.scale).rot(pi/2).push())
T1s.extend([t.cpy().rot(pi/2).push() for t in T1s])
T1s.extend([t.cpy().rot(pi).push() for t in T1s])
T1s.append(T1.cpy().scl(T1.scale).push())
T1s = [t.cpy().rot(-theta).push() for t in T1s]

T2s = []
T2s.append(T2.cpy().tra(T2r[0]).scl(T2.scale).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2.scale).push())
T2s.append(T2.cpy().tra(T2s[-1][2]).scl(T2.scale).flipY().flipX().push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2.scale).push())
T2s.append(T3.cpy().tra(T2s[-1][1]).scl(T2.scale).rot(pi/4).push())
T2s.append(T3.cpy().tra(T2s[-1][0]).scl(T2.scale).flipX().rot(pi/4).push())
T2s.append(T3.cpy().tra(T2s[1][1]).scl(T2.scale).flipX().rot(pi/4).push())
T2s.append(T3.cpy().tra(T2s[-1][1]).scl(T2.scale).flipX().rot(pi/4).push())
T2s.append(T2.cpy().tra(T2s[-3][2]).scl(T2.scale).rot(pi/4).push())
T2s = [t.cpy().flipX().rot(-theta).push() for t in T2s]

T3s = []
T3s.append(T4.cpy().tra(T3[0]).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][3]).scl(T3.scale).flipX().rot(pi/4).push())
T3s.append(T4.cpy().tra(T3s[-1][2]).scl(T3.scale).flipX().push())
T3s.append(T4.cpy().tra(T3s[-1][3]).scl(T3.scale).flipX().push())
T3s.append(T3.cpy().tra(T3s[0][1]).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).rot(pi/2).push())
T3s.append(T3.cpy().tra(T3s[-1][0]).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-2][1]).scl(T3.scale).rot(-pi/2).push())
T3s.append(T3.cpy().tra(T3s[-1][2]).scl(T3.scale).rot(pi/2).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).rot(3*pi/2).push())
T3s.append(T4.cpy().tra(T3s[-1][1]).scl(T3.scale).push())
T3s.append(T4.cpy().tra(T3s[-1][0]).scl(T3.scale).flipX().rot(pi/2).push())
T3s.append(T3.cpy().tra(T3s[-2][2]).scl(T3.scale).flipY().push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).flipX().push())
T3s.append(T1.cpy().tra(T3s[9][0]).tra(T1[2][0]*T3.scale, (T3s[9][2][1]-T3s[9][0][1])/2).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][0]).scl(T3.scale).flipY().push())
T3s.append(T4.cpy().tra(T3[2]).scl(T3.scale).flipY().push())
T3s.append(T3.cpy().tra(T3s[-1][3]).scl(T3.scale).flipX().flipY().rot(pi/4).push())
T3s.append(T3.cpy().tra(T3s[-2][1]).scl(T3.scale).flipY().push())
T3s.extend([t.cpy().tra(T3[1]).flipX().rot(-pi/2).push() for t in T3s])
T3s.append(T3.cpy().tra(T3s[12][1]).scl(T3.scale).push())

T4s = []
T4s.append(T4.cpy().tra(T4[0]).scl(T4.scale).push())
T4s.append(T3.cpy().tra(T4s[-1][3]).scl(T4.scale).flipX().rot(pi/4).push())
T4s.append(T3.cpy().tra(T4s[0][1]).scl(T4.scale).push())
T4s.append(T1.cpy().tra(T4s[-1][1]).tra(T1[2][0]*T4.scale, (T4s[-1][2][1]-T4s[-1][1][1])/2).scl(T4.scale).push())
T4s.append(T3.cpy().tra(T4s[-1][0]).scl(T4.scale).rot(pi/4).push())
T4s.append(T4.cpy().tra(T4s[-1][2]).scl(T4.scale).push())
T4s.append(T3.cpy().tra(T4s[-1][3]).scl(T4.scale).flipY().flipX().push())
T4s.append(T4.cpy().tra(T4s[3][3]).scl(T4.scale).push())
T4s.extend([t.cpy().tra(T4s[-1][3]).push() for t in T4s])
T4s.pop(-1)
T4s.append(T3.cpy().tra(T4s[7][1]).scl(T4.scale).push())
T4s.append(T3.cpy().tra(T4s[-1][2]).scl(T4.scale).flipY().rot(-pi/2).push())
T4s.append(T4.cpy().tra(T4s[-1][2]).scl(T4.scale).push())
T4s.append(T4.cpy().tra(T4s[3][7]).scl(T4.scale).push())
T4s.extend([t.cpy().tra(T4s[-1][1]).push() for t in T4s])
T4s.pop(-1)
T4s.append(T3.cpy().tra(T4s[4][0]).scl(T4.scale).flipX().rot(pi/4).push())
T4s.append(T3.cpy().tra(T4s[-1][2]).scl(T4.scale).rot(pi/4).push())
T4s.append(T4.cpy().tra(T4s[-1][2]).scl(T4.scale).push())
T4s.append(T4.cpy().tra(T4s[-1][3]).scl(T4.scale).push())
T4s.append(T4.cpy().tra(T4s[-1][3]).scl(T4.scale).push())
T4s.append(T3.cpy().tra(T4s[-1][3]).scl(T4.scale).flipX().rot(pi/4).push())
T4s.append(T3.cpy().tra(T4s[-1][2]).scl(T4.scale).rot(pi/4).push())
T4s.append(T4.cpy().tra(T4s[-1][2]).scl(T4.scale).push())

map = {
    T1: T1s,
    T2: T2s,
    T3: T3s,
    T4: T4s,
}