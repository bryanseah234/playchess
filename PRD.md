# PRD: playchess

## Overview
A terminal-based two-player chess game written in Python with a curses-powered text UI. Implements full chess rules (movement validation, pawn promotion, check detection), logs moves with timestamps to `moves.txt`, and includes a debug mode. Originally a NYJC J1 Computing school project.

## Goals
- Implement all chess piece movement rules (King, Queen, Bishop, Knight, Rook, Pawn)
- Detect check and warn players
- Support pawn special moves: first-move double step, diagonal capture, promotion to Queen
- Log all moves with timestamps to `moves.txt`
- Curses-based terminal UI with board rendering
- Unit tests for move validation

## Non-Goals
- AI opponent
- Online multiplayer
- Graphical UI (terminal only)
- Full check/checkmate detection (check detected, but full game-end enforcement may be simplified)

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: `curses` (stdlib), `datetime` (stdlib)
- **Testing**: `test_chess.py` (likely pytest or unittest)

## Architecture
```
playchess/
├── chess.py         # Board class, piece classes, move validation
├── main.py          # Game loop, curses UI entry point
├── interface.py     # Curses rendering + input handling
├── test_chess.py    # Unit tests
├── moves.txt        # Move history log (generated at runtime)
├── run.bat          # Windows runner script
└── criteria.md      # School project grading criteria
```

**Classes (chess.py):**
- `Board` — 8×8 grid as dict `{(col, row): piece}`, move execution, coordinate system
- `King`, `Queen`, `Rook`, `Bishop`, `Knight`, `Pawn` — each with `isvalid(start, end)` method
- `WebInterface` (implied by import) — UI state wrapper

**Game loop:**
1. Render board via curses
2. Prompt current player for start coord, then end coord
3. Validate move via `piece.isvalid()`
4. Execute move, check for pawn promotion
5. Log move to `moves.txt` with timestamp
6. Switch turns, check for check condition

## Deployment / Run
```bash
python main.py          # Linux/Mac
run.bat                 # Windows
```

## Constraints & Notes
- **Curses**: requires terminal with curses support; Windows needs `windows-curses` pip package
- **Board coordinate system**: columns and rows indexed 0-7 with `(col, row)` tuples
- **Check detection**: alerts players but may not enforce stalemate/checkmate end conditions
- **School project**: built for NYJC J1 Computing — grading criteria in `criteria.md`
