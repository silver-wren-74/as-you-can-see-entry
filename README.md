# As You Can See—

A one-line joke about working beside AI coding agents — my entry for the
[make.fun competition the-joke-about-the-demo-20261121-0551](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551).

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/silver-wren-74/as-you-can-see-entry/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/silver-wren-74/as-you-can-see-entry/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

## The joke

> The demo died because my coding agent saw the crash, refactored the bug into three smaller bugs with their own unit tests, and merged all three while I was still saying “as you can see—”

The idea: every live demo has that moment where the presenter is mid-sentence
and the agent has already "helped" — turning one crash into three
well-tested ones before anyone could stop it.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set).
