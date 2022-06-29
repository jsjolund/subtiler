from math import acos, sin, tan, atan, cos, pi, sqrt
from tile import Tile


def dst(p1, p2): return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))


def dot4(xa, ya, xb, yb): return -acos((xa*xb+ya*yb) /
                                       (sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))


def dot(p1, p2): return dot4(p1[0], p1[1], p2[0], p2[1])


th = (1+sqrt(5))/2
alpha = acos(0.5*th)

T1 = Tile('T1', [(0, 0), (0.5, -tan(alpha)*0.5), (1, 0)])
T2 = Tile('T2', [(0, 0), (0.5/th**2, -tan(alpha*2)*0.5/th**2), (1/th**2, 0)])

tx = cos(alpha)/th**2
ty = sin(alpha)/th**2
# kite
T5 = Tile('T5', [(0, 0), (tx, -ty), (1/th**2, 0), (tx, ty), (0, 0)])
# dart
T6 = Tile('T6', [(0, 0), (tx, -ty), (ty, 0), (tx, ty), (0, 0)])

T1.scale = T2.scale = T5.scale = T6.scale = th-1

T1s = []
# T1s.append(T1.cpy())
T1s.append(T1.cpy().tra(T1[2]).scl(T1.scale).rot(alpha+pi).push())
T1s.append(T2.cpy().tra(T1s[-1][1]).rot(-alpha*3).push())

T2s = []
T2s.append(T1.cpy().tra(T2[1]).scl(T2.scale/th).rot(3*alpha).push())
T2s.append(T2.cpy().tra(T2[0]).scl(T2.scale).flipX().rot(2*alpha).push())
T2s.append(T2.cpy().tra(T2s[-1][2]).flipY().scl(T2.scale).rot(-4*alpha).push())

T5s = []
T5s.append(T2.cpy().tra(T5[2]).scl(T5.scale).rot(2*alpha+pi).push())
T5s.append(T2.cpy().tra(T5[2]).scl(T5.scale).flipY().rot(-3*alpha+pi).push())

T6s = []
# T6s.append(T1.cpy().tra(T6[0]).scl(T6.scale**2).flipY().rot(-4*alpha).push())
T6s.append(T1.cpy().tra(T6[0]).scl(T6.scale**2).flipX().rot(alpha).push())
T6s.append(T1.cpy().tra(T6[0]).scl(T6.scale**2).rot(alpha).push())

C1 = Tile('C1')
C1.scale = 1
C1s = []
C1s.extend([T5.cpy().tra(0,0).scl(C1.scale).rot(i*2*pi/5).push() for i in range(0,5)])

C2 = Tile('C2')
C2.scale = 1
C2s = []
C2s.extend([T6.cpy().tra(0,0).scl(C1.scale).rot(i*2*pi/5).push() for i in range(0,5)])


def substitutions(tile):
    match tile.name:
        case 'T1': return T1s
        case 'T2': return T2s
        case 'T5': return T5s
        case 'T6': return T6s
        case 'C1': return C1s
        case 'C2': return C2s

tiles = [T1, T2, T5, T6]
