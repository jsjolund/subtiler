from math import cos, sin, tan, atan, pi
from tile import Tile

alpha = 2*pi/3
beta = atan(tan(pi/3)/5)

T1 = Tile('T1', [(0, 0), (0.5, -tan(pi/3)*0.5), (1, 0)])
T2 = Tile('T2', [(0, 0), (2, 0), (2 + -cos(alpha), -sin(alpha))])

T1scl = 2/(tan(pi/3)/sin(beta))
T2scl = T1scl

T1s = []
T1s.append(T2.cpy().tra(T1[2]).scl(T1scl).rot(beta+pi).push())
T1s.append(T2.cpy().tra(T1[0]).scl(T1scl).rot(beta-pi/3).push())
T1s.append(T2.cpy().tra(T1[1]).scl(T1scl).rot(beta+pi/3).push())
T1s.append(T1.cpy().tra(T1s[0][1]).scl(T1scl).rot(beta).push())

T2s = []
T2s.append(T2.cpy().tra(T2[0]).scl(T2scl).flipX().rot(beta).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2scl).flipX().rot(beta).push())
T2s.append(T1.cpy().tra(T2s[-1][2]).scl(T2scl).flipX().flipY().rot(alpha-beta).push())
T2s.append(T1.cpy().tra(T2s[-1][2]).scl(T2scl).rot(alpha-beta).push())
T2s.append(T1.cpy().tra(T2s[-1][1]).scl(T2scl).flipX().flipY().rot(alpha-beta).push())
T2s.append(T1.cpy().tra(T2[1]).scl(T2scl).flipX().flipY().rot(alpha-beta).push())
T2s.append(T2.cpy().tra(T2s[0][2]).scl(T2scl).flipX().rot(beta).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2scl).flipY().rot(beta).push())
T2s.append(T2.cpy().tra(T2[1]).scl(T2scl).flipY().rot(-alpha+beta).push())

def substitutions(tile):
    match tile.name:
        case 'T1': Ts = T1s
        case 'T2': Ts = T2s
    return Ts