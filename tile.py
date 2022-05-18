from matrix import Matrix3
from copy import deepcopy


class Tile:
    def __init__(self, name, vec):
        self.vec = vec
        self.name = name
        self.transforms = []
        self.m = Matrix3()

    def mul(self, vec, mat):
        new_vec = []
        for v in vec:
            new_vec.append((v[0] * mat.val[0] + v[1] * mat.val[3] + mat.val[6],
                            v[0] * mat.val[1] + v[1] * mat.val[4] + mat.val[7]))
        return new_vec

    def transform(self):
        tra_vec = deepcopy(self.vec)
        for mat in self.transforms:
            tra_vec = self.mul(tra_vec, mat)
        return tra_vec

    def push(self):
        self.transforms.append(self.m)
        self.m = Matrix3()
        return self

    def v_tra(self, px, py=0):
        if type(px) is tuple:
            py = px[1]
            px = px[0]
        res = [(v[0]+px, v[1]+py) for v in self.vec]
        return Tile(self.name, res)

    def flipX(self):
        self.m.flipX()
        return self

    def flipY(self):
        self.m.flipY()
        return self

    def rot(self, t):
        self.m.rot(t)
        return self

    def scl(self, s):
        self.m.scl(s)
        return self

    def tra(self, x, y=0):
        if type(x) is tuple:
            y = x[1]
            x = x[0]
        self.m.tra(x, y)
        return self

    def cpy(self):
        t = Tile(self.name, deepcopy(self.vec))
        t.transforms = [tr.cpy() for tr in self.transforms]
        t.m = self.m.cpy()
        return t

    def __getitem__(self, key):
        return self.transform()[key]
