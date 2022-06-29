from math import cos, sin, tan, pi
from tile import Tile, dst

alpha = pi/7

T1 = Tile('T1', [(0, 0), (cos(alpha)/(cos(alpha*2)*2), -sin(alpha)/(cos(alpha*2)*2)), (1, 0)])

T2 = Tile('T2', [(0, 0), (1, 0), (1+cos(alpha+pi), -sin(alpha+pi))])

T3 = Tile('T3', [(0, 0), (cos(-alpha), sin(-alpha)),
          ((sin(alpha*2) + sin(-alpha))/tan(alpha+pi), sin(alpha*2) + sin(-alpha))])

T1.scale = dst(T1[1], T1[2])/(dst(T3[0], T3[2])+dst(T1[1], T1[2]))
T2.scale = dst(T2[0], T2[2])/(dst(T3[1], T3[2])+dst(T1[1], T1[2]))
T3.scale = dst(T3[0], T3[1])/(dst(T1[0], T1[1])+dst(T1[0], T1[2])+dst(T2[0], T2[1]))

T1s = []
T1s.append(T3.cpy().tra(T1[1]).scl(T1.scale).flipX().rot(-alpha*3).push())
T1s.append(T1.cpy().tra(T1s[-1][1]).scl(T1.scale).push())
T1s.append(T1.cpy().tra(T1s[-1][0]).scl(T1.scale).rot(alpha/2-pi/2).push())
T1s.append(T3.cpy().tra(T1s[-1][0]).scl(T1.scale).rot(-alpha*5).push())
T1s.append(T1.cpy().tra(T1s[-1][0]).scl(T1.scale).rot(pi+alpha).push())
T1s.append(T2.cpy().tra(T1s[-1][2]).scl(T1.scale).flipY().rot(alpha).push())

T2s = []
T2s.append(T3.cpy().tra(T2[2]).scl(T2.scale).flipX().rot(alpha*3).push())
T2s.append(T1.cpy().tra(T2s[-1][1]).scl(T2.scale).rot(alpha+pi).push())
T2s.append(T2.cpy().tra(T2s[-1][0]).scl(T2.scale).rot(alpha+pi).push())
T2s.append(T2.cpy().tra(T2s[-1][0]).scl(T2.scale).flipX().rot(-alpha*5).push())
T2s.append(T2.cpy().tra((T2s[-1][0][0]+T2.scale, T2s[-1][0][1])).scl(T2.scale).rot(pi).push())
T2s.append(T1.cpy().tra(T2s[-1][0]).scl(T2.scale).rot(pi).push())
T2s.append(T1.cpy().tra(T2s[-2][2]).scl(T2.scale).flipX().rot(pi+alpha).push())
T2s.append(T2.cpy().tra(T2s[-1][0]).scl(T2.scale).push())

T3s = []
T3s.append(T2.cpy().tra((T3[0][0]+1*T3.scale, T3[0][1])).scl(T3.scale).flipY().rot(0).push())
T3s.append(T2.cpy().tra(T3s[-1][0]).scl(T3.scale).rot(pi).push())
T3s.append(T3.cpy().tra(T3s[-2][2]).scl(T3.scale).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).scl(T3.scale).flipX().rot(pi+alpha).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3.scale).rot(-alpha).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).scl(T3.scale).flipX().rot(pi+alpha*2).push())
T3s.append(T1.cpy().tra(T3s[-1][0]).scl(T3.scale).flipX().rot(alpha).push())
T3s.append(T3.cpy().tra(T3s[-1][0]).scl(T3.scale).flipX().rot(-alpha).push())
T3s.append(T1.cpy().tra(T3s[-1][0]).scl(T3.scale).flipX().rot(-alpha*2).push())
T3s.append(T1.cpy().tra(T3s[-1][1]).scl(T3.scale).flipX().rot(-alpha*3).push())
T3s.append(T2.cpy().tra(T3s[-2][2]).scl(T3.scale).rot(alpha*4).push())


def substitutions(tile):
    match tile.name:
        case 'T1': return T1s
        case 'T2': return T2s
        case 'T3': return T3s


tiles = [T1, T2, T3]
