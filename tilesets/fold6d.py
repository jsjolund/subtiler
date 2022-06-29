from math import cos, sin, tan, pi
from tile import Tile, dst

alpha = pi/6

T1 = Tile('T1', [(0, 0), (0.5, -tan(alpha)/2), (1, 0)])

T2 = Tile('T2', [(0, 0), (2, 0), (cos(alpha*2), -sin(alpha*2))])
t2s = dst(T1[0], T1[1])/dst(T2[0], T2[2])
T2 = T2.scl(t2s).push()

T3 = Tile('T3', [(0, 0), (2, 0), (1-cos(alpha*2+pi), sin(alpha*2+pi))])
T3 = T3.scl(t2s).push()

T4 = Tile('T4', [(0, 0), (0.5, -tan(alpha*2)/2), (1, 0)])

T5 = T4.cpy()
T5.name = 'T5'

T6 = Tile('T6', [(0, 0), (0.5, -tan(alpha*2)/2), (1.5, -tan(alpha*2)/2),
          (2, 0), (1.5, tan(alpha*2)/2), (0.5, tan(alpha*2)/2)])


T1.scale = dst(T1[0], T1[1])/dst(T1[0], T1[2])
T2.scale = 1
T3.scale = 1
T4.scale = dst(T4[0], T4[1])/(dst(T2[0], T2[1]) + dst(T2[0], T2[2]))
T5.scale = 1/3
T6.scale = 1

T1s = []
T1s.append(T1.cpy().tra(T1[1]).scl(T1.scale).flipX().rot(-alpha).push())
T1s.append(T2.cpy().tra(T1s[-1][1]).scl(T1.scale).flipY().push())

T2s = []
T2s.append(T3.cpy().tra(T2[0]).scl(T2.scale).flipX().rot(alpha).push())
T2s.append(T3.cpy().tra(T2[0]).scl(T2.scale).rot(-alpha).push())
T2s.append(T3.cpy().tra(T2s[0][2]).tra(dst(T3[0], T3[2]), 0).scl(
    T2.scale).flipX().flipY().rot(alpha).push())

T3s = []
T3s.append(T1.cpy().tra(T3[0]).scl(T3.scale).push())
T3s.append(T5.cpy().tra(T3s[-1][2]).scl(T3.scale).push())
T3s.append(T2.cpy().tra(T3s[-2][1]).scl(T3.scale).flipY().rot(pi+alpha).push())

T4s = []
T4s.append(T2.cpy().tra(T4[0]).scl(T4.scale).rot(0).push())
T4s.append(T2.cpy().tra(T4[1]).scl(T4.scale).rot(pi-2*alpha).push())
T4s.append(T2.cpy().tra(T4[2]).scl(T4.scale).rot(pi+2*alpha).push())
T4s.append(T5.cpy().tra(
    T4s[-1][1]).scl(T4.scale).flipY().rot(pi/3+alpha).push())

T5s = []
T5s.append(T4.cpy().tra(T5[2]).scl(T5.scale).flipY().push())
T5s.append(T4.cpy().tra(T5[0]).scl(T5.scale).push())
T5s.append(T6.cpy().tra(T5s[-1][1]).scl(T5.scale).push())
T5s.append(T4.cpy().tra(T5s[-1][1]).scl(T5.scale).push())

T6s1 = []
T6s1.append(T1.cpy().tra(T6[1]).scl(T6.scale).rot(alpha*4).push())
T6s1.append(T2.cpy().tra(T6s1[-1][0]).scl(T6.scale).flipX().rot(-alpha).push())
T6s1.append(T3.cpy().tra(T6s1[-1][0]).scl(T6.scale).rot(alpha).push())
T6s = []
T6s.extend([t.cpy().rot(0).push() for t in T6s1])
T6s.extend([t.cpy().tra(T6s1[-1][2]).rot(2*pi/3).push() for t in T6s1])
T6s.extend([t.cpy().tra(T6s[-1][2]).rot(4*pi/3).push() for t in T6s1])
T6s.append(T4.cpy().tra(T6s[-1][1]).scl(T6.scale).flipX().push())


def substitutions(tile):
    match tile.name:
        case 'T1': return T1s
        case 'T2': return T2s
        case 'T3': return T3s
        case 'T4': return T4s
        case 'T5': return T5s
        case 'T6': return T6s


tiles = [T1, T2, T3, T4, T5, T6]
