# Communication Pitfalls

## Announcement

```markdown
Context:

Selected observations from previous coding dojos.
* What did not work out so well and why?
* How can we improve?

Keywords: primitive obsession, communication, mental models, abstractions, tdd, guiding tests, ...

---

Title: Communication Pitfalls
Subtitle: And how to overcome them? ;)

Abstract:

Based on a few observations from previous coding dojos, I want to
facilitate a discussion about communication and mental models.

We focus on the following questions:
* Why and how primitive obsession hinders communication and clouds ideas?
* What is the difference between asserting values vs. behavior?
* How types and classes, or more generally, abstractions and domain models
  support alignment?
* How test-driven development, and in particular guiding tests or outside-in
  approaches allow us to express our intent (before diving into details).

Langton's ant and the coding dojo code will again serve as specific, hands-on
examples for code review and live coding.

Links:
* https://en.wikipedia.org/wiki/Langton%27s_ant
* https://github.com/PyUGAT/coding-dojo-2024-03-21
* https://github.com/PyUGAT/coding-dojo-2024-05-20

```


## Follow Up Discussion

How can we support collaborative development through an
expressive guiding test?

We aim for a guiding test that facilitates a fruitful
discussion.

* https://en.wikipedia.org/wiki/Wiio%27s_laws
* https://woodyzuill.com/
* https://www.obeythetestinggoat.com/


## Setup

Install requirements:
```console
pip install --requirement requirements.txt
```

Run tests:
```console
# run tests
pytest
# run tests continuously
ptw .
# or using a unix utility
ls *.py | entr pytest
```
