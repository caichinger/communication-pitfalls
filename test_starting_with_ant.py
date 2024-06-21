"""
What do we want?
Let's try to be as explicit as we possibly can!
"""

import enum, dataclasses
import pytest


@dataclasses.dataclass
class Position:
    x: int
    y: int


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1  # Position(1, 0)

    def turn_right(self):
        return Direction.EAST


class Color(enum.Enum):
    WHITE = 0


@dataclasses.dataclass
class Ant:
    position: Position
    direction: Direction

    def move_from_and_maybe_rename_that_later(self, color: Color):
        if color == Color.WHITE:
            self._turn_right()
            self._move_forward()

    def _move_forward(self):
        self.position = Position(x=1, y=0)

    def _turn_right(self):
        self.direction = self.direction.turn_right()


@pytest.mark.skip
def test_ant_something_that_is_not_so_useful_to_facilitate_a_discussion():
    ant = Ant()
    assert ant.move() != ant


def test_that_ant_on_white_square_turns_right():
    # prepare
    ant = Ant(position=Position(x=0, y=0), direction=Direction.NORTH)
    # act
    ant.move_from_and_maybe_rename_that_later(Color.WHITE)
    # assert
    assert ant.position == Position(x=1, y=0)
    assert ant.direction == Direction.EAST


def test_that_from_facing_north_turning_right_results_in_east():
    direction = Direction.NORTH
    assert direction.turn_right() == Direction.EAST
