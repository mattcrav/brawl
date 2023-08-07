# brawl

*An American Football Deckbuilder*

## Overview

- 11 players on offense and defense
- Each has a deck of cards
- Cards are played in 4 x 3 grid of zones
    - 4 regions
    - 3 columns (Left, Middle, Right)
- Trying to win zones by having the highest total on cards played
- X marks starting position of play, no cards are played here

Region | | Lft | Mid | Rgt
--- | --- | --- | --- | ---
Downfield (D) | 4x | - | - | -
Midfield  (M) | 2x | - | - | -
Scrimmage (S) | 1x | - | - | -
Backfield (B) | 0x | - | X | -

3 basic cards available

	Strength
    flat value.
    represents physical strength and prowess.

	Agility
    range of possible values that are rolled at the end of the 3 play series. represents speed and dexterity.

	Focus
    flat value (special rules below).
    represents hand-eye coordination, intelligence, and accuracy.

## Gameplay

Each Round represents a 3 play series.  Each round begins by drawing 3 cards for each player.

1. Offense and Defense play cards simultaneously in secret
2. Each side plays one card from each player into any of the 11 playable zones (1 card per zone)
3. Reveal cards in each zone for offense and defense
4. Repeat until all 3 cards have been played
5. Roll any agility values

Scoring

1. Find all zones won by the offense. A zone is won if:
    - The total on cards played by the offense exceeds the defense AND
    - Zone is orthoganally adjacent to
        - another won zone OR
        - the starting X
    - The value of the won zone is the difference between the totals of the offense and defense
2. Sum the value of each won zone
3. Multiply by highest multiplier of a won zone (see table above)
4. This value is total yards accrued on that 3 play series
5. Determine result:
    - If offense has at least 10 yards first down
    - If offense has enough yards for endzone, touchdown
    - If offense has les than 10 yards, can choose to:
        - punt TODO
        - attempt field goal TODO
        - go for it
            - draw 1 card for each player
            - play cards as in steps 2 and 3 above
            - rescore round again using new totals, values of previously played cards stay the same


## Special rules

    If offense wins zone on focus alone, doesn't have to follow adjacency, completion
    If defense wins zone on focus alone (where offense has cards), interception
    If defense wins zone on strength alone (where offense has cards), fumble
    If offense loses all 3 backfield, sack (no zones count)
    

Each player has a position and depending which region they play their cards can get a strong or weak effect.

    Strong (S) - double the values on the card
    Weak (W) - halve the values on the card (round down)

Position | B | S | M | D 
-- | -- | -- | -- | --
Offense
QB | - | - | - | -
RB | - | S | - | W
WR | W | W | S | S
SLOT | W | - | - | S
TE | - | - | S | W
OT | S | - | - | W
Defense
MLB | - | - | - | -
DT | - | S | - | W
CB | W | W | S | S
S | W | - | - | S
OLB | - | - | S | W
DE | S | - | - | W