from __future__ import annotations
from typing import Union
from matrix import Matrix3
from copy import deepcopy
from math import acos, sqrt, inf


def aabb(vec: list[tuple[float, float]]) -> tuple[tuple[float, float], tuple[float, float]]:
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


def dst(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))


def dot4(xa: float, ya: float, xb: float, yb: float) -> float:
    return -acos((xa*xb+ya*yb) / (sqrt(xa**2+ya**2)*sqrt(xb**2+yb**2)))


def dot(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return dot4(p1[0], p1[1], p2[0], p2[1])


class Tile:
    def __init__(self, name: str, vec: list[tuple[float, float]] = [(0, 0)]) -> None:
        self.vec = vec
        self.name = name
        self.cmb_trans = Matrix3()
        self.trans = Matrix3()
        self.scale = 0.0

    def transform(self) -> list[tuple[float, float]]:
        new_vec = []
        mat = self.cmb_trans
        for v in self.vec:
            new_vec.append((v[0] * mat.val[0] + v[1] * mat.val[3] + mat.val[6],
                            v[0] * mat.val[1] + v[1] * mat.val[4] + mat.val[7]))
        return new_vec

    def inherit_transform(self, tile: Tile) -> Tile:
        self.cmb_trans.mul_left(tile.cmb_trans)
        return self

    def push(self) -> Tile:
        self.cmb_trans.mul_left(self.trans)
        self.trans = Matrix3()
        return self

    def flipX(self) -> Tile:
        self.trans.flipX()
        return self

    def flipY(self) -> Tile:
        self.trans.flipY()
        return self

    def rot(self, radians: float) -> Tile:
        self.trans.rot(radians)
        return self

    def scl(self, scale: float) -> Tile:
        self.trans.scl(scale)
        return self

    def tra(self, x: Union[float, tuple[float, float]], y: float = 0.0) -> Tile:
        if isinstance(x, tuple):
            y = x[1]
            x = x[0]
        self.trans.tra(x, y)
        return self

    def aabb(self) -> tuple[tuple[float, float], tuple[float, float]]:
        return aabb(self.transform())

    def cpy(self) -> Tile:
        t = Tile(self.name, deepcopy(self.vec))
        t.cmb_trans = self.cmb_trans.cpy()
        t.trans = self.trans.cpy()
        t.scale = self.scale
        return t

    def set_name(self, name: str) -> Tile:
        self.name = name
        return self

    def __getitem__(self, key: int) -> tuple[float, float]:
        return self.transform()[key]

    def __repr__(self) -> str:
        return f'{self.name}: ' + ','.join([f'({v[0]}, {v[1]})' for v in self.transform()])
