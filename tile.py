from matrix import Matrix3
from copy import deepcopy


class Tile:
    def __init__(self, name, vec):
        self.vec = vec
        self.name = name
        self.cmb_trans = Matrix3()
        self.trans = Matrix3()

    def transform(self):
        new_vec = []
        mat = self.cmb_trans
        for v in self.vec:
            new_vec.append((v[0] * mat.val[0] + v[1] * mat.val[3] + mat.val[6],
                            v[0] * mat.val[1] + v[1] * mat.val[4] + mat.val[7]))
        return new_vec

    def push(self):
        self.cmb_trans.mul_left(self.trans)
        self.trans = Matrix3()
        return self

    def v_tra(self, px, py=0):
        if type(px) is tuple:
            py = px[1]
            px = px[0]
        res = [(v[0]+px, v[1]+py) for v in self.vec]
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

    def cpy(self):
        t = Tile(self.name, deepcopy(self.vec))
        t.cmb_trans = self.cmb_trans.cpy()
        t.trans = self.trans.cpy()
        return t

    def __getitem__(self, key):
        return self.transform()[key]
