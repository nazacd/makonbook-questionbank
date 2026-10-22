"""Batch 3: drawings 81-130 (each function returns one SVG; PICTURES maps word -> function).

The figures and small shapes (person, face, limb, ...) come from batch_02.py.
"""

import math
import random

from batch_02 import SKIN, heart, limb, person, shadow, sheep, sparkle, star
from common import INK, arrow, bush, carrow, f, pine, svg


def curls(x, y, s, color, long=True):
    """Curly hair for person(..., style="none") at the same x, y, s: drawn before the figure."""
    pts = [(0, -204), (-14, -200), (14, -200), (-24, -190), (24, -190), (-28, -176), (28, -176)]
    if long:
        pts += [(-30, -162), (30, -162), (-28, -148), (28, -148)]
    return (f'<g transform="translate({f(x)} {f(y)}) scale({s})">'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="11" fill="{color}"/>' for cx, cy in pts) + '</g>')


def fringe(color):
    """The curls over the forehead, for person(..., extra=fringe(color))."""
    return "".join(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{color}"/>' for cx, cy in
                   ((-14, -196), (0, -199), (14, -196), (-21, -186), (21, -186)))


def bicycle(color):
    """A bike seen from the side, in local coordinates: wheels touch the ground at y=0."""
    return (f'<circle cx="-45" cy="-30" r="28" fill="none" stroke="{INK}" stroke-width="6"/>'
            f'<circle cx="45" cy="-30" r="28" fill="none" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M-45 -30 L0 -32 L-15 -72 Z M0 -32 L32 -76 L-15 -72 M32 -76 L45 -30" fill="none" stroke="{color}" '
            'stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M32 -76 L34 -88 L44 -88" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
            f'<rect x="-26" y="-80" width="22" height="7" rx="3" fill="{INK}"/>')


def cyclist(x, y, bike, shirt, skin, helmet, look_down=False, k=1.0):
    eye_y = -134 if look_down else -139
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">' + bicycle(bike)
            + limb(((-15, -82), (12, -58), (4, -34)), INK, 11)
            + limb(((-15, -82), (-4, -52), (-6, -30)), "#495057", 11)
            + limb(((-15, -82), (16, -120)), shirt, 18)
            + limb(((16, -118), (38, -92)), shirt, 10) + f'<circle cx="40" cy="-89" r="6" fill="{skin}"/>'
            + f'<circle cx="30" cy="-138" r="16" fill="{skin}"/>'
            f'<path d="M12 -146 Q14 -164 32 -162 Q46 -160 46 -146 Z" fill="{helmet}"/>'
            f'<circle cx="38" cy="{eye_y}" r="3.2" fill="{INK}"/>'
            f'<path d="M31 -144 L44 -139" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M34 -128 H42" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/></g>')


# ---------------------------------------------------------------------------------------------

def fruitless():
    rnd = random.Random(4)
    b = ['<rect width="400" height="110" fill="#a8dadc"/>', '<circle cx="330" cy="50" r="28" fill="#ffd166"/>',
         '<path d="M0 110 Q100 100 200 110 T400 108 V130 H0Z" fill="#4895ef"/>',
         '<rect y="126" width="400" height="274" fill="#f1dca7"/>']
    for x, y in ((60, 180), (170, 160), (300, 170), (80, 290), (330, 270), (180, 360), (40, 370), (350, 360)):
        b += [f'<ellipse cx="{x + 22}" cy="{y - 6}" rx="20" ry="9" fill="#e0c48c"/>',
              f'<ellipse cx="{x}" cy="{y}" rx="26" ry="11" fill="#9c6b3c"/>',
              f'<ellipse cx="{x}" cy="{y + 2}" rx="20" ry="7" fill="#7f5539"/>']
    b += [shadow(206, 344, 44),
          person(206, 342, 1.0, SKIN[2], "#e76f51", "#457b9d", "#1b1b1b", "cap", mood="frown",
                 brows="M-14 -186 L-4 -190 M4 -190 L14 -186", larm=((-10, 40), (-14, 76)),
                 rarm=((22, 30), (40, 54))),
          # the metal detector, swept over the sand with nothing found
          '<line x1="250" y1="250" x2="296" y2="330" stroke="#6c757d" stroke-width="6" stroke-linecap="round"/>',
          '<ellipse cx="304" cy="334" rx="26" ry="9" fill="#495057"/>',
          '<rect x="246" y="240" width="14" height="20" rx="4" fill="#343a40"/>',
          '<path d="M180 128 Q174 140 180 144 Q186 140 180 128 Z" fill="#8ecae6"/>',
          '<path d="M236 126 Q230 138 236 142 Q242 138 236 126 Z" fill="#8ecae6"/>']
    return svg(b, "#f1dca7")


def precursors():
    b = ['<rect y="290" width="400" height="110" fill="#e9d8c4"/>']
    # abacus
    b += ['<rect x="16" y="170" width="96" height="114" rx="6" fill="#7f5539"/>',
          '<rect x="26" y="180" width="76" height="94" fill="#fdf0d5"/>']
    for k, y in enumerate((196, 220, 244, 266)):
        b.append(f'<line x1="26" y1="{y}" x2="102" y2="{y}" stroke="#7f5539" stroke-width="3"/>')
        for j in range(5):
            x = 36 + j * 9 + (24 if j >= 3 - k % 2 else 0)
            b.append(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="7" fill="{("#e63946", "#2a9d8f", "#e9c46a", "#457b9d")[k]}"/>')
    # mechanical calculator with a crank
    b += ['<rect x="150" y="190" width="100" height="94" rx="8" fill="#6c757d"/>',
          '<rect x="162" y="170" width="70" height="26" rx="4" fill="#adb5bd"/>',
          '<rect x="170" y="176" width="54" height="12" fill="#fff"/>']
    for r in range(3):
        for c in range(4):
            b.append(f'<circle cx="{170 + c * 20}" cy="{214 + r * 22}" r="7" fill="#e9ecef"/>')
    b += ['<path d="M250 230 H266 V206 H276" fill="none" stroke="#495057" stroke-width="6" stroke-linecap="round" '
          'stroke-linejoin="round"/>', '<circle cx="278" cy="206" r="6" fill="#e63946"/>',
          # laptop
          '<rect x="300" y="186" width="84" height="64" rx="5" fill="#343a40"/>',
          '<rect x="306" y="192" width="72" height="52" fill="#4895ef"/>',
          '<path d="M310 236 L330 214 L344 226 L374 200" fill="none" stroke="#caf0f8" stroke-width="4"/>',
          '<path d="M288 252 H396 L388 264 H296 Z" fill="#adb5bd"/>',
          arrow(118, 226, 144, 226, INK, 5, 13), arrow(282, 226, 296, 226, INK, 5, 11),
          '<line x1="30" y1="330" x2="370" y2="330" stroke="#8d6e63" stroke-width="4"/>']
    for x in (64, 200, 342):
        b.append(f'<circle cx="{x}" cy="330" r="9" fill="#8d6e63"/>')
    b.append(arrow(330, 330, 382, 330, "#8d6e63", 4, 12))
    return svg(b, "#fdf6ec")


def bypassed():
    rnd = random.Random(7)
    b = ['<path d="M0 200 H400" stroke="#ced4da" stroke-width="16"/>',
         '<path d="M0 200 H400" stroke="#fff" stroke-width="2" stroke-dasharray="10 10"/>']
    # the town the old road runs through
    for _ in range(30):
        a, d = rnd.uniform(0, 2 * math.pi), rnd.uniform(0, 70)
        x, y = 200 + d * math.cos(a), 200 + d * .8 * math.sin(a)
        if abs(y - 200) < 14:
            continue
        c = rnd.choice(("#e76f51", "#f4a261", "#e9c46a", "#bc6c25"))
        b.append(f'<rect x="{f(x - 11)}" y="{f(y - 9)}" width="22" height="18" fill="{c}"/>'
                 f'<line x1="{f(x - 11)}" y1="{f(y)}" x2="{f(x + 11)}" y2="{f(y)}" stroke="#7f5539" stroke-width="2"/>')
    hw = "M-10 330 C 90 330, 90 360, 200 360 C 310 360, 310 330, 410 330"
    hw = "M-10 300 C 60 300, 60 370, 200 370 C 340 370, 340 300, 410 300"
    b += [f'<path d="{hw}" fill="none" stroke="#495057" stroke-width="40"/>',
          f'<path d="{hw}" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="14 12"/>',
          '<path d="M30 300 Q20 250 0 230 M370 300 Q380 250 400 230" fill="none" stroke="#495057" stroke-width="22"/>']
    for t, c in ((.12, "#e63946"), (.3, "#4895ef"), (.5, "#ffd166"), (.68, "#2a9d8f"), (.86, "#e76f51")):
        # points along the two cubic halves
        if t < .5:
            u = t * 2
            p0, p1, p2, p3 = (-10, 300), (60, 300), (60, 370), (200, 370)
        else:
            u = (t - .5) * 2
            p0, p1, p2, p3 = (200, 370), (340, 370), (340, 300), (410, 300)
        x = (1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0] + 3 * (1 - u) * u * u * p2[0] + u ** 3 * p3[0]
        y = (1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1] + 3 * (1 - u) * u * u * p2[1] + u ** 3 * p3[1]
        dx = 3 * (1 - u) ** 2 * (p1[0] - p0[0]) + 6 * (1 - u) * u * (p2[0] - p1[0]) + 3 * u * u * (p3[0] - p2[0])
        dy = 3 * (1 - u) ** 2 * (p1[1] - p0[1]) + 6 * (1 - u) * u * (p2[1] - p1[1]) + 3 * u * u * (p3[1] - p2[1])
        a = math.degrees(math.atan2(dy, dx))
        b.append(f'<rect x="{f(x - 13)}" y="{f(y - 8)}" width="26" height="16" rx="4" fill="{c}" '
                 f'transform="rotate({f(a)} {f(x)} {f(y)})"/>')
    b += [bush(40, 80, 20), bush(360, 70, 24), bush(330, 130, 16), bush(70, 140, 14),
          carrow(60, 270, 200, 330, 340, 270, "#e76f51", 5, 15)]
    return svg(b, "#a7c957")


def ignore():
    headphones = ('<path d="M-26 -178 Q-26 -212 0 -212 Q26 -212 26 -178" fill="none" stroke="#343a40" stroke-width="6"/>'
                  '<rect x="-32" y="-188" width="12" height="22" rx="5" fill="#e63946"/>'
                  '<rect x="20" y="-188" width="12" height="22" rx="5" fill="#e63946"/>'
                  '<rect x="-14" y="-132" width="28" height="40" rx="5" fill="#343a40"/>'
                  '<rect x="-10" y="-128" width="20" height="30" fill="#4895ef"/>')
    b = ['<rect y="340" width="400" height="60" fill="#dee2e6"/>', shadow(130, 344, 40), shadow(290, 344, 40),
         person(130, 342, 1.15, SKIN[0], "#2a9d8f", "#264653", "#7f5539", "short", mood="down",
                larm=((-6, 30), (8, 40)), rarm=((6, 30), (-8, 40)), extra=headphones),
         person(290, 342, 1.15, SKIN[2], "#f4a261", "#457b9d", "#1b1b1b", "bun", mood="wide",
                larm=((-30, -26), (-34, -66)), rarm=((12, 40), (16, 76)),
                brows="M-14 -192 Q-8 -198 -2 -193 M2 -193 Q8 -198 14 -192"),
         '<path d="M230 80 q-10 -8 -8 -20 M214 88 q-14 -6 -16 -18 M268 74 q4 -12 14 -16" fill="none" stroke="#6c757d" '
         'stroke-width="3" stroke-linecap="round"/>']
    for x, y in ((70, 110), (54, 140)):
        b.append(f'<path d="M{x} {y} v-22 l12 -4 v22" fill="none" stroke="#6c757d" stroke-width="3"/>'
                 f'<ellipse cx="{x - 4}" cy="{y}" rx="5" ry="4" fill="#6c757d"/>'
                 f'<ellipse cx="{x + 8}" cy="{y - 4}" rx="5" ry="4" fill="#6c757d"/>')
    return svg(b, "#f8f9fa")


def source():
    b = ['<polygon points="0,260 90,90 160,170 230,60 330,180 400,120 400,400 0,400" fill="#9a8c98"/>',
         '<polygon points="230,60 262,98 246,104 230,92 214,106 204,96" fill="#fff"/>',
         '<polygon points="90,90 112,132 100,128 90,118 80,130 74,122" fill="#fff"/>',
         '<path d="M0 300 Q200 250 400 290 V400 H0Z" fill="#a7c957"/>',
         '<path d="M0 340 Q200 300 400 330 V400 H0Z" fill="#90be6d"/>']
    stream = [((170, 166), (180, 200), 4), ((180, 200), (150, 240), 7), ((150, 240), (190, 290), 11),
              ((190, 290), (140, 340), 18), ((140, 340), (210, 410), 30)]
    for (x1, y1), (x2, y2), w in stream:
        b.append(f'<path d="M{x1} {y1} Q{(x1 + x2) / 2 + 20} {(y1 + y2) / 2} {x2} {y2}" fill="none" stroke="#4895ef" '
                 f'stroke-width="{w}" stroke-linecap="round"/>')
    b += ['<ellipse cx="166" cy="166" rx="34" ry="18" fill="#6c757d"/>', '<ellipse cx="150" cy="160" rx="16" ry="12" fill="#adb5bd"/>',
          '<ellipse cx="190" cy="160" rx="16" ry="11" fill="#adb5bd"/>',
          '<ellipse cx="170" cy="168" rx="12" ry="6" fill="#4895ef"/>']
    for x, y, r in ((166, 150, 5), (176, 140, 4), (160, 132, 3.5), (172, 124, 3)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#4895ef" stroke-width="2.5"/>')
    b += [pine(60, 330, 60), pine(300, 320, 70), pine(340, 340, 50), pine(30, 360, 40),
          sparkle(206, 130, 10, "#fff"), '<circle cx="340" cy="50" r="26" fill="#ffd166"/>']
    return svg(b, "#cfe8f3")


def rejected():
    b = ['<g transform="rotate(-8 200 210)">',
         '<rect x="80" y="130" width="240" height="160" rx="8" fill="#fff" stroke="#ced4da" stroke-width="4"/>',
         '<path d="M84 136 L200 222 L316 136" fill="none" stroke="#ced4da" stroke-width="4"/>',
         '<rect x="270" y="146" width="34" height="40" fill="#a8dadc" stroke="#457b9d" stroke-width="2" '
         'stroke-dasharray="4 3"/>',
         '<path d="M110 240 h80 M110 256 h60" stroke="#adb5bd" stroke-width="5" stroke-linecap="round"/>',
         '<circle cx="232" cy="232" r="48" fill="none" stroke="#e63946" stroke-width="7" opacity=".9"/>',
         '<path d="M208 208 L256 256 M256 208 L208 256" stroke="#e63946" stroke-width="12" stroke-linecap="round" '
         'opacity=".9"/></g>',
         carrow(340, 110, 380, 30, 260, 50, "#e76f51", 7, 18)]
    return svg(b, "#fff1f0")


def teddy(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<circle cx="-14" cy="-40" r="8" fill="#9c6644"/><circle cx="14" cy="-40" r="8" fill="#9c6644"/>'
            '<ellipse cx="0" cy="0" rx="20" ry="22" fill="#9c6644"/>'
            '<circle cx="0" cy="-30" r="17" fill="#9c6644"/>'
            '<ellipse cx="0" cy="-25" rx="8" ry="6" fill="#ddb892"/>'
            f'<circle cx="-6" cy="-34" r="2.5" fill="{INK}"/><circle cx="6" cy="-34" r="2.5" fill="{INK}"/>'
            f'<circle cx="0" cy="-27" r="2.5" fill="{INK}"/><ellipse cx="0" cy="4" rx="11" ry="12" fill="#ddb892"/></g>')


def appeased():
    b = ['<rect y="320" width="400" height="80" fill="#e9d8c4"/>',
         '<rect x="196" y="40" width="8" height="280" fill="#fff" opacity=".7"/>',
         shadow(100, 324, 34), shadow(300, 324, 34),
         person(100, 322, .9, SKIN[1], "#4895ef", "#264653", "#7f5539", "short", mood="cry",
                larm=((-24, -6), (-40, -30)), rarm=((24, -6), (40, -30)),
                brows="M-14 -188 L-4 -192 M4 -192 L14 -188"),
         '<path d="M40 110 l-12 -6 M48 92 l-6 -12 M152 92 l6 -12 M160 110 l12 -6" stroke="#e63946" stroke-width="4" '
         'stroke-linecap="round"/>',
         person(300, 322, .9, SKIN[1], "#4895ef", "#264653", "#7f5539", "short", mood="closed",
                larm=((-14, 34), (6, 54)), rarm=((14, 34), (-6, 54))),
         teddy(300, 254, 1.1),
         f'<circle cx="286" cy="262" r="8" fill="{SKIN[1]}"/><circle cx="314" cy="262" r="8" fill="{SKIN[1]}"/>',
         heart(350, 110, 13), heart(250, 96, 10, "#f4a261"),
         arrow(176, 200, 222, 200, INK, 6, 16)]
    return svg(b, "#fdf6ec")


def inherited():
    red = "#d9480f"
    b = ['<rect x="16" y="40" width="368" height="300" rx="8" fill="#c9a227"/>',
         '<rect x="28" y="52" width="344" height="276" fill="#fdf0d5"/>',
         '<rect x="28" y="290" width="344" height="38" fill="#e9d8c4"/>']
    people = ((90, 330, 1.05, "#7f5539", True), (210, 330, 1.05, "#457b9d", True), (320, 330, .78, "#e9c46a", True))
    moods = ("closed", "smile", "grin")
    for (x, y, s, shirt, lng), mood, sk in zip(people, moods, (SKIN[0], SKIN[0], SKIN[0])):
        extra = fringe(red)
        if mood == "closed":
            extra += (f'<circle cx="-8" cy="-179" r="7" fill="none" stroke="{INK}" stroke-width="2"/>'
                      f'<circle cx="8" cy="-179" r="7" fill="none" stroke="{INK}" stroke-width="2"/>')
        b += [curls(x, y, s, red, lng),
              person(x, y, s, sk, shirt, "#264653", red, "none", mood=mood, extra=extra)]
    b += [carrow(110, 100, 150, 70, 186, 96, "#2a9d8f", 4, 12), carrow(232, 100, 270, 70, 304, 140, "#2a9d8f", 4, 12)]
    return svg(b, "#f2e9e4")


def rival():
    b = ['<rect y="170" width="400" height="230" fill="#adb5bd"/>',
         '<path d="M0 290 H400" stroke="#fff" stroke-width="4" stroke-dasharray="26 18"/>',
         bush(40, 166, 22), bush(370, 162, 26), bush(300, 168, 16), bush(120, 170, 14)]
    for y in (190, 220, 330, 360):
        b.append(f'<line x1="10" y1="{y}" x2="60" y2="{y}" stroke="#fff" stroke-width="5" stroke-linecap="round" '
                 'opacity=".8"/>')
    b += [shadow(214, 262, 96, 6), cyclist(214, 258, "#e63946", "#e63946", SKIN[1], "#9d0208", True, 1.35),
          shadow(200, 384, 96, 6), cyclist(200, 380, "#2a9d8f", "#2a9d8f", SKIN[3], "#264653", False, 1.35),
          '<polygon points="300,150 286,178 300,176 288,204 314,170 300,172 312,150" fill="#ffd166"/>']
    return svg(b, "#e3f2fd")


def worried():
    rnd = random.Random(1)
    b = ['<rect width="400" height="200" fill="#adb5bd"/>',
         '<ellipse cx="120" cy="50" rx="130" ry="44" fill="#495057"/><ellipse cx="300" cy="60" rx="120" ry="40" '
         'fill="#6c757d"/><ellipse cx="220" cy="30" rx="100" ry="34" fill="#495057"/>',
         '<polygon points="300,90 284,128 298,128 286,160 314,118 300,118 312,90" fill="#ffd166"/>']
    for _ in range(26):
        x, y = rnd.uniform(0, 400), rnd.uniform(90, 190)
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 5)}" y2="{f(y + 14)}" stroke="#457b9d" stroke-width="2.5" '
                 'stroke-linecap="round"/>')
    b += ['<rect y="200" width="400" height="200" fill="#e9c46a"/>']
    for k, y in enumerate(range(212, 400, 22)):
        b.append(f'<path d="M0 {y} H400" stroke="#d4a373" stroke-width="3"/>')
        for x in range(10 + (k % 2) * 12, 400, 24):
            b.append(f'<path d="M{x} {y} v-12" stroke="#c9a227" stroke-width="3" stroke-linecap="round"/>')
    hat = ('<ellipse cx="0" cy="-196" rx="38" ry="8" fill="#e9c46a" stroke="#c9a227" stroke-width="2"/>'
           '<path d="M-20 -196 Q-20 -222 0 -222 Q20 -222 20 -196 Z" fill="#e9c46a" stroke="#c9a227" stroke-width="2"/>'
           '<rect x="-20" y="-204" width="40" height="6" fill="#e76f51"/>')
    b += [shadow(200, 384, 50),
          person(200, 384, 1.25, SKIN[1], "#457b9d", "#7f5539", "#5c4033", "none", mood="frown",
                 brows="M-14 -186 L-4 -191 M4 -191 L14 -186", larm=((-18, 26), (-4, -16)),
                 rarm=((12, 40), (16, 76)), extra=hat),
          '<path d="M232 152 Q226 164 232 168 Q238 164 232 152 Z" fill="#8ecae6"/>']
    return svg(b, "#adb5bd")



def dog(x, y, k=1.0, eyes="open", flip=False, leash=False):
    """A sitting dog facing right, paws at (x, y)."""
    sgn = -1 if flip else 1
    eye = {"open": f'<circle cx="34" cy="-118" r="5" fill="{INK}"/><circle cx="35.5" cy="-119.5" r="1.6" fill="#fff"/>',
           "squint": f'<path d="M26 -118 H42" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
                     f'<path d="M24 -128 L42 -124" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'}[eyes]
    lead = ('<path d="M66 -96 Q74 -60 50 -30 Q30 0 -10 4" fill="none" stroke="#e63946" stroke-width="6" '
            'stroke-linecap="round"/><rect x="56" y="-102" width="16" height="8" rx="3" fill="#e63946"/>') if leash else ""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sgn * k)} {k})">'
            '<ellipse cx="-4" cy="2" rx="50" ry="7" fill="#000" opacity=".12"/>'
            '<path d="M-30 -14 Q-64 -30 -60 -66" fill="none" stroke="#c08552" stroke-width="10" stroke-linecap="round"/>'
            '<ellipse cx="-6" cy="-40" rx="36" ry="44" fill="#c08552"/>'
            '<ellipse cx="4" cy="-40" rx="18" ry="30" fill="#e6ccb2"/>'
            '<rect x="0" y="-36" width="14" height="38" rx="7" fill="#c08552"/>'
            '<rect x="18" y="-36" width="14" height="38" rx="7" fill="#c08552"/>'
            '<circle cx="22" cy="-112" r="32" fill="#c08552"/>'
            '<ellipse cx="54" cy="-100" rx="20" ry="14" fill="#e6ccb2"/>'
            f'<circle cx="70" cy="-104" r="7" fill="{INK}"/>'
            f'<path d="M58 -90 Q64 -86 70 -90" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>'
            + eye + lead +
            '<path d="M2 -136 Q-14 -160 -4 -170 Q8 -150 14 -138 Z" fill="#7f5539"/></g>')


def create():
    b = ['<circle cx="200" cy="160" r="150" fill="#fde2c8"/>',
         '<rect x="60" y="320" width="280" height="80" fill="#8d6e63"/>',
         '<ellipse cx="200" cy="300" rx="130" ry="30" fill="#6c757d"/>',
         '<ellipse cx="200" cy="292" rx="130" ry="30" fill="#adb5bd"/>',
         '<path d="M90 314 A130 30 0 0 0 150 320" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>',
         # the vase taking shape
         '<path d="M150 292 Q140 240 172 214 Q182 204 178 170 H222 Q218 204 228 214 Q260 240 250 292 Z" fill="#c8743a"/>',
         '<ellipse cx="200" cy="170" rx="22" ry="6" fill="#9c4a2f"/>',
         '<path d="M168 280 Q158 246 182 222" fill="none" stroke="#e09f6b" stroke-width="5" stroke-linecap="round"/>',
         # the potter's hands
         f'<path d="M60 230 Q120 236 146 248" fill="none" stroke="#457b9d" stroke-width="30" stroke-linecap="round"/>',
         f'<ellipse cx="156" cy="250" rx="20" ry="26" fill="{SKIN[1]}"/>',
         f'<path d="M340 230 Q280 236 254 248" fill="none" stroke="#457b9d" stroke-width="30" stroke-linecap="round"/>',
         f'<ellipse cx="244" cy="250" rx="20" ry="26" fill="{SKIN[1]}"/>',
         '<path d="M70 330 Q200 372 330 330" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="12 10" '
         'opacity=".7"/>',
         arrow(300, 348, 330, 330, "#fff", 4, 12),
         sparkle(110, 120, 12, "#ffd166"), sparkle(290, 100, 10, "#ffd166"), sparkle(250, 150, 7, "#ffd166")]
    return svg([x for x in b if x], "#fff8f0")


def suspicious():
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>',
         '<circle cx="330" cy="60" r="26" fill="#fefae0"/>']
    for x in range(10, 400, 36):
        b.append(f'<path d="M{x} 300 V200 L{x + 12} 186 L{x + 24} 200 V300 Z" fill="#e6ccb2"/>')
    b += ['<rect y="222" width="400" height="10" fill="#d4a373"/><rect y="270" width="400" height="10" fill="#d4a373"/>',
          shadow(270, 344, 40),
          person(270, 342, 1.0, SKIN[0], "#264653", "#343a40", "#1b1b1b", "cap", mood="side", tiptoe=True,
                 larm=((-14, 34), (-30, 58)), rarm=((16, -10), (8, -30)),
                 lleg=((-14, 40), (-26, 80)), rleg=((10, 40), (24, 80))),
          '<path d="M260 120 Q246 70 300 72 Q350 76 336 132 Q320 150 280 146 Z" fill="#b08968"/>',
          '<path d="M290 72 l-6 -12 l14 6" fill="none" stroke="#7f5539" stroke-width="4"/>',
          dog(90, 360, 1.15, "squint"),
          '<path d="M178 200 l14 -8 M184 216 h16" stroke="#6c757d" stroke-width="3" stroke-linecap="round"/>']
    return svg(b, "#3d405b")


def determined():
    bandage = ('<rect x="2" y="-58" width="26" height="16" rx="3" fill="#fff" transform="rotate(10 15 -50)"/>'
               '<path d="M6 -52 H24" stroke="#dee2e6" stroke-width="3" transform="rotate(10 15 -50)"/>')
    b = ['<rect y="320" width="400" height="80" fill="#e76f51"/>',
         '<path d="M0 346 H400 M0 374 H400" stroke="#fff" stroke-width="3" opacity=".6"/>',
         '<rect x="350" y="110" width="10" height="220" fill="#adb5bd"/>',
         '<path d="M355 140 Q330 150 300 146" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>',
         '<rect x="300" y="300" width="8" height="40" fill="#fff"/>',
         '<path d="M30 160 h50 M20 190 h60 M36 220 h40" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/>',
         shadow(190, 342, 40),
         person(190, 340, 1.2, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "short", mood="grin", rot=8,
                brows="M-15 -191 L-3 -186 M3 -186 L15 -191", larm=((-26, 20), (-30, -8)), rarm=((24, 26), (36, 50)),
                lleg=((-6, 44), (-20, 86)), rleg=((14, 40), (24, 80)), extra=bandage),
         '<path d="M136 120 Q130 132 136 136 Q142 132 136 120 Z" fill="#8ecae6"/>',
         '<path d="M250 100 Q244 112 250 116 Q256 112 250 100 Z" fill="#8ecae6"/>',
         arrow(240, 300, 290, 300, INK, 6, 16)]
    return svg(b, "#eaf4f4")


def thumbs_up(x, y, k=1.0, skin=SKIN[1]):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            f'<rect x="-14" y="-10" width="30" height="30" rx="9" fill="{skin}"/>'
            f'<rect x="-12" y="-34" width="12" height="30" rx="6" fill="{skin}"/>'
            '<path d="M2 0 H14 M2 8 H14" stroke="#c68642" stroke-width="2" opacity=".6"/></g>')


def praised():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         '<rect x="40" y="30" width="200" height="120" rx="6" fill="#2d6a4f"/>',
         '<rect x="34" y="24" width="212" height="132" rx="8" fill="none" stroke="#9c6b3c" stroke-width="10"/>',
         '<path d="M70 70 q20 -20 40 0 t40 0 M70 110 h90" fill="none" stroke="#fff" stroke-width="4" opacity=".7"/>',
         shadow(120, 334, 44), shadow(290, 334, 34),
         person(120, 332, 1.1, SKIN[1], "#e76f51", "#264653", "#5c4033", "bun", mood="smile",
                larm=((-12, 40), (-14, 76)), rarm=((34, -6), (60, -20))),
         thumbs_up(196, 172, 1.4),
         person(290, 332, .85, SKIN[3], "#4895ef", "#457b9d", "#1b1b1b", "short", mood="grin",
                larm=((-16, 30), (-18, 62)), rarm=((16, 30), (18, 62))),
         '<g transform="rotate(-4 290 238)"><rect x="248" y="204" width="84" height="68" rx="3" fill="#fff"/>'
         '<path d="M258 252 h44 M258 262 h60" stroke="#adb5bd" stroke-width="4"/></g>',
         star(290, 228, 17, "#ffd166"),
         f'<circle cx="256" cy="262" r="7.5" fill="{SKIN[3]}"/><circle cx="324" cy="262" r="7.5" fill="{SKIN[3]}"/>',
         sparkle(350, 110, 10, "#ffd166"), sparkle(240, 100, 8, "#ffd166"), sparkle(360, 180, 7, "#ffd166")]
    return svg(b, "#fdf6ec")


def improvise():
    rnd = random.Random(3)
    b = ['<rect y="300" width="400" height="100" fill="#6a994e"/>',
         '<ellipse cx="120" cy="40" rx="140" ry="40" fill="#8d99ae"/><ellipse cx="320" cy="50" rx="120" ry="34" fill="#adb5bd"/>']
    for _ in range(40):
        x, y = rnd.uniform(0, 400), rnd.uniform(70, 290)
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 5)}" y2="{f(y + 14)}" stroke="#457b9d" stroke-width="2.5" '
                 'stroke-linecap="round"/>')
    b += [# two trees and the branch tied between them
          '<rect x="30" y="120" width="22" height="190" fill="#7f5539"/>', bush(41, 110, 46),
          '<rect x="268" y="130" width="20" height="180" fill="#7f5539"/>', bush(278, 120, 42),
          '<line x1="40" y1="190" x2="280" y2="190" stroke="#6f4518" stroke-width="10" stroke-linecap="round"/>',
          # the tarp thrown over it
          '<polygon points="60,190 260,190 300,320 20,320" fill="#4895ef"/>',
          '<polygon points="60,190 260,190 220,320 100,320" fill="#457b9d"/>',
          '<polygon points="120,320 160,236 200,320" fill="#264653" opacity=".7"/>',
          '<path d="M20 320 L4 340 M300 320 L318 340" stroke="#adb5bd" stroke-width="3"/>',
          '<rect x="0" y="336" width="8" height="14" fill="#7f5539"/><rect x="314" y="336" width="8" height="14" '
          'fill="#7f5539"/>',
          '<path d="M300 320 Q330 300 346 250" fill="none" stroke="#adb5bd" stroke-width="3"/>',
          shadow(350, 344, 30),
          person(352, 342, .82, SKIN[1], "#e76f51", "#264653", "#5c4033", "cap", mood="shut",
                 larm=((-26, -16), (-14, -40)), rarm=((12, 40), (16, 74)),
                 brows="M-14 -190 L-3 -187 M3 -187 L14 -190")]
    return svg(b, "#cfd8dc")


def footprint(x, y, k, rot):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(k)})">'
            '<ellipse cx="0" cy="0" rx="8" ry="14" fill="#7f5539"/><ellipse cx="0" cy="20" rx="6" ry="7" '
            'fill="#7f5539"/></g>')


def trace():
    b = ['<rect y="120" width="400" height="280" fill="#a7c957"/>',
         '<path d="M0 120 Q200 110 400 124" fill="#90be6d"/>',
         # the barn far off
         '<rect x="270" y="80" width="80" height="60" fill="#c1121f"/>',
         '<polygon points="262,84 310,50 358,84" fill="#9d0208"/>',
         '<rect x="296" y="104" width="28" height="36" fill="#fff"/>',
         '<path d="M296 104 L324 140 M324 104 L296 140" stroke="#c1121f" stroke-width="3"/>',
         bush(380, 120, 18), bush(240, 124, 12)]
    pts = [(122, 360), (150, 340), (130, 320), (170, 296), (160, 270), (200, 250), (196, 228), (232, 210),
           (230, 192), (262, 178), (262, 164), (288, 154)]
    for k, (x, y) in enumerate(pts):
        sc = 1.0 - k * .065
        b.append(footprint(x + (6 if k % 2 else -6) * sc, y, sc, 30 if k % 2 else 20))
    b += [shadow(60, 384, 30),
          person(60, 382, .95, SKIN[2], "#457b9d", "#264653", "#1b1b1b", "short", mood="side",
                 larm=((-12, 40), (-14, 74)), rarm=((36, -2), (72, -6)))]
    return svg(b, "#cfe8f3")


def alter():
    b = ['<rect x="20" y="300" width="360" height="100" fill="#8d6e63"/>',
         '<rect x="20" y="300" width="360" height="10" fill="#a1887f"/>',
         # the pants laid out on the board; the bit below the chalk line is the part cut off
         '<path d="M120 40 H280 L296 330 H222 L200 140 L178 330 H104 Z" fill="#457b9d"/>',
         '<rect x="120" y="40" width="160" height="22" fill="#355c7d"/>',
         '<path d="M104 330 H178 L176 270 H108 Z M222 330 H296 L292 270 H224 Z" fill="#a8dadc"/>',
         '<path d="M96 266 H186 M214 266 H304" stroke="#fff" stroke-width="5" stroke-dasharray="10 7"/>']
    for x in (120, 150, 240, 272):
        b.append(f'<line x1="{x}" y1="252" x2="{x + 6}" y2="276" stroke="#adb5bd" stroke-width="3"/>'
                 f'<circle cx="{x}" cy="252" r="5" fill="#e63946"/>')
    b += [arrow(330, 330, 330, 270, "#e76f51", 6, 16), arrow(70, 330, 70, 270, "#e76f51", 6, 16),
          # scissors
          '<g transform="rotate(-20 340 160)"><path d="M300 150 L380 140 M300 170 L380 140" stroke="#adb5bd" '
          'stroke-width="7" stroke-linecap="round"/><circle cx="292" cy="146" r="12" fill="none" stroke="#e63946" '
          'stroke-width="6"/><circle cx="292" cy="176" r="12" fill="none" stroke="#e63946" stroke-width="6"/></g>',
          # measuring tape
          '<path d="M30 120 Q60 80 90 100 T150 90" fill="none" stroke="#e9c46a" stroke-width="12"/>',
          '<path d="M40 112 v-6 M56 96 v-6 M72 90 v-6 M88 98 v-6" stroke="#7f5539" stroke-width="2"/>']
    return svg(b, "#f2e9e4")


def anticipating():
    b = ['<rect y="320" width="400" height="80" fill="#d4a373"/>',
         '<rect x="230" y="40" width="140" height="282" fill="#7f5539"/>',
         '<rect x="244" y="54" width="112" height="120" rx="4" fill="#9c6b3c"/>',
         '<rect x="244" y="190" width="112" height="120" rx="4" fill="#9c6b3c"/>',
         '<circle cx="250" cy="196" r="8" fill="#e9c46a"/>',
         '<rect x="220" y="318" width="160" height="8" fill="#6f4518"/>',
         dog(120, 330, 1.25, "open", leash=True),
         '<path d="M30 236 l-14 -8 M26 256 h-16 M34 216 l-10 -12" stroke="#6c757d" stroke-width="3" '
         'stroke-linecap="round"/>',
         '<path d="M126 160 l-4 -16 M140 158 l4 -16" stroke="#6c757d" stroke-width="3" stroke-linecap="round"/>',
         heart(190, 100, 12), heart(210, 70, 8, "#f4a261")]
    return svg(b, "#fdf0d5")


def persuade():
    shop = ('<rect x="20" y="40" width="360" height="280" fill="#f4a261"/>'
            '<path d="M20 40 H380 V80 H20 Z" fill="#e76f51"/>'
            + "".join(f'<path d="M{x} 80 a20 16 0 0 0 40 0" fill="{c}"/>' for x, c in
                      zip(range(20, 380, 40), ("#fff", "#e63946") * 5))
            + '<rect x="40" y="120" width="140" height="120" rx="6" fill="#caf0f8"/>'
            '<path d="M346 250 L324 150 H368 Z" fill="#d4a373"/>'
            '<circle cx="334" cy="142" r="20" fill="#ff8fab"/><circle cx="358" cy="142" r="20" fill="#fff"/>'
            '<circle cx="346" cy="120" r="20" fill="#a7c957"/>')
    clasp = (f'<circle cx="0" cy="-122" r="10" fill="{SKIN[0]}"/>'
             '<path d="M-6 -194 l-6 -6 M6 -194 l6 -6" stroke="#ffd166" stroke-width="3" stroke-linecap="round"/>')
    b = [shop, '<rect y="320" width="400" height="80" fill="#ced4da"/>', shadow(110, 364, 30), shadow(240, 364, 44),
         person(110, 362, .8, SKIN[0], "#2a9d8f", "#457b9d", "#e9c46a", "bun", mood="smile",
                larm=((-12, 14), (18, 22)), rarm=((12, 14), (-18, 22)),
                brows="M-14 -190 L-4 -194 M4 -194 L14 -190", extra=clasp),
         person(240, 364, 1.15, SKIN[0], "#457b9d", "#264653", "#7f5539", "short", mood="smile",
                larm=((-10, 40), (-14, 76)), rarm=((24, 24), (8, -14)),
                brows="M-14 -192 Q-8 -196 -2 -192 M2 -190 L14 -190"),
         heart(170, 130, 12), heart(186, 104, 8, "#f4a261")]
    return svg(b, "#fdf6ec")


def imaginative():
    b = ['<rect y="320" width="400" height="80" fill="#e9c46a"/>',
         '<ellipse cx="80" cy="60" rx="50" ry="18" fill="#fff"/><ellipse cx="200" cy="40" rx="50" ry="16" fill="#fff"/>',
         # rocket-ship climbing tower
         '<path d="M268 320 V130 Q268 60 300 30 Q332 60 332 130 V320 Z" fill="#fff"/>',
         '<path d="M276 60 Q300 20 324 60 Z" fill="#e63946"/>',
         '<circle cx="300" cy="110" r="18" fill="#4895ef" stroke="#adb5bd" stroke-width="5"/>',
         '<circle cx="300" cy="190" r="14" fill="#4895ef" stroke="#adb5bd" stroke-width="4"/>',
         '<path d="M268 250 L232 320 H268 Z M332 250 L368 320 H332 Z" fill="#e63946"/>',
         '<rect x="290" y="250" width="20" height="70" fill="#264653" opacity=".6"/>',
         '<polygon points="282,320 300,346 318,320" fill="#f4a261"/>',
         # the dragon whose tail is the slide
         '<path d="M30 320 Q40 230 110 210 Q170 196 196 140 L216 154 Q196 230 130 248 Q80 262 70 320 Z" fill="#52b788"/>',
         '<path d="M196 140 Q206 260 250 320" fill="none" stroke="#40916c" stroke-width="22" stroke-linecap="round"/>',
         '<path d="M190 142 Q204 262 246 322" fill="none" stroke="#a7c957" stroke-width="8" stroke-linecap="round"/>',
         '<circle cx="168" cy="132" r="34" fill="#52b788"/>',
         '<ellipse cx="140" cy="146" rx="26" ry="18" fill="#52b788"/>',
         '<circle cx="124" cy="140" r="3" fill="#264653"/>',
         '<circle cx="168" cy="122" r="9" fill="#fff"/><circle cx="166" cy="122" r="4.5" fill="#264653"/>',
         '<path d="M170 100 L178 78 L188 104 M190 108 L206 92 L204 118" fill="#2d6a4f" stroke="#2d6a4f" '
         'stroke-width="3" stroke-linejoin="round"/>',
         '<path d="M60 246 L72 226 L84 242 L96 222 L108 238" fill="none" stroke="#2d6a4f" stroke-width="6" '
         'stroke-linejoin="round"/>',
         '<path d="M126 158 Q140 166 152 158" fill="none" stroke="#264653" stroke-width="3" stroke-linecap="round"/>',
         person(236, 296, .5, SKIN[2], "#f4a261", "#457b9d", "#1b1b1b", "short", mood="grin",
                larm=((-26, -22), (-34, -50)), rarm=((26, -22), (34, -50)), rot=-30)]
    return svg(b, "#cfe8f3")



def side_runner(x, y, k, shirt, skin, hair, pants=INK, mood="grin"):
    """A runner seen from the side, heading right, mid-stride (feet just off the ground at y)."""
    mouth = {"grin": '<path d="M24 -141 Q29 -137 33 -142" fill="none" stroke="#264653" stroke-width="2.5" '
                     'stroke-linecap="round"/>',
             "tense": '<path d="M24 -140 H33" stroke="#264653" stroke-width="2.5" stroke-linecap="round"/>'}[mood]
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            + limb(((0, -80), (-6, -42), (-34, -14)), pants, 14)
            + limb(((10, -126), (-8, -106), (-24, -116)), shirt, 11) + f'<circle cx="-26" cy="-117" r="6" fill="{skin}"/>'
            + limb(((0, -80), (28, -54), (20, -22)), pants, 14)
            + f'<ellipse cx="-38" cy="-12" rx="10" ry="5" fill="{INK}"/><ellipse cx="26" cy="-20" rx="10" ry="5" fill="{INK}"/>'
            + limb(((0, -82), (10, -126)), shirt, 26)
            + limb(((12, -124), (28, -106), (42, -122)), shirt, 11) + f'<circle cx="44" cy="-124" r="6" fill="{skin}"/>'
            + f'<circle cx="18" cy="-150" r="17" fill="{skin}"/>'
            f'<path d="M2 -150 Q0 -170 18 -169 Q32 -168 34 -158 Q20 -160 12 -152 Z" fill="{hair}"/>'
            f'<circle cx="26" cy="-152" r="2.8" fill="{INK}"/>'
            f'<path d="M21 -160 L31 -157" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>' + mouth + '</g>')


def house_lines(x, y, w, color, sw, rough=0):
    rnd = random.Random(2)
    j = lambda: rnd.uniform(-rough, rough)
    out = []
    for _ in range(2 if rough else 1):
        out.append(f'<path d="M{f(x + j())} {f(y + j())} H{f(x + w + j())} V{f(y + w * .7 + j())} H{f(x + j())} Z '
                   f'M{f(x - w * .1 + j())} {f(y + j())} L{f(x + w / 2 + j())} {f(y - w * .45 + j())} '
                   f'L{f(x + w * 1.1 + j())} {f(y + j())} M{f(x + w * .4)} {f(y + w * .7)} V{f(y + w * .35)} '
                   f'H{f(x + w * .62)} V{f(y + w * .7)}" fill="none" stroke="{color}" stroke-width="{sw}" '
                   'stroke-linejoin="round" stroke-linecap="round"/>')
    return "".join(out)


def sketch():
    b = ['<rect y="330" width="400" height="70" fill="#b08968"/>',
         # the finished painting, propped behind
         '<rect x="250" y="70" width="130" height="110" fill="#fff" stroke="#c9a227" stroke-width="8"/>',
         '<rect x="258" y="78" width="114" height="94" fill="#caf0f8"/>',
         '<rect x="258" y="150" width="114" height="22" fill="#52b788"/>',
         '<rect x="286" y="112" width="58" height="42" fill="#e9c46a"/>',
         '<polygon points="280,114 315,88 350,114" fill="#e63946"/>',
         '<rect x="308" y="130" width="14" height="24" fill="#7f5539"/>', '<circle cx="356" cy="92" r="9" fill="#ffd166"/>',
         # the notepad with the pencil sketch
         '<g transform="rotate(-8 160 240)">'
         '<rect x="40" y="120" width="230" height="200" rx="6" fill="#fff" stroke="#dee2e6" stroke-width="3"/>'
         + "".join(f'<circle cx="{x}" cy="120" r="7" fill="none" stroke="#6c757d" stroke-width="4"/>'
                   for x in range(64, 260, 24))
         + house_lines(100, 210, 110, "#6c757d", 3, 6)
         + '<path d="M80 300 h150" stroke="#adb5bd" stroke-width="3" stroke-dasharray="14 6"/>'
         '<path d="M220 160 a14 14 0 1 0 1 0" fill="none" stroke="#adb5bd" stroke-width="3"/></g>',
         # pencil
         '<g transform="rotate(-35 300 290)"><rect x="240" y="282" width="110" height="16" fill="#ffd166"/>'
         '<rect x="350" y="282" width="16" height="16" fill="#e76f51"/>'
         '<polygon points="240,282 216,290 240,298" fill="#e6ccb2"/><polygon points="224,287 216,290 224,293" '
         f'fill="{INK}"/></g>']
    return svg(b, "#fdf6ec")


def imitated():
    def yogi(x, y, s, shirt, pants, hair, style, skin):
        return person(x, y, s, skin, shirt, pants, hair, style, mood="closed",
                      larm=((-12, -42), (22, -80)), rarm=((12, -42), (-22, -80)),
                      lleg=((-2, 44), (-2, 86)), rleg=((30, 26), (-6, 40)))
    b = ['<rect y="330" width="400" height="70" fill="#e9d8c4"/>',
         '<rect x="40" y="330" width="170" height="16" rx="6" fill="#2a9d8f"/>',
         '<rect x="250" y="330" width="120" height="16" rx="6" fill="#e76f51"/>',
         yogi(122, 332, 1.25, "#457b9d", "#264653", "#5c4033", "bun", SKIN[1]),
         yogi(306, 332, .72, "#f4a261", "#457b9d", "#5c4033", "short", SKIN[1]),
         carrow(170, 60, 240, 20, 290, 120, "#2a9d8f", 5, 14)]
    return svg(b, "#f1faee")


def crab(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<path d="M-14 0 l-10 8 M-10 4 l-8 10 M14 0 l10 8 M10 4 l8 10" stroke="#e63946" stroke-width="4" '
            'stroke-linecap="round"/>'
            '<path d="M-16 -6 Q-30 -16 -24 -26 M16 -6 Q30 -16 24 -26" fill="none" stroke="#e63946" stroke-width="4"/>'
            '<circle cx="-24" cy="-28" r="7" fill="#e63946"/><circle cx="24" cy="-28" r="7" fill="#e63946"/>'
            '<ellipse cx="0" cy="0" rx="20" ry="13" fill="#e63946"/>'
            f'<path d="M-6 -12 v-8 M6 -12 v-8" stroke="{INK}" stroke-width="2"/>'
            f'<circle cx="-6" cy="-21" r="3" fill="{INK}"/><circle cx="6" cy="-21" r="3" fill="{INK}"/></g>')


def exposed():
    b = ['<rect width="400" height="110" fill="#caf0f8"/>',
         '<path d="M0 110 Q100 100 200 112 T400 108 V160 Q300 150 200 162 T0 158 Z" fill="#4895ef"/>',
         '<path d="M0 158 Q100 148 200 160 T400 156 V400 H0 Z" fill="#e9d8a6"/>',
         '<path d="M0 158 Q100 148 200 160 T400 156" fill="none" stroke="#fff" stroke-width="5"/>',
         # where the water usually reaches
         '<path d="M0 360 Q100 350 200 362 T400 356" fill="none" stroke="#457b9d" stroke-width="3" stroke-dasharray="10 8"/>',
         arrow(360, 330, 360, 190, "#457b9d", 5, 14), arrow(40, 330, 40, 190, "#457b9d", 5, 14),
         '<ellipse cx="120" cy="250" rx="54" ry="30" fill="#6c757d"/><ellipse cx="104" cy="240" rx="24" ry="14" fill="#adb5bd"/>',
         '<ellipse cx="270" cy="230" rx="40" ry="24" fill="#6c757d"/>',
         '<ellipse cx="160" cy="268" rx="44" ry="8" fill="#a8dadc" opacity=".7"/>',
         crab(230, 300, 1.2), crab(110, 320, .8),
         star(300, 300, 22, "#f4a261", .42), star(80, 200, 12, "#e76f51", .42),
         '<path d="M180 204 q10 -16 20 0 Z" fill="#fff" stroke="#e6ccb2" stroke-width="2"/>',
         '<path d="M330 248 q8 -14 16 0 Z" fill="#ff8fab"/>',
         '<path d="M150 340 q8 -14 16 0 Z" fill="#fff" stroke="#e6ccb2" stroke-width="2"/>',
         '<path d="M262 216 q-6 -12 6 -18 M282 210 q2 -12 12 -12" fill="none" stroke="#2d6a4f" stroke-width="4" '
         'stroke-linecap="round"/>']
    return svg(b, "#e9d8a6")


def subdued():
    b = ['<rect y="320" width="400" height="80" fill="#8d99ae"/>',
         '<rect x="20" y="40" width="360" height="200" fill="#adb5bd" opacity=".35"/>',
         '<rect x="30" y="250" width="340" height="16" rx="4" fill="#6c757d"/>',
         '<rect x="50" y="266" width="10" height="56" fill="#495057"/><rect x="340" y="266" width="10" height="56" '
         'fill="#495057"/>']
    for x, sk, hair in ((90, SKIN[0], "#7f5539"), (200, SKIN[3], "#1b1b1b"), (310, SKIN[1], "#5c4033")):
        b.append(person(x, 336, 1.0, sk, "#457b9d", "#264653", hair, "short", mood="down",
                        brows="M-14 -184 L-4 -188 M4 -188 L14 -184",
                        larm=((-6, 36), (10, 56)), rarm=((6, 36), (-10, 56)),
                        lleg=((-4, 20), (-4, 54)), rleg=((4, 20), (4, 54))))
    b += ['<path d="M140 362 Q170 340 196 360 Q172 376 140 362 Z" fill="#e76f51"/>',
          '<path d="M150 358 q14 -6 30 2" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>',
          '<ellipse cx="120" cy="60" rx="70" ry="22" fill="#6c757d" opacity=".5"/>']
    return svg(b, "#ced4da")


def catastrophic():
    rnd = random.Random(8)
    b = ['<rect width="400" height="400" fill="#6c757d"/>',
         '<ellipse cx="80" cy="30" rx="140" ry="50" fill="#343a40"/><ellipse cx="320" cy="20" rx="140" ry="50" '
         'fill="#495057"/>',
         '<polygon points="250,40 230,90 248,90 232,140 272,80 254,80 268,40" fill="#ffd166"/>']
    for _ in range(50):
        x, y = rnd.uniform(0, 400), rnd.uniform(50, 380)
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 6)}" y2="{f(y + 16)}" stroke="#adb5bd" stroke-width="2" '
                 'opacity=".7"/>')
    # rooftops just above the flood
    for x, w, c in ((30, 90, "#9d0208"), (150, 80, "#6f4518"), (260, 110, "#9d0208")):
        b += [f'<polygon points="{x},230 {x + w / 2},170 {x + w},230" fill="{c}"/>',
              f'<rect x="{x + w * .7}" y="176" width="12" height="30" fill="#495057"/>']
    b += ['<path d="M0 222 Q25 212 50 222 T100 222 T150 222 T200 222 T250 222 T300 222 T350 222 T400 222 V400 H0 Z" '
          'fill="#8d6e63"/>',
          '<path d="M0 222 Q25 212 50 222 T100 222 T150 222 T200 222 T250 222 T300 222 T350 222 T400 222" fill="none" '
          'stroke="#d7b899" stroke-width="4"/>',
          '<path d="M0 290 Q40 280 80 290 T160 290 T240 290 T320 290 T400 290 M0 350 Q40 340 80 350 T160 350 T240 350 '
          'T320 350 T400 350" fill="none" stroke="#a1887f" stroke-width="4"/>',
          # what the water carried off
          '<rect x="60" y="300" width="70" height="14" rx="6" fill="#5c4033" transform="rotate(-12 95 307)"/>',
          '<circle cx="300" cy="320" r="18" fill="none" stroke="#212529" stroke-width="9"/>',
          '<rect x="180" y="260" width="60" height="22" rx="6" fill="#4895ef" transform="rotate(8 210 271)"/>',
          '<path d="M350 250 Q340 210 360 190 Q380 210 370 250 Z" fill="#2d6a4f"/>',
          '<path d="M360 250 V222" stroke="#5c4033" stroke-width="5"/>']
    return svg(b, "#6c757d")


def craft():
    b = ['<rect y="300" width="400" height="100" fill="#9c6b3c"/>',
         '<rect y="300" width="400" height="10" fill="#b08968"/>']
    for x, y, r in ((80, 330, 0), (130, 350, 40), (300, 340, -20), (330, 370, 60), (60, 380, 20), (260, 380, 90)):
        b.append(f'<path d="M{x} {y} q10 -12 20 0 q-6 10 -16 4" fill="none" stroke="#e6ccb2" stroke-width="4" '
                 f'transform="rotate({r} {x} {y})"/>')
    # the half-carved bird: finished on top, still a block below
    b += ['<rect x="150" y="230" width="110" height="60" rx="4" fill="#d4a373"/>',
          '<path d="M150 240 Q160 180 210 176 Q250 172 262 200 L290 196 L268 214 Q262 236 236 240 Z" fill="#e6ccb2"/>',
          '<circle cx="250" cy="196" r="4" fill="#7f5539"/>',
          '<path d="M180 206 Q208 226 238 208" fill="none" stroke="#c08552" stroke-width="4"/>',
          '<path d="M154 236 L126 214 L138 238 Z" fill="#e6ccb2"/>',
          '<path d="M160 290 V250 M190 290 V246 M226 290 V244" stroke="#c08552" stroke-width="2" opacity=".6"/>',
          # holding hand and carving hand with the knife
          '<path d="M30 300 Q80 280 150 268" fill="none" stroke="#2a9d8f" stroke-width="36" stroke-linecap="round"/>',
          f'<ellipse cx="156" cy="266" rx="24" ry="22" fill="{SKIN[1]}"/>',
          '<path d="M390 180 Q330 170 290 150" fill="none" stroke="#2a9d8f" stroke-width="34" stroke-linecap="round"/>',
          f'<ellipse cx="282" cy="148" rx="22" ry="20" fill="{SKIN[1]}"/>',
          '<rect x="252" y="140" width="22" height="12" rx="4" fill="#5c4033" transform="rotate(30 263 146)"/>',
          '<polygon points="256,150 218,182 228,186 264,160" fill="#ced4da"/>',
          '<path d="M210 176 q-10 -14 2 -24 q10 -6 14 4 M196 168 q-8 -12 4 -18" fill="none" stroke="#d4a373" '
          'stroke-width="4" stroke-linecap="round"/>',
          sparkle(120, 140, 10, "#ffd166"), sparkle(330, 240, 8, "#ffd166")]
    return svg(b, "#fdf0d5")


def bridge(x, y, w, color="#e63946"):
    t1, t2 = x + w * .25, x + w * .75
    return (f'<rect x="{x}" y="{y}" width="{w}" height="8" fill="{color}"/>'
            f'<rect x="{f(t1 - 5)}" y="{f(y - 60)}" width="10" height="90" fill="{color}"/>'
            f'<rect x="{f(t2 - 5)}" y="{f(y - 60)}" width="10" height="90" fill="{color}"/>'
            f'<path d="M{x} {y} Q{f((x + t1) / 2)} {f(y - 20)} {f(t1)} {f(y - 58)} Q{f(x + w / 2)} {f(y - 4)} {f(t2)} '
            f'{f(y - 58)} Q{f((t2 + x + w) / 2)} {f(y - 20)} {x + w} {y}" fill="none" stroke="{color}" stroke-width="4"/>'
            + "".join(f'<line x1="{f(xx)}" y1="{y}" x2="{f(xx)}" y2="{f(y - 40 + abs(xx - x - w / 2) * .2)}" '
                      f'stroke="{color}" stroke-width="2"/>' for xx in range(int(x + 16), int(x + w), 16)
                      if abs(xx - t1) > 8 and abs(xx - t2) > 8))


def visualize():
    b = ['<rect y="320" width="400" height="80" fill="#d4a373"/>',
         '<rect x="20" y="290" width="200" height="14" rx="4" fill="#7f5539"/>',
         '<rect x="36" y="304" width="10" height="40" fill="#6f4518"/><rect x="194" y="304" width="10" height="40" '
         'fill="#6f4518"/>',
         person(110, 330, 1.0, SKIN[0], "#e76f51", "#264653", "#7f5539", "side", mood="closed",
                larm=((-12, 40), (2, 64)), rarm=((12, 40), (-2, 64))),
         '<rect x="60" y="270" width="80" height="20" fill="#e9c46a"/>',
         '<path d="M70 270 l20 -10 M100 270 l-6 -12 M126 270 l12 -10" stroke="#e6ccb2" stroke-width="5" '
         'stroke-linecap="round"/>',
         '<circle cx="160" cy="114" r="7" fill="#fff" stroke="#ced4da" stroke-width="2"/>',
         '<circle cx="180" cy="92" r="11" fill="#fff" stroke="#ced4da" stroke-width="2"/>',
         '<ellipse cx="290" cy="110" rx="112" ry="90" fill="#fff8d6"/>',
         '<ellipse cx="290" cy="110" rx="100" ry="80" fill="#fff" stroke="#ffd166" stroke-width="4"/>',
         '<path d="M196 150 Q290 140 384 150 V176 Q290 190 196 176 Z" fill="#a8dadc"/>',
         bridge(212, 140, 156), sparkle(368, 50, 10, "#ffd166"), sparkle(214, 50, 8, "#ffd166"),
         sparkle(380, 170, 7, "#ffd166")]
    return svg(b, "#eef4ff")


def gaining_on():
    b = ['<rect y="260" width="400" height="140" fill="#e76f51"/>',
         '<path d="M0 300 H400 M0 360 H400" stroke="#fff" stroke-width="4" opacity=".7"/>',
         bush(30, 256, 20), bush(370, 252, 26), bush(200, 258, 14),
         shadow(280, 342, 40, 5), shadow(170, 342, 40, 5),
         side_runner(270, 326, 1.4, "#457b9d", SKIN[0], "#e9c46a", mood="tense"),
         side_runner(170, 326, 1.4, "#2a9d8f", SKIN[3], "#1b1b1b"),
         '<path d="M40 150 h60 M30 180 h70 M46 210 h56" stroke="#fff" stroke-width="6" stroke-linecap="round"/>',
         arrow(204, 90, 236, 90, INK, 5, 13), arrow(268, 90, 240, 90, INK, 5, 13),
         '<path d="M200 76 V104 M272 76 V104" stroke="#264653" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#e3f2fd")


def exaggerate():
    rnd = random.Random(5)
    fish = ("M60 110 Q130 30 250 70 Q300 80 340 110 Q300 140 250 150 Q130 190 60 110 Z "
            "M60 110 L20 70 L30 110 L20 150 Z")
    b = ['<rect y="320" width="400" height="80" fill="#a8dadc"/>',
         '<path d="M0 320 Q50 312 100 320 T200 320 T300 320 T400 320" fill="none" stroke="#fff" stroke-width="4"/>',
         '<rect y="300" width="400" height="24" fill="#b08968"/>',
         f'<path d="{fish}" fill="#caf0f8" opacity=".6" stroke="#457b9d" stroke-width="4" stroke-dasharray="12 9"/>',
         shadow(180, 304, 40),
         person(180, 302, .95, SKIN[1], "#e9c46a", "#457b9d", "#5c4033", "cap", mood="grin",
                larm=((-60, -30), (-116, -40)), rarm=((60, -30), (120, -46))),
         # the bucket and the real catch
         '<path d="M290 254 H360 L352 302 H298 Z" fill="#adb5bd"/>',
         '<ellipse cx="325" cy="254" rx="35" ry="7" fill="#6c757d"/>',
         '<path d="M308 254 Q322 236 338 250 L348 240 L346 260 L338 256 Q322 268 308 254 Z" fill="#f4a261"/>',
         f'<circle cx="317" cy="250" r="2.5" fill="{INK}"/>']
    return svg(b, "#e3f2fd")


def reconcile():
    hug_l = limb(((22, -146), (40, -120), (60, -130)), "#e76f51", 15) + f'<circle cx="62" cy="-131" r="8.5" fill="{SKIN[1]}"/>'
    b = ['<rect y="340" width="400" height="60" fill="#e9d8c4"/>', shadow(200, 344, 80),
         person(240, 342, 1.25, SKIN[3], "#2a9d8f", "#264653", "#1b1b1b", "short", mood="closed", rot=-6,
                larm=((-22, 20), (-50, 4)), rarm=((12, 40), (16, 76))),
         person(160, 342, 1.25, SKIN[1], "#e76f51", "#457b9d", "#7f5539", "bun", mood="closed", rot=6,
                larm=((-12, 40), (-16, 76)), rarm=((0, 4),), extra=hug_l),
         # a mended heart
         heart(200, 46, 26, "#e63946"),
         '<path d="M200 32 L194 42 L205 52 L197 64" fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round"/>',
         '<rect x="186" y="40" width="28" height="10" rx="4" fill="#fefae0" transform="rotate(-30 200 45)"/>',
         sparkle(130, 50, 9, "#ffd166"), sparkle(276, 60, 9, "#ffd166")]
    return svg(b, "#fde2e4")



def gold_coin(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<ellipse cx="0" cy="3" rx="20" ry="7" fill="#c9a227"/><rect x="-20" y="-2" width="40" height="5" fill="#c9a227"/>'
            '<ellipse cx="0" cy="-2" rx="20" ry="7" fill="#f2cc5b" stroke="#c9a227" stroke-width="1.5"/></g>')


def paucity_of():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>', shadow(200, 334, 100, 8),
         '<rect x="100" y="80" width="200" height="252" rx="34" fill="#eef7fb" stroke="#8ecae6" stroke-width="6"/>',
         '<rect x="114" y="50" width="172" height="36" rx="8" fill="#2a9d8f"/>',
         '<rect x="114" y="76" width="172" height="10" fill="#21867a"/>',
         '<rect x="116" y="104" width="12" height="200" rx="6" fill="#fff" opacity=".7"/>',
         gold_coin(214, 318, .9), sparkle(240, 296, 7, "#ffd166")]
    return svg(b, "#fdfcdc")


def swan(x, y, k, body, beak="#f4a261", flip=False):
    sgn = -1 if flip else 1
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sgn * k)} {k})">'
            f'<path d="M-30 0 Q-34 -26 -6 -26 Q20 -26 30 -8 Q10 6 -30 0 Z" fill="{body}"/>'
            f'<path d="M20 -14 Q28 -40 14 -54 Q6 -64 14 -70" fill="none" stroke="{body}" stroke-width="8" '
            'stroke-linecap="round"/>'
            f'<circle cx="16" cy="-70" r="7" fill="{body}"/><polygon points="20,-72 32,-66 20,-64" fill="{beak}"/></g>')


def refute():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         '<rect x="20" y="30" width="260" height="200" rx="6" fill="#457b9d"/>',
         '<rect x="20" y="30" width="260" height="200" rx="6" fill="none" stroke="#7f5539" stroke-width="8"/>']
    for r in range(2):
        for c in range(3):
            x, y = 70 + c * 82, 112 + r * 92
            b += [f'<rect x="{x - 36}" y="{y - 70}" width="72" height="80" fill="#a8dadc"/>', swan(x, y, .85, "#fff")]
    b += ['<rect x="20" y="230" width="10" height="100" fill="#7f5539"/><rect x="270" y="230" width="10" height="100" '
          'fill="#7f5539"/>',
          shadow(320, 364, 34),
          person(320, 362, 1.1, SKIN[2], "#fff", "#264653", "#1b1b1b", "short", mood="grin",
                 larm=((-26, -14), (-46, -40)), rarm=((12, 40), (16, 76))),
          '<g transform="translate(-36 -36) rotate(-8 252 150)"><rect x="200" y="100" width="104" height="104" '
          'fill="#fff"/><rect x="208" y="108" width="88" height="80" fill="#cdb4db"/>'
          + swan(256, 176, .95, "#212529", "#e63946") + '</g>',
          f'<circle cx="246" cy="158" r="9" fill="{SKIN[2]}"/>',
          sparkle(200, 84, 9, "#ffd166"), sparkle(318, 90, 8, "#ffd166")]
    return svg(b, "#f1faee")


def offered():
    plate = ('<ellipse cx="72" cy="-128" rx="34" ry="9" fill="#fff" stroke="#ced4da" stroke-width="2"/>'
             + "".join(f'<circle cx="{cx}" cy="{cy}" r="10" fill="#d4a373"/>'
                       f'<circle cx="{cx - 3}" cy="{cy - 2}" r="2" fill="#5c4033"/><circle cx="{cx + 3}" cy="{cy + 2}" '
                       'r="2" fill="#5c4033"/>' for cx, cy in ((56, -134), (74, -136), (92, -134), (66, -146), (84, -146))))
    b = ['<rect y="340" width="400" height="60" fill="#a7c957"/>',
         '<rect x="230" y="20" width="170" height="330" fill="#e9d8c4"/>',
         '<rect x="262" y="70" width="110" height="272" fill="#3d405b"/>',
         '<polygon points="262,70 300,84 300,330 262,342" fill="#7f5539"/>',
         '<rect x="252" y="62" width="130" height="10" fill="#9c6b3c"/>',
         shadow(330, 346, 34), shadow(130, 346, 40),
         person(332, 344, 1.05, SKIN[3], "#e9c46a", "#457b9d", "#1b1b1b", "bun", mood="smile",
                larm=((-12, 40), (-14, 76)), rarm=((12, 40), (14, 76))),
         person(130, 344, 1.05, SKIN[0], "#2a9d8f", "#264653", "#7f5539", "short", mood="grin",
                larm=((26, 10), (58, 4)), rarm=((24, 10), (62, 0)), extra=plate),
         heart(206, 112, 10), heart(190, 90, 7, "#f4a261")]
    return svg(b, "#cfe8f3")


def costly():
    rnd = random.Random(6)
    b = ['<rect y="320" width="400" height="80" fill="#e9d8c4"/>', shadow(254, 326, 140, 10)]
    coins = []
    for row in range(11):
        n = 11 - row
        for c in range(n):
            x = 254 - (n - 1) * 12 + c * 24 + rnd.uniform(-3, 3)
            coins.append((x, 320 - row * 20 + rnd.uniform(-2, 2)))
    for x, y in coins:
        b.append(gold_coin(x, y, .8))
    b += [sparkle(160, 120, 10, "#fff"), sparkle(300, 90, 12, "#fff"), sparkle(250, 200, 8, "#fff"),
          # the tiny toy car on its stand, with a blank price tag
          '<rect x="34" y="296" width="70" height="26" fill="#adb5bd"/>',
          '<path d="M46 296 V286 Q48 280 56 280 L62 272 H80 L88 280 Q96 281 96 288 V296 Z" fill="#e63946"/>',
          '<rect x="66" y="275" width="10" height="7" fill="#caf0f8"/>',
          '<circle cx="56" cy="297" r="5" fill="#343a40"/><circle cx="86" cy="297" r="5" fill="#343a40"/>',
          '<path d="M90 280 Q110 250 116 240" fill="none" stroke="#6c757d" stroke-width="2"/>',
          '<rect x="108" y="226" width="26" height="16" rx="3" fill="#fff" stroke="#adb5bd" stroke-width="2" '
          'transform="rotate(-20 121 234)"/>',
          arrow(110, 160, 140, 200, INK, 4, 12)]
    return svg(b, "#fdf6ec")


def surrendered():
    helmet = ('<path d="M-25 -170 Q-26 -206 0 -206 Q26 -206 25 -170 Z" fill="#6c757d"/>'
              f'<rect x="-18" y="-186" width="36" height="6" rx="3" fill="{INK}"/>')
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>', '<circle cx="340" cy="56" r="26" fill="#fefae0"/>',
         shadow(130, 334, 46), shadow(310, 334, 40),
         # the knight giving up: hands high, a white flag in one of them
         person(130, 332, 1.15, "#e0ac69", "#adb5bd", "#6c757d", "#000", "none", mood="frown",
                larm=((-24, -30), (-30, -70)), rarm=((24, -30), (30, -70)), extra=helmet),
         '<line x1="70" y1="190" x2="70" y2="40" stroke="#7f5539" stroke-width="5"/>',
         '<path d="M73 44 Q100 36 124 50 Q110 66 124 82 Q100 74 73 82 Z" fill="#fff"/>',
         f'<circle cx="70" cy="64" r="9" fill="#e0ac69"/>',
         # sword and shield laid down on the grass
         '<g transform="rotate(-6 200 356)"><rect x="150" y="352" width="110" height="9" rx="3" fill="#dee2e6"/>'
         '<polygon points="260,352 276,356 260,361" fill="#dee2e6"/>'
         '<rect x="140" y="344" width="8" height="26" rx="3" fill="#e9c46a"/><rect x="118" y="351" width="24" height="12" '
         'rx="4" fill="#7f5539"/></g>',
         '<path d="M196 350 H252 V366 Q252 388 224 394 Q196 388 196 366 Z" fill="#457b9d" '
         'transform="rotate(-10 224 372)"/>',
         '<path d="M224 354 V388" stroke="#e9c46a" stroke-width="5" transform="rotate(-10 224 372)"/>',
         # the other knight, sword lowered
         person(310, 332, 1.15, "#c68642", "#adb5bd", "#6c757d", "#000", "none", mood="flat",
                larm=((-12, 40), (-14, 76)), rarm=((14, 38), (20, 72)), extra=helmet),
         '<rect x="331" y="244" width="8" height="90" fill="#dee2e6" transform="rotate(-12 335 250)"/>',
         '<rect x="320" y="236" width="30" height="8" rx="3" fill="#e9c46a" transform="rotate(-12 335 240)"/>']
    return svg(b, "#e3f2fd")


def powerful():
    rnd = random.Random(10)
    b = ['<polygon points="0,0 130,0 150,400 0,400" fill="#6c757d"/>',
         '<polygon points="270,0 400,0 400,400 250,400" fill="#495057"/>',
         '<rect x="0" y="0" width="400" height="40" fill="#52b788"/>',
         pine(30, 40, 50), pine(80, 40, 40), pine(330, 40, 50), pine(380, 40, 44),
         '<path d="M120 40 Q200 30 280 40 L262 300 H138 Z" fill="#4895ef"/>']
    for x in range(130, 280, 16):
        b.append(f'<path d="M{x} 40 L{f(140 + (x - 130) * .82)} 300" stroke="#caf0f8" stroke-width="5" opacity=".75"/>')
    b += ['<rect y="300" width="400" height="100" fill="#457b9d"/>']
    for _ in range(30):
        x, y, r = min(310, max(90, rnd.gauss(200, 70))), rnd.uniform(270, 330), rnd.uniform(14, 34)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="#fff" opacity=".85"/>')
    b += ['<path d="M0 360 Q50 350 100 360 T200 360 T300 360 T400 360" fill="none" stroke="#a8dadc" stroke-width="4"/>',
          '<path d="M90 230 l-26 -10 M88 260 l-30 4 M312 230 l26 -10 M312 260 l30 4" stroke="#fff" stroke-width="5" '
          'stroke-linecap="round"/>']
    return svg(b, "#a8dadc")


def discovered():
    b = ['<rect width="400" height="400" fill="#212529"/>',
         '<path d="M0 0 H400 V70 Q340 110 300 80 Q250 120 200 90 Q150 130 100 90 Q50 120 0 80 Z" fill="#343a40"/>',
         '<path d="M0 330 Q100 310 200 330 T400 324 V400 H0Z" fill="#495057"/>',
         '<circle cx="270" cy="270" r="130" fill="#ffd166" opacity=".18"/>',
         '<circle cx="270" cy="270" r="80" fill="#ffd166" opacity=".2"/>',
         '<circle cx="110" cy="210" r="90" fill="#fff3b0" opacity=".14"/>']
    for a in range(-160, -10, 22):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(275 + 60 * ca)}" y1="{f(262 + 60 * sa)}" x2="{f(275 + 92 * ca)}" y2="{f(262 + 92 * sa)}" '
                 'stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>')
    b += ['<polygon points="224,240 236,188 314,188 326,240" fill="#6f4518"/>',
          '<rect x="220" y="270" width="110" height="64" rx="4" fill="#9c6644"/>',
          '<path d="M218 270 L222 236 H328 L332 270 Z" fill="#7f5539"/>',
          '<path d="M226 254 Q275 214 324 254" fill="#ffd166"/>',
          gold_coin(250, 250, .7), gold_coin(290, 246, .7), '<circle cx="272" cy="236" r="9" fill="#e63946"/>',
          '<rect x="220" y="284" width="110" height="8" fill="#e9c46a"/>',
          '<rect x="266" y="284" width="18" height="24" rx="3" fill="#e9c46a"/>',

          shadow(110, 336, 34, 6, .3),
          person(110, 334, 1.05, SKIN[1], "#e9c46a", "#7f5539", "#5c4033", "cap", mood="wide",
                 larm=((-12, 40), (-14, 74)), rarm=((30, -6), (52, -18))),
          '<line x1="166" y1="172" x2="166" y2="184" stroke="#adb5bd" stroke-width="3"/>',
          '<rect x="156" y="184" width="20" height="30" rx="5" fill="#ffd166" stroke="#c9a227" stroke-width="3"/>',
          sparkle(350, 190, 12, "#ffd166"), sparkle(200, 200, 9, "#ffd166")]
    return svg(b, "#212529")


def focused():
    distractions = ('<g filter="url(#blur)" opacity=".75">'
                    '<rect x="20" y="40" width="70" height="110" rx="10" fill="#343a40"/>'
                    '<rect x="28" y="52" width="54" height="80" fill="#4895ef"/>'
                    '<path d="M100 60 l14 -8 M100 90 h16" stroke="#e63946" stroke-width="5" stroke-linecap="round"/>'
                    '<rect x="280" y="40" width="100" height="70" rx="6" fill="#343a40"/>'
                    '<rect x="288" y="48" width="84" height="54" fill="#e76f51"/>'
                    '<circle cx="340" cy="210" r="30" fill="#e9c46a"/><circle cx="330" cy="200" r="4" fill="#264653"/>'
                    '<path d="M260 190 l-16 -6 M262 210 h-18 M266 230 l-14 8" stroke="#e63946" stroke-width="5" '
                    'stroke-linecap="round"/>'
                    '<circle cx="60" cy="230" r="24" fill="#a7c957"/>'
                    '<path d="M100 220 q10 -10 20 0 q10 10 20 0" fill="none" stroke="#e63946" stroke-width="5"/></g>')
    b = [distractions,
         '<polygon points="160,0 240,0 330,330 70,330" fill="#fff3b0" opacity=".55"/>',
         '<rect y="330" width="400" height="70" fill="#d4a373"/>',
         person(200, 330, 1.05, SKIN[2], "#e76f51", "#264653", "#1b1b1b", "short", mood="down",
                brows="M-15 -190 L-3 -186 M3 -186 L15 -190",
                larm=((-14, 38), (2, 60)), rarm=((16, 34), (34, 54))),
         '<rect x="90" y="280" width="220" height="14" rx="4" fill="#7f5539"/>',
         '<rect x="104" y="294" width="10" height="40" fill="#6f4518"/><rect x="286" y="294" width="10" height="40" '
         'fill="#6f4518"/>',
         f'<circle cx="179" cy="282" r="9" fill="{SKIN[2]}"/><circle cx="236" cy="278" r="9" fill="{SKIN[2]}"/>',
         '<path d="M146 268 L200 276 L254 268 V282 H146 Z" fill="#fff" stroke="#ced4da" stroke-width="2"/>',
         '<path d="M156 276 h30 M214 276 h30" stroke="#adb5bd" stroke-width="2"/>',
         '<line x1="236" y1="268" x2="250" y2="252" stroke="#e9c46a" stroke-width="5" stroke-linecap="round"/>']
    return svg(b, "#e9ecef", '<filter id="blur" x="-20%" y="-20%" width="140%" height="140%">'
               '<feGaussianBlur stdDeviation="5"/></filter>')


def extended():
    def section(x, y, w, h, c):
        rungs = "".join(f'<line x1="{x}" y1="{yy}" x2="{x + w}" y2="{yy}" stroke="{c}" stroke-width="5"/>'
                        for yy in range(int(y + 14), int(y + h), 26))
        return (f'<rect x="{x - 4}" y="{y}" width="8" height="{h}" fill="{c}"/>'
                f'<rect x="{x + w - 4}" y="{y}" width="8" height="{h}" fill="{c}"/>' + rungs)
    b = ['<rect x="200" y="0" width="200" height="400" fill="#f4a261"/>',
         '<rect x="200" y="0" width="200" height="400" fill="none" stroke="#e76f51" stroke-width="0"/>',
         '<rect y="340" width="400" height="60" fill="#a7c957"/>']
    for y in range(20, 340, 40):
        b.append(f'<path d="M200 {y} H400" stroke="#e76f51" stroke-width="2" opacity=".5"/>')
    b += ['<rect x="200" y="20" width="200" height="60" fill="#2a9d8f"/>',
          section(240, 230, 60, 112, "#6c757d"), section(246, 130, 48, 110, "#adb5bd"),
          section(250, 30, 40, 110, "#ced4da"),
          '<path d="M232 236 H312" stroke="#adb5bd" stroke-width="3" stroke-dasharray="8 6"/>',
          arrow(340, 220, 340, 110, "#264653", 6, 16), arrow(340, 300, 340, 250, "#264653", 6, 16),
          shadow(140, 344, 34),
          person(140, 342, 1.0, SKIN[1], "#fff", "#457b9d", "#5c4033", "cap", mood="smile",
                 larm=((-12, 40), (-14, 74)), rarm=((40, -6), (86, -40))),
          '<path d="M60 316 H100 L96 342 H64 Z" fill="#adb5bd"/><ellipse cx="80" cy="316" rx="20" ry="5" fill="#264653"/>']
    return svg(b, "#cfe8f3")


def insurmountable():
    b = ['<linearGradient id="cliff" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6d597a"/>'
         '<stop offset="1" stop-color="#9a8c98"/></linearGradient>']
    b = ['<rect x="150" y="0" width="250" height="360" fill="url(#cliff)"/>',
         '<path d="M150 0 V360" stroke="#5e548e" stroke-width="6"/>',
         '<path d="M220 0 V360 M300 0 V360" stroke="#fff" stroke-width="3" opacity=".12"/>',
         '<ellipse cx="60" cy="50" rx="50" ry="16" fill="#fff"/><ellipse cx="300" cy="60" rx="70" ry="18" fill="#fff" '
         'opacity=".8"/>',
         '<rect y="350" width="400" height="50" fill="#a7c957"/>',
         shadow(110, 354, 14, 3), '<rect x="96" y="300" width="10" height="16" rx="3" fill="#2a9d8f"/>',
         person(110, 352, .3, SKIN[2], "#e63946", "#264653", "#1b1b1b", "cap", mood="wide",
                larm=((-12, 40), (-14, 74)), rarm=((22, -24), (30, -60))),
         '<path d="M116 280 Q140 160 170 20" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="6 7"/>',
         arrow(190, 330, 190, 30, "#fff", 4, 14)]
    return svg(b, "#cfe8f3", '<linearGradient id="cliff" x1="0" y1="0" x2="0" y2="1"><stop offset="0" '
               'stop-color="#6d597a"/><stop offset="1" stop-color="#9a8c98"/></linearGradient>')



def cone(x, y, k, scoop, scoop2=None):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<path d="M-20 0 L0 56 L20 0 Z" fill="#d4a373"/>'
            '<path d="M-14 8 L10 30 M-6 2 L14 18 M14 6 L-8 30" stroke="#c08552" stroke-width="2"/>'
            f'<circle cx="0" cy="-12" r="22" fill="{scoop}"/>'
            + (f'<circle cx="0" cy="-40" r="18" fill="{scoop2}"/>' if scoop2 else "")
            + '<circle cx="-8" cy="-18" r="5" fill="#fff" opacity=".5"/></g>')


def choose():
    b = ['<rect y="340" width="400" height="60" fill="#e9d8c4"/>', shadow(200, 344, 34),
         person(200, 342, 1.0, SKIN[2], "#2a9d8f", "#457b9d", "#1b1b1b", "bun", mood="side",
                larm=((-12, 40), (-14, 76)), rarm=((16, 24), (0, -6)),
                brows="M-14 -192 Q-8 -196 -2 -192 M2 -190 L14 -192"),
         # two cones held out from either side
         '<path d="M0 230 Q40 226 70 214" fill="none" stroke="#457b9d" stroke-width="20" stroke-linecap="round"/>',
         f'<circle cx="76" cy="212" r="12" fill="{SKIN[0]}"/>', cone(80, 170, 1.2, "#ff8fab", "#fff"),
         '<path d="M400 230 Q360 226 330 214" fill="none" stroke="#e76f51" stroke-width="20" stroke-linecap="round"/>',
         f'<circle cx="324" cy="212" r="12" fill="{SKIN[1]}"/>', cone(320, 170, 1.2, "#7f5539", "#e9c46a"),
         carrow(130, 70, 200, 20, 270, 70, "#6c757d", 4, 12), carrow(270, 90, 200, 50, 130, 90, "#6c757d", 4, 12)]
    return svg(b, "#fff4e6")


def box(x, y, w, h, flaps=True):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#d4a373"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="10" fill="#c08552"/>']
    if flaps:
        out += [f'<polygon points="{x},{y} {x - 22},{y - 26} {x + 10},{y - 22} {x + 16},{y}" fill="#e6ccb2"/>',
                f'<polygon points="{x + w},{y} {x + w + 22},{y - 26} {x + w - 10},{y - 22} {x + w - 16},{y}" fill="#e6ccb2"/>']
    return "".join(out)


def affinity_for():
    b = ['<rect y="320" width="400" height="80" fill="#cdb4db" opacity=".5"/>',
         box(20, 250, 90, 74), box(300, 236, 84, 88), box(320, 170, 60, 66, False),
         shadow(200, 330, 90, 8),
         # the cat, curled up in its favourite box
         '<path d="M290 236 Q320 210 300 180" fill="none" stroke="#f4a261" stroke-width="14" stroke-linecap="round"/>',
         '<ellipse cx="200" cy="232" rx="78" ry="30" fill="#f4a261"/>',
         '<circle cx="170" cy="206" r="36" fill="#f4a261"/>',
         '<polygon points="140,190 140,154 164,176" fill="#f4a261"/><polygon points="176,174 198,152 202,188" fill="#f4a261"/>',
         '<polygon points="146,184 146,164 158,176" fill="#ffb4a2"/><polygon points="182,176 194,162 196,184" fill="#ffb4a2"/>',
         f'<path d="M150 208 Q157 214 164 208 M178 208 Q185 214 192 208" fill="none" stroke="{INK}" stroke-width="3" '
         'stroke-linecap="round"/>',
         f'<path d="M164 222 Q171 228 178 222" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>',
         '<path d="M190 224 l24 -4 M190 230 l24 4 M152 224 l-24 -4 M152 230 l-24 4" stroke="#fff" stroke-width="2"/>',
         box(110, 236, 180, 92),
         '<path d="M240 240 Q256 216 236 200" fill="none" stroke="#f4a261" stroke-width="12" stroke-linecap="round"/>',
         heart(130, 120, 14), heart(210, 96, 18), heart(270, 140, 11, "#f4a261"), heart(60, 180, 10, "#f4a261")]
    return svg(b, "#fdf6ec")


def inviting():
    rnd = random.Random(19)
    b = ['<rect width="400" height="400" fill="#264653"/>']
    for _ in range(60):
        b.append(f'<circle cx="{f(rnd.uniform(0, 400))}" cy="{f(rnd.uniform(0, 330))}" r="{rnd.choice((2, 2.5, 3))}" '
                 'fill="#fff" opacity=".9"/>')
    b += ['<rect x="60" y="120" width="280" height="210" fill="#bc6c25"/>',
          '<polygon points="40,124 200,50 360,124" fill="#7f5539"/>',
          '<path d="M44 122 Q200 52 356 122" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round"/>',
          '<rect x="150" y="96" width="100" height="24" rx="4" fill="#e9d8c4"/>',
          '<path d="M186 104 h20 v10 a6 6 0 0 1 -6 6 h-8 a6 6 0 0 1 -6 -6 Z M206 106 h4 a3 3 0 0 1 0 8 h-4" fill="#7f5539"/>',
          # warm windows with steaming cups
          '<rect x="80" y="150" width="90" height="80" rx="4" fill="#ffd166"/>',
          '<rect x="80" y="150" width="90" height="80" rx="4" fill="none" stroke="#6f4518" stroke-width="5"/>',
          '<rect x="96" y="200" width="20" height="18" rx="3" fill="#e76f51"/><rect x="130" y="200" width="20" height="18" '
          'rx="3" fill="#fff"/>',
          '<path d="M104 196 q-4 -8 0 -16 M140 196 q4 -8 0 -16" fill="none" stroke="#fff" stroke-width="3" '
          'stroke-linecap="round"/>',
          # the open door and its light on the snow
          '<polygon points="220,330 300,330 360,400 160,400" fill="#ffd166" opacity=".55"/>',
          '<rect x="220" y="170" width="80" height="160" fill="#ffd166"/>',
          '<polygon points="220,170 244,182 244,322 220,330" fill="#6f4518"/>',
          '<path d="M0 330 Q100 320 200 330 T400 326 V400 H0Z" fill="#fff" opacity=".9"/>',
          '<polygon points="220,330 300,330 350,400 170,400" fill="#ffd166" opacity=".4"/>',
          '<path d="M60 120 H340" stroke="#fff" stroke-width="8" stroke-linecap="round"/>']
    for x in range(70, 340, 30):
        b.append(f'<circle cx="{x}" cy="132" r="5" fill="#ffd166"/>')
    b += [pine(30, 340, 90, "#2d6a4f"), pine(370, 340, 80, "#2d6a4f")]
    return svg(b, "#264653")


def clashed_with():
    helmet = ('<path d="M-25 -170 Q-26 -206 0 -206 Q26 -206 25 -170 Z" fill="#6c757d"/>'
              '<path d="M0 -206 Q-6 -222 4 -228" fill="none" stroke="#e63946" stroke-width="6" stroke-linecap="round"/>')
    b = ['<rect y="330" width="400" height="70" fill="#a7c957"/>', shadow(100, 334, 40), shadow(300, 334, 40),
         person(100, 332, 1.1, "#e0ac69", "#457b9d", "#6c757d", "#000", "none", mood="angry",
                larm=((-12, 40), (-16, 72)), rarm=((40, -20), (66, -50)), extra=helmet),
         person(300, 332, 1.1, "#8d5524", "#e76f51", "#6c757d", "#000", "none", mood="angry",
                larm=((-40, -20), (-66, -50)), rarm=((12, 40), (16, 72)), extra=helmet),
         # crossed swords
         '<line x1="176" y1="122" x2="282" y2="30" stroke="#dee2e6" stroke-width="9" stroke-linecap="round"/>',
         '<line x1="224" y1="122" x2="118" y2="30" stroke="#dee2e6" stroke-width="9" stroke-linecap="round"/>',
         '<rect x="166" y="120" width="26" height="8" rx="3" fill="#e9c46a" transform="rotate(-41 179 124)"/>',
         '<rect x="208" y="120" width="26" height="8" rx="3" fill="#e9c46a" transform="rotate(41 221 124)"/>',
         star(200, 82, 30, "#ffd166", .4), star(200, 82, 14, "#fff", .45)]
    for a in range(-150, 40, 34):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(200 + 38 * ca)}" y1="{f(82 + 38 * sa)}" x2="{f(200 + 54 * ca)}" y2="{f(82 + 54 * sa)}" '
                 'stroke="#f4a261" stroke-width="4" stroke-linecap="round"/>')
    return svg(b, "#e3f2fd")


def race_car(x, y, op=1.0, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})" opacity="{op}">'
            '<path d="M-60 -6 V-22 L-40 -26 L-20 -44 H14 L30 -26 L64 -20 V-6 Z" fill="#e63946"/>'
            '<rect x="-64" y="-40" width="10" height="20" fill="#e63946"/>'
            '<path d="M-14 -40 H10 L20 -27 H-14 Z" fill="#caf0f8"/>'
            '<circle cx="-36" cy="-4" r="14" fill="#212529"/><circle cx="-36" cy="-4" r="5" fill="#adb5bd"/>'
            '<circle cx="40" cy="-4" r="14" fill="#212529"/><circle cx="40" cy="-4" r="5" fill="#adb5bd"/>'
            '<circle cx="-2" cy="-16" r="7" fill="#fff"/></g>')


def accelerate():
    b = ['<rect y="230" width="400" height="170" fill="#495057"/>',
         '<path d="M0 340 H400" stroke="#fff" stroke-width="4" stroke-dasharray="26 18"/>',
         '<rect y="226" width="400" height="8" fill="#e63946"/>']
    for r in range(8):
        for c in range(2):
            b.append(f'<rect x="{20 + c * 10}" y="{236 + r * 20}" width="10" height="10" fill="#fff"/>'
                     f'<rect x="{30 - c * 10}" y="{246 + r * 20}" width="10" height="10" fill="#fff"/>')
    b += [race_car(84, 316, .2, .72), race_car(140, 316, .35, .72), race_car(214, 316, .6, .72),
          race_car(322, 316, 1.0, .72)]
    for y, l in ((280, 90), (296, 120), (312, 70)):
        b.append(f'<line x1="{266 - l}" y1="{y}" x2="266" y2="{y}" stroke="#fff" stroke-width="4" stroke-linecap="round" '
                 'opacity=".8"/>')
    b += [arrow(70, 190, 110, 190, "#e76f51", 3, 10), arrow(140, 170, 210, 170, "#e76f51", 5, 13),
          arrow(240, 145, 370, 145, "#e76f51", 8, 20),
          '<circle cx="60" cy="60" r="26" fill="#ffd166"/>']
    return svg(b, "#cfe8f3")


def partition():
    b = ['<rect y="300" width="400" height="100" fill="#d4a373"/>',
         '<rect x="0" y="20" width="400" height="10" fill="#adb5bd"/>',
         # left room: a desk; right room: a bed
         '<rect x="30" y="230" width="100" height="12" rx="3" fill="#7f5539"/>',
         '<rect x="40" y="242" width="8" height="60" fill="#6f4518"/><rect x="114" y="242" width="8" height="60" '
         'fill="#6f4518"/>',
         '<rect x="60" y="196" width="40" height="34" rx="3" fill="#457b9d"/>',
         '<rect x="40" y="90" width="70" height="60" fill="#caf0f8" stroke="#fff" stroke-width="6"/>',
         '<rect x="270" y="250" width="110" height="40" rx="6" fill="#e76f51"/>',
         '<rect x="270" y="220" width="16" height="80" fill="#7f5539"/>',
         '<rect x="292" y="240" width="40" height="16" rx="6" fill="#fff"/>',
         '<circle cx="330" cy="110" r="22" fill="#ffd166"/>']
    # the folding wall, pulled across the middle
    for k in range(6):
        x = 170 + k * 12
        c = "#e9c46a" if k % 2 else "#d4a373"
        b.append(f'<polygon points="{x},30 {x + 12},36 {x + 12},300 {x},306" fill="{c}"/>')
    b += ['<rect x="166" y="24" width="84" height="8" fill="#6c757d"/>',
          arrow(150, 170, 106, 170, INK, 5, 14), arrow(262, 170, 306, 170, INK, 5, 14)]
    return svg(b, "#f1faee")


def deceptive():
    wolf = ('<g transform="translate(170 316) scale(1.3)">'
            '<path d="M-36 -20 Q-70 -14 -82 -44" fill="none" stroke="#6c757d" stroke-width="12" stroke-linecap="round"/>'
            f'<path d="M-24 -14 V4 M-8 -14 V4 M10 -14 V4 M24 -14 V4" stroke="#495057" stroke-width="7" '
            'stroke-linecap="round"/>'
            + "".join(f'<circle cx="{dx}" cy="{dy}" r="{r}" fill="#fff"/>' for dx, dy, r in
                      ((-30, -46, 20), (-4, -54, 22), (24, -46, 20), (-18, -28, 20), (14, -28, 20)))
            + '<path d="M30 -70 L36 -100 L50 -76 Z M54 -76 L68 -100 L70 -70 Z" fill="#6c757d"/>'
            '<path d="M30 -74 Q30 -40 52 -36 Q90 -40 92 -58 Q76 -76 54 -80 Q36 -82 30 -74 Z" fill="#6c757d"/>'
            '<path d="M60 -50 Q76 -44 90 -54" fill="none" stroke="#fff" stroke-width="2"/>'
            '<path d="M66 -48 l3 6 l3 -6 M76 -48 l3 6 l3 -6" fill="#fff"/>'
            '<circle cx="92" cy="-58" r="5" fill="#212529"/>'
            '<path d="M44 -66 L56 -62" stroke="#212529" stroke-width="3" stroke-linecap="round"/>'
            '<circle cx="52" cy="-58" r="3.5" fill="#ffd166"/>'
            + "".join(f'<circle cx="{dx}" cy="{dy}" r="{r}" fill="#fff"/>' for dx, dy, r in ((30, -80, 10), (44, -86, 9)))
            + '</g>')
    b = ['<rect y="170" width="400" height="230" fill="#a7c957"/>', '<circle cx="60" cy="60" r="26" fill="#ffd166"/>',
         bush(340, 166, 22), bush(380, 172, 16),
         sheep(60, 236, k=.8), sheep(350, 236, True, .8), sheep(56, 380, k=1.0), sheep(350, 384, True, 1.0), wolf]
    return svg(b, "#cfe8f3")


def unpredictable():
    rnd = random.Random(23)
    b = ['<rect width="200" height="140" fill="#fff3b0"/>', '<rect x="200" width="200" height="140" fill="#adb5bd"/>',
         '<rect y="140" width="200" height="140" fill="#dee2e6"/>', '<rect x="200" y="140" width="200" height="140" '
         'fill="#6c757d"/>',
         '<circle cx="90" cy="64" r="32" fill="#ffd166"/>']
    for a in range(0, 360, 45):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(90 + 40 * ca)}" y1="{f(64 + 40 * sa)}" x2="{f(90 + 52 * ca)}" y2="{f(64 + 52 * sa)}" '
                 'stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>')
    b += ['<ellipse cx="300" cy="50" rx="66" ry="24" fill="#6c757d"/>']
    for x in range(250, 360, 18):
        b.append(f'<line x1="{x}" y1="84" x2="{x - 6}" y2="104" stroke="#4895ef" stroke-width="3" stroke-linecap="round"/>')
    b += ['<ellipse cx="96" cy="170" rx="66" ry="22" fill="#adb5bd"/>']
    for _ in range(14):
        x, y = rnd.uniform(40, 160), rnd.uniform(200, 260)
        b.append(sparkle(x, y, 5, "#fff"))
    b += ['<ellipse cx="300" cy="166" rx="66" ry="22" fill="#343a40"/>',
          '<polygon points="300,186 284,220 298,220 284,256 320,212 304,212 316,186" fill="#ffd166"/>',
          '<polygon points="0,400 0,320 120,200 170,240 220,170 290,250 400,300 400,400" fill="#6d597a"/>',
          '<polygon points="220,170 246,200 230,206 220,196 208,208 198,198" fill="#fff"/>',
          '<rect y="360" width="400" height="40" fill="#52b788"/>']
    return svg(b, "#dee2e6")


def renounce():
    crown = ('<path d="M0 0 L-4 -30 L12 -14 L24 -36 L36 -14 L52 -30 L48 0 Z" fill="#e9c46a"/>'
             '<circle cx="24" cy="-12" r="5" fill="#e63946"/>')
    b = ['<rect y="330" width="400" height="70" fill="#9c6b3c"/>',
         '<rect x="0" y="0" width="400" height="330" fill="#9d0208" opacity=".25"/>',
         '<rect x="30" y="250" width="120" height="12" rx="3" fill="#7f5539"/>',
         '<rect x="44" y="262" width="10" height="70" fill="#6f4518"/><rect x="126" y="262" width="10" height="70" '
         'fill="#6f4518"/>',
         '<ellipse cx="90" cy="244" rx="46" ry="10" fill="#e63946"/>',
         f'<g transform="translate(66 240)">{crown}</g>', sparkle(140, 196, 9, "#ffd166"),
         shadow(270, 334, 40),
         '<path d="M240 160 Q270 150 300 160 L326 304 Q270 314 214 304 Z" fill="#9d0208"/>',
         person(270, 332, 1.15, SKIN[0], "#e63946", "#264653", "#adb5bd", "short", mood="closed",
                larm=((-14, 40), (-24, 72)), rarm=((14, 40), (26, 70)),
                lleg=((-14, 44), (-24, 86)), rleg=((14, 44), (24, 86))),
         '<path d="M190 300 h-30 M196 280 h-40" stroke="#6c757d" stroke-width="4" stroke-linecap="round"/>',
         arrow(320, 140, 380, 140, INK, 6, 16)]
    return svg(b, "#fdf0d5")


def oversees():
    b = ['<rect y="320" width="400" height="80" fill="#adb5bd"/>',
         # balcony with the supervisor
         '<g transform="translate(0 18)">',
         '<rect x="0" y="130" width="150" height="16" fill="#6c757d"/>',
         '<path d="M0 100 H150 M20 100 V130 M50 100 V130 M80 100 V130 M110 100 V130 M140 100 V130" stroke="#495057" '
         'stroke-width="5"/>',
         person(70, 130, .6, SKIN[2], "#457b9d", "#264653", "#1b1b1b", "short", mood="down",
                larm=((-12, 40), (-14, 74)), rarm=((24, 10), (34, -6))),
         '<rect x="88" y="48" width="18" height="24" rx="2" fill="#e9c46a"/></g>',
         # conveyor belt and workers
         '<rect x="120" y="270" width="270" height="20" rx="10" fill="#495057"/>',
         '<circle cx="132" cy="280" r="8" fill="#6c757d"/><circle cx="378" cy="280" r="8" fill="#6c757d"/>',
         '<rect x="140" y="290" width="8" height="32" fill="#6c757d"/><rect x="364" y="290" width="8" height="32" '
         'fill="#6c757d"/>']
    for x in (160, 230, 300, 350):
        b.append(f'<rect x="{x}" y="244" width="30" height="26" fill="#d4a373"/><rect x="{x + 12}" y="244" width="6" '
                 'height="26" fill="#e9c46a"/>')
    for x, sk, c in ((200, SKIN[0], "#f4a261"), (280, SKIN[3], "#2a9d8f"), (360, SKIN[1], "#e76f51")):
        b.append(person(x, 366, .55, sk, c, "#264653", "#5c4033", "cap", mood="smile",
                        larm=((-14, 30), (-6, 50)), rarm=((14, 30), (6, 50))))
    b += [f'<path d="M86 68 L200 230 M86 68 L280 230 M86 68 L360 230" stroke="{INK}" stroke-width="2.5" '
          'stroke-dasharray="6 6" opacity=".55"/>',
          '<rect x="0" y="164" width="20" height="158" fill="#6c757d"/><rect x="120" y="164" width="20" height="106" '
          'fill="#6c757d"/>']
    return svg(b, "#e9ecef")


PICTURES = {
    "fruitless": fruitless,
    "precursors": precursors,
    "bypassed": bypassed,
    "ignore": ignore,
    "source": source,
    "rejected": rejected,
    "appeased": appeased,
    "inherited": inherited,
    "rival": rival,
    "worried": worried,
    "create": create,
    "suspicious": suspicious,
    "determined": determined,
    "praised": praised,
    "improvise": improvise,
    "trace": trace,
    "alter": alter,
    "anticipating": anticipating,
    "persuade": persuade,
    "imaginative": imaginative,
    "sketch": sketch,
    "imitated": imitated,
    "exposed": exposed,
    "subdued": subdued,
    "catastrophic": catastrophic,
    "craft": craft,
    "visualize": visualize,
    "gaining on": gaining_on,
    "exaggerate": exaggerate,
    "reconcile": reconcile,
    "paucity of": paucity_of,
    "refute": refute,
    "offered": offered,
    "costly": costly,
    "surrendered": surrendered,
    "powerful": powerful,
    "discovered": discovered,
    "focused": focused,
    "extended": extended,
    "insurmountable": insurmountable,
    "choose": choose,
    "affinity for": affinity_for,
    "inviting": inviting,
    "clashed with": clashed_with,
    "accelerate": accelerate,
    "partition": partition,
    "deceptive": deceptive,
    "unpredictable": unpredictable,
    "renounce": renounce,
    "oversees": oversees,
}
