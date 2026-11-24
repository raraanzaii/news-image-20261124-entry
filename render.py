#!/usr/bin/env python3
"""Render the news-image-20261124 entry: a one-page newspaper front sheet
summing up the world news of Tuesday 24 November 2026.

The stories below were gathered on 24 November 2026 from live editions
published that day (Reuters, The Daily Edition No. 279, the iqmia
worldwide summary for 2026-11-24, Daily Summary Of world edition for
2026-11-24, the Fiat Elpis live desk tape timestamped 2026-11-24,
MyKhel's Sports Bulletin of November 24 and IANS wires dated Nov 24).
Every item carries the outlet it was reported by.

Run locally with Pillow to produce entry.png. The shipped main.py does
not use this file; it only copies the committed entry.png.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 20)
GREY = (96, 92, 86)
RULE = (30, 30, 34)
ACCENT = (146, 24, 24)
BAND = (24, 24, 30)

FONT_DIR = "/usr/share/fonts/truetype/noto/"
BLACK = FONT_DIR + "NotoSans-Black.ttf"
BOLD = FONT_DIR + "NotoSans-Bold.ttf"
REG = FONT_DIR + "NotoSans-Regular.ttf"
CBOLD = FONT_DIR + "NotoSans-CondensedBold.ttf"
CREG = FONT_DIR + "NotoSans-Condensed.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


LEADS = [
    {
        "kicker": "CLIMATE",
        "head": "COP31 TALKS COLLAPSE IN ANTALYA WITHOUT A DEAL",
        "body": "After 50 hours of overtime, more than 90 nations reject a "
                "final text that never mentions fossil fuels. Hosts call it "
                "climate diplomacy's darkest moment.",
        "src": "GRIST / THE DAILY EDITION",
    },
    {
        "kicker": "WAR AT SEA",
        "head": "UN SEEKS PROBE AFTER UKRAINE DRONES SINK RUSSIAN CORVETTE IN LIBYA",
        "body": "Kyiv says seven naval drones sank the corvette Merkury at "
                "Benghazi, taking the Black Sea fight into the Mediterranean. "
                "The UN mission demands an independent inquiry.",
        "src": "UNSMIL / MIDDLE EAST EYE",
    },
    {
        "kicker": "MARKETS",
        "head": "HUANG BACK AT NVIDIA AFTER TRUMP CALL; WALL STREET ERUPTS",
        "body": "Nvidia reinstates Jensen Huang as CEO 11 days after his "
                "resignation. Shares jump 31 percent, the Nasdaq 6.5 percent "
                "and the S and P 500 4.7 percent.",
        "src": "REUTERS",
    },
]

# (section title, [(headline, source), ...]) - headlines kept short so
# most sit on one line; sections are ordered so the three columns of the
# page balance: WORLD+CONFLICT, MONEY+TECH, CLIMATE+SPORT+CULTURE.
SECTIONS = [
    ("WORLD AND POLITICS", [
        ("Russia warns Estonia moves risk open war", "Russia Foreign Ministry"),
        ("Russian drone briefly enters Polish airspace", "Polish Armed Forces"),
        ("Putin open to Article 5-style cover for Ukraine", "Washington Post"),
        ("Zelensky urges four-party peace talks soon", "Daily Summary Of"),
        ("Pentagon rebukes Canada on defence, F-35s", "US Defense Dept"),
        ("China sentences official Ma to death for spying", "Gold Wall Press"),
        ("Hasina seeks Dec 16 return to Bangladesh", "Reuters"),
        ("ICJ ruling raises duty to prevent genocide", "ICJ"),
        ("Somalia, Uganda step up anti-Shabaab fight", "Joint statement"),
        ("India holds No. 3 in Asia Power Index", "Asia Power Index"),
        ("Deputy FBI director Raia to retire in Dec", "Washington Post"),
        ("Car bomb wrecks buildings in Colombia", "AFP"),
    ]),
    ("CONFLICT AND SECURITY", [
        ("UK logs record Iranian attacks in Hormuz", "UKMTO"),
        ("Gaza strikes kill three, incl. UNRWA worker", "Al Jazeera"),
        ("Houthis: Saudi strike kills 17 in Hodeida", "Houthi statement"),
        ("Russia hits vessel near Odesa, substation", "Russia Defence Ministry"),
        ("US yet to OK 60 Patriot missiles for Kyiv", "Financial Times"),
        ("US blacklists Megaspeed in Nvidia scandal", "US Commerce Dept"),
        ("Russian jets enter Korea air defence zone", "South Korea military"),
        ("Vance, Rubio meet Qatari PM on Iran talks", "Washington Post"),
        ("Israel clears flydubai flights to resume", "Israel Transport Ministry"),
    ]),
    ("MONEY AND BUSINESS", [
        ("CrowdStrike buys Zscaler in $43.9bn deal", "Reuters"),
        ("SpaceX-Tesla merger talks: $3.5tn plan", "Financial Times"),
        ("Korea launches short-selling task force", "FSS / Korea Exchange"),
        ("Shenzhen urges firms to lift confidence", "Fiat Elpis desk"),
        ("Ether funds lose $131M; BitMine tops 6M ETH", "KuCoin News"),
        ("Europe fertiliser plants shut on energy costs", "Financial Times"),
        ("Malaysia curbs blacklisted firms' data centres", "Malaysia Trade Ministry"),
        ("India gives $1.62bn aid package to Nepal", "Reuters"),
        ("Modi talks tough to India Inc on jobs", "Reuters"),
        ("Gulf crude exports fall amid Iran stalemate", "Reuters / Kpler"),
    ]),
    ("TECH AND SCIENCE", [
        ("Oregon, Virginia sue SpaceX over Grok images", "State attorneys general"),
        ("Arm extends CEO Haas contract to 2033", "Arm Holdings"),
        ("GTA 6 gets first PS5 patch 01.002.002", "Rockstar"),
        ("Gut antibody IgA helps good bacteria persist", "Nature"),
        ("LISA may spot exoplanets via gravity waves", "ESA research"),
        ("NASA rovers find odd rocks on Mars", "NASA"),
        ("China unveils square-metre shielding films", "Chinese Acad. of Sciences"),
        ("Voyager 1 marks one light-day from Earth", "Bored Panda"),
        ("HPV patterns linked to cervical precancer", "Cohort study"),
        ("Midlife metabolism tied to Alzheimer signs", "RSNA"),
    ]),
    ("CLIMATE AND PLANET", [
        ("California braces for king-tide flooding", "US officials"),
        ("India completes landslide-risk mapping", "Indian officials"),
        ("Nigeria hands rescued pangolins to carers", "Nigeria Customs"),
        ("Lahore tops world pollution list, AQI 500+", "Times of India"),
        ("5.4 quake jolts Nepal, felt in India", "Times of India"),
    ]),
    ("SPORT", [
        ("Brentford rout Everton 4-0 in Premier League", "IANS"),
        ("Kaprizov, Wild beat Sharks 5-2, run hits 15", "Reuters"),
        ("Babar Azam hits 86 on ILT20 debut", "MyKhel"),
        ("Gill urges ICC to rethink saliva ban", "MyKhel"),
        ("Gukesh braces for Sindarov title clash", "MyKhel"),
        ("Tickner out of 2nd Test vs India", "IANS"),
        ("Bangladesh bowled out for 91 at Centurion", "IANS"),
        ("Priyansh Arya smashes 181, T20's No. 2 score", "Match Score Hub"),
        ("Man Utd to appeal Yoro red card at Anfield", "Match Score Hub"),
        ("FIFA names 2031, 2035 Women's WC hosts", "FIFA via MyKhel"),
    ]),
    ("CULTURE AND LIFE", [
        ("Spielberg to direct Heart of Winter film", "Focus Features"),
        ("Avengers: Doomsday trailer teases X-Men", "Marvel"),
        ("DNA genealogy solves 1968 Ontario case", "London, Ont. police"),
        ("Two Americans jailed for life in Quebec case", "Court report"),
        ("Zimbabwe curbs Tagwirei after lender pushback", "iqmia"),
    ]),
]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_masthead(draw):
    draw.rectangle([0, 0, W, 8], fill=ACCENT)
    f_title = font(BLACK, 58)
    title = "THE WORLD TODAY"
    tw = draw.textlength(title, font=f_title)
    draw.text(((W - tw) / 2, 14), title, font=f_title, fill=INK)
    draw.line([28, 84, W - 28, 84], fill=RULE, width=3)
    draw.rectangle([0, 90, W, 122], fill=BAND)
    f_date = font(BOLD, 20)
    draw.text((28, 96), "TUESDAY 24 NOVEMBER 2026", font=f_date,
              fill=(255, 255, 255))
    f_mid = font(REG, 14)
    mid = "The world's news of one day, in one image"
    mw = draw.textlength(mid, font=f_mid)
    draw.text(((W - mw) / 2, 99), mid, font=f_mid, fill=(210, 205, 195))
    f_r = font(BOLD, 14)
    right = "60+ STORIES INSIDE"
    rw = draw.textlength(right, font=f_r)
    draw.text((W - 28 - rw, 99), right, font=f_r, fill=(255, 210, 120))
    return 132


def draw_leads(draw, y0):
    gap = 14
    col_w = (W - 56 - 2 * gap) // 3
    f_kick = font(BOLD, 13)
    f_head = font(BLACK, 20)
    f_body = font(CREG, 13)
    f_src = font(BOLD, 10)
    heights = []
    x = 28
    for lead in LEADS:
        draw.text((x, y0), lead["kicker"], font=f_kick, fill=ACCENT)
        y = y0 + 19
        for line in wrap(draw, lead["head"], f_head, col_w):
            draw.text((x, y), line, font=f_head, fill=INK)
            y += 23
        y += 3
        for line in wrap(draw, lead["body"], f_body, col_w):
            draw.text((x, y), line, font=f_body, fill=(52, 50, 46))
            y += 15
        y += 3
        draw.text((x, y), lead["src"], font=f_src, fill=GREY)
        y += 13
        heights.append(y)
        x += col_w + gap
    y1 = max(heights) + 6
    draw.line([28, y1, W - 28, y1], fill=RULE, width=2)
    return y1 + 9


def column_blocks():
    blocks = []
    for title, items in SECTIONS:
        blocks.append(("head", title))
        for head, src in items:
            blocks.append(("item", (head, src)))
    return blocks


def draw_columns(draw, y0, y_bottom):
    margin = 28
    gap = 18
    cols = 3
    col_w = (W - 2 * margin - (cols - 1) * gap) // cols
    f_sec = font(BOLD, 13)
    f_head = font(CBOLD, 13)
    f_src = font(CREG, 10)
    col = 0
    x = margin
    y = y0
    placed = 0
    last_col_end = y0
    for kind, payload in column_blocks():
        if kind == "head":
            # a section header needs room for itself plus one item
            if y + 24 + 30 > y_bottom and col < cols - 1:
                col += 1
                x = margin + col * (col_w + gap)
                y = y0
            draw.rectangle([x, y, x + col_w, y + 19], fill=BAND)
            draw.text((x + 6, y + 3), payload, font=f_sec,
                      fill=(255, 255, 255))
            y += 24
        else:
            head, src = payload
            lines = wrap(draw, head, f_head, col_w)
            need = len(lines) * 14 + 14
            if y + need > y_bottom and col < cols - 1:
                col += 1
                x = margin + col * (col_w + gap)
                y = y0
            for line in lines:
                draw.text((x, y), line, font=f_head, fill=INK)
                y += 14
            draw.text((x, y), src.upper(), font=f_src, fill=GREY)
            y += 15
            placed += 1
        last_col_end = max(last_col_end, y)
    return placed, last_col_end


def draw_footer(draw, total):
    y = H - 32
    draw.line([28, y, W - 28, y], fill=RULE, width=2)
    f = font(REG, 12)
    txt = ("Compiled from wire and press reports published on Tuesday 24 "
           "November 2026 - " + str(total) + " stories in all.")
    tw = draw.textlength(txt, font=f)
    draw.text(((W - tw) / 2, y + 7), txt, font=f, fill=GREY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    y = draw_masthead(draw)
    y = draw_leads(draw, y)
    placed, end_y = draw_columns(draw, y, H - 42)
    print("columns end at y =", end_y, "(limit", H - 42, ")")
    draw_footer(draw, placed + len(LEADS))
    img.save("entry.png", optimize=True)
    print("stories placed in columns:", placed,
          "| total:", placed + len(LEADS))


if __name__ == "__main__":
    main()
