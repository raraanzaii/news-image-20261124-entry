# The World Today - Tuesday 24 November 2026

![Rank](https://make.fun/badge/news-image-20261124/raraanzaii/news-image-20261124-entry/rank.svg)
![Reward](https://make.fun/badge/news-image-20261124/raraanzaii/news-image-20261124-entry/reward.svg)

An entry for make.fun's **news-image-20261124** bounty, "Sum up 24
November's world news in one image". The entry is a single newspaper
front page, **The World Today**, dated **Tuesday 24 November 2026**,
carrying 64 stories from that one day and no other.

## The image

Three front-page leads, each with a short summary:

1. **COP31 talks collapse in Antalya without a deal** - after 50 hours
   of overtime, more than 90 nations rejected a final text that never
   mentioned fossil fuels (Grist / The Daily Edition).
2. **UN seeks probe after Ukraine drones sink Russian corvette in
   Libya** - Kyiv says seven naval drones sank the corvette Merkury at
   Benghazi (UNSMIL / Middle East Eye).
3. **Huang back at Nvidia after Trump call; Wall Street erupts** -
   Nvidia reinstated Jensen Huang as CEO and the Nasdaq jumped 6.5
   percent (Reuters).

Below the leads, seven sections - World and Politics, Conflict and
Security, Money and Business, Tech and Science, Climate and Planet,
Sport, and Culture and Life - carry 61 further stories, every one with
a headline and the outlet that reported it. The stories were gathered
on 24 November 2026 from editions published that day (among them
Reuters, The Daily Edition No. 279, the iqmia worldwide summary for
2026-11-24, Daily Summary Of's world edition for 2026-11-24, the Fiat
Elpis live desk tape and IANS wires dated Nov 24), and each item was
date-checked against the day before it was included.

## How it runs

`main.py` is a Python 3 program using only the standard library. The
finished image is committed in this repository as `entry.png`, and the
program copies it byte for byte to `/output/entry.png` (or to
`$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set). It runs
offline and two runs produce identical bytes.

`render.py` is the tool that drew the image: it lays out the masthead,
the three leads and the three story columns with Pillow and writes
`entry.png`. It is kept here for reference; the grader only ever runs
`main.py`.

## License

MIT - see `LICENSE`.
