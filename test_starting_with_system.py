"""
What do we want?
Let's try to be as explicit as we possibly can!
"""

import enum, dataclasses
import pytest


@dataclasses.dataclass(frozen=True)
class Position:
    x: int
    y: int


class Color(enum.Enum):
    WHITE = 0
    BLACK = 1


@dataclasses.dataclass
class Grid:
    positions: set[Position] = dataclasses.field(default_factory=set)

    def look_at(self, position: Position):
        if position not in self.positions:
            return Color.WHITE
        return Color.BLACK

    def flip_at(self, position: Position):
        if position in self.positions:
            self.positions.remove(position)
        else:
            self.positions.add(position)


def test_grid_behavior():
    position = Position(x=0, y=0)
    grid = Grid()

    assert grid.look_at(position) == Color.WHITE
    grid.flip_at(position)
    assert grid.look_at(position) == Color.BLACK
    grid.flip_at(position)
    assert grid.look_at(position) == Color.WHITE


@dataclasses.dataclass
class Ant:
    position: Position

    def move_from(self, color: Color):
        pass


@dataclasses.dataclass
class State:
    grid: Grid
    ant: Ant

    def advance(self):
        color = self.grid.look_at(self.ant.position)
        self.ant.move_from(color)
        self.grid.flip_at(self.ant.position)


def test_how_system_is_composed_and_how_parts_interact(mocker):

    # parameters
    position = Position(x=0, y=0)
    color = Color.WHITE

    # prepare
    grid = Grid()
    ant = Ant(position=position)
    state = State(grid, ant)

    # a little more preparation to make this kind of test work
    # here we can talk about "how parts interact"
    spy_grid_look_at = mocker.spy(grid, "look_at")
    spy_grid_flip_at = mocker.spy(grid, "flip_at")
    spy_ant_move_from = mocker.spy(ant, "move_from")

    # act
    state.advance()

    # assert
    spy_grid_look_at.assert_called_once_with(position)
    assert spy_grid_look_at.spy_return == color
    spy_ant_move_from.assert_called_once_with(color)
    spy_grid_flip_at.assert_called_once_with(position)
