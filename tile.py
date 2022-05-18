from matrix import Matrix3
from copy import deepcopy


class Tile:
    def __init__(self, name, vec, locl=Matrix3(), glob=Matrix3()):
        self.vec = vec
        self.name = name
        self.locl = locl
        self.glob = glob

    def mul(self, vec, mat):
        new_vec = []
        for v in vec:
            new_vec.append((v[0] * mat.val[0] + v[1] * mat.val[3] + mat.val[6],
                            v[0] * mat.val[1] + v[1] * mat.val[4] + mat.val[7]))
        return new_vec

    def transform(self):
        tra_vec = self.mul(self.vec, self.locl)
        tra_vec = self.mul(tra_vec, self.glob)
        return tra_vec

    def v_tra(self, px, py=0):
        if type(px) is tuple:
            py = px[1]
            px = px[0]
        res = [(v[0]+px, v[1]+py) for v in self.vec]
        return Tile(self.name, res)

    def l_flipX(self):
        self.locl.flipX()
        return self

    def l_flipY(self):
        self.locl.flipY()
        return self

    def l_rot(self, t):
        self.locl.rot(t)
        return self

    def l_scl(self, s):
        self.locl.scl(s)
        return self

    def l_tra(self, x, y=0):
        if type(x) is tuple:
            y = x[1]
            x = x[0]
        self.locl.tra(x, y)
        return self

    def g_tra(self, x, y=0):
        if type(x) is tuple:
            y = x[1]
            x = x[0]
        self.glob.tra(x, y)
        return self

    def g_rot(self, t):
        self.glob.rot(t)
        return self

    def g_flipX(self):
        self.glob.flipX()
        return self

    def cpy(self):
        return Tile(self.name, deepcopy(self.vec), self.locl.cpy(), self.glob.cpy())

    def __getitem__(self, key):
        return self.transform()[key]
