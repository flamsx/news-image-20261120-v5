#!/usr/bin/env python3
"""Render the v5 front page for news-image-20261120, from SPEC-v5.md.

Fresh code, written in this session. Pre-renders entry.png (1024x1024)
with Pillow locally; the shipped main.py is stdlib-only and just copies
the image to /output/entry.png.
"""
import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(HERE, "fonts", "Lexend-Variable.ttf")

W = H = 1024
PAPER = (247, 243, 234)
INK = (22, 19, 14)
RED = (180, 35, 24)
GREY = (96, 90, 80)
LIGHT_GREY = (120, 114, 104)
TEAL = (14, 90, 90)
NAVY = (27, 42, 74)
GREEN = (46, 107, 52)
OCHRE = (201, 138, 27)
RULE = (200, 192, 176)

MARGIN = 20
INNER = W - 2 * MARGIN  # 984

_cache = {}


def font(size, weight=700):
    key = (size, weight)
    if key not in _cache:
        fnt = ImageFont.truetype(FONT_PATH, size)
        fnt.set_variation_by_axes([weight])
        _cache[key] = fnt
    return _cache[key]


def text_w(text, fnt):
    return fnt.getlength(text)


def wrap(text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if text_w(trial, fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, text, fnt, x, y, max_w, fill, leading=None, max_lines=None):
    lines = wrap(text, fnt, max_w)
    if max_lines is not None:
        assert len(lines) <= max_lines, "OVERFLOW %r -> %d lines: %s" % (text, len(lines), lines)
        lines = lines[:max_lines]
    lh = leading if leading is not None else int(fnt.size * 1.08)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


# ---------------------------------------------------------------- data
HEROES = [
    {
        "region": "ASIA", "color": TEAL, "kicker": "ASIA · CYCLONE",
        "headline": "CYCLONE AKVAN SLAMS ODISHA",
        "fact": "440,000 EVACUATED · NO DEATHS",
        "source": "IMD · THE HINDU",
        "art": "cyclone",
    },
    {
        "region": "EUROPE", "color": NAVY, "kicker": "EUROPE · WAR",
        "headline": "MISSILES HIT KYIV BRIDGES",
        "fact": "3 BRIDGES HIT · 9 KILLED",
        "source": "KYIV INDEPENDENT",
        "art": "bridges",
    },
    {
        "region": "WORLD", "color": GREEN, "kicker": "WORLD · CLIMATE",
        "headline": "COP31 ENDS WITH NO DEAL",
        "fact": "NO DEAL · TALKS IN OVERTIME",
        "source": "UN NEWS",
        "art": "globe",
    },
]

CARDS = [
    ("GTA VI: $3.79BN IN A DAY", "TAKE-TWO · THE AMERICAS", RED),
    ("NIKKEI DIVES 5% IN ASIA AI ROUT", "NIKKEI ASIA · ASIA-PACIFIC", TEAL),
    ("ANTHROPIC −9% AFTER $81BN IPO", "BUSINESS TIMES · THE AMERICAS", NAVY),
    ("UK–EU DEAL: 100,000 VISAS", "REUTERS · EUROPE", OCHRE),
    ("SENATE BLOCKS IRAN BID 51–48", "REUTERS · THE AMERICAS", NAVY),
    ("TANKER HIT BY FIRE IN HORMUZ", "UKMTO · MIDEAST", RED),
    ("SIX KILLED IN GAZA STRIKES", "AFP · MIDEAST", RED),
    ("TONGA SCHOOLS SHUT IN DROUGHT", "PINA · OCEANIA", TEAL),
    ("PUTIN, TRUMP AND XI MEET", "CNN · WORLD", GREEN),
]

BRIEFS = [
    ("India 159/1 after New Zealand's 368", TEAL),
    ("1,144 children killed or hurt in Ukraine", NAVY),
    ("Denmark approves Greenland pact 109–0", NAVY),
    ("California subpoenas Nvidia over China risks", RED),
    ("Two Russian missiles land in Poland", NAVY),
    ("Hackers leak data of 16,000 bank customers", RED),
    ("Trump sacks cyber chief after tech outages", RED),
    ("Iran readies tanker convoy to test blockade", RED),
    ("Saudi coalition hits Houthi threats", RED),
    ("Ukraine retakes 14 settlements in Kharkiv", NAVY),
    ("Europe offers Ukraine binding guarantees", NAVY),
    ("US, China agree human control of war AI", GREEN),
    ("TSMC, Samsung pause advanced chip sales", TEAL),
    ("China bars Bloomberg reporter from summit", TEAL),
    ("IEA: Hormuz shock is largest energy cut ever", GREEN),
    ("Colombia marches against tax rises", RED),
    ("Kenya opposition warns over 2027 vote", OCHRE),
    ("Van Gogh sells for record $190.4m", NAVY),
    ("Scientists grow potatoes in moon soil", GREEN),
    ("Texas botches execution of killer", RED),
    ("Indonesia daycare chief jailed for abuse", TEAL),
    ("China warns climbers over Mount Fuji", TEAL),
    ("De Villepin launches French presidential bid", NAVY),
    ("US sanctions Cambodia scam enablers", TEAL),
]

STATS = [
    ("70–80 kmph", "AKVAN WINDS, GUSTING 90"),
    ("$3.79bn", "GTA VI DAY-ONE SALES"),
    ("400+ drones", "FIRED AT UKRAINE"),
    ("−5%", "NIKKEI FRIDAY FALL"),
]


# ---------------------------------------------------------------- art
def art_cyclone(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=TEAL)
    cx, cy = x + w // 2, y + h // 2 + 6
    for r, col in ((46, (247, 243, 234)), (34, (140, 200, 200)),
                   (23, (247, 243, 234)), (12, (201, 138, 27))):
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=300,
                 fill=col, width=5)
    for i in range(5):  # rain streaks
        rx = x + 14 + i * 26
        draw.line([rx, y + h - 26, rx - 8, y + h - 8], fill=(200, 225, 225), width=3)
    draw.line([x + w - 70, y + h - 6, x + w, y + h - 22], fill=(247, 243, 234), width=3)


def art_bridges(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=NAVY)
    draw.rectangle([x, y + h - 22, x + w, y + h], fill=(58, 96, 130))
    for i, bx in enumerate((x + 18, x + w // 2 - 40, x + w - 92)):
        draw.arc([bx, y + 22, bx + 82, y + h - 6], start=180, end=360,
                 fill=(247, 243, 234), width=4)
        draw.line([bx + 41, y + 22, bx + 41, y + 34], fill=(247, 243, 234), width=3)
    # burst top right
    bx, by = x + w - 30, y + 16
    for ang in range(0, 360, 45):
        import math
        dx = int(13 * math.cos(math.radians(ang)))
        dy = int(13 * math.sin(math.radians(ang)))
        draw.line([bx, by, bx + dx, by + dy], fill=OCHRE, width=3)
    draw.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=OCHRE)


def art_globe(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=GREEN)
    cx, cy = x + w // 2 - 30, y + h // 2
    r = 26
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(140, 200, 140),
                 outline=(247, 243, 234), width=3)
    draw.arc([cx - r, cy - r, cx + r, cy + r], start=200, end=340,
             fill=(247, 243, 234), width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=(247, 243, 234), width=2)
    draw.ellipse([cx - r + 6, cy - r + 8, cx - r + 18, cy - r + 20],
                 fill=(46, 107, 52))
    # sun top right + small flags
    sx, sy = x + w - 34, y + 16
    draw.ellipse([sx - 9, sy - 9, sx + 9, sy + 9], fill=OCHRE)
    for i, col in enumerate((RED, (247, 243, 234), NAVY)):
        fx = x + w - 96 + i * 16
        draw.rectangle([fx, y + h - 26, fx + 13, y + h - 12], fill=col)


ART = {"cyclone": art_cyclone, "bridges": art_bridges, "globe": art_globe}


# ---------------------------------------------------------------- page
def render(path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # top black band
    d.rectangle([0, 0, W, 24], fill=INK)
    f_band = font(16, 700)
    d.text((MARGIN, 4), "THE WORLD IN ONE PAGE", font=f_band, fill=PAPER)
    right = "FRIDAY EDITION"
    d.text((W - MARGIN - text_w(right, f_band), 4), right, font=f_band, fill=PAPER)

    # date
    y = 28
    f_date = font(64, 800)
    date = "FRIDAY 20 NOVEMBER 2026"
    assert text_w(date, f_date) <= INNER, "date too wide: %d" % text_w(date, f_date)
    d.text(((W - text_w(date, f_date)) / 2, y), date, font=f_date, fill=INK)
    y += 70

    # red sub-headline
    f_sub = font(29, 700)
    sub = "CYCLONE HITS ODISHA · KYIV BRIDGES HIT · COP31 NO DEAL"
    assert text_w(sub, f_sub) <= INNER, "sub too wide: %d" % text_w(sub, f_sub)
    d.text(((W - text_w(sub, f_sub)) / 2, y), sub, font=f_sub, fill=RED)
    y += 38

    # stat strip
    y0 = y
    cell_w = INNER // 4
    f_num = font(28, 800)
    f_lab = font(16, 600)
    for i, (num, lab) in enumerate(STATS):
        cx = MARGIN + i * cell_w
        assert text_w(lab, f_lab) <= cell_w - 8, "STAT LABEL TOO WIDE %r" % lab
        d.text((cx, y0), num, font=f_num, fill=INK)
        d.text((cx, y0 + 30), lab, font=f_lab, fill=GREY)
        if i:
            d.line([cx - 8, y0 + 2, cx - 8, y0 + 46], fill=RULE, width=1)
    y = y0 + 48
    d.line([MARGIN, y, W - MARGIN, y], fill=INK, width=2)
    y += 8

    # heroes: 3 columns, 196 tall
    hero_y = y
    hero_h = 196
    col_w = (INNER - 24) // 3
    for i, hero in enumerate(HEROES):
        hx = MARGIN + i * (col_w + 12)
        ART[hero["art"]](d, hx, hero_y, col_w, 54)
        hy = hero_y + 54 + 6
        d.text((hx, hy), hero["kicker"], font=font(16, 800), fill=hero["color"])
        hy += 19
        hy = draw_wrapped(d, hero["headline"], font(33, 800), hx, hy, col_w,
                          INK, leading=35, max_lines=2)
        f_fact = font(18, 700)
        assert text_w(hero["fact"], f_fact) <= col_w, "FACT TOO WIDE %r" % hero["fact"]
        d.text((hx, hy + 2), hero["fact"], font=f_fact, fill=RED)
        hy += 24
        d.text((hx, hy + 2), hero["source"], font=font(16, 600), fill=GREY)
    y = hero_y + hero_h
    d.line([MARGIN, y + 2, W - MARGIN, y + 2], fill=RULE, width=1)
    y += 10

    # cards: 3x3, rows of 86
    card_y = y
    row_h = 86
    f_card = font(28, 800)
    f_src = font(16, 600)
    for idx, (headline, source, color) in enumerate(CARDS):
        r, c = divmod(idx, 3)
        cx = MARGIN + c * (col_w + 12)
        cy = card_y + r * row_h
        d.rectangle([cx, cy + 4, cx + 5, cy + row_h - 12], fill=color)
        tx = cx + 14
        end = draw_wrapped(d, headline, f_card, tx, cy, col_w - 14,
                           INK, leading=30, max_lines=2)
        d.text((tx, cy + 62), source, font=f_src, fill=GREY)
    y = card_y + 3 * row_h
    d.line([MARGIN, y + 2, W - MARGIN, y + 2], fill=RULE, width=1)
    y += 8

    # briefs header
    f_bhead = font(20, 800)
    d.text((MARGIN, y), "ALSO TODAY — 24 MORE STORIES", font=f_bhead, fill=INK)
    y += 24

    # briefs: 2 columns x 12 rows, 24px rows
    f_brief = font(20, 700)
    brief_col_w = (INNER - 24) // 2
    for idx, (text, color) in enumerate(BRIEFS):
        c = idx % 2
        r = idx // 2
        bx = MARGIN + c * (brief_col_w + 24)
        by = y + r * 21
        assert text_w(text, f_brief) <= brief_col_w - 18, \
            "BRIEF TOO WIDE %r: %d" % (text, text_w(text, f_brief))
        d.ellipse([bx, by + 8, bx + 8, by + 16], fill=color)
        d.text((bx + 14, by), text, font=f_brief, fill=INK)
    y += 12 * 21 + 6

    # footer
    d.line([MARGIN, y, W - MARGIN, y], fill=INK, width=2)
    y += 6
    f_foot = font(16, 600)
    d.text((MARGIN, y), "SOURCES: Reuters · AP · AFP · BBC · IMD · UN News · Nikkei Asia · "
           "Kyiv Independent · Take-Two · UKMTO · PINA · IANS",
           font=f_foot, fill=GREY)
    y += 18
    d.text((MARGIN, y), "REGIONS: EUROPE 9 · THE AMERICAS 8 · ASIA-PACIFIC 8 · "
           "MIDEAST 4 · WORLD 5 · AFRICA 1 · OCEANIA 1 = 36 STORIES",
           font=f_foot, fill=INK)
    y += 18
    d.text((MARGIN, y), "DATE CHECK — NOT TODAY: World Court Myanmar verdict 19 Nov · "
           "Anthropic IPO debut 19 Nov · Fiji disaster 18 Nov",
           font=f_foot, fill=RED)
    y += 18
    d.text((MARGIN, y), "Kerch Bridge span down 17 Nov · Nvidia chief resigns 12 Nov",
           font=f_foot, fill=RED)
    y += 18
    assert y <= H, "page overflow: y=%d" % y

    img.save(path, format="PNG", optimize=True)
    return path


if __name__ == "__main__":
    out = os.path.join(HERE, "entry.png")
    render(out)
    data = open(out, "rb").read()
    print("bytes:", len(data), "sha256:", hashlib.sha256(data).hexdigest())
    assert len(data) <= 1048576, "entry over 1 MiB"
    im = Image.open(out)
    assert im.size == (1024, 1024), im.size
    print("OK 1024x1024, under 1 MiB")
