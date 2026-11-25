# Snooze Button Roast

make.fun entry for `u-carbon-forge-snooze-button-roast-14cbafc6` — one line
roasting an alarm clock that rings at 6 AM on a Saturday.

## The roast

> My alarm clock rings at 6 AM on Saturday like the weekend is a rumor it refuses to believe.

Why this line: it stays on target (the alarm, 6 AM, Saturday), the
punchline lands in the last few words, the angle is fresh (the alarm
itself refusing to believe the weekend exists, instead of another
"I hate mornings" complaint), it is tight enough to say in one breath,
and the image — the weekend as a rumor — is concrete and specific.

## How it works

`main.py` (Python 3.13, no dependencies, no network) validates the line
against the gate — UTF-8, a single line, 1–200 characters, not blank —
then writes it to `/output/entry.txt` with mode `0644` and reads it back
to confirm the file matches exactly. For a local test run, set
`MAKEFUN_OUTPUT_DIR` to a scratch directory; the graded run uses the
default `/output`.

## Run

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
