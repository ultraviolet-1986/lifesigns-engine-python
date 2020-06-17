# Lifesigns Engine (Python)

## Introduction

A Python-based text adventure game engine which contains many real-life objects
represented in Python.

## Instructions

To make use of the Lifesigns Engine, you must first download the source code.
In a file next to Lifesigns Engine folder, place the following code within a
file to import the engine:

```python
import lifesigns_engine_python as le
```

From that point onward, game objects, characters and locations may all be
declared and used. The Lifesigns Engine keeps objects stored within the top
level of the package, so declaring (for example) a `StickyNote` object can be as
simple as:

```python
note = le.StickyNote("Name", "Description", "Contents", True)
```

...as opposed to:

```python
note = le.assets.StickyNote("Name", "Description", "Contents", True)
```

From that point, the declared object may be interacted with by using one of its
methods such as:

```python
note.read()
```

The above command will output the contents of the `note` object for the player
to read. The same approach can be taken with other pre-defined objects.
