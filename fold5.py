from math import sin, cos, pi, tan, atan
from tile import Tile

beta = 2*pi/5
alpha = atan((sin(2*beta))/(2 - cos(2*beta)))
dx = cos(beta)
dy = sin(beta)

T1 = Tile('T1', [(0, 0), (1, 0), (1 + dx, -dy),
          (1 + dx + cos(2*beta), -dy - sin(2*beta)), (-dx, -dy)])
T1 = T1.tra_vec(-0.5, -tan((pi+2*pi/5)/2)*0.5)
T1scl = 1/(sin(2*beta)/sin(alpha))

T2 = Tile('T2', [(0, 0), (2, 0), (2 - cos(2*beta), -sin(2*beta))])
T2scl = T1scl

T345v = [(0, 0), (-cos(2*beta), -sin(2*beta)), (-2*cos(2*beta), 0)]
T3 = Tile('T3', T345v)
T4 = Tile('T4', T345v)
T5 = Tile('T5', T345v)
T3scl = -2*cos(2*beta)/(-2*cos(2*beta)*7 + 2)

T67v = [(0, 0), (cos(beta), -sin(beta)), (2*cos(beta), 0)]
T6 = Tile('T6', T67v)
T7 = Tile('T7', T67v)

T1s1 = []
T1s1.append(T2.cpy().tra(T1[0]).scl(T1scl).rot(alpha+beta+pi).push())
T1s1.append(T4.cpy().tra(T1[0]).scl(T1scl).flipX().rot(-alpha+beta).push())
T1s1.append(T5.cpy().tra(T1s1[-1][0]).scl(T1scl).rot(alpha-beta).push())
T1s1.append(T5.cpy().tra(T1s1[-1][1]).scl(T1scl).rot(alpha-beta).push())
T1s1.append(T5.cpy().tra(T1s1[-1][0]).scl(T1scl).flipX().rot(-alpha+beta).push())
T1s = []
T1s.extend([t.cpy() for t in T1s1])
T1s.extend([t.cpy().rot(beta).push() for t in T1s1])
T1s.extend([t.cpy().rot(beta*2).push() for t in T1s1])
T1s.extend([t.cpy().rot(beta*3).push() for t in T1s1])
T1s.extend([t.cpy().rot(beta*4).push() for t in T1s1])
T1s.append(T1.cpy().scl(T1scl).rot(alpha).push())

T2s = []
T2s.append(T2.cpy().tra(T2[0]).scl(T2scl).flipX().rot(alpha).push())
T2s.append(T2.cpy().tra(T2s[-1][2]).scl(T2scl).flipX().rot(alpha).push())
T2s.append(T2.cpy().tra(T2s[-1][2]).scl(T2scl).flipX().rot(alpha-2*beta+pi).push())
T2s.append(T7.cpy().tra(T2s[-3][2]).scl(T2scl).flipX().flipY().rot(pi-alpha-beta).push())
T2s.append(T6.cpy().tra(T2s[-1][2]).scl(T2scl).rot(pi-alpha-beta).push())
T2s.append(T7.cpy().tra(T2s[-1][1]).scl(T2scl).flipX().flipY().rot(pi-alpha-beta).push())
T2s.append(T6.cpy().tra(T2s[-1][2]).scl(T2scl).rot(pi-alpha-beta).push())
T2s.append(T5.cpy().tra(T2s[-1][0]).scl(T2scl).flipY().rot(alpha+pi).push())
T2s.append(T5.cpy().tra(T2s[-1][1]).scl(T2scl).flipY().rot(alpha+pi).push())
T2s.append(T5.cpy().tra(T2s[-1][0]).scl(T2scl).rot(-alpha).push())
T2s.append(T5.cpy().tra(T2s[-1][1]).scl(T2scl).flipY().rot(alpha+pi).push())

T3s = []
T3s.append(T3.cpy().tra(T3[0]).scl(T3scl).push())
T3s.append(T4.cpy().tra(T3s[-1][1]).scl(T3scl).flipX().push())
T3s.append(T7.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().rot(-beta).push())
T3s.append(T7.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().rot(-beta+pi).push())
T3s.append(T3.cpy().tra(T3s[-1][0]).scl(T3scl).push())
T3s.append(T4.cpy().tra(T3s[-1][1]).scl(T3scl).flipX().push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3scl).push())
T3s.append(T5.cpy().tra(T3s[-1][1]).scl(T3scl).flipX().push())
T3s.append(T3.cpy().tra(T3s[0][1]).scl(T3scl).push())
T3s.append(T4.cpy().tra(T3s[-1][1]).scl(T3scl).flipX().push())
T3s.append(T7.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().rot(-beta).push())
T3s.append(T7.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().rot(-beta+pi).push())
T3s.append(T5.cpy().tra(T3s[-1][0]).scl(T3scl).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3scl).flipX().push())
T3s.append(T5.cpy().tra(T3s[-1][1]).scl(T3scl).push())
T3s.append(T4.cpy().tra(T3s[8][1]).scl(T3scl).push())
T3s.append(T3.cpy().tra(T3s[-1][1]).scl(T3scl).flipX().push())
T3s.append(T6.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().rot(-beta).push())
T3s.append(T6.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().rot(-beta+pi).push())
T3s.append(T3.cpy().tra(T3s[-1][0]).scl(T3scl).push())
T3s.append(T1.cpy().tra(T3s[-1][2]).tra(0, -0.5/cos((pi-2*pi/5)/2)*T3scl).scl(T3scl).rot(pi).push())
T3s.append(T4.cpy().tra(T3s[15][1]).scl(T3scl).push())
T3s.append(T7.cpy().tra(T3s[-1][2]).scl(T3scl).rot(-beta).push())
T3s.append(T6.cpy().tra(T3s[-1][2]).scl(T3scl).rot(-beta+pi).push())
T3s.append(T4.cpy().tra(T3s[-2][1]).scl(T3scl).flipX().rot(-2*beta-pi).push())
T3s.append(T4.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().rot(-beta).push())
T3s.append(T5.cpy().tra(T3s[-1][0]).scl(T3scl).rot(beta).push())
T3s.append(T6.cpy().tra(T3s[-1][1]).scl(T3scl).rot(-beta).push())
T3s.append(T6.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().flipY().rot(-beta).push())
T3s.append(T4.cpy().tra(T3s[-2][1]).scl(T3scl).flipX().rot(-2*beta-pi).push())
T3s.append(T4.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().rot(-beta).push())
T3s.append(T3.cpy().tra(T3s[-1][0]).scl(T3scl).rot(beta).push())
T3s.extend([t.cpy().tra(-2*cos(2*beta)).flipY().push() for t in T3s])
T3s.append(T4.cpy().tra(T3s[7][1]).scl(T3scl).push())
T3s.append(T4.cpy().tra(T3s[14][1]).scl(T3scl).push())
T3s.append(T4.cpy().tra(T3s[-1][2]).scl(T3scl).flipX().flipY().push())
T3s.append(T6.cpy().tra(T3s[20][0]).scl(T3scl).flipX().rot(0).push())
T3s.append(T6.cpy().tra(T3s[-1][0]).scl(T3scl).push())
T3s.append(T4.cpy().tra(T3s[-6][0]).scl(T3scl).rot(pi).push())
T3s.append(T4.cpy().tra(T3s[-1][2]).scl(T3scl).push())

def substitutions(tile):
    match tile.name:
        case 'T1': Ts = T1s
        case 'T2': Ts = T2s
        case 'T3': Ts = T3s
        case 'T4': Ts = T4s
    return Ts
