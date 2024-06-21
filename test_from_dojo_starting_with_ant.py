"""
Discuss & Improve Test Case?

By asking questions:
* What do we want?
* What does it say?
* What is left out?
* Is everything clear?
* Is there anything that you would improve?

What do we want?
Let's try to be as explicit as we possibly can!
How/where can we be more explicit?
"""

import pytest

WHITE = 0
NORTH = (0, 1)
EAST = (1, 0)


@pytest.mark.skip
def test_update_ant_state():
    position = (0, 0)  # x, y
    new_position = (1, 0)
    # (position, NORTH) this IS the ant
    updated_ant = (new_position, EAST)
    assert update_ant_state(position, NORTH, WHITE) == updated_ant


@pytest.mark.skip
def test_move():
    new_position = move((0, 0), (1, 0))
    assert new_position == (1, 0)


@pytest.mark.skip
def test_next_rule():
    assert decide_direction((0, 1), 0) == (1, 0)
