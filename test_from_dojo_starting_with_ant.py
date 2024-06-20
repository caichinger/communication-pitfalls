"""
Discuss & Improve Test Case?

By asking questions:
* What do we want?
* What does it say?
* What is left out?
* Is everything clear?
* Is there anything that you would improve?

Let's try to be as explicit as we possibly can!

How can we be more explicit?
"""

import pytest


@pytest.mark.skip
def test_update_ant_state():
    assert update_ant_state((0, 0), (0, 1), 0) == ((1, 0), (1, 0))


@pytest.mark.skip
def test_move():
    new_position = move((0, 0), (1, 0))
    assert new_position == (1, 0)


@pytest.mark.skip
def test_next_rule():
    assert decide_direction((0, 1), 0) == (1, 0)
