"""Batch 5: drawings 181-230 (each function returns one SVG; PICTURES maps word -> function).

The figures and small shapes come from batch_02.py, batch_03.py and batch_04.py.
"""

import math
import random

from batch_02 import SKIN, cactus, heart, limb, person, shadow, sheep, sparkle
from batch_03 import bicycle, dog, side_runner, teddy
from batch_04 import bulb
from common import INK, arrow, bush, carrow, f, pine, svg


def diamond(x, y, k=1.0, fill="#4895ef", light="#a8dadc", dark="#457b9d"):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<polygon points="-24,-20 24,-20 38,-4 0,40 -38,-4" fill="' + fill + '"/>'
            '<polygon points="-24,-20 24,-20 12,-4 -12,-4" fill="' + light + '"/>'
            '<polygon points="-38,-4 -12,-4 0,40" fill="' + dark + '"/>'
            '<polygon points="12,-4 38,-4 0,40" fill="#3a86ff" opacity=".6"/></g>')


# ---------------------------------------------------------------------------------------------

def valuable():
    b = ['<rect y="330" width="400" height="70" fill="#7f5539"/>',
         shadow(110, 334, 36),
         person(110, 332, 1.2, SKIN[1], "#495057", "#264653", "#adb5bd", "short", mood="wide",
                larm=((-12, 40), (-14, 72)), rarm=((40, -6), (84, -14))),
         '<line x1="218" y1="166" x2="246" y2="154" stroke="#adb5bd" stroke-width="5" stroke-linecap="round"/>',
         '<line x1="218" y1="174" x2="246" y2="170" stroke="#adb5bd" stroke-width="5" stroke-linecap="round"/>',
         '<circle cx="290" cy="160" r="70" fill="#fff3b0" opacity=".45"/>',
         diamond(290, 156, 1.5),
         sparkle(220, 90, 12, "#ffd166"), sparkle(366, 80, 14, "#ffd166"), sparkle(360, 230, 10, "#ffd166"),
         sparkle(230, 250, 8, "#ffd166")]
    for a in range(-170, 20, 30):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(290 + 80 * ca)}" y1="{f(160 + 80 * sa)}" x2="{f(290 + 96 * ca)}" y2="{f(160 + 96 * sa)}" '
                 'stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>')
    return svg(b, "#3d405b")


def delivered():
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>',
         '<polygon points="0,300 60,220 130,300" fill="#6a994e"/><polygon points="280,300 360,200 440,300" fill="#6a994e"/>',
         # the helicopter
         '<rect x="150" y="26" width="200" height="8" rx="4" fill="#495057"/>',
         '<rect x="246" y="32" width="8" height="18" fill="#495057"/>',
         '<path d="M190 60 Q190 46 214 46 H290 Q318 50 318 80 Q318 100 290 100 H214 Q190 100 190 80 Z" fill="#e63946"/>',
         '<path d="M290 54 Q312 58 312 80 H280 V54 Z" fill="#caf0f8"/>',
         '<path d="M190 70 H110 L100 56 H92 L96 82 H190" fill="#e63946"/>',
         '<path d="M206 108 H300 M220 100 V108 M286 100 V108" stroke="#495057" stroke-width="4"/>',
         # the box on its line
         '<line x1="252" y1="100" x2="252" y2="214" stroke="#495057" stroke-width="3"/>',
         '<path d="M252 214 L226 230 M252 214 L278 230" stroke="#495057" stroke-width="2"/>',
         '<rect x="222" y="228" width="60" height="44" fill="#d4a373"/>',
         '<rect x="248" y="228" width="8" height="44" fill="#e9c46a"/>',
         # the village
         '<rect x="40" y="270" width="60" height="44" fill="#e6ccb2"/><polygon points="32,272 70,236 108,272" fill="#9c6644"/>',
         '<rect x="330" y="276" width="50" height="38" fill="#e6ccb2"/><polygon points="322,278 355,248 388,278" fill="#9c6644"/>',
         person(150, 330, .55, SKIN[3], "#f4a261", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-24, -24), (-36, -56)), rarm=((24, -24), (36, -56))),
         person(300, 336, .5, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "bun", mood="grin",
                larm=((-12, 40), (-14, 72)), rarm=((24, -24), (36, -56))),
         arrow(312, 160, 312, 220, "#264653", 4, 12)]
    return svg(b, "#cfe8f3")


def paper_stack(x, y, n, w=70, rot_seed=1):
    rnd = random.Random(rot_seed)
    out = []
    for k in range(n):
        out.append(f'<rect x="{f(x - w / 2 + rnd.uniform(-3, 3))}" y="{y - (k + 1) * 7}" width="{w}" height="7" '
                   f'fill="{"#fff" if k % 2 else "#f1f3f5"}" stroke="#dee2e6" stroke-width="1"/>')
    return "".join(out)


def tedious():
    b = ['<rect y="330" width="400" height="70" fill="#8d6e63"/>',
         '<circle cx="330" cy="60" r="28" fill="#fff" stroke="#495057" stroke-width="5"/>',
         '<path d="M330 60 V40 M330 60 L344 68" stroke="#495057" stroke-width="4" stroke-linecap="round"/>',
         person(170, 330, 1.05, SKIN[0], "#adb5bd", "#495057", "#7f5539", "short", mood="down",
                brows="M-14 -186 L-4 -190 M4 -190 L14 -186",
                larm=((-10, 34), (6, 54)), rarm=((16, 34), (30, 52))),
         '<rect x="40" y="260" width="340" height="14" rx="4" fill="#7f5539"/>',
         '<rect x="56" y="274" width="12" height="60" fill="#6f4518"/><rect x="352" y="274" width="12" height="60" fill="#6f4518"/>',
         '<rect x="140" y="246" width="60" height="16" fill="#fff" stroke="#dee2e6" stroke-width="2"/>',
         '<path d="M146 252 h40 M146 257 h30" stroke="#adb5bd" stroke-width="2"/>',
         '<line x1="200" y1="252" x2="214" y2="234" stroke="#264653" stroke-width="4" stroke-linecap="round"/>',
         paper_stack(310, 260, 26, 76, 3), paper_stack(60, 260, 4, 60, 4),
         '<path d="M134 136 q-8 -10 -2 -20 M150 128 q-2 -12 6 -18" fill="none" stroke="#6c757d" stroke-width="3" '
         'stroke-linecap="round" opacity=".0"/>',
         '<path d="M208 128 Q202 140 208 144 Q214 140 208 128 Z" fill="#8ecae6"/>']
    return svg(b, "#e9ecef")


def hard_hat(color="#ffd166"):
    return (f'<path d="M-26 -186 Q-26 -210 0 -210 Q26 -210 26 -186 Z" fill="{color}"/>'
            f'<rect x="-30" y="-190" width="60" height="7" rx="3" fill="{color}"/>')


def collaboration():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         '<rect x="0" y="80" width="30" height="250" fill="#adb5bd"/><rect x="370" y="80" width="30" height="250" fill="#adb5bd"/>']
    xs = (70, 160, 250, 340)
    for k, x in enumerate(xs):
        b.append(shadow(x, 334, 30))
        b.append(person(x, 332, .9, SKIN[k % 4], ("#f4a261", "#2a9d8f", "#e76f51", "#457b9d")[k], "#264653",
                        "#3e2723", "none", mood="grin", brows="M-14 -190 L-3 -186 M3 -186 L14 -190",
                        larm=((-12, -36), (-4, -76)), rarm=((12, -36), (4, -76)), extra=hard_hat()))
    b += ['<rect x="20" y="104" width="360" height="26" rx="4" fill="#b08968"/>',
          '<path d="M30 114 H370 M30 122 H370" stroke="#9c6b3c" stroke-width="2"/>']
    b += [arrow(200, 70, 200, 30, "#e76f51", 5, 14)]
    return svg(b, "#e3f2fd")


def cookie(x, y, r=14):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{r}" fill="#d4a373"/>'
            + "".join(f'<circle cx="{f(x + dx * r)}" cy="{f(y + dy * r)}" r="{f(r * .14)}" fill="#5c4033"/>'
                      for dx, dy in ((-.4, -.3), (.3, -.4), (.1, .2), (-.3, .45), (.5, .3))))


def limited():
    b = ['<rect y="320" width="400" height="80" fill="#d4a373"/>',
         person(200, 330, .95, SKIN[1], "#e63946", "#264653", "#5c4033", "short", mood="wide",
                larm=((-6, 34), (8, 58)), rarm=((6, 34), (-8, 58))),
         '<rect x="140" y="210" width="120" height="112" rx="22" fill="#eef7fb" stroke="#8ecae6" stroke-width="5"/>',
         '<rect x="150" y="194" width="100" height="22" rx="6" fill="#e76f51"/>',
         cookie(184, 302, 15), cookie(216, 304, 15),
         '<rect x="150" y="228" width="10" height="76" rx="5" fill="#fff" opacity=".6"/>',
         person(60, 360, .8, SKIN[0], "#2a9d8f", "#264653", "#7f5539", "bun", mood="wide",
                larm=((-12, 40), (-14, 72)), rarm=((30, -10), (70, -30))),
         person(340, 360, .8, SKIN[3], "#e9c46a", "#264653", "#1b1b1b", "short", mood="wide",
                larm=((-30, -10), (-70, -30)), rarm=((12, 40), (14, 72)))]
    return svg(b, "#fdf6ec")


def overcome():
    b = ['<rect y="300" width="400" height="100" fill="#e76f51"/>',
         '<path d="M0 340 H400 M0 380 H400" stroke="#fff" stroke-width="3" opacity=".7"/>',
         # a very high hurdle
         '<rect x="186" y="196" width="10" height="134" fill="#adb5bd"/><rect x="250" y="196" width="10" height="134" fill="#adb5bd"/>',
         '<rect x="176" y="190" width="94" height="16" fill="#fff"/>',
         '<path d="M186 190 h18 v16 h-18 Z M222 190 h18 v16 h-18 Z" fill="#e63946"/>',
         '<path d="M60 320 Q140 90 330 300" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="8 8"/>',
         shadow(220, 330, 40, 5),
         '<g transform="rotate(-10 230 176)">' + side_runner(226, 178, .9, "#2a9d8f", SKIN[2], "#1b1b1b") + '</g>',
         sparkle(310, 80, 10, "#ffd166"), sparkle(140, 90, 8, "#ffd166")]
    return svg(b, "#e3f2fd")


def hawk(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<path d="M0 0 Q-30 -20 -70 -8 Q-40 -4 -20 6 Z" fill="#7f5539"/>'
            '<path d="M0 0 Q30 -20 70 -8 Q40 -4 20 6 Z" fill="#7f5539"/>'
            '<ellipse cx="0" cy="4" rx="12" ry="18" fill="#9c6644"/>'
            '<path d="M-8 20 L0 34 L8 20 Z" fill="#7f5539"/>'
            '<circle cx="0" cy="-10" r="8" fill="#e6ccb2"/><polygon points="-3,-6 3,-6 0,2" fill="#e9c46a"/></g>')


def hiding():
    rnd = random.Random(3)
    b = ['<ellipse cx="200" cy="110" rx="140" ry="40" fill="none" stroke="#6c757d" stroke-width="2.5" '
         'stroke-dasharray="8 8"/>',
         hawk(300, 90, 1.0),
         '<rect y="240" width="400" height="160" fill="#a7c957"/>',
         # the rabbit, only its ears and eyes showing
         '<ellipse cx="190" cy="250" rx="10" ry="34" fill="#adb5bd" transform="rotate(-10 190 250)"/>',
         '<ellipse cx="214" cy="250" rx="10" ry="34" fill="#adb5bd" transform="rotate(10 214 250)"/>',
         '<ellipse cx="190" cy="250" rx="4" ry="24" fill="#ffb4a2" transform="rotate(-10 190 250)"/>',
         '<ellipse cx="214" cy="250" rx="4" ry="24" fill="#ffb4a2" transform="rotate(10 214 250)"/>',
         '<circle cx="202" cy="300" r="30" fill="#adb5bd"/>',
         '<circle cx="192" cy="296" r="5" fill="#fff"/><circle cx="212" cy="296" r="5" fill="#fff"/>',
         f'<circle cx="193" cy="294" r="2.5" fill="{INK}"/><circle cx="213" cy="294" r="2.5" fill="{INK}"/>']
    for _ in range(120):
        x = rnd.uniform(0, 400)
        h = rnd.uniform(60, 130)
        y0 = rnd.uniform(380, 405)
        b.append(f'<path d="M{f(x)} {f(y0)} Q{f(x + rnd.uniform(-8, 8))} {f(y0 - h * .6)} {f(x + rnd.uniform(-14, 14))} '
                 f'{f(y0 - h)}" fill="none" stroke="{rnd.choice(("#52b788", "#40916c", "#6a994e", "#2d6a4f"))}" '
                 'stroke-width="5" stroke-linecap="round"/>')
    return svg(b, "#cfe8f3")


def superficial():
    b = ['<rect y="160" width="400" height="240" fill="#4895ef"/>',
         '<rect y="160" width="400" height="240" fill="#1d3557" opacity=".25"/>',
         # the small tip above the water and the huge part below
         '<polygon points="160,160 196,104 220,120 248,160" fill="#fff"/>',
         '<polygon points="196,104 220,120 212,160 186,160" fill="#e9ecef"/>',
         '<polygon points="160,160 248,160 330,240 340,330 270,390 120,392 60,320 80,230" fill="#caf0f8" opacity=".75"/>',
         '<polygon points="160,160 120,240 130,330 180,390 120,392 60,320 80,230" fill="#a8dadc" opacity=".6"/>',
         '<path d="M0 160 Q25 152 50 160 T100 160 T150 160 T200 160 T250 160 T300 160 T350 160 T400 160" fill="none" '
         'stroke="#fff" stroke-width="4"/>',
         # the little boat
         '<path d="M310 160 H380 L370 176 H320 Z" fill="#e76f51"/>',
         '<path d="M344 158 V110 L366 150 Z" fill="#fff"/>',
         '<circle cx="330" cy="150" r="7" fill="#f1c27d"/>',
         '<path d="M322 148 L250 128" stroke="#6c757d" stroke-width="2" stroke-dasharray="5 5"/>',
         '<circle cx="80" cy="60" r="26" fill="#ffd166"/>']
    return svg(b, "#cfe8f3")


def wheelchair_user(x, y, k=1.0, shirt="#2a9d8f", skin=SKIN[2]):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<circle cx="-6" cy="-40" r="40" fill="none" stroke="#343a40" stroke-width="7"/>'
            '<circle cx="-6" cy="-40" r="4" fill="#343a40"/>'
            '<circle cx="44" cy="-10" r="10" fill="none" stroke="#343a40" stroke-width="5"/>'
            '<path d="M-36 -100 V-54 H34 L44 -20" fill="none" stroke="#6c757d" stroke-width="6" stroke-linejoin="round"/>'
            + limb(((-14, -60), (26, -60), (30, -20)), "#264653", 14)
            + f'<ellipse cx="34" cy="-16" rx="11" ry="6" fill="{INK}"/>'
            + limb(((-18, -64), (-14, -110)), shirt, 26)
            + limb(((-12, -104), (8, -82), (-2, -62)), shirt, 10) + f'<circle cx="-4" cy="-58" r="6" fill="{skin}"/>'
            + f'<circle cx="-10" cy="-132" r="18" fill="{skin}"/>'
            '<path d="M-28 -132 Q-30 -152 -10 -152 Q8 -152 8 -136 Q-6 -144 -28 -132 Z" fill="#1b1b1b"/>'
            f'<circle cx="-2" cy="-132" r="2.5" fill="{INK}"/><circle cx="-14" cy="-132" r="2.5" fill="{INK}"/>'
            f'<path d="M-12 -124 Q-6 -120 0 -124" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/></g>')


def accessible():
    b = ['<rect y="330" width="400" height="70" fill="#adb5bd"/>',
         # the library entrance
         '<rect x="230" y="70" width="170" height="210" fill="#e9d8c4"/>',
         '<polygon points="220,74 315,30 410,74" fill="#b08968"/>',
         '<rect x="250" y="100" width="14" height="180" fill="#fff"/><rect x="366" y="100" width="14" height="180" fill="#fff"/>',
         '<rect x="290" y="190" width="56" height="90" fill="#7f5539"/>',
         '<rect x="292" y="120" width="52" height="40" rx="4" fill="#457b9d"/>',
         '<path d="M300 150 V128 Q318 124 318 132 Q318 124 336 128 V150 Q318 146 318 152 Q318 146 300 150 Z" fill="#fff"/>',
         '<rect x="220" y="280" width="180" height="50" fill="#ced4da"/>',
         # the ramp
         '<polygon points="20,330 220,280 220,330" fill="#dee2e6"/>',
         '<path d="M20 326 L220 276" stroke="#6c757d" stroke-width="4"/>',
         '<path d="M40 302 L220 256 M40 302 V326 M130 280 V304 M220 256 V280" stroke="#495057" stroke-width="4" fill="none"/>',
         f'<g transform="rotate(-14 120 300)">{wheelchair_user(120, 306, .95)}</g>',
         arrow(150, 220, 200, 206, "#2a9d8f", 5, 14)]
    return svg(b, "#cfe8f3")



def conceal():
    rnd = random.Random(6)
    b = ['<path d="M0 230 Q120 200 240 220 T400 200" fill="none" stroke="#6f4518" stroke-width="16" stroke-linecap="round"/>']
    leaves = []
    while len(leaves) < 60:
        x, y = rnd.uniform(0, 400), rnd.uniform(60, 360)
        if len(leaves) >= 30 and (110 < x < 350 and 140 < y < 250 or math.hypot(x - 306, y - 198) < 50):
            continue
        leaves.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="22" ry="11" fill="{rnd.choice(("#52b788", "#40916c", "#74c69d"))}" '
                      f'transform="rotate({rnd.randint(-60, 60)} {f(x)} {f(y)})"/>')
    b = leaves[:30] + b
    # the chameleon, the same greens as the leaves
    b += ['<path d="M120 220 Q110 150 200 150 Q280 150 290 210 Z" fill="#52b788"/>',
          '<path d="M130 210 Q170 190 200 206 Q230 190 280 206" fill="none" stroke="#40916c" stroke-width="5"/>',
          '<path d="M150 180 l10 8 M180 170 l10 8 M210 168 l10 8 M240 174 l10 8" stroke="#74c69d" stroke-width="4" '
          'stroke-linecap="round"/>',
          '<path d="M290 200 Q326 176 330 210 Q318 222 290 218 Z" fill="#52b788"/>',
          '<circle cx="306" cy="198" r="13" fill="#74c69d"/><circle cx="309" cy="198" r="5" fill="#264653"/>',
          '<path d="M120 214 Q80 220 80 250 Q82 274 104 270 Q118 262 108 252 Q96 252 98 244" fill="none" stroke="#52b788" '
          'stroke-width="12" stroke-linecap="round"/>',
          '<path d="M160 214 L150 230 M250 214 L262 230" stroke="#52b788" stroke-width="10" stroke-linecap="round"/>']
    b += leaves[30:]
    b += ['<circle cx="306" cy="198" r="28" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="6 5"/>']
    return svg(b, "#d8f3dc")


def cobweb(x, y, r, flip=False):
    sgn = -1 if flip else 1
    out = [f'<g transform="translate({x} {y}) scale({sgn} 1)" stroke="#dee2e6" stroke-width="2" fill="none">']
    for a in (0, 22, 45, 68, 90):
        out.append(f'<line x1="0" y1="0" x2="{f(r * math.cos(math.radians(a)))}" y2="{f(r * math.sin(math.radians(a)))}"/>')
    for rr in (r * .35, r * .6, r * .85):
        pts = " ".join(f"{f(rr * math.cos(math.radians(a)))},{f(rr * math.sin(math.radians(a)))}" for a in (0, 22, 45, 68, 90))
        out.append(f'<polyline points="{pts}"/>')
    out.append('</g>')
    return "".join(out)


def forgotten():
    rnd = random.Random(2)
    b = ['<polygon points="0,0 400,0 400,40 200,0" fill="#6c757d" opacity=".0"/>',
         '<polygon points="0,0 200,0 0,120" fill="#5c4d43"/><polygon points="400,0 200,0 400,120" fill="#5c4d43"/>',
         '<rect y="300" width="400" height="100" fill="#8d7b6d"/>',
         '<path d="M0 320 H400 M0 350 H400 M0 380 H400" stroke="#7a685b" stroke-width="3"/>',
         '<polygon points="300,0 360,0 260,300 160,300" fill="#fff8e1" opacity=".18"/>',
         cobweb(0, 0, 90), cobweb(400, 0, 80, True),
         '<rect x="40" y="220" width="70" height="80" fill="#9c8577"/><rect x="40" y="220" width="70" height="10" fill="#8a7466"/>',
         '<g opacity=".75">', teddy(220, 288, 1.7), '</g>',
         '<path d="M190 210 l-10 -10 l10 -10 l10 10 Z" fill="none" stroke="#dee2e6" stroke-width="1.5" opacity=".0"/>']
    for _ in range(30):
        x, y = rnd.uniform(160, 330), rnd.uniform(30, 290)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{rnd.choice((1.5, 2, 2.5))}" fill="#fff" opacity=".6"/>')
    b += [cobweb(250, 240, 40)]
    return svg(b, "#a1887f")


def calendar(x, y, k=1.0, mark=None, later=None):
    out = [f'<g transform="translate({f(x)} {f(y)}) scale({k})">',
           '<rect x="0" y="0" width="110" height="100" rx="5" fill="#fff"/>',
           '<rect x="0" y="0" width="110" height="22" rx="5" fill="#e63946"/>']
    for kk in range(12):
        cx, cy = 8 + (kk % 4) * 25, 28 + (kk // 4) * 23
        out.append(f'<rect x="{cx}" y="{cy}" width="20" height="18" rx="2" fill="#f1f3f5"/>')
    if mark is not None and later is not None:
        (a, b2) = mark, later
        ax, ay = 18 + (a % 4) * 25, 37 + (a // 4) * 23
        bx, by = 18 + (b2 % 4) * 25, 37 + (b2 // 4) * 23
        out.append(f'<rect x="{ax - 10}" y="{ay - 9}" width="20" height="18" rx="2" fill="#adb5bd"/>')
        out.append(f'<rect x="{bx - 10}" y="{by - 9}" width="20" height="18" rx="2" fill="#a7c957"/>')
        out.append(carrow(ax, ay - 8, (ax + bx) / 2, ay - 40, bx, by - 10, "#2a9d8f", 3, 9))
    out.append('</g>')
    return "".join(out)


def postpone():
    rnd = random.Random(1)
    b = ['<ellipse cx="120" cy="40" rx="140" ry="40" fill="#8d99ae"/><ellipse cx="300" cy="30" rx="120" ry="36" fill="#adb5bd"/>',
         '<rect y="290" width="400" height="110" fill="#a7c957"/>']
    for _ in range(30):
        x, y = rnd.uniform(0, 240), rnd.uniform(70, 280)
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 4)}" y2="{f(y + 14)}" stroke="#4895ef" stroke-width="3" '
                 'stroke-linecap="round"/>')
    b += [# house on the right
          '<rect x="290" y="190" width="110" height="110" fill="#e9c46a"/>', '<polygon points="280,194 345,140 410,194" fill="#bc6c25"/>',
          '<rect x="316" y="236" width="34" height="64" fill="#7f5539"/>',
          # the picnic blanket left behind, folded
          '<polygon points="30,320 130,320 150,350 10,350" fill="#e63946"/>',
          '<path d="M40 320 L30 350 M70 320 L66 350 M100 320 L104 350" stroke="#fff" stroke-width="4"/>',
          person(210, 330, .8, SKIN[1], "#2a9d8f", "#264653", "#5c4033", "short", mood="smile",
                 larm=((-12, 40), (-14, 72)), rarm=((24, 20), (34, 40))),
          '<path d="M222 230 H260 L254 262 H228 Z" fill="#c08552"/><path d="M228 230 Q241 210 254 230" fill="none" '
          'stroke="#7f5539" stroke-width="4"/>',
          person(260, 336, .6, SKIN[1], "#f4a261", "#457b9d", "#7f5539", "bun", mood="smile",
                 larm=((-24, 10), (-40, 0)), rarm=((12, 40), (14, 72))),
          arrow(240, 150, 300, 150, INK, 5, 14),
          calendar(24, 120, 1.1, 1, 7)]
    return svg(b, "#cfe8f3")


def horse_head(x, y, k, coat, mane, flip=False, stripes=False):
    sgn = -1 if flip else 1
    st = ""
    if stripes:
        st = ''.join(f'<path d="M{dx} -150 Q{dx + 14} -100 {dx - 4} -20" fill="none" stroke="#1b1b1b" stroke-width="9"/>'
                     for dx in (-34, -14, 6, 26)) +              '<path d="M30 -170 Q56 -160 70 -120 M40 -150 Q60 -130 72 -100" fill="none" stroke="#1b1b1b" stroke-width="7"/>'
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sgn * k)} {k})">'
            '<clipPath id="hc' + str(int(x)) + '"><path d="M-50 0 Q-60 -120 -10 -170 Q30 -196 60 -170 Q90 -130 96 -96 '
            'Q100 -76 80 -70 Q50 -80 30 -60 Q20 -30 30 0 Z"/></clipPath>'
            f'<path d="M-50 0 Q-60 -120 -10 -170 Q30 -196 60 -170 Q90 -130 96 -96 Q100 -76 80 -70 Q50 -80 30 -60 Q20 -30 30 0 Z" '
            f'fill="{coat}"/>'
            f'<g clip-path="url(#hc{int(x)})">{st}</g>'
            f'<path d="M-50 0 Q-66 -120 -20 -176 L-6 -170 Q-40 -110 -30 0 Z" fill="{mane}"/>'
            '<path d="M14 -180 L20 -206 L34 -176 Z" fill="' + coat + '"/>'
            f'<circle cx="40" cy="-140" r="6" fill="{INK}"/>'
            f'<ellipse cx="86" cy="-86" rx="5" ry="4" fill="{INK}"/></g>')


def distinctive():
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>',
         horse_head(60, 320, .8, "#9c6644", "#5c4033"),
         horse_head(340, 320, .8, "#8d6e63", "#5c4033", flip=True),
         horse_head(170, 360, 1.15, "#fff", "#1b1b1b", stripes=True),
         sparkle(300, 80, 12, "#ffd166"), sparkle(90, 90, 9, "#ffd166")]
    return svg(b, "#e3f2fd")


def book(x, y, w, h, color, rot=0):
    return (f'<g transform="rotate({rot} {f(x + w / 2)} {f(y + h / 2)})"><rect x="{f(x)}" y="{f(y)}" width="{w}" height="{h}" '
            f'rx="2" fill="{color}"/><rect x="{f(x + 4)}" y="{f(y + 3)}" width="{w - 8}" height="{h - 6}" fill="#fff" '
            f'opacity=".25"/></g>')


def haphazard():
    rnd = random.Random(11)
    colors = ["#e63946", "#2a9d8f", "#e9c46a", "#457b9d", "#f4a261", "#6a994e", "#9c6644"]
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>']
    y = 330
    x = 200
    for k in range(10):
        w, h = rnd.uniform(90, 150), rnd.uniform(16, 26)
        x += rnd.uniform(-18, 18)
        b.append(book(x - w / 2, y - h, w, h, rnd.choice(colors), rnd.uniform(-14, 14)))
        y -= h - 2
    for _ in range(5):
        bx, by = rnd.uniform(20, 380), rnd.uniform(300, 360)
        if 120 < bx < 280:
            continue
        b.append(book(bx - 30, by - 10, 60, 18, rnd.choice(colors), rnd.uniform(-60, 60)))
    b += [book(40, 260, 20, 70, "#457b9d", -24), book(320, 270, 20, 64, "#e63946", 30)]
    return svg(b, "#fdf6ec")


def harsh():
    rnd = random.Random(7)
    b = ['<rect y="320" width="400" height="80" fill="#f8f9fa"/>',
         '<path d="M0 320 Q100 300 200 318 T400 312" fill="#fff"/>']
    for _ in range(80):
        x, y = rnd.uniform(0, 440), rnd.uniform(0, 330)
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 34)}" y2="{f(y + 10)}" stroke="#fff" stroke-width="3" '
                 'stroke-linecap="round" opacity=".85"/>')
    scarf = ('<path d="M-20 -160 H20 L60 -170 L66 -158 L22 -150 H-20 Z" fill="#e63946"/>'
             '<path d="M-26 -176 Q-28 -206 0 -206 Q28 -206 26 -176 Z" fill="#457b9d"/>')
    b += [shadow(170, 324, 34),
          person(170, 322, 1.15, SKIN[0], "#264653", "#343a40", "#000", "none", mood="shut", rot=-18,
                 brows="M-14 -188 L-3 -184 M3 -184 L14 -188",
                 larm=((-14, 30), (-4, 60)), rarm=((14, 30), (4, 60)),
                 lleg=((-14, 40), (-20, 84)), rleg=((12, 44), (26, 86)), extra=scarf)]
    for _ in range(30):
        x, y = rnd.uniform(0, 400), rnd.uniform(0, 320)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{rnd.choice((2, 3, 4))}" fill="#fff"/>')
    return svg(b, "#8d99ae")


def drained():
    b = ['<rect y="330" width="400" height="70" fill="#ced4da"/>',
         # the chair
         '<rect x="90" y="150" width="30" height="190" rx="6" fill="#457b9d"/>',
         '<rect x="90" y="250" width="200" height="30" rx="8" fill="#457b9d"/>',
         '<rect x="100" y="280" width="10" height="56" fill="#343a40"/><rect x="270" y="280" width="10" height="56" fill="#343a40"/>',
         # the nurse, slumped
         limb(((150, 250), (230, 256), (236, 330)), "#2a9d8f", 18),
         limb(((150, 254), (220, 262), (214, 330)), "#2a9d8f", 18),
         '<ellipse cx="240" cy="334" rx="14" ry="6" fill="#fff"/><ellipse cx="210" cy="334" rx="14" ry="6" fill="#fff"/>',
         limb(((142, 250), (132, 176)), "#a8dadc", 40),
         limb(((136, 182), (170, 230), (186, 296)), "#a8dadc", 14), f'<circle cx="186" cy="300" r="8" fill="{SKIN[1]}"/>',
         f'<g transform="rotate(30 150 150)"><circle cx="150" cy="150" r="24" fill="{SKIN[1]}"/>'
         '<path d="M126 146 Q126 124 150 124 Q174 124 174 146 Z" fill="#fff"/>'
         f'<path d="M138 152 q5 4 10 0 M154 152 q5 4 10 0" fill="none" stroke="{INK}" stroke-width="2.5" '
         'stroke-linecap="round"/>'
         f'<path d="M144 166 q6 -3 12 0" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/></g>',
         # an empty battery above
         '<rect x="250" y="70" width="100" height="50" rx="8" fill="none" stroke="#495057" stroke-width="6"/>',
         '<rect x="350" y="84" width="10" height="22" rx="3" fill="#495057"/>',
         '<rect x="258" y="78" width="14" height="34" rx="3" fill="#e63946"/>',
         '<rect x="300" y="290" width="22" height="30" rx="4" fill="#fff"/><path d="M322 298 q10 0 10 8 q0 8 -10 8" fill="none" '
         'stroke="#fff" stroke-width="4"/>']
    return svg(b, "#e9ecef")


def alarmed():
    b = ['<polygon points="0,400 0,250 400,90 400,400" fill="#a7c957"/>',
         '<path d="M0 300 Q50 290 100 300 T200 300 T300 300 T400 300 V400 H0 Z" fill="#8d6e63" opacity=".85"/>',
         '<path d="M0 300 Q50 290 100 300 T200 300 T300 300 T400 300" fill="none" stroke="#d7b899" stroke-width="4"/>',
         '<path d="M0 340 Q50 330 100 340 T200 340 T300 340" fill="none" stroke="#a1887f" stroke-width="3"/>',
         '<rect x="30" y="250" width="50" height="40" fill="#e6ccb2"/><polygon points="24,252 55,226 86,252" fill="#9c6644"/>',
         arrow(80, 370, 80, 316, "#4895ef", 6, 16),
         sheep(230, 206, k=.75), sheep(300, 180, k=.7),
         person(170, 250, .75, SKIN[2], "#e76f51", "#264653", "#1b1b1b", "short", mood="wide", rot=12,
                larm=((-14, 30), (-30, 50)), rarm=((24, -10), (40, -30)), lleg=((-14, 40), (-26, 80)),
                rleg=((12, 40), (22, 78))),
         person(350, 150, .65, SKIN[0], "#2a9d8f", "#264653", "#7f5539", "bun", mood="wide", rot=12,
                larm=((-24, -16), (-40, -40)), rarm=((12, 40), (14, 72)), lleg=((-14, 40), (-26, 80)),
                rleg=((12, 40), (22, 78))),
         carrow(150, 120, 230, 60, 330, 60, "#e76f51", 5, 14)]
    return svg(b, "#adb5bd")


def discovery():
    rnd = random.Random(5)
    b = ['<circle cx="330" cy="60" r="30" fill="#ffd166"/>',
         '<path d="M0 180 Q100 160 200 176 T400 168 V400 H0 Z" fill="#e9c46a"/>',
         '<path d="M0 220 Q140 200 260 214 T400 210 V400 H0 Z" fill="#e0c48c"/>',
         # the huge dinosaur skull, half out of the sand
         '<path d="M30 316 Q34 240 90 214 Q140 194 180 214 Q230 226 262 248 L300 262 Q318 270 314 288 L300 300 Z" '
         'fill="#f1f3f5"/>',
         '<ellipse cx="128" cy="244" rx="26" ry="20" fill="#6c757d"/>',
         '<ellipse cx="200" cy="246" rx="14" ry="10" fill="#6c757d"/>',
         '<ellipse cx="282" cy="268" rx="8" ry="5" fill="#6c757d"/>',
         '<path d="M190 286 L198 304 L206 288 L214 306 L222 290 L230 308 L238 292 L246 308 L254 294 L262 306 L270 294" '
         'fill="#fff" stroke="#ced4da" stroke-width="2" stroke-linejoin="round"/>',
         '<path d="M60 262 Q90 236 120 238" fill="none" stroke="#dee2e6" stroke-width="5"/>',
         '<path d="M20 304 Q200 286 340 302 V330 Q200 312 20 330 Z" fill="#e0c48c"/>',
         shadow(340, 364, 30),
         person(340, 362, .9, SKIN[1], "#e9c46a", "#7f5539", "#5c4033", "cap", mood="wide",
                larm=((-30, 20), (-60, 40)), rarm=((12, 40), (14, 72))),
         '<rect x="256" y="230" width="36" height="12" rx="4" fill="#bc6c25" transform="rotate(-30 274 236)"/>',
         '<path d="M250 236 l-12 -4 M252 244 l-14 2" stroke="#9c6644" stroke-width="3"/>']
    for _ in range(14):
        x, y = rnd.uniform(240, 300), rnd.uniform(200, 240)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="2" fill="#c9a227"/>')
    b += [sparkle(110, 170, 10, "#fff"), sparkle(200, 160, 8, "#fff")]
    return svg(b, "#fff3b0")


def crate(x, y, veg):
    out = [f'<rect x="{x}" y="{y}" width="70" height="44" fill="#d4a373"/>',
           f'<path d="M{x} {y + 14} H{x + 70} M{x} {y + 30} H{x + 70}" stroke="#b08968" stroke-width="3"/>']
    for k in range(4):
        out.append(f'<circle cx="{x + 12 + k * 16}" cy="{y - 4}" r="9" fill="{veg[k % len(veg)]}"/>')
    return "".join(out)


def supplied():
    b = ['<rect y="330" width="400" height="70" fill="#ced4da"/>',
         # school kitchen door
         '<rect x="250" y="80" width="150" height="252" fill="#e9d8c4"/>',
         '<rect x="290" y="150" width="70" height="182" fill="#f8f9fa"/>',
         '<rect x="296" y="160" width="58" height="40" fill="#caf0f8"/>',
         person(330, 340, .8, SKIN[3], "#fff", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-24, 6), (-40, -10)), rarm=((12, 40), (14, 72)),
                extra='<path d="M-20 -196 H20 V-208 Q30 -214 26 -226 Q18 -236 6 -230 Q0 -240 -10 -232 Q-22 -236 '
                      '-26 -224 Q-30 -212 -20 -208 Z" fill="#fff" stroke="#dee2e6" stroke-width="2"/>'),
         crate(190, 288, ("#e76f51", "#e63946")), crate(190, 244, ("#a7c957", "#6a994e")),
         shadow(110, 344, 34),
         person(110, 342, 1.0, SKIN[1], "#457b9d", "#264653", "#7f5539", "cap", mood="grin",
                larm=((30, 0), (56, 4)), rarm=((24, 0), (52, 6))),
         crate(124, 200, ("#f4a261", "#e9c46a")),
         arrow(160, 110, 210, 110, "#2a9d8f", 5, 14)]
    return svg(b, "#e3f2fd")


def penguin(x, y, k=1.0, chick=False):
    body, belly = ("#adb5bd", "#dee2e6") if chick else ("#264653", "#fff")
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<ellipse cx="0" cy="2" rx="22" ry="5" fill="#000" opacity=".12"/>'
            f'<ellipse cx="0" cy="-34" rx="24" ry="34" fill="{body}"/>'
            f'<ellipse cx="0" cy="-28" rx="16" ry="26" fill="{belly}"/>'
            f'<circle cx="0" cy="-70" r="18" fill="{body}"/>'
            + ('' if chick else '<ellipse cx="0" cy="-66" rx="11" ry="10" fill="#fff"/><path d="M-12 -60 Q0 -52 12 -60" '
               'fill="#ffd166"/>')
            + f'<circle cx="-6" cy="-72" r="2.5" fill="{INK}"/><circle cx="6" cy="-72" r="2.5" fill="{INK}"/>'
            '<polygon points="-4,-66 4,-66 0,-58" fill="#f4a261"/>'
            '<path d="M-10 0 h8 M2 0 h8" stroke="#f4a261" stroke-width="4" stroke-linecap="round"/></g>')


def distinguish():
    rnd = random.Random(4)
    b = ['<rect y="200" width="400" height="200" fill="#f8f9fa"/>']
    spots = []
    for r in range(4):
        for c in range(7):
            spots.append((40 + c * 54 + (r % 2) * 26, 240 + r * 44))
    target = spots[17]
    for x, y in spots:
        b.append(penguin(x, y, .6, True))
    b += [f'<circle cx="{target[0]}" cy="{target[1] - 26}" r="34" fill="none" stroke="#e76f51" stroke-width="4"/>',
          heart(target[0], target[1] - 76, 10),
          penguin(70, 170, 1.4),
          f'<path d="M100 90 Q{target[0] - 40} 60 {target[0]} {target[1] - 66}" fill="none" stroke="#6c757d" stroke-width="3" '
          'stroke-dasharray="7 7"/>']
    return svg(b, "#cfe8f3")


def saturated_with():
    rnd = random.Random(3)
    b = ['<rect y="330" width="400" height="70" fill="#dee2e6"/>',
         '<ellipse cx="200" cy="346" rx="120" ry="18" fill="#4895ef" opacity=".7"/>',
         '<ellipse cx="200" cy="346" rx="80" ry="10" fill="none" stroke="#caf0f8" stroke-width="3"/>',
         '<path d="M200 0 V96" stroke="#457b9d" stroke-width="34" stroke-linecap="round"/>',
         f'<ellipse cx="200" cy="112" rx="30" ry="18" fill="{SKIN[1]}"/>',
         '<rect x="110" y="110" width="180" height="120" rx="20" fill="#ffd166"/>',
         '<rect x="110" y="110" width="180" height="120" rx="20" fill="#4895ef" opacity=".25"/>']
    for _ in range(26):
        x, y, r = rnd.uniform(126, 274), rnd.uniform(124, 216), rnd.uniform(3, 7)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="#e9c46a"/>')
    for x, y in ((140, 236), (180, 240), (220, 238), (260, 236)):
        b.append(f'<path d="M{x} {y} Q{x - 4} {y + 10} {x} {y + 14} Q{x + 4} {y + 10} {x} {y} Z" fill="#4895ef"/>')
    for x, y in ((150, 280), (210, 300), (250, 272), (190, 316)):
        b.append(f'<path d="M{x} {y - 10} Q{x - 6} {y + 2} {x} {y + 6} Q{x + 6} {y + 2} {x} {y - 10} Z" fill="#4895ef"/>')
    b += ['<path d="M188 104 V122 M200 102 V124 M212 104 V122" stroke="#c68642" stroke-width="2.5" stroke-linecap="round"/>']
    return svg(b, "#f1faee")



def encompass():
    rnd = random.Random(9)
    b = ['<rect width="400" height="400" fill="#a7c957"/>']
    for _ in range(14):
        x, y = rnd.uniform(0, 400), rnd.uniform(0, 400)
        if math.hypot(x - 200, y - 200) > 180:
            b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="6" fill="#6a994e"/>')
    b += ['<circle cx="200" cy="200" r="168" fill="#90be6d"/>',
          '<ellipse cx="236" cy="236" rx="70" ry="48" fill="#4895ef"/>',
          '<ellipse cx="226" cy="226" rx="40" ry="20" fill="#a8dadc" opacity=".6"/>']
    for x, y, r in ((130, 120, 26), (170, 100, 22), (110, 170, 24), (150, 160, 20), (200, 140, 22), (100, 230, 20),
                    (140, 280, 24), (250, 120, 20), (300, 170, 22), (130, 210, 16)):
        b.append(bush(x, y, r))
    for k in range(48):
        a = math.radians(k * 7.5)
        x, y = 200 + 168 * math.cos(a), 200 + 168 * math.sin(a)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="5" fill="#7f5539"/>')
    b.append('<circle cx="200" cy="200" r="168" fill="none" stroke="#9c6644" stroke-width="5"/>')
    return svg(b, "#a7c957")


def empty():
    b = ['<rect y="0" width="400" height="120" fill="#22223b"/>',
         '<rect x="40" y="20" width="320" height="80" fill="#9d0208"/>',
         '<path d="M40 20 H360 V40 Q280 56 200 40 Q120 56 40 40 Z" fill="#c1121f"/>',
         '<rect x="30" y="100" width="340" height="16" fill="#9c6b3c"/>']
    for r in range(5):
        y = 150 + r * 50
        n = 7 + r
        w = 340 + r * 14
        for c in range(n):
            x = 200 - w / 2 + (c + .5) * w / n
            b.append(f'<rect x="{f(x - 18)}" y="{y}" width="36" height="32" rx="8" fill="#e63946"/>'
                     f'<rect x="{f(x - 18)}" y="{y + 22}" width="36" height="14" rx="4" fill="#9d0208"/>')
    return svg(b, "#3d405b")


def torch(x, y, rot, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({k})">'
            '<rect x="-4" y="-6" width="8" height="40" rx="3" fill="#7f5539"/>'
            '<path d="M0 -30 Q-14 -14 -8 -4 Q0 2 8 -4 Q14 -14 0 -30 Z" fill="#f77f00"/>'
            '<path d="M0 -20 Q-6 -10 -3 -4 Q0 -2 3 -4 Q6 -10 0 -20 Z" fill="#ffd166"/></g>')


def skilled_in():
    b = ['<rect y="330" width="400" height="70" fill="#9c6b3c"/>',
         '<path d="M50 300 Q200 -160 350 300" fill="none" stroke="#6c757d" stroke-width="2" stroke-dasharray="6 7"/>',
         shadow(200, 334, 40),
         person(200, 332, 1.05, SKIN[2], "#e63946", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-26, 10), (-56, -6)), rarm=((26, 10), (56, -6)))]
    for t, rot in ((.1, -40), (.28, -15), (.5, 0), (.72, 20), (.9, 40)):
        x = 50 + 300 * t
        y = (1 - t) ** 2 * 300 + 2 * (1 - t) * t * -160 + t ** 2 * 300
        b.append(torch(x, y, rot, 1.2))
    b += [sparkle(40, 60, 9, "#ffd166"), sparkle(360, 60, 9, "#ffd166")]
    return svg(b, "#22223b")


def arranged():
    colors = ["#e63946", "#f4a261", "#ffd166", "#a7c957", "#2a9d8f", "#4895ef", "#457b9d", "#6d597a"]
    b = ['<rect x="30" y="40" width="340" height="320" rx="6" fill="#7f5539"/>',
         '<rect x="44" y="54" width="312" height="292" fill="#e6ccb2"/>']
    for r, y in enumerate((150, 250, 346)):
        b.append(f'<rect x="44" y="{y - 4}" width="312" height="10" fill="#7f5539"/>')
        x = 50
        for c in range(len(colors)):
            for k in range(2):
                h = 76 + (k * 6)
                b.append(f'<rect x="{x}" y="{y - 4 - h}" width="17" height="{h}" rx="2" fill="{colors[c]}"/>'
                         f'<rect x="{x + 3}" y="{y - h + 6}" width="11" height="6" fill="#fff" opacity=".4"/>')
                x += 19
    return svg(b, "#fdf6ec")


def disguise():
    coat_hat = ('<path d="M-30 -196 Q-30 -224 0 -224 Q30 -224 30 -196 Z" fill="#495057"/>'
                '<ellipse cx="0" cy="-196" rx="40" ry="8" fill="#343a40"/>'
                '<circle cx="-9" cy="-180" r="9" fill="#caf0f8" stroke="#264653" stroke-width="3"/>'
                '<circle cx="9" cy="-180" r="9" fill="#caf0f8" stroke="#264653" stroke-width="3"/>'
                '<path d="M-14 -168 Q-7 -162 0 -166 Q7 -162 14 -168 Q8 -158 0 -162 Q-8 -158 -14 -168 Z" fill="#3e2723"/>'
                '<path d="M-30 -154 L-38 -44 H38 L30 -154 Z" fill="#9c6644"/>'
                '<path d="M0 -150 V-44" stroke="#7f5539" stroke-width="3"/>'
                '<circle cx="-6" cy="-120" r="3" fill="#5c4033"/><circle cx="-6" cy="-96" r="3" fill="#5c4033"/>'
                '<path d="M-26 -160 L-34 -132 L-6 -152 Z M26 -160 L34 -132 L6 -152 Z" fill="#7f5539"/>')
    b = ['<rect y="340" width="400" height="60" fill="#adb5bd"/>',
         '<rect x="0" y="40" width="70" height="300" fill="#6c757d"/><rect x="330" y="80" width="70" height="260" fill="#6c757d"/>',
         '<circle cx="300" cy="40" r="20" fill="#fefae0"/>',
         shadow(200, 344, 44),
         person(200, 342, 1.25, SKIN[1], "#b08968", "#495057", "#000", "none", mood="side",
                larm=((-14, 40), (-18, 74)), rarm=((14, 40), (18, 74)), extra=coat_hat),
         '<path d="M165 150 L150 330 H250 L235 150 Z" fill="#9c6644" opacity=".0"/>']
    return svg(b, "#3d405b")


def whistle():
    return ('<rect x="0" y="-6" width="20" height="12" rx="5" fill="#adb5bd"/><circle cx="20" cy="0" r="7" fill="#adb5bd"/>')


def biased():
    stripes = "".join(f'<rect x="{x}" y="-156" width="8" height="72" fill="#212529"/>' for x in (-24, -8, 8, 24))
    b = ['<rect y="320" width="400" height="80" fill="#52b788"/>',
         '<path d="M0 340 H400" stroke="#fff" stroke-width="3"/>',
         person(80, 340, .85, SKIN[0], "#e63946", "#fff", "#7f5539", "short", mood="frown",
                larm=((-12, 40), (-14, 72)), rarm=((12, 40), (14, 72))),
         person(330, 340, .85, SKIN[3], "#4895ef", "#fff", "#1b1b1b", "short", mood="grin",
                larm=((-24, -30), (-34, -66)), rarm=((24, -30), (34, -66))),
         shadow(200, 344, 36),
         person(200, 342, 1.05, SKIN[1], "#fff", "#212529", "#5c4033", "short", mood="sly",
                larm=((-30, -6), (-60, -10)), rarm=((24, 30), (50, 40)), extra=stripes),
         f'<g transform="translate(172 168)">{whistle()}</g>',
         '<path d="M150 160 l-20 -10 M148 176 l-22 2" stroke="#e63946" stroke-width="4" stroke-linecap="round"/>',
         # a small blue pennant hidden behind the back, waved for the blue team
         '<line x1="256" y1="210" x2="270" y2="160" stroke="#7f5539" stroke-width="4"/>',
         '<polygon points="270,160 300,172 266,182" fill="#4895ef"/>',
         heart(296, 136, 10, "#4895ef")]
    return svg(b, "#e3f2fd")


def dangerous():
    rnd = random.Random(2)
    b = ['<polygon points="0,180 230,180 250,210 236,240 260,270 240,400 0,400" fill="#8d6e63"/>',
         '<polygon points="0,180 230,180 236,196 0,196" fill="#a7c957"/>',
         '<path d="M250 210 L236 240 L260 270" fill="none" stroke="#5c4033" stroke-width="3"/>',
         '<path d="M180 200 L210 230 L196 250" fill="none" stroke="#5c4033" stroke-width="3"/>']
    for x, y, r in ((276, 250, 10), (300, 300, 8), (290, 350, 12), (320, 220, 6)):
        b.append(f'<polygon points="{x - r},{y} {x},{y - r} {x + r},{y + r * .4} {x - r * .2},{y + r}" fill="#8d6e63"/>')
    b += ['<path d="M280 236 v8 M300 286 v8" stroke="#6c757d" stroke-width="2"/>',
          person(196, 182, .75, SKIN[2], "#e76f51", "#264653", "#1b1b1b", "cap", mood="wide",
                 larm=((-24, -16), (-40, -40)), rarm=((24, -16), (40, -40))),
          '<rect x="120" y="50" width="16" height="70" fill="#2a9d8f" opacity=".0"/>',
          # the warning sign
          '<rect x="54" y="120" width="6" height="64" fill="#6c757d"/>',
          '<polygon points="57,70 92,128 22,128" fill="#ffd166" stroke="#e76f51" stroke-width="4" stroke-linejoin="round"/>',
          '<polygon points="50,116 60,96 70,116" fill="#264653"/><circle cx="66" cy="94" r="5" fill="#264653"/>']
    return svg(b, "#cfe8f3")


def reprieve():
    rnd = random.Random(14)
    b = ['<rect x="0" y="40" width="80" height="260" fill="#adb5bd"/><rect x="320" y="60" width="80" height="240" fill="#ced4da"/>',
         '<ellipse cx="200" cy="40" rx="190" ry="44" fill="#8d99ae"/>',
         '<circle cx="360" cy="40" r="24" fill="#ffd166" opacity=".5"/>',
         '<rect y="300" width="400" height="100" fill="#adb5bd"/>']
    for _ in range(50):
        x, y = rnd.uniform(0, 400), rnd.uniform(80, 300)
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 3)}" y2="{f(y + 14)}" stroke="#4895ef" stroke-width="3" '
                 'stroke-linecap="round"/>')
    for x, sk, c in ((90, SKIN[0], "#e76f51"), (200, SKIN[3], "#2a9d8f"), (310, SKIN[1], "#e9c46a")):
        b.append(person(x, 350, .9, sk, c, "#264653", "#3e2723", "short", mood="up",
                        larm=((-26, -24), (-40, -54)), rarm=((26, -24), (40, -54))))
    b += ['<path d="M50 200 l-12 -8 M240 196 l12 -8" stroke="#fff" stroke-width="0"/>']
    return svg(b, "#dbe7f0")


def tolerate():
    b = ['<circle cx="320" cy="80" r="50" fill="#ffd166"/>', '<circle cx="320" cy="80" r="66" fill="#ffd166" opacity=".3"/>',
         '<rect y="260" width="400" height="140" fill="#e9c46a"/>',
         '<path d="M40 300 L80 320 L70 350 M140 290 L170 310 M260 320 L300 300 L320 330 M330 370 L360 350" fill="none" '
         'stroke="#bc6c25" stroke-width="3"/>',
         '<path d="M100 120 q-6 -10 0 -20 t0 -20 M60 160 q-6 -10 0 -20 t0 -20 M150 90 q-6 -10 0 -20 t0 -20" fill="none" '
         'stroke="#f4a261" stroke-width="3" stroke-linecap="round"/>']
    b += [shadow(200, 320, 50, 8), cactus(200, 320, 220), '<circle cx="200" cy="96" r="12" fill="#ff8fab"/>',
          '<circle cx="200" cy="96" r="5" fill="#ffd166"/>',
          # thermometer near the top
          '<rect x="44" y="190" width="18" height="90" rx="9" fill="#fff" stroke="#adb5bd" stroke-width="3"/>',
          '<circle cx="53" cy="286" r="16" fill="#e63946"/><rect x="48" y="196" width="10" height="90" rx="5" fill="#e63946"/>']
    return svg(b, "#fff3b0")



def confident():
    b = ['<rect y="330" width="400" height="70" fill="#9c6b3c"/>',
         '<rect x="0" y="0" width="400" height="330" fill="#457b9d" opacity=".15"/>',
         '<polygon points="160,0 240,0 300,330 100,330" fill="#fff3b0" opacity=".45"/>',
         shadow(200, 334, 40),
         person(200, 332, 1.2, SKIN[3], "#e76f51", "#264653", "#1b1b1b", "bun", mood="grin",
                larm=((-14, 40), (-18, 72)), rarm=((30, 0), (58, -20))),
         # the podium
         '<path d="M130 236 H270 L256 334 H144 Z" fill="#7f5539"/>',
         '<rect x="124" y="226" width="152" height="14" rx="3" fill="#9c6b3c"/>',
         '<circle cx="200" cy="286" r="18" fill="#e9c46a"/>',
         '<path d="M228 226 L240 196" stroke="#495057" stroke-width="4"/><ellipse cx="242" cy="190" rx="6" ry="9" fill="#343a40"/>',
         sparkle(110, 100, 10, "#ffd166"), sparkle(300, 70, 12, "#ffd166")]
    return svg(b, "#e3f2fd")


def defends():
    b = ['<rect y="300" width="400" height="100" fill="#52b788"/>',
         # the goal and its net
         '<rect x="30" y="100" width="340" height="12" fill="#fff"/>',
         '<rect x="30" y="100" width="12" height="220" fill="#fff"/><rect x="358" y="100" width="12" height="220" fill="#fff"/>']
    for x in range(54, 358, 24):
        b.append(f'<line x1="{x}" y1="112" x2="{x}" y2="310" stroke="#fff" stroke-width="1.5" opacity=".6"/>')
    for y in range(124, 310, 24):
        b.append(f'<line x1="42" y1="{y}" x2="358" y2="{y}" stroke="#fff" stroke-width="1.5" opacity=".6"/>')
    b += ['<g transform="rotate(62 200 230)">',
          person(200, 300, 1.05, SKIN[1], "#ffd166", "#264653", "#5c4033", "short", mood="grin",
                 brows="M-14 -190 L-3 -186 M3 -186 L14 -190",
                 larm=((-14, -40), (-10, -76)), rarm=((14, -40), (10, -76))),
          '</g>',
          '<circle cx="356" cy="156" r="22" fill="#fff" stroke="#264653" stroke-width="2"/>',
          '<polygon points="356,146 366,153 362,166 350,166 346,153" fill="#264653"/>',
          '<path d="M330 116 l-8 -12 M352 112 v-14 M374 120 l8 -12" stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>',
          shadow(200, 330, 80, 6)]
    return svg(b, "#cfe8f3")


def duckling(x, y, k=1.0, c="#fff"):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            f'<ellipse cx="0" cy="0" rx="20" ry="11" fill="{c}"/><circle cx="14" cy="-12" r="9" fill="{c}"/>'
            '<polygon points="22,-13 30,-11 22,-8" fill="#f4a261"/>'
            f'<circle cx="16" cy="-14" r="2" fill="{INK}"/></g>')


def counting():
    b = ['<rect y="200" width="400" height="200" fill="#4895ef"/>',
         '<path d="M0 200 Q100 190 200 200 T400 196" fill="none" stroke="#a8dadc" stroke-width="4"/>',
         '<rect y="330" width="140" height="70" fill="#a7c957"/>']
    birds = ((190, 250), (250, 236), (310, 262), (220, 300), (290, 320), (360, 290))
    for k, (x, y) in enumerate(birds):
        b.append(duckling(x, y, 1.1))
        if k < 3:
            b.append(f'<circle cx="{x}" cy="{y - 40}" r="12" fill="#52b788"/>'
                     f'<path d="M{x - 6} {y - 40} L{x - 1} {y - 35} L{x + 7} {y - 45}" fill="none" stroke="#fff" '
                     'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    b += [person(70, 380, .9, SKIN[0], "#fff", "#264653", "#7f5539", "short", mood="side",
                 larm=((-12, 30), (-6, 54)), rarm=((40, -10), (90, -30))),
          '<rect x="40" y="250" width="30" height="40" rx="2" fill="#e9c46a"/>',
          '<path d="M164 240 L216 228" stroke="#6c757d" stroke-width="2" stroke-dasharray="5 5"/>']
    return svg(b, "#cfe8f3")


def horse_side(x, y, k=1.0, coat="#9c6644"):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            f'<path d="M-40 -40 L-46 0 M-24 -40 L-20 0 M24 -40 L20 0 M40 -40 L48 0" stroke="{coat}" stroke-width="11" '
            'stroke-linecap="round"/>'
            f'<ellipse cx="0" cy="-56" rx="52" ry="26" fill="{coat}"/>'
            f'<path d="M36 -70 L60 -112 L84 -100 L60 -60 Z" fill="{coat}"/>'
            f'<path d="M60 -112 L92 -96 Q98 -88 90 -82 L70 -88 Z" fill="{coat}"/>'
            '<path d="M52 -116 Q40 -100 38 -76" fill="none" stroke="#3e2723" stroke-width="8"/>'
            '<path d="M-50 -64 Q-70 -50 -66 -20" fill="none" stroke="#3e2723" stroke-width="8" stroke-linecap="round"/>'
            f'<circle cx="74" cy="-102" r="3" fill="{INK}"/></g>')


def pulled():
    b = ['<polygon points="0,400 0,300 400,170 400,400" fill="#7f5539"/>',
         '<polygon points="0,400 0,320 400,190 400,400" fill="#6f4518"/>']
    for x, y in ((60, 310), (120, 290), (180, 270)):
        b.append(f'<ellipse cx="{x}" cy="{y + 16}" rx="16" ry="5" fill="#5c4033"/>')
    b += ['<g transform="translate(130 300) scale(.85) rotate(-18)">'
          '<rect x="-90" y="-60" width="130" height="56" rx="4" fill="#bc6c25"/>'
          '<rect x="-84" y="-90" width="40" height="32" fill="#d4a373"/><rect x="-40" y="-84" width="40" height="26" fill="#e9c46a"/>'
          '<circle cx="-62" cy="0" r="22" fill="none" stroke="#3e2723" stroke-width="6"/>'
          '<circle cx="18" cy="0" r="22" fill="none" stroke="#3e2723" stroke-width="6"/>'
          '<line x1="40" y1="-30" x2="120" y2="-40" stroke="#3e2723" stroke-width="4"/>'
          + horse_side(170, 0, .9) + horse_side(230, -6, .9, "#7f5539") + '</g>',
         '<path d="M40 180 l-10 -8 M50 200 l-14 -2" stroke="#6c757d" stroke-width="0"/>',
         arrow(240, 80, 340, 40, "#e76f51", 6, 16)]
    return svg(b, "#cfe8f3")


def invented():
    b = ['<rect y="330" width="400" height="70" fill="#8d6e63"/>',
         '<rect x="260" y="250" width="130" height="14" rx="3" fill="#7f5539"/>',
         '<rect x="270" y="264" width="10" height="70" fill="#6f4518"/><rect x="370" y="264" width="10" height="70" fill="#6f4518"/>',
         '<circle cx="300" cy="236" r="12" fill="#adb5bd"/><rect x="320" y="226" width="40" height="24" fill="#6c757d"/>',

         shadow(160, 334, 40),
         person(160, 332, 1.15, SKIN[0], "#fff", "#264653", "#adb5bd", "short", mood="grin",
                larm=((-12, 40), (-14, 72)), rarm=((30, -26), (40, -66))),
         bulb(212, 110, 1.4, True, 0),
         f'<circle cx="208" cy="148" r="9" fill="{SKIN[0]}"/>',
         sparkle(130, 60, 10, "#ffd166"), sparkle(290, 120, 12, "#ffd166")]
    return svg(b, "#3d405b")


def genuine():
    b = ['<rect y="320" width="400" height="80" fill="#7f5539"/>',
         '<ellipse cx="110" cy="260" rx="70" ry="14" fill="#9d0208"/>', '<ellipse cx="290" cy="260" rx="70" ry="14" fill="#9d0208"/>',
         '<circle cx="110" cy="200" r="64" fill="#fff3b0" opacity=".35"/>',
         diamond(110, 196, 1.3),
         sparkle(54, 140, 12, "#ffd166"), sparkle(170, 150, 10, "#ffd166"), sparkle(160, 240, 8, "#ffd166"),
         diamond(290, 200, 1.3, "#adb5bd", "#ced4da", "#8d99ae"),
         '<path d="M280 180 L292 200 L284 214 L296 232" fill="none" stroke="#6c757d" stroke-width="3"/>',
         '<circle cx="110" cy="80" r="26" fill="#52b788"/>',
         '<path d="M98 80 L107 89 L124 70" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" '
         'stroke-linejoin="round"/>',
         '<circle cx="290" cy="80" r="26" fill="#e63946"/>',
         '<path d="M280 70 L300 90 M300 70 L280 90" stroke="#fff" stroke-width="6" stroke-linecap="round"/>']
    return svg(b, "#3d405b")


def secluded():
    rnd = random.Random(12)
    b = ['<rect y="260" width="400" height="140" fill="#6a994e"/>', '<circle cx="80" cy="60" r="24" fill="#fefae0"/>']
    trees = []
    for _ in range(40):
        x, y = rnd.uniform(-20, 420), rnd.uniform(200, 400)
        if 130 < x < 280 and 230 < y < 330:
            continue
        trees.append((y, x))
    for y, x in sorted(trees):
        h = 70 + (y - 200) * .5
        b.append(pine(x, y, h, rnd.choice(("#2d6a4f", "#386641", "#40916c"))))
    b += ['<rect x="164" y="248" width="80" height="56" fill="#9c6644"/>',
          '<path d="M164 262 H244 M164 276 H244 M164 290 H244" stroke="#7f5539" stroke-width="3"/>',
          '<polygon points="156,252 204,214 252,252" fill="#6f4518"/>',
          '<rect x="222" y="214" width="12" height="24" fill="#5c4033"/>',
          '<rect x="196" y="270" width="18" height="34" fill="#5c4033"/>',
          '<rect x="174" y="262" width="16" height="14" fill="#ffd166"/>',
          '<path d="M228 210 q-8 -12 2 -22 q10 -10 0 -24" fill="none" stroke="#dee2e6" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#cfe8f3")


def gear_small(cx, cy, r, color):
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>']
    for a in range(0, 360, 45):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        out.append(f'<rect x="{f(cx + r * ca - 3)}" y="{f(cy + r * sa - 3)}" width="6" height="6" fill="{color}"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{f(r * .35)}" fill="#fff"/>')
    return "".join(out)


def meticulous():
    b = ['<rect x="20" y="180" width="360" height="200" rx="8" fill="#2d6a4f"/>',
         '<rect x="30" y="190" width="340" height="180" rx="4" fill="#40916c"/>']
    for r in range(3):
        for c in range(6):
            x, y = 70 + c * 50, 220 + r * 50
            kind = (r + c) % 3
            if r == 2 and c == 5:
                continue
            if kind == 0:
                b.append(gear_small(x, y, 12, "#e9c46a"))
            elif kind == 1:
                b.append(f'<circle cx="{x}" cy="{y}" r="7" fill="#adb5bd"/><circle cx="{x}" cy="{y}" r="3" fill="#495057"/>')
            else:
                b.append(f'<rect x="{x - 3}" y="{y - 14}" width="6" height="28" rx="3" fill="#ced4da"/>')
    b += ['<line x1="400" y1="200" x2="330" y2="316" stroke="#adb5bd" stroke-width="6" stroke-linecap="round"/>',
          '<line x1="390" y1="190" x2="324" y2="314" stroke="#ced4da" stroke-width="5" stroke-linecap="round"/>',
          gear_small(320, 320, 10, "#e9c46a"),
          '<circle cx="320" cy="320" r="24" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="5 5"/>',
          # the watch face above
          '<circle cx="200" cy="90" r="64" fill="#e9c46a"/><circle cx="200" cy="90" r="54" fill="#fff"/>',
          '<path d="M200 90 V52 M200 90 L226 104" stroke="#264653" stroke-width="5" stroke-linecap="round"/>',
          '<circle cx="200" cy="90" r="5" fill="#264653"/>']
    for a in range(0, 360, 30):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(200 + 44 * ca)}" y1="{f(90 + 44 * sa)}" x2="{f(200 + 50 * ca)}" y2="{f(90 + 50 * sa)}" '
                 'stroke="#264653" stroke-width="3"/>')
    b += ['<rect x="190" y="18" width="20" height="12" rx="3" fill="#e9c46a"/>']
    return svg(b, "#fdf6ec")


def judge():
    b = ['<rect y="0" width="400" height="200" fill="#5c4d7d"/>',
         '<polygon points="170,0 230,0 270,200 130,200" fill="#fff3b0" opacity=".3"/>',
         '<rect y="196" width="400" height="16" fill="#9c6b3c"/>',
         person(200, 200, .7, SKIN[2], "#e63946", "#264653", "#1b1b1b", "bun", mood="grin",
                larm=((-30, -20), (-50, -46)), rarm=((24, 30), (40, 50)), lleg=((-6, 44), (-6, 86)),
                rleg=((30, 30), (60, 20)), skirt=True),
         '<rect y="212" width="400" height="188" fill="#e9d8c4"/>']
    for x, sk, c in ((80, SKIN[0], "#457b9d"), (200, SKIN[3], "#2a9d8f"), (320, SKIN[1], "#6c757d")):
        b.append(person(x, 400, .85, sk, c, "#264653", "#3e2723", "short", mood="flat",
                        larm=((-12, 40), (-14, 72)), rarm=((26, -16), (36, -50))))
        b.append(f'<rect x="{x + 30}" y="210" width="44" height="36" rx="3" fill="#fff" stroke="#adb5bd" stroke-width="2"/>')
        b.append(f'<line x1="{x + 52}" y1="246" x2="{x + 52}" y2="270" stroke="#7f5539" stroke-width="4"/>')
    b += ['<rect x="20" y="330" width="360" height="70" fill="#7f5539"/>']
    return svg(b, "#e9d8c4")


def protect():
    b = ['<rect y="0" width="400" height="160" fill="#adb5bd"/>',
         '<rect x="0" y="140" width="190" height="260" fill="#4895ef"/>',
         '<path d="M0 200 Q40 140 90 180 Q130 110 160 170" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round"/>',
         '<path d="M150 160 q12 -14 22 -2 M160 140 q10 -10 18 0" fill="none" stroke="#fff" stroke-width="5"/>',
         '<circle cx="168" cy="150" r="8" fill="#fff"/><circle cx="180" cy="130" r="6" fill="#fff"/><circle cx="160" cy="124" r="5" fill="#fff"/>',
         # the sea wall
         '<rect x="180" y="150" width="34" height="250" fill="#6c757d"/>',
         '<path d="M180 180 H214 M180 220 H214 M180 260 H214 M180 300 H214 M180 340 H214" stroke="#495057" stroke-width="3"/>',
         '<rect x="214" y="250" width="186" height="150" fill="#e9d8c4"/>']
    for x, y, c in ((240, 220, "#e76f51"), (300, 210, "#f4a261"), (350, 226, "#e9c46a")):
        b += [f'<rect x="{x}" y="{y}" width="44" height="40" fill="{c}"/>',
              f'<polygon points="{x - 4},{y + 2} {x + 22},{y - 22} {x + 48},{y + 2}" fill="#9d0208"/>',
              f'<rect x="{x + 16}" y="{y + 20}" width="12" height="20" fill="#7f5539"/>']
    b += ['<rect x="214" y="258" width="186" height="10" fill="#a7c957"/>', bush(380, 250, 14),
          arrow(120, 280, 172, 280, "#264653", 5, 14)]
    return svg(b, "#adb5bd")


def shapeless():
    b = ['<rect x="0" y="0" width="400" height="400" fill="#f2e9e4"/>',
         '<line x1="40" y1="60" x2="360" y2="60" stroke="#adb5bd" stroke-width="8" stroke-linecap="round"/>',
         '<path d="M200 60 V80 M200 80 L140 110 H260 Z" fill="none" stroke="#6c757d" stroke-width="5" stroke-linejoin="round"/>',
         # the saggy sweater
         '<path d="M150 108 Q200 100 250 108 Q270 180 262 260 Q250 330 230 360 Q200 340 180 362 Q150 330 142 260 '
         'Q132 180 150 108 Z" fill="#e76f51"/>',
         '<path d="M150 112 Q110 180 110 260 Q106 330 96 380 Q120 384 130 360 Q140 290 146 230" fill="#e76f51"/>',
         '<path d="M250 112 Q290 180 290 260 Q294 330 304 380 Q280 384 270 360 Q260 290 254 230" fill="#e76f51"/>',
         '<path d="M170 120 Q200 140 230 120" fill="none" stroke="#c1553b" stroke-width="5"/>',
         '<path d="M160 330 Q180 340 200 330 T240 330" fill="none" stroke="#c1553b" stroke-width="4"/>',
         '<path d="M96 374 Q116 380 130 362 M304 374 Q284 380 270 362" fill="none" stroke="#c1553b" stroke-width="4"/>']
    return svg(b, "#f2e9e4")


def rewards():
    b = ['<rect y="330" width="400" height="70" fill="#a7c957"/>',
         dog(130, 340, 1.1),
         '<path d="M84 196 l-10 -6 M86 214 l-12 0" stroke="#6c757d" stroke-width="0"/>',
         shadow(300, 344, 34),
         person(300, 342, 1.05, SKIN[2], "#457b9d", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-30, 10), (-62, 0)), rarm=((12, 40), (14, 72))),
         '<path d="M222 182 h22 a5 5 0 0 1 0 10 h-22 a5 5 0 0 1 0 -10 Z" fill="#d4a373"/>',
         '<circle cx="218" cy="182" r="5" fill="#d4a373"/><circle cx="218" cy="192" r="5" fill="#d4a373"/>',
         heart(180, 110, 14), heart(210, 80, 10, "#f4a261"), sparkle(250, 140, 9, "#ffd166")]
    return svg(b, "#e3f2fd")


def delegate():
    paint = ('<path d="M-16 -150 H16 L12 -114 H-12 Z" fill="#4895ef"/>'
             '<path d="M-14 -150 Q0 -166 14 -150" fill="none" stroke="#6c757d" stroke-width="3"/>')
    hammer = ('<rect x="-4" y="-170" width="8" height="56" rx="3" fill="#7f5539"/>'
              '<rect x="-16" y="-176" width="32" height="14" rx="3" fill="#6c757d"/>')
    broom = ('<line x1="0" y1="-190" x2="0" y2="-50" stroke="#bc6c25" stroke-width="6" stroke-linecap="round"/>'
             '<path d="M-14 -60 H14 L20 -20 H-20 Z" fill="#e9c46a"/>')
    b = ['<rect y="330" width="400" height="70" fill="#ced4da"/>',
         shadow(80, 334, 34),
         person(80, 332, 1.1, SKIN[1], "#264653", "#264653", "#5c4033", "short", mood="smile",
                larm=((-12, 40), (-14, 72)), rarm=((40, -10), (80, -20)))]
    for x, sk, c, tool in ((196, SKIN[0], "#e76f51", paint), (266, SKIN[3], "#2a9d8f", hammer),
                           (336, SKIN[2], "#e9c46a", broom)):
        b += [shadow(x, 344, 26),
              person(x, 342, .8, sk, c, "#457b9d", "#3e2723", "short", mood="smile",
                     larm=((-12, 40), (-14, 72)), rarm=((24, 0), (24, 30)),
                     extra=f'<g transform="translate(40 0)">{tool}</g>')]
    b += [carrow(170, 120, 190, 70, 206, 150, "#e76f51", 4, 12), carrow(176, 100, 230, 40, 270, 150, "#e76f51", 4, 12),
          carrow(176, 90, 280, 10, 340, 140, "#e76f51", 4, 12)]
    return svg(b, "#f1faee")


def lacking():
    b = ['<rect y="320" width="400" height="80" fill="#adb5bd"/>', shadow(200, 324, 120, 6),
         '<g transform="translate(200 320) scale(2)">' + bicycle("#e63946") + '</g>',
         # the front wheel is missing
         '<circle cx="290" cy="260" r="66" fill="#cfe8f3"/>',
         '<circle cx="290" cy="260" r="56" fill="none" stroke="#6c757d" stroke-width="4" stroke-dasharray="10 9"/>',
         '<path d="M264 168 L290 262" stroke="#e63946" stroke-width="12" stroke-linecap="round"/>']
    return svg(b, "#cfe8f3")


def signpost(x, y):
    out = [f'<rect x="{x - 4}" y="{y - 150}" width="8" height="150" fill="#7f5539"/>']
    for k, (rot, c) in enumerate(((-30, "#e76f51"), (20, "#2a9d8f"), (160, "#e9c46a"), (200, "#457b9d"))):
        out.append(f'<g transform="rotate({rot} {x} {y - 130 + k * 24})"><polygon points="{x},{y - 140 + k * 24} '
                   f'{x + 54},{y - 140 + k * 24} {x + 66},{y - 130 + k * 24} {x + 54},{y - 120 + k * 24} {x},{y - 120 + k * 24}" '
                   f'fill="{c}"/></g>')
    return "".join(out)


def confused():
    b = ['<rect y="260" width="400" height="140" fill="#a7c957"/>',
         '<path d="M180 400 L200 260 H220 L240 400 Z M0 300 H400 V330 H0 Z" fill="#e6ccb2"/>',
         signpost(310, 290),
         shadow(140, 354, 34),
         person(140, 352, 1.1, SKIN[0], "#f4a261", "#457b9d", "#7f5539", "cap", mood="frown",
                brows="M-14 -186 L-4 -191 M4 -194 Q10 -198 16 -192",
                larm=((-24, 20), (-30, 34)), rarm=((24, 20), (30, 34))),
         # the map, upside down
         '<g transform="rotate(180 140 236)"><rect x="96" y="210" width="88" height="56" fill="#fff"/>'
         '<path d="M96 210 V266 M126 210 V266 M156 210 V266" stroke="#adb5bd" stroke-width="2"/>'
         '<path d="M104 250 Q130 220 176 236" fill="none" stroke="#e63946" stroke-width="3"/>'
         '<polygon points="160,226 176,236 160,240" fill="#e63946"/></g>',
         carrow(70, 120, 60, 80, 96, 60, "#6c757d", 3, 10), carrow(210, 120, 230, 80, 196, 60, "#6c757d", 3, 10)]
    return svg(b, "#cfe8f3")


def pitchfork(x, y, rot=0):
    return (f'<g transform="rotate({rot} {x} {y})"><line x1="{x}" y1="{y}" x2="{x}" y2="{y - 90}" stroke="#7f5539" '
            f'stroke-width="4"/><path d="M{x - 10} {y - 110} V{y - 90} H{x + 10} V{y - 110} M{x} {y - 90} V{y - 112}" '
            'fill="none" stroke="#6c757d" stroke-width="3"/></g>')


def rebellion():
    b = ['<rect y="270" width="400" height="130" fill="#a7c957"/>', '<circle cx="60" cy="50" r="20" fill="#fefae0"/>',
         # the castle on the hill
         '<path d="M200 270 Q300 200 400 220 V270 Z" fill="#6a994e"/>',
         '<rect x="290" y="130" width="100" height="100" fill="#9a8c98"/>',
         '<rect x="280" y="100" width="30" height="130" fill="#8d8199"/><rect x="370" y="100" width="30" height="130" fill="#8d8199"/>',
         '<path d="M280 100 v-10 h8 v10 h6 v-10 h8 v10 M370 100 v-10 h8 v10 h6 v-10 h8 v10" fill="#8d8199"/>',
         '<path d="M326 230 V196 Q340 180 354 196 V230 Z" fill="#5c4033"/>']
    for k, x in enumerate((40, 100, 160, 220)):
        sk = SKIN[k % 4]
        b.append(person(x, 380, .75, sk, ("#bc6c25", "#6a994e", "#e76f51", "#457b9d")[k], "#7f5539", "#3e2723",
                        "short", mood="angry", larm=((-12, 40), (-14, 72)), rarm=((24, -26), (34, -60)), rot=6))
        if k % 2:
            b.append(torch(x + 38, 220, 10, 1.1))
        else:
            b.append(pitchfork(x + 32, 260, 10))
    b += [arrow(250, 330, 320, 290, "#264653", 5, 14)]
    return svg(b, "#5c4d7d")


def guess():
    rnd = random.Random(8)
    colors = ["#e63946", "#ffd166", "#2a9d8f", "#4895ef", "#f4a261", "#a7c957", "#ff8fab", "#fff"]
    b = ['<rect y="330" width="400" height="70" fill="#9c6b3c"/>',
         '<rect x="200" y="100" width="170" height="232" rx="26" fill="#eef7fb" stroke="#8ecae6" stroke-width="5"/>',
         '<rect x="212" y="80" width="146" height="26" rx="6" fill="#e76f51"/>']
    for _ in range(170):
        x, y = rnd.uniform(214, 356), rnd.uniform(150, 322)
        b.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="8" ry="5" fill="{rnd.choice(colors)}" '
                 f'transform="rotate({rnd.randint(0, 180)} {f(x)} {f(y)})"/>')
    b += ['<rect x="212" y="120" width="10" height="190" rx="5" fill="#fff" opacity=".6"/>',
          shadow(90, 344, 34),
          person(90, 342, 1.05, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "bun", mood="side",
                 brows="M-12 -188 L0 -186 M4 -190 Q10 -196 16 -190",
                 larm=((-12, 40), (-14, 72)), rarm=((20, 20), (2, -8))),
          '<circle cx="140" cy="80" r="8" fill="#fff" stroke="#ced4da" stroke-width="2"/>',
          '<circle cx="160" cy="54" r="12" fill="#fff" stroke="#ced4da" stroke-width="2"/>',
          '<ellipse cx="110" cy="40" rx="0" ry="0" fill="#fff"/>']
    return svg(b, "#fdf6ec")


def innovation():
    b = ['<rect y="290" width="400" height="110" fill="#d4a373"/>', '<path d="M0 330 H400" stroke="#b08968" stroke-width="3"/>',
         '<circle cx="340" cy="60" r="26" fill="#ffd166"/>',
         # the old way: a horse and carriage
         '<rect x="14" y="230" width="66" height="50" rx="6" fill="#7f5539"/>',
         '<circle cx="28" cy="290" r="16" fill="none" stroke="#3e2723" stroke-width="4"/>',
         '<circle cx="68" cy="290" r="16" fill="none" stroke="#3e2723" stroke-width="4"/>',
         '<line x1="80" y1="262" x2="104" y2="262" stroke="#3e2723" stroke-width="3"/>',
         horse_side(140, 304, .62),
         # the new way: the first automobile rolling past
         '<g transform="translate(300 306) scale(.95)">'
         '<rect x="-70" y="-60" width="130" height="34" rx="6" fill="#e63946"/>'
         '<path d="M-40 -60 V-96 H20 V-60" fill="none" stroke="#343a40" stroke-width="5"/>'
         '<rect x="-46" y="-102" width="72" height="8" rx="3" fill="#343a40"/>'
         '<circle cx="-46" cy="-14" r="22" fill="none" stroke="#343a40" stroke-width="6"/>'
         '<circle cx="40" cy="-14" r="22" fill="none" stroke="#343a40" stroke-width="6"/>'
         '<circle cx="60" cy="-46" r="7" fill="#ffd166"/></g>',
         '<path d="M210 248 h-18 M212 266 h-24 M212 284 h-16" stroke="#fff" stroke-width="4" stroke-linecap="round"/>',
         sparkle(300, 150, 12, "#ffd166"), sparkle(372, 190, 9, "#ffd166"),
         # amazed onlookers
         person(120, 392, .52, SKIN[0], "#457b9d", "#264653", "#7f5539", "cap", mood="wide",
                larm=((-12, 40), (-14, 72)), rarm=((24, -10), (40, -30))),
         person(176, 394, .5, SKIN[3], "#e9c46a", "#264653", "#1b1b1b", "bun", mood="wide", skirt=True,
                larm=((-24, -10), (-40, -30)), rarm=((12, 40), (14, 72)))]
    return svg(b, "#cfe8f3")


def extricated():
    b = ['<rect y="300" width="400" height="100" fill="#adb5bd"/>',
         '<rect x="0" y="260" width="180" height="60" fill="#6c757d"/>',
         '<ellipse cx="180" cy="290" rx="20" ry="32" fill="#343a40"/>',
         '<rect x="0" y="252" width="180" height="10" fill="#495057"/>',
         # the little dog, half out
         '<ellipse cx="216" cy="282" rx="40" ry="22" fill="#e9c46a"/>',
         '<circle cx="250" cy="262" r="20" fill="#e9c46a"/>',
         '<ellipse cx="238" cy="246" rx="8" ry="14" fill="#c08552" transform="rotate(-30 238 246)"/>',
         f'<circle cx="256" cy="258" r="3.5" fill="{INK}"/><circle cx="268" cy="266" r="4" fill="{INK}"/>',
         '<path d="M252 272 Q258 278 264 272" fill="none" stroke="#264653" stroke-width="2.5"/>',
         person(300, 340, 1.0, SKIN[1], "#e63946", "#264653", "#1b1b1b", "cap", mood="smile",
                larm=((-30, 40), (-70, 64)), rarm=((-10, 46), (-56, 72))),
         person(370, 336, .9, SKIN[3], "#f4a261", "#264653", "#1b1b1b", "short", mood="smile",
                larm=((-30, 20), (-60, 40)), rarm=((12, 40), (14, 72))),
         heart(280, 120, 12), sparkle(220, 220, 9, "#ffd166"),
         arrow(150, 200, 220, 200, "#2a9d8f", 5, 14)]
    return svg(b, "#e3f2fd")


def jam_jar(x, y, fruit, lid="#e63946"):
    return (f'<rect x="{x - 26}" y="{y - 70}" width="52" height="70" rx="10" fill="{fruit}"/>'
            f'<rect x="{x - 20}" y="{y - 62}" width="8" height="50" rx="4" fill="#fff" opacity=".35"/>'
            f'<rect x="{x - 28}" y="{y - 82}" width="56" height="14" rx="4" fill="{lid}"/>'
            f'<path d="M{x - 28} {y - 80} l6 -8 l8 6 l8 -6 l8 6 l8 -6 l8 6 l8 -6 l4 8" fill="#fff"/>'
            f'<rect x="{x - 16}" y="{y - 46}" width="32" height="22" rx="3" fill="#fefae0"/>')


def preserving():
    b = ['<rect x="20" y="20" width="360" height="360" rx="6" fill="#9c6644"/>',
         '<rect x="34" y="34" width="332" height="332" fill="#e6ccb2"/>']
    rows = ((150, ("#e63946", "#9d0208", "#f77f00", "#6d597a", "#e63946")),
            (260, ("#f4a261", "#6d597a", "#e63946", "#a7c957", "#9d0208")),
            (360, ("#9d0208", "#f77f00", "#6d597a", "#e63946", "#f4a261")))
    for y, fruits in rows:
        b.append(f'<rect x="34" y="{y}" width="332" height="12" fill="#7f5539"/>')
        for k, fr in enumerate(fruits):
            b.append(jam_jar(70 + k * 65, y, fr, ("#e63946", "#2a9d8f", "#e9c46a")[k % 3]))
    return svg(b, "#fdf6ec")


PICTURES = {
    "valuable": valuable,
    "delivered": delivered,
    "tedious": tedious,
    "collaboration": collaboration,
    "limited": limited,
    "overcome": overcome,
    "hiding": hiding,
    "superficial": superficial,
    "accessible": accessible,
    "conceal": conceal,
    "forgotten": forgotten,
    "postpone": postpone,
    "distinctive": distinctive,
    "haphazard": haphazard,
    "harsh": harsh,
    "drained": drained,
    "alarmed": alarmed,
    "discovery": discovery,
    "supplied": supplied,
    "distinguish": distinguish,
    "saturated with": saturated_with,
    "encompass": encompass,
    "empty": empty,
    "skilled in": skilled_in,
    "arranged": arranged,
    "disguise": disguise,
    "biased": biased,
    "dangerous": dangerous,
    "reprieve": reprieve,
    "tolerate": tolerate,
    "confident": confident,
    "defends": defends,
    "counting": counting,
    "pulled": pulled,
    "invented": invented,
    "genuine": genuine,
    "secluded": secluded,
    "meticulous": meticulous,
    "judge": judge,
    "protect": protect,
    "shapeless": shapeless,
    "rewards": rewards,
    "delegate": delegate,
    "lacking": lacking,
    "confused": confused,
    "rebellion": rebellion,
    "guess": guess,
    "innovation": innovation,
    "extricated": extricated,
    "preserving": preserving,
}
