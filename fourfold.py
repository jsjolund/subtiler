from math import sin, atan, pi
from tile import Tile

# Prototile T1
T1 = Tile('T1', [(0, 0), (0, -1), (1, -1), (1, 0)])

# Prototile T2
T2 = Tile('T2', [(0, 0), (1, 0), (1, -2)])

theta = atan(1/2)

# Scaling of substitution elements
T1scl = sin(theta)
T2scl = 1/(sin(theta)*5)

T1s = []
T1s.append(T2.cpy().tra(T1[1]).scl(T1scl).flipX().rot(-theta).push())
T1s.append(T2.cpy().tra(T1[2]).scl(T1scl).flipX().rot(-theta-pi/2).push())
T1s.append(T2.cpy().tra(T1[3]).scl(T1scl).flipX().rot(-theta+pi).push())
T1s.append(T2.cpy().tra(T1[0]).scl(T1scl).flipX().rot(-theta+pi/2).push())
T1s.append(T1.cpy().tra(T1s[-1][1]).scl(T1scl).rot(theta).push())

T2s = []
T2s.append(T2.cpy().tra(T2[0]).scl(T2scl).flipY().rot(-theta-pi/2).push())
T2s.append(T1.cpy().tra(T2s[-1][1]).scl(T2scl).rot(theta).push())
T2s.append(T1.cpy().tra(T2s[-1][1]).scl(T2scl).rot(theta).push())
T2s.append(T2.cpy().tra(T2[1]).scl(T2scl).flipY().rot(-theta).push())
T2s.append(T2.cpy().tra(T2s[-1][2]).scl(T2scl).flipY().rot(-theta).push())


def substitutions(tile):
    match tile.name:
        case 'T1': Ts = T1s
        case 'T2': Ts = T2s
    return Ts
