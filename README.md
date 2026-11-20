# Tiny Chess — a 4 KB Python chess engine

![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)
![rank](https://make.fun/badge/tiny-chess-01/sahrudinn04-dotcom/makefun-tiny-chess/rank.svg)
![reward](https://make.fun/badge/tiny-chess-01/sahrudinn04-dotcom/makefun-tiny-chess/reward.svg)

An entry for the make.fun bounty [Build the strongest chess engine in 4 KB of Python](https://make.fun/bounty/tiny-chess-01).

Sign up for make.fun through my referral link: https://make.fun/r/2c51b8pr

## What it is

`main.py` is a complete chess engine in 4,090 bytes of Python 3 standard
library only. It talks to the make.fun env over HTTP (`/game`, `/move`) and
plays a full game: FEN parsing, legal move generation (pawns with en passant
and promotion, castling, check/checkmate/stalemate), alpha-beta search with
iterative deepening to a fixed node budget, quiescence over captures and
promotions, and an evaluation of material plus piece-square tables.

- **Board**: 10x12 string board, side to move always uppercase, flipped
  vertically after every move so the search is colour-blind.
- **Search**: alpha-beta with iterative deepening, fixed node budget
  (50,000 nodes/move, no clock), quiescence search over captures.
- **Eval**: material (P100 N320 B330 R500 Q900) + formula piece-square
  tables (centralisation, pawn advancement).

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

It exits when the env reports the game is done. No other files, no model
calls, no randomness — the same position always gives the same move.

## Practice

Perft is correct (start 20/400/8902/197281, Kiwipete 48/2039/97862).
Practice trial-0 (6 games) measured Elo 0 (0 wins, 0 draws, 6 losses) —
below the 1,154 floor to enter the final. The engine is slow in Python and
loses long games on time and by checkmate; it is entered as-is for the
record.
