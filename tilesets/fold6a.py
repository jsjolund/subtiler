from math import cos, sin, tan, atan, pi
from tile import Tile

alpha = 2*pi/6
beta = atan(tan(alpha)/5)
dx = cos(alpha)
dy = sin(alpha)

T1 = Tile('T1', [(0, 0), (dx, -dy), (dx + 1, -dy),
          (dx*2+1, 0), (dx + 1, dy), (dx, dy)])
T1.vec = [(v[0]-dx-0.5, v[1]) for v in T1.vec]
T1.scale = 2/(tan(pi/3)/sin(beta))

T2 = Tile('T2', [(0, 0), (2, 0), (2  +cos(alpha), -sin(alpha))])
T2.scale = T1.scale

T3 = Tile('T3', [(0, 0), (0.5, -sin(pi/3)), (1, 0)])
T3.scale = 1/7

T1s = []
T1s.append(T2.cpy().tra(T1[0]).scl(T1.scale).rot(beta+2*alpha+pi).push())
T1s.append(T2.cpy().tra(T1[1]).scl(T1.scale).rot(beta).push())
T1s.append(T2.cpy().tra(T1[2]).scl(T1.scale).rot(beta+alpha).push())
T1s.append(T2.cpy().tra(T1[3]).scl(T1.scale).rot(beta+2*alpha).push())
T1s.append(T2.cpy().tra(T1[4]).scl(T1.scale).rot(beta+pi).push())
T1s.append(T2.cpy().tra(T1[5]).scl(T1.scale).rot(beta+alpha+pi).push())
T13s = []
T13s.append(T3.cpy().tra(T1[0]).scl(T1.scale).rot(beta).push())
T13s.append(T3.cpy().tra(T13s[-1][1]).scl(T1.scale).rot(beta).push())
T13s.append(T3.cpy().tra(T13s[-2][2]).scl(T1.scale).rot(beta).push())
T13s.append(T3.cpy().tra(T13s[-3][1]).scl(T1.scale).rot(beta+pi/3).push())
T1s.extend(T13s)
T1s.extend([t.cpy().rot(pi/3).push() for t in T13s])
T1s.extend([t.cpy().rot(2*pi/3).push() for t in T13s])
T1s.extend([t.cpy().rot(pi).push() for t in T13s])
T1s.extend([t.cpy().rot(4*pi/3).push() for t in T13s])
T1s.extend([t.cpy().rot(5*pi/3).push() for t in T13s])
T1s.append(T1.cpy().scl(T1.scale).rot(beta).push())

T2s = []
T2s.append(T2.cpy().tra(T2[0]).scl(T2.scale).flipX().rot(beta).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2.scale).flipX().rot(beta).push())
T2s.append(T3.cpy().tra(T2s[-1][1]).scl(T2.scale).flipX().flipY().rot(alpha-beta+pi).push())
T2s.append(T3.cpy().tra(T2s[-1][2]).scl(T2.scale).rot(alpha-beta).push())
T2s.append(T3.cpy().tra(T2s[-1][1]).scl(T2.scale).flipX().flipY().rot(alpha-beta).push())
T2s.append(T3.cpy().tra(T2s[-1][2]).scl(T2.scale).flipX().flipY().rot(alpha-beta+pi).push())
T2s.append(T2.cpy().tra(T2s[0][2]).scl(T2.scale).flipX().rot(beta).push())
T2s.append(T2.cpy().tra(T2s[-1][1]).scl(T2.scale).flipY().rot(beta).push())
T2s.append(T2.cpy().tra(T2s[-5][2]).scl(T2.scale).flipY().rot(beta+alpha+pi).push())

T3s = []
T3s.append(T3.cpy().tra(T3[0]).scl(T3.scale).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).tra((0.5+dx)*T3.scale, 0).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).tra((0.5+dx)*T3.scale, 0).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).tra((0.5+dx)*T3.scale, 0).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[1][3]).scl(T3.scale).rot(-alpha).push())
T3s.append(T3.cpy().tra(T3s[3][3]).scl(T3.scale).rot(-alpha).push())
T3s.append(T3.cpy().tra(T3s[1][4]).scl(T3.scale).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).tra((0.5+dx)*T3.scale, 0).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).tra((0.5+dx)*T3.scale, 0).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-4][3]).scl(T3.scale).rot(-alpha).push())
T3s.append(T3.cpy().tra(T3s[-5][4]).scl(T3.scale).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).tra((0.5+dx)*T3.scale, 0).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).push())
T3s.append(T3.cpy().tra(T3s[-2][4]).scl(T3.scale).push())

map = {
    T1: T1s,
    T2: T2s,
    T3: T3s,
}