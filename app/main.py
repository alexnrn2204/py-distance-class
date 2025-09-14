from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        elif isinstance(other, Distance):
            return Distance(self.km + other.km)

        raise TypeError("Can only add Distances or integer")

    def __iadd__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            raise TypeError("Can only add Distances or integer")

        return self

    def __mul__(self, other: (int, float)) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

        raise TypeError("Can only multiply Distances or integer")

    def __truediv__(self, other: (int, float)) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))

        raise TypeError("Can only div Distances or integer")

    def __lt__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km

        raise TypeError("Can only compare Distances or integer")

    def __gt__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km

        raise TypeError("Can only compare Distances or integer")

    def __eq__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km

        raise TypeError("Can only compare Distances or integer")

    def __le__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km

        raise TypeError("Can only compare Distances or integer")

    def __ge__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km

        raise TypeError("Can only compare Distances or integer")
