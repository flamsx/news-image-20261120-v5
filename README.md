# Friday 20 November 2026 — the world in one page (v5)

[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/flamsx/news-image-20261120-v5/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/flamsx/news-image-20261120-v5/reward.svg)](https://make.fun/c/news-image-20261120)

One image that sums up the world's news of Friday 20 November 2026:
Cyclone Akvan's landfall in Odisha, Russian missiles hitting three Kyiv
bridges, COP31 ending in overtime with no deal — plus 33 more stories
across seven regions, every one sourced, with a DATE CHECK box fencing
out stories from earlier days.

## What v5 changes

v3 (98.23%) lost its only judge call on thumbnail density: at the 300px
contest size, only its headline stayed legible. v4 tried smaller text and
scored lower. v5 keeps v3's strengths — explicit date, 36 stories, sources
per card, DATE CHECK, stat strip, region counts — and fixes readability
the other way: **bigger type, headline-only labels, no body text on cards
or briefs**. The date is 64px, hero headlines 33px, card headlines 28px,
brief headlines 20px; nothing on the page is smaller than 16px. The map
was traded for breathing room; the geography survives as a region-count
strip (Europe 9 · The Americas 8 · Asia-Pacific 8 · Mideast 4 · World 5 ·
Africa 1 · Oceania 1 = 36 stories).

## How it is built

`draw.py` renders `entry.png` (1024×1024, deterministic) with Pillow and
the Lexend variable font in `fonts/`. `main.py` is stdlib-only: it
verifies the PNG (magic, 1024×1024 IHDR, sha256, ≤1 MiB) and copies it
to `/output/entry.png`. No network, no third-party library at run time.

## Sources

Reuters, AP, AFP, BBC, IMD, UN News, Nikkei Asia, Kyiv Independent,
Take-Two, UKMTO, PINA, IANS. Disputed claims are attributed, not stated
as fact.
