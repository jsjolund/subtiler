from math import sin, cos, pi, tan
from tile import Tile, dst

alpha = pi/5

T1 = Tile('T1', [(0, 0), (0.5, -tan(alpha)*0.5), (1, 0)])
T2 = Tile('T2', [(0, 0), (1, 0), (cos(alpha), -sin(alpha))])

T1.scale = dst(T1[0], T1[1])/dst(T1[0], T1[2])
T2.scale = dst(T2[1], T2[2])/dst(T2[0], T2[2])

T1s = []
T1s.append(T2.cpy().tra(T1[0]).scl(T1.scale).push())
T1s.append(T1.cpy().tra(T1[2]).scl(T1.scale).rot(pi+alpha).push())

T2s = []
T2s.append(T1.cpy().tra(T2[0]).scl(T2.scale).push())
T2s.append(T2.cpy().tra(T2[2]).scl(T2.scale).rot(pi/2+alpha/2).push())
T2s.append(T2.cpy().tra(T2[2]).scl(T2.scale).rot(pi/2+1.5*alpha).push())

map = {
    T1: T1s,
    T2: T2s,
}