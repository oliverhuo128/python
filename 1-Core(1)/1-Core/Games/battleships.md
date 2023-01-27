# Battleships

A game of [battleships](https://en.wikipedia.org/wiki/Battleship_(game)) should be playable on a single computer between two players.

A game of battleships has the following two stages:

- Ship placement
- Game play

## Requirements

### Ship placement

- Players should be able to choose their ships coordinate and orientation.
- Players should also have the option to randomly allocate their ships coordinate and orientation for a speedy set up.
- In both cases, the game should handle any invalid off grid ship placements.

### Game play

A player should be able choose the coordinates they wish to target, and be told if their hit was either:

- A direct hit
- A miss
- Invalid (either off grid, or the coordinate has been previously hit)

And if invalid, the player should be allowed to re-enter another set of coordinates. When all the opponents ships are destroyed, the game should end and a winner declared.

### Visual

- Initially, this game should be played in the command line with a simple ascii art grid.
- A player should be shown both their primary grid of their ships and the coordinates of where the opponent has targeted their grid, and a secondary tracking grid of their past hits on their opponent (distinguished by whether the hit was on target or not).
- (Extension) Between turns, a handover screen should be shown to avoid either player seeing the opponent's grid.
- (Extension) The past turns should be cleared in the terminal window to avoid an opponent scrolling up.

## Extensions

These extensions should be tackled in order.

### Larger Grid

The traditional battleship grid is 10x10, the player should be able to choose any grid dimensions from 10x10 - 20x20, allowing all rectangular combinations as well. The total area of the larger grid should be used to automatically scale the number of and/or size of ships so that the ship coverage on the grid covers the same ratio as the 10x10 grid (17 ship tiles / 100 possible tiles).

### 2-Dimensional Ships

Traditionally there are 5 different 1-dimensional ship types supported by battleships up to 5 squares in length, with a combined area of 17 tiles.

This extension allows players to choose their ships from all the different possible 2d versions of these ships i.e the 5-tile carrier, could take the [following shapes](https://en.wikipedia.org/wiki/Pentomino).

### Play Against the Computer

A single player mode that allows plays to play against the computer.

- Computer Level 1: Random hits.
- Computer Level 2: Random hits, but when a successful hit is made, future hits target the surrounding areas until exhausted.

### GUI Extension

Explore the [pygame library](https://www.pygame.org/docs/) to make a GUI for your game.
