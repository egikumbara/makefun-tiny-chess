# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/egikumbara/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/egikumbara/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A compact chess engine in a single 4,081-byte Python file. 0x88 board, negamax alpha-beta search with iterative deepening by node budget, quiescence on captures, MVV-LVA move ordering, and material + piece-square evaluation. It plays the make.fun tiny-chess-01 gauntlet through the env API — no model calls, fully deterministic.

## Run it

```sh
python3 -P -s /bot/main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=q1q35jmc&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
