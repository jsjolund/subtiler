from math import cos, sin, tan, atan, pi
from tile import Tile

alpha = 2*pi/3
beta = atan(tan(pi/3)/5)

T1 = Tile('T1', [(0, 0), (0.5, -tan(pi/3)*0.5), (1, 0)])
T2 = Tile('T2', [(0, 0), (2, 0), (2 + -cos(alpha), -sin(alpha))])

T1.scale = 2/(tan(pi/3)/sin(beta))
T2.scale = T1.scale

T1s = []
T1s.append(T2.cpy().tra(T1[2]).scl(T1.scale).rot(beta+pi).push())
T1s.append(T2.cpy().tra(T1[0]).scl(T1.scale).rot(beta-pi/3).push())
T1s.append(T2.cpy().tra(T1[1]).scl(T1.scale).rot(beta+pi/3).push())
T1s.append(T1.cpy().tra(T1s[0][1]).scl(T1.scale).rot(beta).push())

T2s = []
T2s.append(T2.cpy().tra(T2[0]).scl(T2.scale).flipX().rot(beta).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2.scale).flipX().rot(beta).push())
T2s.append(T1.cpy().tra(T2s[-1][2]).scl(T2.scale).flipX().flipY().rot(alpha-beta).push())
T2s.append(T1.cpy().tra(T2s[-1][2]).scl(T2.scale).rot(alpha-beta).push())
T2s.append(T1.cpy().tra(T2s[-1][1]).scl(T2.scale).flipX().flipY().rot(alpha-beta).push())
T2s.append(T1.cpy().tra(T2[1]).scl(T2.scale).flipX().flipY().rot(alpha-beta).push())
T2s.append(T2.cpy().tra(T2s[0][2]).scl(T2.scale).flipX().rot(beta).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2.scale).flipY().rot(beta).push())
T2s.append(T2.cpy().tra(T2[1]).scl(T2.scale).flipY().rot(-alpha+beta).push())

map = {
    T1: T1s,
    T2: T2s,
}