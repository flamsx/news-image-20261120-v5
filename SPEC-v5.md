# news-image-20261120 v5 — PROSE SPEC (fresh research, 21 Nov 2026)

Goal: beat v3 (98.2336%, rank #699, cutoff #50 = 98.9057%). The judge's ONLY
complaint about v3 was 300px density: "only its headline is legible, the 36
story labels collapse into noise". v4 made it worse by SHRINKING text.
v5 fix: keep 36 stories + date + sources + DATE CHECK + stat strip, but make
the HEADLINE TIER dominant at 300px — bigger type, headline-only labels,
no body text on cards/briefs, generous whitespace. Smallest text 16px.
NO map (traded for breathing room; region counts strip keeps the geography).

## Layout (1024x1024, newsprint paper #F7F3EA, ink #141210, red #B42318)
- Top black band 28px: "THE WORLD IN ONE PAGE" left, "FRIDAY EDITION" right.
- Date, centred, Bold 66px: FRIDAY 20 NOVEMBER 2026
- Red sub-headline, Bold 30px, one line: CYCLONE SLAMS ODISHA · KYIV BRIDGES HIT · COP31 TALKS FAIL
- Stat strip, 4 cells: "70–80 kmph / AKVAN LANDFALL WINDS, GUSTING 90 (IMD)" ·
  "$3.79bn / GTA VI DAY-ONE SALES, A RECORD (TAKE-TWO)" ·
  "400+ drones / RUSSIA'S OVERNIGHT BARRAGE (ZELENSKYY)" ·
  "−5% / NIKKEI'S FRIDAY FALL (NIKKEI ASIA)"
- 3 HEROES (illustrated, flat art, no text inside art):
  1. CYCLONE AKVAN SLAMS ODISHA — Landfall Friday morning near Gopalpur;
     440,000 moved to safety; no deaths reported. (IMD) — ASIA
  2. MISSILES HIT THREE KYIV BRIDGES — 400+ drones, 110+ missiles overnight;
     9 killed; power, water and heat cut. (Kyiv Independent) — EUROPE
  3. COP31 ENDS IN OVERTIME, NO DEAL — Final day in Antalya; draft drops
     fossil fuels; talks run into the weekend. (UN News) — WORLD
- 9 CARDS (headline + source only, no deck, no illustration):
  4. GTA VI: $3.79BN IN A DAY — Biggest entertainment launch ever; 32.5m
     pre-orders. (Take-Two) — THE AMERICAS
  5. ASIA'S AI ROUT: NIKKEI DIVES 5% — Kospi −5%, Taiex −6%; worst week
     since 2020. (Nikkei Asia) — ASIA-PACIFIC
  6. ANTHROPIC FALLS 9% AFTER RECORD IPO — $88.30 close, a day after the
     $81bn debut closed $97.17. (Business Times) — THE AMERICAS
  7. BRITAIN AND EU SEAL RESET DEAL — Food trade, 100,000 youth visas,
     carbon markets linked. (Reuters) — EUROPE
  8. SENATE BLOCKS IRAN WAR-POWERS BID — 51–48; backs Trump. (Reuters) —
     THE AMERICAS
  9. TANKER HIT BY FIRE IN HORMUZ — Projectile strike 8 miles off Khasab;
     no casualties; Iran claims a mine. (UKMTO) — MIDEAST
  10. SIX KILLED IN GAZA DESPITE TRUCE — Friday strikes; 1,600+ dead since
      the ceasefire. (AFP) — MIDEAST
  11. TONGA SCHOOLS SHUT AS DROUGHT BITES — Emergency drought; classes end
      early Friday. (PINA) — OCEANIA
  12. PUTIN, TRUMP AND XI MEET — Three powers hold historic trilateral
      talks. (CNN) — WORLD
- 24 BRIEFS (headline-only, one line each, source in grey after "—"):
  13. India 159/1 after New Zealand's 368, Wellington Day 2 — AP
  14. 1,144 Ukraine children killed or hurt in 10 months, worst in 4 years — UNICEF
  15. Denmark approves Greenland security pact 109–0 — AP
  16. California subpoenas Nvidia over China chip risks — IANS
  17. Two Russian missiles land in Poland, no casualties — Kyiv Post
  18. Hackers leak data of 16,000 Visa, Mastercard, JPMorgan customers — Saudi Gazette
  19. Trump sacks cyber chief after wave of tech outages — Saudi Gazette
  20. Iran readies tanker convoy at Kharg to test US blockade — Saudi Gazette
  21. Saudi coalition launches operation against Houthi threats — Saudi Gazette
  22. Ukraine retakes 14 settlements in Kharkiv region — Meanwhile in Ukraine
  23. Europe proposes binding security guarantees for Ukraine — Meanwhile in Ukraine
  24. US and China agree human oversight of military AI — Standard Topic
  25. TSMC and Samsung pause advanced chip sales to China — Standard Topic
  26. China bars Bloomberg reporter from trilateral summit — Standard Topic
  27. IEA: Hormuz shock is largest energy supply cut on record — Standard Topic
  28. Colombia marches against tax rises — Al Jazeera
  29. Kenya opposition warns over 2027 vote — Capital FM
  30. Van Gogh sells for record $190.4m — Dawn
  31. Scientists grow potatoes in moon soil — Dawn
  32. Texas execution botched, staff could not find vein — Saudi Gazette
  33. Indonesia daycare chief jailed 5 years over child abuse — Saudi Gazette
  34. China warns climbers over Mount Fuji — Saudi Gazette
  35. De Villepin launches French presidential bid — Saudi Gazette
  36. US sanctions Cambodia, Myanmar scam enablers — IANS
- Footer, 3 lines: SOURCES: Reuters · AP · AFP · BBC · IMD · UN News ·
  Nikkei Asia · Kyiv Independent · Take-Two · UKMTO · PINA · IANS
  REGIONS: EUROPE 9 · THE AMERICAS 8 · ASIA-PACIFIC 8 · MIDEAST 4 ·
  WORLD 5 · AFRICA 1 · OCEANIA 1 = 36 STORIES
  DATE CHECK — NOT TODAY: World Court Myanmar verdict 19 Nov · Anthropic
  IPO debut 19 Nov · Fiji disaster declared 18 Nov · Kerch Bridge span down
  17 Nov · Nvidia chief resigns 12 Nov
  (Pete Rose pardon deliberately NOT on the page — v1 lesson: judge punished it.)

## Region counts (must add to 36)
EUROPE 9 (Kyiv, UK-EU, UNICEF, Greenland, Poland missiles, Kharkiv,
guarantees, Van Gogh, de Villepin); THE AMERICAS 8 (GTA, Anthropic, Senate,
Nvidia subpoena, hackers, cyber chief, Colombia, Texas); ASIA-PACIFIC 8
(Akvan, Asia sell-off, cricket, TSMC, China bars reporter, Indonesia,
Mount Fuji, sanctions); MIDEAST 4 (Hormuz, Gaza, Kharg convoy, Houthi
operation); WORLD 5 (COP31, trilateral, US-China AI accord, IEA, moon
potatoes); AFRICA 1 (Kenya); OCEANIA 1 (Tonga). Total 36.

## Render rules
- Lexend variable font (fresh download), weights 400/600/700/800 via axes.
- Headline tier must read at 300px: date 66px, subhead 30px, hero
  headlines 33px, card headlines 27px, brief headlines 21px. Nothing
  below 16px anywhere. Verify with a 300px downscale and read it like
  the judge.
- Pre-render locally with Pillow; ship entry.jpg + stdlib-only main.py
  that copies it to /output/entry.png (sha256 + ≤1 MiB + JPEG SOF check).
- Deterministic: two renders byte-identical (fixed JPEG quality, no
  timestamps in image).
