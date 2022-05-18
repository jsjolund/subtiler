import math
from copy import deepcopy

M00 = 0
M01 = 3
M02 = 6
M10 = 1
M11 = 4
M12 = 7
M20 = 2
M21 = 5
M22 = 8

# Column major matrix
class Matrix3:
    def __repr__(self):
        return str(self.val)
        
    def __init__(self):
        self.val = [0]*9
        self.tmp = [0]*9
        self.idt()

    def cpy(self):
        m = Matrix3()
        m.val = deepcopy(self.val)
        m.tmp = deepcopy(self.tmp)
        return m

    def flipX(self):
        self.val[M11] = -self.val[M11]
        return self

    def flipY(self):
        self.val[M00] = -self.val[M00]
        return self

    def idt(self):
        self.val[M00] = 1
        self.val[M10] = 0
        self.val[M20] = 0
        self.val[M01] = 0
        self.val[M11] = 1
        self.val[M21] = 0
        self.val[M02] = 0
        self.val[M12] = 0
        self.val[M22] = 1
        return self

    def mul(self, m):
        val = self.val

        v00 = val[M00] * m[M00] + val[M01] * m[M10] + val[M02] * m[M20]
        v01 = val[M00] * m[M01] + val[M01] * m[M11] + val[M02] * m[M21]
        v02 = val[M00] * m[M02] + val[M01] * m[M12] + val[M02] * m[M22]

        v10 = val[M10] * m[M00] + val[M11] * m[M10] + val[M12] * m[M20]
        v11 = val[M10] * m[M01] + val[M11] * m[M11] + val[M12] * m[M21]
        v12 = val[M10] * m[M02] + val[M11] * m[M12] + val[M12] * m[M22]

        v20 = val[M20] * m[M00] + val[M21] * m[M10] + val[M22] * m[M20]
        v21 = val[M20] * m[M01] + val[M21] * m[M11] + val[M22] * m[M21]
        v22 = val[M20] * m[M02] + val[M21] * m[M12] + val[M22] * m[M22]

        val[M00] = v00
        val[M10] = v10
        val[M20] = v20
        val[M01] = v01
        val[M11] = v11
        val[M21] = v21
        val[M02] = v02
        val[M12] = v12
        val[M22] = v22
        return self


    def tra(self, x, y=0):
        if type(x) is tuple:
            y = x[1]
            x = x[0]
        self.tmp[M00] = 1
        self.tmp[M10] = 0
        self.tmp[M20] = 0

        self.tmp[M01] = 0
        self.tmp[M11] = 1
        self.tmp[M21] = 0

        self.tmp[M02] = x
        self.tmp[M12] = y
        self.tmp[M22] = 1
        self.mul(self.tmp)
        return self
    
    def scl(self, s):
        self.val[M00] *= s
        self.val[M11] *= s
        return self
    
    def rot(self, t):
        if t == 0:
            return self
        cos = math.cos(t)
        sin = math.sin(t)

        self.tmp[M00] = cos
        self.tmp[M10] = sin
        self.tmp[M20] = 0

        self.tmp[M01] = -sin
        self.tmp[M11] = cos
        self.tmp[M21] = 0

        self.tmp[M02] = 0
        self.tmp[M12] = 0
        self.tmp[M22] = 1
        self.mul(self.tmp)
        return self
