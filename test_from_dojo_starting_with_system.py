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


@pytest.mark.skip
def test_advance_state_returns_state():
    new_state = advance_state()
    assert new_state is not None


@pytest.mark.skip
def test_first_step_from_default_state_correct():
    ant_position, _, _ = advance_state()
    assert ant_position == (1, 0)


@pytest.mark.skip
def test_grid_state_after_first_step_from_default_state():
    _, _, new_grid = advance_state()
    assert new_grid == {(0, 0): 1}


@pytest.mark.skip
def test_first_step_from_default_state_correct():
    default_ant = (0, 0), "NORTH"
    default_grid = {}
    default_state = default_ant, default_grid
    ant_position, ant_direction, grid = advance_state(default_state)
    assert ant_position == (1, 0)
    assert grid == {(0, 0): 1}
