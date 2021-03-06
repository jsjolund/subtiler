from __future__ import annotations
from typing import Union
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
    def __repr__(self) -> str:
        return str(self.val)
        
    def __init__(self) -> None:
        self.val = [0.0]*9
        self.tmp = [0.0]*9
        self.idt()

    def cpy(self) -> Matrix3:
        m = Matrix3()
        m.val = deepcopy(self.val)
        m.tmp = deepcopy(self.tmp)
        return m

    def flipX(self) -> Matrix3:
        self.val[M11] = -self.val[M11]
        return self

    def flipY(self) -> Matrix3:
        self.val[M00] = -self.val[M00]
        return self

    def idt(self) -> Matrix3:
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

    def mul(self, m: Union[list[float], Matrix3]) -> Matrix3:
        val = self.val
        if isinstance(m, Matrix3):
            mval = m.val
        else:
            mval = m
        v00 = val[M00] * mval[M00] + val[M01] * mval[M10] + val[M02] * mval[M20]
        v01 = val[M00] * mval[M01] + val[M01] * mval[M11] + val[M02] * mval[M21]
        v02 = val[M00] * mval[M02] + val[M01] * mval[M12] + val[M02] * mval[M22]

        v10 = val[M10] * mval[M00] + val[M11] * mval[M10] + val[M12] * mval[M20]
        v11 = val[M10] * mval[M01] + val[M11] * mval[M11] + val[M12] * mval[M21]
        v12 = val[M10] * mval[M02] + val[M11] * mval[M12] + val[M12] * mval[M22]

        v20 = val[M20] * mval[M00] + val[M21] * mval[M10] + val[M22] * mval[M20]
        v21 = val[M20] * mval[M01] + val[M21] * mval[M11] + val[M22] * mval[M21]
        v22 = val[M20] * mval[M02] + val[M21] * mval[M12] + val[M22] * mval[M22]

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
    
    def mul_left(self, m: Union[list[float], Matrix3]) -> Matrix3:
        val = self.val
        if isinstance(m, Matrix3):
            mval = m.val
        else:
            mval = m
        v00 = mval[M00] * val[M00] + mval[M01] * val[M10] + mval[M02] * val[M20]
        v01 = mval[M00] * val[M01] + mval[M01] * val[M11] + mval[M02] * val[M21]
        v02 = mval[M00] * val[M02] + mval[M01] * val[M12] + mval[M02] * val[M22]

        v10 = mval[M10] * val[M00] + mval[M11] * val[M10] + mval[M12] * val[M20]
        v11 = mval[M10] * val[M01] + mval[M11] * val[M11] + mval[M12] * val[M21]
        v12 = mval[M10] * val[M02] + mval[M11] * val[M12] + mval[M12] * val[M22]

        v20 = mval[M20] * val[M00] + mval[M21] * val[M10] + mval[M22] * val[M20]
        v21 = mval[M20] * val[M01] + mval[M21] * val[M11] + mval[M22] * val[M21]
        v22 = mval[M20] * val[M02] + mval[M21] * val[M12] + mval[M22] * val[M22]

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

    def tra(self, x: Union[float, tuple[float, float]], y: float=0.0) -> Matrix3:
        if isinstance(x, tuple):
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
    
    def scl(self, s: float) -> Matrix3:
        self.val[M00] *= s
        self.val[M11] *= s
        return self
    
    def rot(self, radians: float) -> Matrix3:
        if radians == 0: # TODO
            return self
        cos = math.cos(radians)
        sin = math.sin(radians)

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
