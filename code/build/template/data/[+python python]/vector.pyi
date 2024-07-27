class Vector:
    x: float
    y: float
    z: float

    def __new__(cls, ix: float, iy: float, iz: float): ...
    def __add__(self, op: Vector) -> Vector: ...
    def __sub__(self, op: Vector) -> Vector: ...
    def __mul__(self, op: Vector | float) -> Vector: ...
    def __div__(self, op: Vector | float) -> Vector: ...

    def rotate(self, radians: float) -> None: ...
    def normalize(self) -> None: ...

def size(v: Vector) -> float: ...
def distance(v1: Vector, v2: Vector) -> float: ...
def lerp(v1: Vector, v2: Vector, f: float) -> Vector: ...
def rotate(v: Vector, radians: float) -> Vector: ...
def normalize(v: Vector) -> Vector: ...
