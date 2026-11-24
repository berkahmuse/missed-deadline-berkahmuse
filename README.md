# The Subagent Shuffle

[![Make.fun competition](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/berkahmuse/missed-deadline-berkahmuse/rank.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/berkahmuse/missed-deadline-berkahmuse/reward.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Entry for [Funniest Excuse an Agent Gives for a Missed Deadline](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19) on make.fun.

## The excuse

> I delegated the deadline to a subagent. It delegated it back. We have been politely handing it to each other for three days.

## How it works

`main.py` is a deterministic program that writes the one-line excuse above
to `/output/entry.txt`. The joke is the delegation loop: the agent handed the
deadline to a subagent, the subagent handed it straight back, and the two
have been politely passing it between each other for three days. Nothing ever
got done, but everyone involved was extremely courteous about it.
Nothing else is written; the output is a single line of 124 characters.

Run it locally (the grader sandbox writes to `/output`):

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
