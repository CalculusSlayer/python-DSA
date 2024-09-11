# distance.py
from typing import Tuple

def intersects_at(position_speed1: Tuple[int], position_speed2: Tuple[int]) -> float:
    position1, speed1 = position_speed1
    position2, speed2 = position_speed2
    return (position2 - position1)/(speed1 - speed2)