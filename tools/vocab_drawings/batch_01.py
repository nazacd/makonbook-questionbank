"""Batch 1: the first 30 drawings (each function returns one SVG; PICTURES maps word -> function)."""

import math
import random

from common import INK, arc_arrow, arrow, bush, carrow, f, pine, svg, zzz

def dormant():
    b = ['<circle cx="70" cy="70" r="30" fill="#fff3c4"/>',
         '<path d="M0 290 Q100 262 200 288 T400 280 V400 H0Z" fill="#a7c957"/>',
         '<path d="M50 340 L165 130 Q200 118 235 130 L350 340 Z" fill="#8d6e63"/>',
         '<path d="M165 130 Q200 118 235 130 L258 172 Q246 164 234 176 Q219 162 204 177 Q189 162 175 176 '
         'Q160 164 142 172 Z" fill="#fff"/>',
         '<ellipse cx="200" cy="129" rx="35" ry="8" fill="#5d4037"/>',
         f'<path d="M158 232 Q170 242 182 232 M218 232 Q230 242 242 232" fill="none" stroke="{INK}" '
         'stroke-width="5" stroke-linecap="round"/>',
         '<circle cx="160" cy="258" r="10" fill="#e5989b" opacity=".6"/>'
         '<circle cx="240" cy="258" r="10" fill="#e5989b" opacity=".6"/>',
         f'<path d="M190 266 Q200 273 210 266" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>',
         zzz(240, 100, 14), zzz(264, 70, 20, w=5), zzz(294, 32, 26, w=6),
         '<path d="M0 335 Q110 318 200 338 T400 330 V400 H0Z" fill="#6a994e"/>',
         pine(30, 340, 60), pine(370, 336, 70), pine(335, 350, 45), pine(70, 352, 40)]
    return svg(b, "#cfe8f3")


def converge():
    rivers = ["M-20 50 C 70 70, 150 150, 200 235", "M200 -20 C 192 80, 208 160, 200 235",
              "M420 50 C 330 70, 250 150, 200 235"]
    out = "M200 228 C 200 300, 192 350, 200 420"
    b = []
    for d in rivers:
        b.append(f'<path d="{d}" fill="none" stroke="#e9d8a6" stroke-width="36" stroke-linecap="round"/>')
    b.append(f'<path d="{out}" fill="none" stroke="#e9d8a6" stroke-width="62" stroke-linecap="round"/>')
    for d in rivers:
        b.append(f'<path d="{d}" fill="none" stroke="#4ea8de" stroke-width="22" stroke-linecap="round"/>')
    b.append(f'<path d="{out}" fill="none" stroke="#4ea8de" stroke-width="46" stroke-linecap="round"/>')
    b.append('<path d="M196 270 q4 -6 8 0 M190 320 q4 -6 8 0 M206 355 q4 -6 8 0" fill="none" stroke="#caf0f8" '
             'stroke-width="3" stroke-linecap="round"/>')
    for x, y, r in ((120, 40, 18), (282, 40, 18), (60, 200, 22), (95, 240, 16), (340, 200, 22), (305, 240, 16),
                    (90, 320, 24), (310, 320, 24), (130, 370, 16), (275, 372, 18), (40, 380, 20), (365, 375, 18)):
        b.append(bush(x, y, r))
    return svg(b, "#b5d99c")


def diverge():
    paths = ["M200 420 C 200 340, 200 300, 200 250", "M200 250 C 190 190, 120 140, 40 -20",
             "M200 250 C 210 190, 280 140, 360 -20"]
    b = []
    for d in paths:
        b.append(f'<path d="{d}" fill="none" stroke="#b08968" stroke-width="46" stroke-linecap="round"/>')
    for d in paths:
        b.append(f'<path d="{d}" fill="none" stroke="#e6ccb2" stroke-width="38" stroke-linecap="round"/>')
    for x, y, r in ((200, 120, 26), (200, 45, 20), (60, 250, 24), (95, 310, 20), (340, 255, 24),
                    (40, 360, 22), (360, 360, 22), (70, 120, 18), (330, 120, 18)):
        b.append(bush(x, y, r, "#386641", "#6a994e"))
    # signpost beside the fork
    b.append('<ellipse cx="276" cy="352" rx="14" ry="4" fill="#000" opacity=".15"/>')
    b.append('<rect x="272" y="282" width="8" height="70" rx="2" fill="#7f5539"/>')
    b.append('<g transform="rotate(25 276 292)"><polygon points="242,284 276,284 276,300 242,300 232,292" '
             'fill="#fefae0" stroke="#7f5539" stroke-width="3" stroke-linejoin="round"/></g>')
    b.append('<g transform="rotate(-25 276 316)"><polygon points="276,308 310,308 320,316 310,324 276,324" '
             'fill="#fefae0" stroke="#7f5539" stroke-width="3" stroke-linejoin="round"/></g>')
    return svg(b, "#a7c957")


def fragile():
    b = ['<rect y="318" width="400" height="82" fill="#e0d2c0"/>',
         # wine glass with a crack
         '<path d="M78 112 Q74 200 115 216 Q156 200 152 112 Z" fill="#d8eef7" stroke="#8ecae6" stroke-width="4"/>',
         '<path d="M140 125 Q144 170 128 196" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>',
         '<line x1="115" y1="216" x2="115" y2="306" stroke="#8ecae6" stroke-width="6"/>',
         '<ellipse cx="115" cy="310" rx="34" ry="8" fill="#d8eef7" stroke="#8ecae6" stroke-width="4"/>',
         '<path d="M92 112 L104 138 L95 152 L110 172 L103 190" fill="none" stroke="#1d3557" stroke-width="3" '
         'stroke-linejoin="round"/>',
         '<path d="M104 138 L118 142 M95 152 L84 160" fill="none" stroke="#1d3557" stroke-width="2"/>',
         '<path d="M58 92 l-12 -10 M70 80 l-5 -14 M160 92 l12 -10 M150 80 l5 -14" stroke="#e76f51" '
         'stroke-width="4" stroke-linecap="round"/>',
         '<polygon points="52,338 66,328 70,342" fill="#d8eef7" stroke="#8ecae6" stroke-width="2"/>',
         '<polygon points="160,344 176,336 172,350" fill="#d8eef7" stroke="#8ecae6" stroke-width="2"/>',
         # box with the "fragile" glass symbol
         '<polygon points="200,190 230,160 380,160 350,190" fill="#e0b88a"/>',
         '<polygon points="350,190 380,160 380,300 350,330" fill="#b9895a"/>',
         '<rect x="200" y="190" width="150" height="140" fill="#d4a373"/>',
         '<polygon points="268,190 298,160 312,160 282,190" fill="#c9a46b"/>',
         '<rect x="268" y="190" width="14" height="26" fill="#c9a46b"/>',
         '<path d="M260 232 H292 Q294 262 276 270 Q258 262 260 232 Z" fill="#d62828"/>',
         '<path d="M270 232 L279 246 L272 253 L281 266" fill="none" stroke="#d4a373" stroke-width="3.5"/>',
         '<rect x="273" y="270" width="6" height="22" fill="#d62828"/><rect x="263" y="292" width="26" height="6" '
         'rx="2" fill="#d62828"/>',
         arrow(222, 300, 222, 252, INK, 4, 12), arrow(236, 300, 236, 252, INK, 4, 12)]
    return svg(b, "#f6efe6")


def ladybug(x, y, r, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot})">'
            f'<circle cx="0" cy="{f(-r * .95)}" r="{f(r * .5)}" fill="#222"/>'
            f'<circle r="{f(r)}" fill="#e63946"/>'
            f'<line x1="0" y1="{f(-r)}" x2="0" y2="{f(r)}" stroke="#222" stroke-width="{f(r * .12)}"/>'
            + "".join(f'<circle cx="{f(sx * r)}" cy="{f(sy * r)}" r="{f(rr * r)}" fill="#222"/>'
                      for sx, sy, rr in ((-.45, -.2, .18), (.45, -.2, .18), (-.42, .42, .16), (.42, .42, .16)))
            + f'<circle cx="{f(-r * .35)}" cy="{f(-r * .5)}" r="{f(r * .15)}" fill="#fff" opacity=".7"/></g>')


def magnify():
    leaf = ('<path d="M30 330 C 60 180, 230 120, 380 60 C 350 220, 220 330, 30 330 Z" fill="#95d5b2"/>'
            '<path d="M30 330 C 150 250, 260 160, 380 60" fill="none" stroke="#74c69d" stroke-width="4"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#74c69d"/>'
                      for x, y in ((228, 168), (241, 186), (222, 190), (246, 166), (214, 176), (250, 180))))
    scene = leaf + ladybug(232, 178, 9, 25)
    b = [scene, ladybug(95, 300, 9, 40), ladybug(150, 262, 9, 10), ladybug(320, 120, 8, -20),
         '<g clip-path="url(#lens)"><g transform="translate(235 175) scale(3.5) translate(-235 -175)">'
         + scene + '</g></g>',
         '<circle cx="235" cy="175" r="80" fill="#fff" opacity=".12"/>',
         '<path d="M190 120 A62 62 0 0 1 250 108" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" '
         'opacity=".8"/>',
         '<line x1="300" y1="240" x2="365" y2="305" stroke="#6d4c41" stroke-width="24" stroke-linecap="round"/>',
         f'<line x1="290" y1="230" x2="306" y2="246" stroke="{INK}" stroke-width="26"/>',
         f'<circle cx="235" cy="175" r="80" fill="none" stroke="{INK}" stroke-width="12"/>']
    return svg(b, "#e8f5e9", '<clipPath id="lens"><circle cx="235" cy="175" r="80"/></clipPath>')


def amplify():
    def wave(cx, cy, r, w, color, deg=40):
        a = math.radians(deg)
        x, y1, y2 = cx + r * math.cos(a), cy - r * math.sin(a), cy + r * math.sin(a)
        return (f'<path d="M{f(x)} {f(y1)} A{r} {r} 0 0 1 {f(x)} {f(y2)}" fill="none" stroke="{color}" '
                f'stroke-width="{w}" stroke-linecap="round"/>')
    b = [wave(40, 200, 16, 3, INK), wave(40, 200, 28, 3, INK),
         f'<rect x="86" y="186" width="28" height="28" rx="6" fill="{INK}"/>',
         '<path d="M112 184 L250 128 L250 272 L112 216 Z" fill="#f4a261"/>',
         '<path d="M150 170 L150 230" stroke="#fff" stroke-width="8" opacity=".45"/>',
         f'<path d="M150 214 L158 270 L176 270 L172 222 Z" fill="{INK}"/>',
         '<ellipse cx="250" cy="200" rx="15" ry="73" fill="#e76f51"/>',
         '<ellipse cx="253" cy="200" rx="8" ry="62" fill="#9c4a2f"/>',
         wave(262, 200, 45, 7, "#e76f51"), wave(262, 200, 80, 10, "#e76f51"), wave(262, 200, 115, 13, "#e76f51")]
    return svg(b, "#fdf0d5")


def acorn(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({s})">'
            '<ellipse cx="0" cy="3" rx="9" ry="11" fill="#b5651d"/>'
            '<ellipse cx="-3" cy="2" rx="2.5" ry="5" fill="#d08c4a"/>'
            '<path d="M-11 -3 Q0 -15 11 -3 Q0 1 -11 -3 Z" fill="#6b4226"/>'
            '<path d="M0 -10 L1 -15" stroke="#6b4226" stroke-width="2.5" stroke-linecap="round"/></g>')


def hoard():
    rnd = random.Random(3)
    b = ['<path d="M0 340 H400 V400 H0Z" fill="#d4a373"/>']
    for x, y, c in ((40, 370, "#e76f51"), (370, 380, "#f4a261"), (220, 385, "#e9c46a"), (120, 390, "#f4a261")):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="5" fill="{c}" transform="rotate(-20 {x} {y})"/>')
    for i in range(8):
        n = 8 - i
        for j in range(n):
            x = 278 - (n - 1) * 10.5 + j * 21 + rnd.uniform(-2, 2)
            b.append(acorn(x, 330 - i * 19 + rnd.uniform(-2, 2), 1.0, rnd.uniform(-25, 25)))
    b += ['<path d="M95 325 C 25 305, 15 190, 60 150 C 95 120, 135 160, 110 190 C 90 210, 80 260, 120 300 Z" '
          'fill="#b5651d"/>',
          '<path d="M68 168 C 48 195, 50 255, 88 292" fill="none" stroke="#d08c4a" stroke-width="6" '
          'stroke-linecap="round"/>',
          '<ellipse cx="140" cy="282" rx="38" ry="50" fill="#c8743a"/>',
          '<ellipse cx="155" cy="292" rx="20" ry="34" fill="#f1c27d"/>',
          '<circle cx="160" cy="220" r="28" fill="#c8743a"/>',
          '<path d="M146 198 L150 170 L166 194 Z" fill="#b5651d"/>',
          '<ellipse cx="176" cy="230" rx="14" ry="11" fill="#f1c27d"/>',
          f'<circle cx="168" cy="212" r="4.5" fill="{INK}"/><circle cx="169.5" cy="210.5" r="1.5" fill="#fff"/>',
          f'<circle cx="189" cy="226" r="4" fill="{INK}"/>',
          '<ellipse cx="150" cy="332" rx="24" ry="8" fill="#b5651d"/>',
          acorn(193, 258, 1.2, 15),
          '<ellipse cx="180" cy="266" rx="15" ry="8" fill="#b5651d" transform="rotate(-25 180 266)"/>']
    return svg(b, "#fbe8d3")


def hibernation():
    rnd = random.Random(5)
    hill = "M10 345 Q50 150 200 140 Q350 150 390 345 Z"
    b = [f'<circle cx="{rnd.randint(5, 395)}" cy="{rnd.randint(5, 340)}" r="{rnd.choice((2.5, 3, 4))}" fill="#fff"/>'
         for _ in range(70)]
    b += [f'<path d="{hill}" fill="#8d99ae"/>',
          '<g clip-path="url(#hill)"><path d="M0 0 H400 V215 Q370 200 345 212 Q320 196 295 210 Q270 194 245 208 '
          'Q220 192 195 207 Q170 192 145 208 Q120 194 95 210 Q70 196 45 212 Q20 200 0 214 Z" fill="#fff"/></g>',
          '<path d="M105 345 Q112 225 200 220 Q288 225 295 345 Z" fill="#3d405b"/>',
          '<path d="M120 342 Q200 334 282 342" stroke="#e9c46a" stroke-width="6" fill="none"/>',
          '<ellipse cx="212" cy="312" rx="68" ry="32" fill="#8b5a2b"/>',
          '<ellipse cx="230" cy="292" rx="40" ry="16" fill="#9c6b3c"/>',
          '<circle cx="150" cy="306" r="25" fill="#8b5a2b"/>',
          '<circle cx="140" cy="285" r="9" fill="#8b5a2b"/><circle cx="140" cy="285" r="4" fill="#6f4518"/>',
          '<ellipse cx="131" cy="314" rx="12" ry="8" fill="#c08552"/>',
          f'<ellipse cx="122" cy="311" rx="4" ry="3" fill="{INK}"/>',
          f'<path d="M144 301 Q150 307 156 301" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>',
          '<ellipse cx="174" cy="334" rx="17" ry="8" fill="#6f4518"/>',
          zzz(168, 268, 10, "#fff", 3), zzz(184, 249, 13, "#fff", 3.5), zzz(204, 229, 16, "#fff", 4),
          '<path d="M0 345 Q100 333 200 345 T400 341 V400 H0Z" fill="#fff"/>',
          '<path d="M360 346 L363 245 M362 290 L386 262 M362 272 L340 248 M375 276 L383 286" fill="none" '
          'stroke="#5c4033" stroke-width="5" stroke-linecap="round"/>']
    return svg(b, "#dbe7f0", f'<clipPath id="hill"><path d="{hill}"/></clipPath>')


def fluctuate():
    xs = [85 + i * 25.5 for i in range(11)]
    ys = [250, 150, 235, 110, 265, 165, 300, 120, 215, 95, 240]
    pts = " ".join(f"{f(x)},{y}" for x, y in zip(xs, ys))
    b = ['<rect x="40" y="45" width="330" height="310" rx="18" fill="#fff"/>']
    b += [f'<line x1="72" y1="{y}" x2="350" y2="{y}" stroke="#e9ecef" stroke-width="2"/>' for y in (100, 150, 200, 250, 300)]
    b += [f'<path d="M72 68 V322 H352" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>',
          f'<polyline points="{pts}" fill="none" stroke="#e76f51" stroke-width="6" stroke-linejoin="round" '
          'stroke-linecap="round"/>']
    b += [f'<circle cx="{f(x)}" cy="{y}" r="7" fill="#fff" stroke="#e76f51" stroke-width="4"/>' for x, y in zip(xs, ys)]
    return svg(b, "#f1faee")


def coin(cx, cy):
    return (f'<ellipse cx="{cx}" cy="{f(cy)}" rx="26" ry="8" fill="#c9a227"/>'
            f'<rect x="{cx - 26}" y="{f(cy - 6)}" width="52" height="6" fill="#c9a227"/>'
            f'<ellipse cx="{cx}" cy="{f(cy - 6)}" rx="26" ry="8" fill="#f2cc5b" stroke="#c9a227" stroke-width="1.5"/>')


def accumulate():
    b = ['<rect y="336" width="400" height="64" fill="#dde5b6"/>']
    for x, n in ((65, 1), (132, 3), (200, 6), (268, 10), (335, 15)):
        for k in range(n):
            b.append(coin(x, 332 - 7 * k))
    b.append('<g transform="rotate(-25 335 150)"><ellipse cx="335" cy="150" rx="26" ry="8" fill="#c9a227"/>'
             '<rect x="309" y="144" width="52" height="6" fill="#c9a227"/>'
             '<ellipse cx="335" cy="144" rx="26" ry="8" fill="#f2cc5b" stroke="#c9a227" stroke-width="1.5"/></g>')
    b.append('<path d="M322 112 v-22 M338 108 v-26 M354 112 v-22" stroke="#c9a227" stroke-width="3" '
             'stroke-linecap="round"/>')
    b.append(carrow(50, 290, 120, 110, 280, 95, "#2a9d8f", 6, 18))
    return svg(b, "#eef6f0")


def apple(x, y, r=10):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{r}" fill="#e63946"/>'
            f'<circle cx="{f(x - r * .35)}" cy="{f(y - r * .35)}" r="{f(r * .28)}" fill="#fff" opacity=".6"/>'
            f'<path d="M{f(x)} {f(y - r)} l1 -5" stroke="#6b4226" stroke-width="2" stroke-linecap="round"/>')


def abundant():
    rnd = random.Random(11)
    canopy = [(200, 140, 95), (120, 170, 60), (280, 170, 60), (150, 95, 55), (255, 95, 55), (200, 70, 55)]
    b = ['<path d="M0 330 Q200 312 400 330 V400 H0Z" fill="#90be6d"/>',
         '<path d="M185 335 L190 230 Q170 200 150 190 L158 182 Q185 195 197 215 Q210 190 245 178 L250 187 '
         'Q220 200 210 230 L215 335 Z" fill="#7f5539"/>']
    b += [f'<circle cx="{x}" cy="{y}" r="{r}" fill="#52b788"/>' for x, y, r in canopy]
    b += [f'<circle cx="{x - r * .25:.0f}" cy="{y - r * .25:.0f}" r="{r * .55:.0f}" fill="#74c69d" opacity=".55"/>'
          for x, y, r in canopy]
    pts = []
    while len(pts) < 34:
        x, y = rnd.uniform(70, 330), rnd.uniform(30, 230)
        if any(math.hypot(x - cx, y - cy) < r - 12 for cx, cy, r in canopy) and \
                all(math.hypot(x - px, y - py) > 24 for px, py in pts):
            pts.append((x, y))
    b += [apple(x, y) for x, y in pts]
    b += [apple(x, y) for x, y in ((262, 292), (282, 288), (302, 290), (322, 293), (272, 276), (292, 274),
                                   (312, 277), (292, 259))]
    b += ['<path d="M245 300 H345 L333 345 H257 Z" fill="#bc8a5f"/>',
          '<path d="M249 315 H341 M252 330 H338" stroke="#99582a" stroke-width="3"/>',
          '<path d="M275 300 L277 345 M295 300 V345 M315 300 L313 345" stroke="#99582a" stroke-width="3"/>']
    b += [apple(x, y) for x, y in ((225, 345), (365, 343), (150, 350), (120, 340))]
    return svg(b, "#e3f2fd")


def meager():
    b = [f'<line x1="0" y1="{y}" x2="400" y2="{y}" stroke="#c99a6e" stroke-width="3"/>' for y in (80, 160, 240, 320)]
    b += ['<circle cx="203" cy="206" r="135" fill="#000" opacity=".08"/>',
          '<circle cx="200" cy="200" r="135" fill="#fff"/>',
          '<circle cx="200" cy="200" r="96" fill="#f8f9fa" stroke="#e9ecef" stroke-width="3"/>']
    for x, y in ((193, 203), (206, 197), (202, 211)):
        b.append(f'<circle cx="{x}" cy="{y}" r="6.5" fill="#80b918"/><circle cx="{x - 2}" cy="{y - 2}" r="2" '
                 'fill="#d4ed91"/>')
    b += ['<rect x="34" y="150" width="12" height="160" rx="6" fill="#adb5bd"/>',
          '<path d="M28 98 V140 Q28 152 40 152 Q52 152 52 140 V98" fill="none" stroke="#adb5bd" stroke-width="4"/>',
          '<path d="M36 98 V138 M44 98 V138" stroke="#adb5bd" stroke-width="4"/>',
          '<path d="M354 90 Q376 120 368 200 H354 Z" fill="#ced4da"/>',
          '<rect x="352" y="200" width="16" height="112" rx="7" fill="#adb5bd"/>']
    return svg(b, "#d4a373")


def intersect():
    b = ['<rect x="0" y="165" width="400" height="70" fill="#6c757d"/>',
         '<rect x="165" y="0" width="70" height="400" fill="#6c757d"/>']
    for x in range(5, 400, 32):
        if not 130 < x < 260:
            b.append(f'<rect x="{x}" y="198" width="18" height="4" fill="#fff"/>')
            b.append(f'<rect x="198" y="{x}" width="4" height="18" fill="#fff"/>')
    for k in range(6):
        o = 170 + k * 10.5
        b += [f'<rect x="140" y="{o:.1f}" width="18" height="5" fill="#fff"/>',
              f'<rect x="242" y="{o:.1f}" width="18" height="5" fill="#fff"/>',
              f'<rect x="{o:.1f}" y="140" width="5" height="18" fill="#fff"/>',
              f'<rect x="{o:.1f}" y="242" width="5" height="18" fill="#fff"/>']
    b += [f'<circle cx="200" cy="200" r="16" fill="#ffd166" stroke="{INK}" stroke-width="4"/>',
          '<rect x="60" y="172" width="42" height="20" rx="5" fill="#e76f51"/>',
          '<rect x="88" y="175" width="9" height="14" rx="2" fill="#caf0f8"/>',
          '<rect x="208" y="300" width="20" height="42" rx="5" fill="#457b9d"/>',
          '<rect x="211" y="305" width="14" height="9" rx="2" fill="#caf0f8"/>']
    for x, y in ((75, 75), (320, 80), (80, 320), (325, 325), (120, 110), (290, 290)):
        b.append(bush(x, y, 26))
    return svg(b, "#95d5b2")


def isolate():
    b = ['<circle cx="140" cy="215" r="112" fill="#e9f5fb" stroke="#8ecae6" stroke-width="6"/>',
         '<circle cx="140" cy="215" r="100" fill="none" stroke="#cde8f6" stroke-width="2"/>']
    gap = (182, 200)
    for row in range(-3, 4):
        for col in range(-4, 5):
            x = 140 + col * 29 + (14.5 if row % 2 else 0)
            y = 215 + row * 25
            if math.hypot(x - 140, y - 215) > 84:
                continue
            if math.hypot(x - gap[0], y - gap[1]) < 12:
                b.append(f'<circle cx="{f(x)}" cy="{y}" r="13" fill="none" stroke="#adb5bd" stroke-width="2.5" '
                         'stroke-dasharray="5 4"/>')
                continue
            b.append(f'<circle cx="{f(x)}" cy="{y}" r="13" fill="#4895ef"/><circle cx="{f(x - 4)}" cy="{y - 4}" r="3.5" '
                     'fill="#fff" opacity=".6"/>')
    b += ['<circle cx="322" cy="215" r="55" fill="#fff4e6" stroke="#f4a261" stroke-width="6"/>',
          '<circle cx="322" cy="215" r="16" fill="#f77f00"/><circle cx="317" cy="210" r="4" fill="#fff" opacity=".6"/>',
          carrow(200, 165, 255, 80, 310, 150, INK, 5, 16)]
    return svg(b, "#f1faee")


def immense():
    defs = ('<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#48cae4"/>'
            '<stop offset="1" stop-color="#03045e"/></linearGradient>')
    b = ['<rect y="0" width="400" height="92" fill="#bde0fe"/>',
         '<rect y="90" width="400" height="310" fill="url(#sea)"/>',
         '<path d="M0 90 q10 -5 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 '
         't20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#fff" stroke-width="3"/>',
         '<path d="M290 86 H314 L309 93 H295 Z" fill="#e76f51"/><path d="M302 86 V70 L311 84 Z" fill="#fff"/>',
         '<path d="M70 250 C 52 240, 32 220, 10 194 C 20 216, 34 234, 50 248 C 32 260, 20 278, 10 304 '
         'C 32 284, 50 266, 70 254 Z" fill="#457b9d"/>',
         '<path d="M62 250 C 100 190, 210 165, 320 180 C 372 189, 392 228, 360 255 C 300 300, 160 300, 100 266 '
         'C 84 259, 72 254, 62 250 Z" fill="#457b9d"/>',
         '<path d="M150 285 C 220 300, 310 285, 362 252" fill="none" stroke="#a8dadc" stroke-width="3"/>',
         '<path d="M190 280 C 250 290, 320 276, 365 245" fill="none" stroke="#a8dadc" stroke-width="3"/>',
         '<path d="M235 272 C 290 278, 340 262, 368 238" fill="none" stroke="#a8dadc" stroke-width="3"/>',
         '<path d="M300 236 Q340 244 378 230" fill="none" stroke="#1d3557" stroke-width="3"/>',
         '<path d="M240 268 C 236 300, 218 320, 196 328 C 214 306, 220 290, 222 270 Z" fill="#355c7d"/>',
         f'<circle cx="335" cy="214" r="5" fill="{INK}"/>']
    for x, y, r in ((352, 160, 6), (360, 135, 4), (348, 115, 5), (362, 100, 3)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#fff" stroke-width="2"/>')
    return svg(b, "#48cae4", defs)


def seed(x, y, rot, s=1.0, l=14, color="#fff", stem="#7f5539"):
    fan = "".join(f'<line x1="0" y1="{-l}" x2="{dx}" y2="{-l - dy}" stroke="{color}" stroke-width="1.6" '
                  'stroke-linecap="round"/>' for dx, dy in ((-7, 7), (-4, 10), (0, 11), (4, 10), (7, 7)))
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({s})">'
            f'<line x1="0" y1="0" x2="0" y2="{-l}" stroke="{color}" stroke-width="1.6"/>{fan}'
            f'<ellipse cx="0" cy="1" rx="1.8" ry="3.5" fill="{stem}"/></g>')


def dispersed():
    rnd = random.Random(8)
    b = ['<path d="M0 360 Q200 344 400 360 V400 H0Z" fill="#90be6d"/>',
         '<path d="M150 120 Q200 100 250 120 T350 115" fill="none" stroke="#fff" stroke-width="4" '
         'stroke-linecap="round" opacity=".7"/>',
         '<path d="M130 255 Q190 235 240 255 T340 250" fill="none" stroke="#fff" stroke-width="4" '
         'stroke-linecap="round" opacity=".7"/>',
         '<path d="M210 185 Q250 172 290 185" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" '
         'opacity=".7"/>',
         '<path d="M70 400 Q60 300 95 215" fill="none" stroke="#588157" stroke-width="6"/>',
         '<path d="M68 395 Q40 370 30 340 L45 350 L40 330 L55 345 L55 325 Q65 360 72 392 Z" fill="#588157"/>']
    for a in range(100, 300, 12):
        b.append(seed(95, 200, a + 90, 1.0, 34))
    b.append('<circle cx="95" cy="200" r="9" fill="#a3a380"/>')
    for _ in range(18):
        x, y = rnd.uniform(150, 385), rnd.uniform(40, 330)
        b.append(seed(x, y, rnd.uniform(-50, 50), rnd.uniform(1.0, 1.4)))
    return svg(b, "#a9d6f5")


def glass(x):
    return (f'<path d="M{x - 38} 168 L{x - 30} 318 H{x + 30} L{x + 38} 168 Z" fill="#bde0fe" opacity=".75"/>'
            f'<path d="M{x - 40} 128 L{x - 30} 320 H{x + 30} L{x + 40} 128" fill="none" stroke="#8ecae6" '
            'stroke-width="5" stroke-linejoin="round"/>'
            f'<line x1="{x - 38}" y1="168" x2="{x + 38}" y2="168" stroke="#8ecae6" stroke-width="3"/>')


def cube(x, y, s, rot=0):
    d = s * .25
    return (f'<g transform="rotate({rot} {x + s / 2} {y + s / 2})">'
            f'<polygon points="{x},{y} {x + d},{y - d} {x + s + d},{y - d} {x + s},{y}" fill="#f1f3f5" '
            'stroke="#adb5bd" stroke-width="1.5"/>'
            f'<polygon points="{x + s},{y} {x + s + d},{y - d} {x + s + d},{y + s - d} {x + s},{y + s}" '
            'fill="#dee2e6" stroke="#adb5bd" stroke-width="1.5"/>'
            f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="#fff" stroke="#adb5bd" stroke-width="1.5"/></g>')


def dissolve():
    rnd = random.Random(4)
    b = ['<rect y="318" width="400" height="82" fill="#f2e2d0"/>', glass(75), glass(200), glass(325),
         cube(60, 284, 30), cube(193, 298, 16, 18)]
    for _ in range(26):
        x, y = rnd.gauss(201, 14), rnd.uniform(220, 314)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{rnd.choice((1.5, 2, 2.5))}" fill="#fff" stroke="#adb5bd" '
                 'stroke-width=".8"/>')
    for _ in range(8):
        x, y = rnd.uniform(300, 350), rnd.uniform(185, 310)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="1.5" fill="#fff" opacity=".8"/>')
    b += [arrow(120, 235, 152, 235, INK, 5, 13), arrow(245, 235, 277, 235, INK, 5, 13)]
    return svg(b, "#fff8f0")


def constrict():
    tube = ("M20 140 H130 C165 140, 172 185, 200 185 C 228 185, 235 140, 270 140 H380 V260 H270 "
            "C235 260, 228 215, 200 215 C172 215, 165 260, 130 260 H20 Z")
    b = [f'<path d="{tube}" fill="#a8dadc" stroke="#457b9d" stroke-width="5" stroke-linejoin="round"/>',
         '<path d="M30 160 H120" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".7"/>',
         '<path d="M280 160 H370" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".7"/>',
         arrow(40, 215, 100, 215, "#457b9d", 5, 14), arrow(300, 215, 360, 215, "#457b9d", 5, 14),
         arrow(200, 70, 200, 170, "#e76f51", 8, 22), arrow(200, 330, 200, 230, "#e76f51", 8, 22)]
    return svg(b, "#f8f9fa")


def jar(items_fn, seed_):
    rnd = random.Random(seed_)
    b = ['<rect y="355" width="400" height="45" fill="#ddb892"/>',
         '<rect x="100" y="108" width="200" height="248" rx="34" fill="#eef7fb" stroke="#8ecae6" stroke-width="6"/>',
         '<g clip-path="url(#inside)">']
    for i, y in enumerate(range(338, 150, -26)):
        xs = range(122, 280, 30) if i % 2 == 0 else range(137, 270, 30)
        for x in xs:
            b.append(items_fn(x, y, rnd))
    b += ['</g>', '<rect x="113" y="128" width="12" height="200" rx="6" fill="#fff" opacity=".55"/>',
          '<rect x="114" y="78" width="172" height="36" rx="8" fill="#e76f51"/>',
          '<rect x="114" y="104" width="172" height="10" fill="#c1553b"/>']
    return svg(b, "#fdfcdc", '<clipPath id="inside"><rect x="106" y="114" width="188" height="236" rx="28"/></clipPath>')


def homogeneous():
    return jar(lambda x, y, r: (f'<circle cx="{x}" cy="{y}" r="13.5" fill="#3a86ff"/>'
                                f'<circle cx="{x - 4}" cy="{y - 4}" r="3.5" fill="#fff" opacity=".6"/>'), 1)


def heterogeneous():
    colors = ["#e63946", "#f4a261", "#e9c46a", "#2a9d8f", "#3a86ff", "#8338ec", "#ff006e", "#06d6a0", "#6d4c41"]

    def item(x, y, r):
        c, s = r.choice(colors), r.uniform(8, 14)
        k = r.choice(("circle", "square", "triangle", "star", "diamond"))
        rot = r.uniform(0, 90)
        if k == "circle":
            return f'<circle cx="{x}" cy="{y}" r="{f(s)}" fill="{c}"/>'
        if k == "square":
            return (f'<rect x="{f(x - s * .8)}" y="{f(y - s * .8)}" width="{f(s * 1.6)}" height="{f(s * 1.6)}" rx="2" '
                    f'fill="{c}" transform="rotate({f(rot)} {x} {y})"/>')
        if k == "diamond":
            return f'<polygon points="{x},{f(y - s)} {f(x + s * .7)},{y} {x},{f(y + s)} {f(x - s * .7)},{y}" fill="{c}"/>'
        if k == "triangle":
            pts = " ".join(f"{f(x + s * math.cos(math.radians(a + rot)))},{f(y + s * math.sin(math.radians(a + rot)))}"
                           for a in (-90, 30, 150))
            return f'<polygon points="{pts}" fill="{c}"/>'
        pts = " ".join(f"{f(x + (s if i % 2 == 0 else s * .45) * math.cos(math.radians(-90 + i * 36)))},"
                       f"{f(y + (s if i % 2 == 0 else s * .45) * math.sin(math.radians(-90 + i * 36)))}"
                       for i in range(10))
        return f'<polygon points="{pts}" fill="{c}"/>'
    return jar(item, 7)


def transparent():
    bowl_clip = '<clipPath id="bowl"><rect x="0" y="118" width="400" height="300"/></clipPath>'
    water_clip = '<clipPath id="water"><circle cx="215" cy="215" r="112"/></clipPath>'
    b = ['<rect y="330" width="400" height="70" fill="#ddb892"/>',
         # plant behind the bowl, seen through the glass
         '<path d="M80 280 H150 L142 330 H88 Z" fill="#bc6c25"/>',
         '<ellipse cx="100" cy="190" rx="16" ry="70" fill="#52b788" transform="rotate(-18 100 190)"/>',
         '<ellipse cx="130" cy="195" rx="16" ry="70" fill="#40916c" transform="rotate(14 130 195)"/>',
         '<ellipse cx="115" cy="175" rx="14" ry="80" fill="#2d6a4f"/>',
         '<g clip-path="url(#bowl)"><circle cx="215" cy="215" r="115" fill="#caf0f8" opacity=".25" '
         'stroke="#48cae4" stroke-width="5"/></g>',
         '<g clip-path="url(#water)"><rect x="90" y="140" width="260" height="200" fill="#90e0ef" opacity=".35"/>'
         + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="6" fill="{c}"/>'
                   for x, y, c in ((160, 318, "#adb5bd"), (180, 322, "#ced4da"), (200, 320, "#adb5bd"),
                                   (222, 323, "#dee2e6"), (245, 321, "#adb5bd"), (268, 318, "#ced4da"),
                                   (190, 312, "#dee2e6"), (233, 313, "#ced4da")))
         + '<path d="M260 316 Q250 290 262 268 Q272 248 262 228" fill="none" stroke="#52b788" stroke-width="6" '
           'stroke-linecap="round"/></g>',
         '<ellipse cx="215" cy="140" rx="70" ry="7" fill="none" stroke="#90e0ef" stroke-width="2"/>',
         '<path d="M190 230 L172 216 L172 244 Z" fill="#f77f00"/>',
         '<ellipse cx="218" cy="230" rx="30" ry="18" fill="#f77f00"/>',
         '<path d="M212 214 Q220 200 232 214" fill="#f77f00"/>',
         f'<circle cx="235" cy="225" r="4" fill="{INK}"/><circle cx="236" cy="224" r="1.3" fill="#fff"/>',
         '<path d="M150 275 L138 266 L138 284 Z" fill="#ffd166"/><ellipse cx="165" cy="275" rx="17" ry="10" fill="#ffd166"/>',
         f'<circle cx="174" cy="272" r="2.5" fill="{INK}"/>',
         '<circle cx="250" cy="200" r="4" fill="none" stroke="#fff" stroke-width="2"/>',
         '<circle cx="256" cy="182" r="3" fill="none" stroke="#fff" stroke-width="2"/>',
         '<ellipse cx="215" cy="118" rx="62" ry="10" fill="none" stroke="#48cae4" stroke-width="4"/>',
         '<path d="M290 170 A90 90 0 0 1 300 250" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" '
         'opacity=".85"/>']
    return svg(b, "#fef6e4", bowl_clip + water_clip)


def bird(x, y, body, wing, flip=False, eye=INK, k=1.0):
    s = -1 if flip else 1
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s * k)} {k})">'
            f'<path d="M-3 0 v5 M4 0 v5" stroke="{INK}" stroke-width="2"/>'
            f'<polygon points="-11,-13 -25,-5 -12,-6" fill="{wing}"/>'
            f'<ellipse cx="0" cy="-13" rx="14" ry="11" fill="{body}"/>'
            f'<ellipse cx="-2" cy="-13" rx="9" ry="6" fill="{wing}"/>'
            f'<circle cx="10" cy="-25" r="8" fill="{body}"/>'
            f'<polygon points="16,-27 24,-25 16,-22" fill="#f4a261"/>'
            f'<circle cx="12" cy="-27" r="1.8" fill="{eye}"/></g>')


def conspicuous():
    rnd = random.Random(2)
    b = ['<path d="M-10 150 Q200 185 410 150" fill="none" stroke="#343a40" stroke-width="3"/>',
         '<path d="M-10 270 Q200 305 410 270" fill="none" stroke="#343a40" stroke-width="3"/>']
    for base in (150, 270):
        for x in (42, 94, 146, 198, 250, 302, 354):
            t = (x + 10) / 420
            y = base + 70 * t * (1 - t)
            if base == 270 and x == 198:
                b.append(bird(x, y, "#e63946", "#9d0208", flip=rnd.random() < .5, k=1.4))
            else:
                b.append(bird(x, y, "#8d99ae", "#6c757d", flip=rnd.random() < .5, k=1.4))
    b.append('<circle cx="60" cy="60" r="26" fill="#fff" opacity=".7"/><circle cx="95" cy="55" r="20" fill="#fff" '
             'opacity=".7"/><circle cx="330" cy="70" r="24" fill="#fff" opacity=".7"/>')
    return svg(b, "#caf0f8")


def ephemeral():
    defs = ('<radialGradient id="bub" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff" stop-opacity=".1"/>'
            '<stop offset=".75" stop-color="#bde0fe" stop-opacity=".3"/><stop offset=".93" stop-color="#cdb4db" '
            'stop-opacity=".7"/><stop offset="1" stop-color="#a2d2ff" stop-opacity=".95"/></radialGradient>')
    b = ['<circle cx="70" cy="200" r="44" fill="url(#bub)"/>',
         '<ellipse cx="55" cy="180" rx="11" ry="7" fill="#fff" opacity=".9" transform="rotate(-35 55 180)"/>',
         '<circle cx="200" cy="200" r="44" fill="none" stroke="#a2d2ff" stroke-width="4" stroke-dasharray="20 16" '
         'opacity=".9"/>']
    for a in range(0, 360, 45):
        r1, r2 = 52, 66
        ca, sa = math.cos(math.radians(a + 20)), math.sin(math.radians(a + 20))
        b.append(f'<line x1="{f(200 + r1 * ca)}" y1="{f(200 + r1 * sa)}" x2="{f(200 + r2 * ca)}" y2="{f(200 + r2 * sa)}" '
                 'stroke="#8ecae6" stroke-width="4" stroke-linecap="round"/>')
    for x, y, r in ((316, 220, 3), (334, 232, 2.5), (322, 248, 2), (342, 210, 2), (328, 262, 1.8)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#8ecae6"/>')
    b += ['<circle cx="330" cy="200" r="44" fill="none" stroke="#ced4da" stroke-width="2" stroke-dasharray="4 7"/>',
          arrow(120, 200, 146, 200, INK, 5, 12), arrow(254, 200, 280, 200, INK, 5, 12)]
    return svg(b, "#eef4ff", defs)


def depleted():
    b = [f'<rect x="60" y="140" width="250" height="120" rx="18" fill="#fff" stroke="{INK}" stroke-width="10"/>',
         f'<rect x="312" y="174" width="26" height="52" rx="6" fill="{INK}"/>']
    for i, x in enumerate(range(78, 300, 37)):
        if i == 0:
            b.append(f'<rect x="{x}" y="158" width="28" height="84" rx="5" fill="#e63946"/>')
        else:
            b.append(f'<rect x="{x}" y="158" width="28" height="84" rx="5" fill="none" stroke="#dee2e6" '
                     'stroke-width="3" stroke-dasharray="6 5"/>')
    b.append(arrow(185, 285, 185, 345, "#e63946", 6, 16))
    return svg(b, "#fff1f0")


def cell(x, y, r):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{r}" fill="#95d5b2" stroke="#2d6a4f" stroke-width="3"/>'
            f'<circle cx="{f(x + r * .15)}" cy="{f(y + r * .1)}" r="{f(r * .36)}" fill="#2d6a4f"/>'
            f'<circle cx="{f(x - r * .4)}" cy="{f(y - r * .4)}" r="{f(r * .15)}" fill="#fff" opacity=".7"/>')


def multiplying():
    b = [cell(55, 200, 30), cell(145, 165, 24), cell(145, 235, 24)]
    b += [cell(x, y, 18) for x in (221, 259) for y in (162, 238)]
    b += [cell(x, y, 13) for x in (322, 350) for y in (110, 165, 235, 290)]
    b += [arrow(92, 200, 116, 200, INK, 4, 11), arrow(175, 200, 197, 200, INK, 4, 11),
          arrow(283, 200, 302, 200, INK, 4, 11)]
    return svg(b, "#f3effa")


def obstructed():
    b = ['<rect y="150" width="400" height="250" fill="#80b918"/>',
         '<path d="M120 400 L188 150 H212 L280 400 Z" fill="#6c757d"/>']
    for y0, y1 in ((160, 172), (185, 200), (215, 235), (290, 318), (340, 375)):
        w0, w1 = 1 + (y0 - 150) * .02, 1 + (y1 - 150) * .02
        b.append(f'<polygon points="{f(200 - w0)},{y0} {f(200 + w0)},{y0} {f(200 + w1)},{y1} {f(200 - w1)},{y1}" fill="#fff"/>')
    b += [pine(40, 160, 40, "#2d6a4f"), pine(70, 158, 30, "#2d6a4f"), pine(345, 162, 45, "#2d6a4f"),
          '<path d="M78 268 L84 236 L92 248 L98 232 L106 246 L112 238 L114 270 Z" fill="#7f5539"/>',
          '<ellipse cx="200" cy="274" rx="105" ry="7" fill="#000" opacity=".2"/>'
          '<g transform="rotate(-6 200 255)"><rect x="105" y="244" width="200" height="24" rx="10" fill="#7f5539"/>'
          '<path d="M120 252 H180 M200 260 H260" stroke="#5c4033" stroke-width="3"/></g>',
          bush(318, 236, 30, "#386641", "#6a994e"), bush(350, 252, 26, "#386641", "#6a994e"),
          bush(330, 270, 20, "#386641", "#6a994e"),
          '<rect x="160" y="330" width="80" height="45" rx="10" fill="#457b9d"/>',
          '<rect x="172" y="312" width="56" height="26" rx="8" fill="#a8dadc"/>',
          '<rect x="164" y="340" width="16" height="8" rx="2" fill="#e63946"/>',
          '<rect x="220" y="340" width="16" height="8" rx="2" fill="#e63946"/>',
          f'<rect x="166" y="372" width="16" height="14" rx="3" fill="{INK}"/>',
          f'<rect x="218" y="372" width="16" height="14" rx="3" fill="{INK}"/>',
          '<rect x="306" y="300" width="5" height="50" fill="#adb5bd"/>',
          '<polygon points="308,272 330,308 286,308" fill="#ffd166" stroke="#e76f51" stroke-width="3" '
          'stroke-linejoin="round"/>',
          f'<rect x="306" y="284" width="4" height="13" fill="{INK}"/><circle cx="308" cy="302" r="2.3" fill="{INK}"/>']
    return svg(b, "#bde0fe")


def gear(cx, cy, R, teeth, rot, color):
    step = 360 / teeth
    r = R - 15
    pts = []
    for i in range(teeth):
        a = rot + i * step
        for frac, rad in ((0, r), (.12, R), (.38, R), (.5, r)):
            t = math.radians(a + frac * step)
            pts.append((cx + rad * math.cos(t), cy + rad * math.sin(t)))
        for k in range(1, 4):
            t = math.radians(a + (.5 + k * .125) * step)
            pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts) + " Z"
    return (f'<path d="{d}" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
            f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * .45)}" fill="#fff" stroke="{INK}" stroke-width="3"/>'
            f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * .15)}" fill="{INK}"/>')


def interdependent():
    big = (145, 225, 88, 12)
    th1 = -30
    d1 = big[2] + 62 - 16
    med = (big[0] + d1 * math.cos(math.radians(th1)), big[1] + d1 * math.sin(math.radians(th1)), 62, 9)
    th2 = 60
    d2 = 62 + 48 - 16
    small = (med[0] + d2 * math.cos(math.radians(th2)), med[1] + d2 * math.sin(math.radians(th2)), 48, 7)
    step = lambda g: 360 / g[3]
    rot_big = th1 - .25 * step(big)
    rot_med = th1 + 180 - .75 * step(med)
    p = ((th2 - rot_med) / step(med) - .25) % 1  # med's phase at the contact (0 = tooth centre)
    rot_small = th2 + 180 - .25 * step(small) - ((.5 - p) % 1) * step(small)
    b = [gear(*big, rot_big, "#2a9d8f"), gear(*med, rot_med, "#e9c46a"), gear(*small, rot_small, "#e76f51"),
         arc_arrow(big[0], big[1], big[2] + 18, 120, 200, INK, 5),
         arc_arrow(med[0], med[1], med[2] + 18, -60, -140, INK, 5),
         arc_arrow(small[0], small[1], small[2] + 18, 10, 80, INK, 5)]
    return svg(b, "#f1faee")


def erratic():
    path = ("M50 335 L105 255 Q140 200 90 195 Q40 190 75 150 L170 232 L150 125 C 150 60, 250 80, 215 140 "
            "C 190 185, 260 260, 205 285 L300 250 L255 140 L340 175 L308 80")
    b = [f'<path d="{path}" fill="none" stroke="#6c757d" stroke-width="4" stroke-dasharray="10 8" '
         'stroke-linecap="round" stroke-linejoin="round"/>',
         '<circle cx="50" cy="335" r="8" fill="#2a9d8f"/>',
         '<g transform="translate(316 62) rotate(-35)">'
         '<ellipse cx="-4" cy="-12" rx="12" ry="7" fill="#caf0f8" stroke="#8ecae6" stroke-width="2" '
         'transform="rotate(-25 -4 -12)"/>'
         '<ellipse cx="6" cy="-12" rx="12" ry="7" fill="#caf0f8" stroke="#8ecae6" stroke-width="2" '
         'transform="rotate(25 6 -12)"/>'
         f'<ellipse cx="0" cy="0" rx="14" ry="8" fill="{INK}"/><circle cx="14" cy="0" r="6" fill="{INK}"/>'
         '<circle cx="16" cy="-2" r="2.5" fill="#e63946"/></g>',
         '<path d="M345 40 l12 -6 M350 58 l14 0 M345 76 l12 6" stroke="#adb5bd" stroke-width="3" '
         'stroke-linecap="round"/>']
    return svg(b, "#fefae0")


def tranquil():
    defs = ('<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a2d2ff"/>'
            '<stop offset="1" stop-color="#ffd6a5"/></linearGradient>'
            '<linearGradient id="lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cde4f5"/>'
            '<stop offset="1" stop-color="#7fb7d9"/></linearGradient>')
    hills = ('<circle cx="290" cy="178" r="30" fill="#fff1d0"/>'
             '<path d="M0 205 L70 140 L130 185 L200 118 L270 172 L330 128 L400 190 V212 H0Z" fill="#9d8189"/>'
             '<path d="M0 212 L60 182 L120 200 L180 168 L250 205 L310 178 L400 210 V212 H0Z" fill="#6d597a"/>')
    b = ['<rect width="400" height="212" fill="url(#sky)"/>', hills,
         '<rect y="210" width="400" height="190" fill="url(#lake)"/>',
         f'<g transform="translate(0 422) scale(1 -1)" opacity=".35">{hills}</g>',
         '<path d="M60 250 H120 M250 262 H340 M90 330 H170 M230 350 H300 M40 300 H80" stroke="#fff" '
         'stroke-width="2.5" stroke-linecap="round" opacity=".7"/>',
         '<path d="M115 288 H178 Q171 302 154 304 H136 Q120 302 115 288 Z" fill="#6d4c41"/>',
         '<line x1="146" y1="288" x2="146" y2="276" stroke="#6d4c41" stroke-width="3"/>',
         '<ellipse cx="146" cy="310" rx="36" ry="4" fill="#5e548e" opacity=".25"/>',
         '<path d="M80 80 q6 -6 12 0 q6 -6 12 0 M120 60 q5 -5 10 0 q5 -5 10 0" fill="none" stroke="#6d597a" '
         'stroke-width="2.5" stroke-linecap="round"/>',
         '<path d="M360 400 Q356 360 350 330 M372 400 Q372 355 378 322 M384 400 Q386 368 394 345" fill="none" '
         'stroke="#588157" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#a2d2ff", defs)


def withstand():
    rnd = random.Random(9)
    defs = ('<linearGradient id="storm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22223b"/>'
            '<stop offset="1" stop-color="#5c677d"/></linearGradient>'
            '<clipPath id="tower"><path d="M215 300 L228 128 H272 L285 300 Z"/></clipPath>')
    b = ['<rect width="400" height="400" fill="url(#storm)"/>',
         '<polygon points="250,108 0,40 0,150" fill="#fff3b0" opacity=".3"/>',
         '<polygon points="250,108 400,60 400,160" fill="#fff3b0" opacity=".3"/>']
    for _ in range(60):
        x, y = rnd.uniform(0, 420), rnd.uniform(0, 300)
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 8)}" y2="{f(y + 18)}" stroke="#adb5bd" stroke-width="1.5" '
                 'opacity=".5"/>')
    b += ['<ellipse cx="60" cy="20" rx="90" ry="35" fill="#1b1b2f"/><ellipse cx="190" cy="10" rx="80" ry="30" '
          'fill="#1b1b2f"/><ellipse cx="340" cy="22" rx="100" ry="36" fill="#1b1b2f"/>',
          '<polygon points="70,60 52,100 66,100 50,140 84,92 70,92 86,60" fill="#ffd166"/>',
          '<path d="M215 300 L228 128 H272 L285 300 Z" fill="#fff"/>',
          '<g clip-path="url(#tower)"><rect x="200" y="160" width="100" height="26" fill="#d62828"/>'
          '<rect x="200" y="225" width="100" height="26" fill="#d62828"/></g>',
          '<rect x="241" y="270" width="18" height="30" rx="8" fill="#6d4c41"/>',
          f'<rect x="212" y="120" width="76" height="9" fill="{INK}"/>',
          '<rect x="226" y="94" width="48" height="27" fill="#ffd166"/>',
          f'<path d="M226 94 V121 M242 94 V121 M258 94 V121 M274 94 V121" stroke="{INK}" stroke-width="3"/>',
          '<path d="M218 95 L250 66 L282 95 Z" fill="#d62828"/>',
          '<path d="M178 360 Q182 300 212 296 L300 296 Q345 305 350 360 Z" fill="#495057"/>',
          '<path d="M0 290 Q55 215 130 245 Q165 260 158 292 Q138 302 124 330 L0 360 Z" fill="#457b9d"/>',
          '<path d="M0 290 Q55 215 130 245 Q165 260 158 292" fill="none" stroke="#fff" stroke-width="6" '
          'stroke-linecap="round"/>',
          '<path d="M400 300 Q350 240 310 268 Q292 282 300 300" fill="#457b9d"/>',
          '<path d="M400 300 Q350 240 310 268 Q292 282 300 300" fill="none" stroke="#fff" stroke-width="5" '
          'stroke-linecap="round"/>']
    for x, y, r in ((168, 280, 6), (178, 262, 4), (160, 262, 3.5), (186, 248, 3), (302, 276, 5), (292, 258, 3.5),
                    (312, 255, 3)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff"/>')
    b += ['<path d="M0 340 Q50 320 100 340 T200 340 T300 340 T400 340 V400 H0Z" fill="#1d3557"/>',
          '<path d="M0 365 Q50 348 100 365 T200 365 T300 365 T400 365 V400 H0Z" fill="#14213d"/>']
    return svg(b, "#22223b", defs)


PICTURES = {
    "dormant": dormant,
    "converge": converge,
    "diverge": diverge,
    "fragile": fragile,
    "magnify": magnify,
    "amplify": amplify,
    "hoard": hoard,
    "hibernation": hibernation,
    "fluctuate": fluctuate,
    "accumulate": accumulate,
    "abundant": abundant,
    "meager": meager,
    "intersect": intersect,
    "isolate": isolate,
    "immense": immense,
    "dispersed": dispersed,
    "dissolve": dissolve,
    "constrict": constrict,
    "homogeneous": homogeneous,
    "heterogeneous": heterogeneous,
    "transparent": transparent,
    "conspicuous": conspicuous,
    "ephemeral": ephemeral,
    "depleted": depleted,
    "multiplying": multiplying,
    "obstructed": obstructed,
    "interdependent": interdependent,
    "erratic": erratic,
    "tranquil": tranquil,
    "withstand": withstand,
}
