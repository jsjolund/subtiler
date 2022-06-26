from math import sin, atan, pi
from tile import Tile

alpha = 2*pi/4
beta = atan(1/2)

T1 = Tile('T1', [(0, 0), (0, -1), (1, -1), (1, 0)])
T2 = Tile('T2', [(0, 0), (1, 0), (1, -2)])

T1.scale = sin(beta)
T2.scale = 1/(sin(beta)*5)

T1s = []
T1s.append(T2.cpy().tra(T1[1]).scl(T1.scale).flipX().rot(-beta).push())
T1s.append(T2.cpy().tra(T1[2]).scl(T1.scale).flipX().rot(-beta-alpha).push())
T1s.append(T2.cpy().tra(T1[3]).scl(T1.scale).flipX().rot(-beta+pi).push())
T1s.append(T2.cpy().tra(T1[0]).scl(T1.scale).flipX().rot(-beta+alpha).push())
T1s.append(T1.cpy().tra(T1s[-1][1]).scl(T1.scale).rot(beta).push())

T2s = []
T2s.append(T2.cpy().tra(T2[0]).scl(T2.scale).flipY().rot(-beta-alpha).push())
T2s.append(T1.cpy().tra(T2s[-1][1]).scl(T2.scale).rot(beta).push())
T2s.append(T1.cpy().tra(T2s[-1][1]).scl(T2.scale).rot(beta).push())
T2s.append(T2.cpy().tra(T2[1]).scl(T2.scale).flipY().rot(-beta).push())
T2s.append(T2.cpy().tra(T2s[-1][2]).scl(T2.scale).flipY().rot(-beta).push())


def substitutions(tile):
    match tile.name:
        case 'T1': return T1s
        case 'T2': return T2s

tiles = [T1, T2]
