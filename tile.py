from matrix import Matrix3
from copy import deepcopy
import math


class Tile:
    def __init__(self, name, vec):
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

    def tra_vec(self, x, y=0):
        if type(x) is tuple:
            y = x[1]
            x = x[0]
        res = [(v[0]+x, v[1]+y) for v in self.vec]
        return Tile(self.name, res)

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
        x_min = math.inf
        x_max = -math.inf
        y_min = math.inf
        y_max = -math.inf
        for v in self.transform():
            if v[0] > x_max:
                x_max = v[0]
            if v[0] < x_min:
                x_min = v[0]
            if v[1] > y_max:
                y_max = v[1]
            if v[1] < y_min:
                y_min = v[1]
        return ((x_min, y_min), (x_max, y_max))

    def cpy(self):
        t = Tile(self.name, deepcopy(self.vec))
        t.cmb_trans = self.cmb_trans.cpy()
        t.trans = self.trans.cpy()
        t.scale = self.scale
        return t

    def __getitem__(self, key):
        return self.transform()[key]

    def __repr__(self) -> str:
        return f'{self.name}: ' + ','.join([f'({v[0]}, {v[1]})' for v in self.transform()])
