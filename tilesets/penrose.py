from math import acos, sin, tan, atan, cos, pi, sqrt
from tile import Tile


def dst(p1, p2): return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))


def dot4(xa, ya, xb, yb): return -acos((xa*xb+ya*yb) /
                                       (sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))


def dot(p1, p2): return dot4(p1[0], p1[1], p2[0], p2[1])


th = (1+sqrt(5))/2
alpha = acos(0.5*th)

tx = cos(alpha)/th**2
ty = sin(alpha)/th**2

T1 = Tile('T1', [(0, 0), (0.5, -tan(alpha)*0.5), (1, 0)])
T2 = Tile('T2', [(0, 0), (0.5/th**2, -tan(alpha*2)*0.5/th**2), (1/th**2, 0)])
T3 = Tile('T3', [(0, 0), (tx, -ty), (1/th**2, 0), (tx, ty), (0, 0)]) # kite
T4 = Tile('T4', [(0, 0), (tx, -ty), (ty, 0), (tx, ty), (0, 0)]) # dart

T1.scale = T2.scale = T3.scale = T4.scale = th-1

T1s = []
T1s.append(T1.cpy().tra(T1[2]).scl(T1.scale).rot(alpha+pi).push())
T1s.append(T2.cpy().tra(T1s[-1][2]).flipY().rot(3*alpha).push())

T2s = []
T2s.append(T1.cpy().tra(T2[1]).scl(T2.scale/th).rot(3*alpha).push())
T2s.append(T2.cpy().tra(T2s[-1][2]).scl(T2.scale).rot(3*alpha).push())
T2s.append(T2.cpy().tra(T2s[-1][0]).flipY().scl(T2.scale).rot(-4*alpha).push())

T3s = []
T3s.append(T2.cpy().tra(T3[2]).scl(T3.scale).rot(2*alpha+pi).push())
T3s.append(T2.cpy().tra(T3[2]).scl(T3.scale).flipY().rot(-3*alpha+pi).push())

T4s = []
T4s.append(T1.cpy().tra(T4[0]).scl(T4.scale**2).flipX().rot(alpha).push())
T4s.append(T1.cpy().tra(T4[0]).scl(T4.scale**2).rot(alpha).push())

C1 = Tile('C1')
C1.scale = 1
C1s = []
C1s.extend([T3.cpy().tra(0,0).scl(C1.scale).rot(i*2*pi/5).push() for i in range(0,5)])

C2 = Tile('C2')
C2.scale = 1
C2s = []
C2s.extend([T4.cpy().tra(0,0).scl(C1.scale).rot(i*2*pi/5).push() for i in range(0,5)])


def substitutions(tile):
    match tile.name:
        case 'T1': return T1s
        case 'T2': return T2s
        case 'T3': return T3s
        case 'T4': return T4s
        case 'C1': return C1s
        case 'C2': return C2s

tiles = [T1, T2, T3, T4]
