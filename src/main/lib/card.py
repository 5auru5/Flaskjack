
from dataclasses import dataclass


@dataclass
class Card():
    face : str
    value : int

    def __init__(self, face: str, value : int) -> None:
        self.face = face
        self.value = value