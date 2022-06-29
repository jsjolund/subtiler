from matrix import Matrix3
from copy import deepcopy
from math import acos, sin, tan, atan, cos, pi, sqrt, inf

def aabb(vec):
    x_min = inf
    x_max = -inf
    y_min = inf
    y_max = -inf
    for v in vec:
        if v[0] > x_max:
            x_max = v[0]
        if v[0] < x_min:
            x_min = v[0]
        if v[1] > y_max:
            y_max = v[1]
        if v[1] < y_min:
            y_min = v[1]
    return ((x_min, y_min), (x_max, y_max))

def dst(p1, p2): return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def dot4(xa, ya, xb, yb): return -acos((xa*xb+ya*yb) /
                                       (sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))

def dot(p1, p2): return dot4(p1[0], p1[1], p2[0], p2[1])

class Tile:
    def __init__(self, name, vec=[(0, 0)]):
        self.vec = vec
        self.name = name
        self.cmb_trans = Matrix3()
        self.trans = Matrix3()
        self.scale = 0

    def transform(self):
        new_vec = []
        mat = self.cmb_trans
        for v in self.vec:
            new_vec.append((v[0] * mat.val[0] + v[1] * mat.val[3] + mat.val[6],
                            v[0] * mat.val[1] + v[1] * mat.val[4] + mat.val[7]))
        return new_vec

    def inherit_transform(self, tile):
        self.cmb_trans.mul_left(tile.cmb_trans)
        return self

    def push(self):
        self.cmb_trans.mul_left(self.trans)
        self.trans = Matrix3()
        return self

    def flipX(self):
        self.trans.flipX()
        return self

    def flipY(self):
        self.trans.flipY()
        return self

    def rot(self, t):
        self.trans.rot(t)
        return self

    def scl(self, s):
        self.trans.scl(s)
        return self

    def tra(self, x, y=0):
        if type(x) is tuple:
            y = x[1]
            x = x[0]
        self.trans.tra(x, y)
        return self

    def aabb(self):
        return aabb(self.transform())

    def cpy(self):
        t = Tile(self.name, deepcopy(self.vec))
        t.cmb_trans = self.cmb_trans.cpy()
        t.trans = self.trans.cpy()
        t.scale = self.scale
        return t

    def set_name(self, name):
        self.name = name
        return self

    def __getitem__(self, key):
        return self.transform()[key]

    def __repr__(self) -> str:
        return f'{self.name}: ' + ','.join([f'({v[0]}, {v[1]})' for v in self.transform()])
