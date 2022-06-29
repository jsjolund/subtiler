from math import cos, sin, tan, pi
from tile import Tile, dst

alpha = pi/6

T1 = Tile('T1', [(0, 0), (0.5, -tan(alpha)/2), (1, 0)])
T2 = Tile('T2', [(0, 0), (2, 0), (cos(alpha*2), -sin(alpha*2))])
T2 = T2.scl(dst(T1[0], T1[1])/dst(T2[0], T2[2])).push()
T3 = Tile('T3', [(0, 0), (0.5, -tan(alpha*2)/2), (1, 0)])

T1.scale = dst(T1[0], T1[1])/dst(T1[0], T1[2])
T2.scale = 1
T3.scale = dst(T3[0], T3[1])/(dst(T2[0], T2[1]) + dst(T2[0], T2[2]))

T1s = []
T1s.append(T1.cpy().tra(T1[0]).scl(T1.scale).flipX().rot(alpha).push())
T1s.append(T2.cpy().tra(T1s[-1][1]).scl(T1.scale).push())

T2s = []
T2s.append(T3.cpy().tra(T2[0]).scl(T2.scale).push())
T2s.append(T1.cpy().tra(T2s[-1][2]).scl(T2.scale).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2.scale).rot(pi+alpha).push())

T3s = []
T3s.append(T2.cpy().tra(T3[0]).scl(T3.scale).flipX().rot(alpha*2).push())
T3s.append(T2.cpy().tra(T3[2]).scl(T3.scale).flipY().push())
T3s.append(T2.cpy().tra(T3[1]).scl(T3.scale).flipX().rot(pi+alpha*4).push())
T3s.append(T3.cpy().tra(T3s[-1][2]).scl(T3.scale).rot(pi/3+alpha).push())


def substitutions(tile):
    match tile.name:
        case 'T1': return T1s
        case 'T2': return T2s
        case 'T3': return T3s


tiles = [T1, T2, T3]
