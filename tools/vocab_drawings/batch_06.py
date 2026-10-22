"""Batch 6: drawings 231-280 (each function returns one SVG; PICTURES maps word -> function).

The figures and small shapes come from batch_01.py to batch_05.py.
"""

import math
import random

from batch_01 import apple, bird, gear
from batch_02 import SKIN, bee, duck, heart, limb, person, shadow, sparkle
from batch_03 import curls, side_runner
from batch_05 import crate, hard_hat
from common import INK, arc_arrow, arrow, bush, carrow, f, svg


def painting(x, y, w, h, sky, sun, hill, hill2, frame="#b08968"):
    return (f'<rect x="{f(x - 8)}" y="{f(y - 8)}" width="{f(w + 16)}" height="{f(h + 16)}" fill="{frame}"/>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{sky}"/>'
            f'<circle cx="{f(x + w * .7)}" cy="{f(y + h * .32)}" r="{f(w * .13)}" fill="{sun}"/>'
            f'<path d="M{f(x)} {f(y + h * .78)} Q{f(x + w * .3)} {f(y + h * .45)} {f(x + w * .6)} {f(y + h * .72)} '
            f'T{f(x + w)} {f(y + h * .6)} V{f(y + h)} H{f(x)} Z" fill="{hill}"/>'
            f'<path d="M{f(x)} {f(y + h)} Q{f(x + w * .5)} {f(y + h * .7)} {f(x + w)} {f(y + h * .92)} V{f(y + h)} Z" '
            f'fill="{hill2}"/>')


def accentuate():
    dim = ("#4a4e69", "#6c6f7d", "#3d5a50", "#344e41", "#5c4d3c")
    b = ['<rect y="320" width="400" height="80" fill="#2b2d42"/>',
         painting(28, 150, 80, 64, *dim), painting(292, 150, 80, 64, *dim),
         # the spotlight
         '<polygon points="178,34 222,34 304,320 96,320" fill="#fff3b0" opacity=".22"/>',
         '<ellipse cx="200" cy="322" rx="104" ry="12" fill="#fff3b0" opacity=".3"/>',
         '<rect x="196" y="0" width="8" height="16" fill="#6c757d"/>',
         '<polygon points="184,14 216,14 224,36 176,36" fill="#adb5bd"/>',
         '<rect x="128" y="110" width="144" height="124" fill="#fff3b0" opacity=".45"/>',
         painting(144, 126, 112, 92, "#caf0f8", "#ffd166", "#52b788", "#2d6a4f", "#e9c46a"),
         sparkle(118, 120, 10, "#ffd166"), sparkle(286, 110, 12, "#ffd166"), sparkle(282, 236, 8, "#ffd166"),
         sparkle(116, 230, 7, "#ffd166")]
    return svg(b, "#22223b")


def vacate():
    b = ['<rect y="330" width="400" height="70" fill="#ced4da"/>',
         # the emptied building with scaffolding on it
         '<rect x="30" y="50" width="170" height="280" fill="#d4a373"/>',
         '<rect x="22" y="40" width="186" height="14" fill="#9c6644"/>']
    for r in range(4):
        for c in range(3):
            b.append(f'<rect x="{48 + c * 52}" y="{74 + r * 48}" width="30" height="30" fill="#264653"/>')
    b += ['<rect x="96" y="268" width="40" height="62" fill="#343a40"/>',
          '<polygon points="136,268 156,276 156,334 136,330" fill="#9c6644"/>',
          '<path d="M40 40 V330 M190 40 V330" stroke="#6c757d" stroke-width="5"/>',
          '<path d="M34 156 H196 M34 236 H196" stroke="#adb5bd" stroke-width="8"/>',
          person(70, 232, .45, SKIN[2], "#f4a261", "#264653", "#000", "none", mood="smile",
                 rarm=((24, -10), (40, -24)), extra=hard_hat("#ffd166") +
                 '<rect x="56" y="-196" width="8" height="34" fill="#7f5539" transform="rotate(30 60 -170)"/>'
                 '<rect x="50" y="-200" width="24" height="12" fill="#6c757d" transform="rotate(30 60 -170)"/>')]
    suitcase = ('<path d="M-52 -60 V-88" stroke="#495057" stroke-width="4"/>'
                '<rect x="-74" y="-62" width="44" height="54" rx="6" fill="{c}"/>'
                '<circle cx="-66" cy="-4" r="4" fill="#343a40"/><circle cx="-38" cy="-4" r="4" fill="#343a40"/>')
    for x, sk, shirt, hair, style, c in ((246, SKIN[0], "#457b9d", "#5c4033", "short", "#e63946"),
                                         (340, SKIN[3], "#2a9d8f", "#1b1b1b", "bun", "#7209b7")):
        b += [shadow(x, 344, 30),
              person(x, 342, .86, sk, shirt, "#264653", hair, style, mood="side",
                     larm=((-20, 30), (-30, 58)), rarm=((14, 40), (18, 72)),
                     lleg=((-10, 44), (-16, 86)), rleg=((10, 44), (18, 86)),
                     extra=suitcase.replace("{c}", c))]
    b.append(arrow(160, 374, 380, 374, "#e76f51", 7, 18))
    return svg(b, "#e3f2fd")


def running_to():
    rnd = random.Random(4)
    b = ['<rect y="310" width="400" height="90" fill="#b08968"/>',
         # the window and the parade outside it
         '<rect x="236" y="56" width="152" height="196" fill="#fff"/>',
         '<rect x="246" y="66" width="132" height="176" fill="#caf0f8"/>',
         '<rect x="246" y="200" width="132" height="42" fill="#adb5bd"/>',
         '<path d="M246 86 Q312 108 378 86" fill="none" stroke="#6c757d" stroke-width="2"/>']
    for k, c in enumerate(("#e63946", "#ffd166", "#2a9d8f", "#4895ef", "#e63946", "#f4a261")):
        x = 256 + k * 22
        y = 86 + 22 * math.sin(math.pi * (x - 246) / 132) * .45
        b.append(f'<polygon points="{f(x - 7)},{f(y - 1)} {f(x + 7)},{f(y + 1)} {f(x)},{f(y + 14)}" fill="{c}"/>')
    for x, shirt, hat in ((276, "#e63946", "#ffd166"), (318, "#4895ef", "#e63946"), (356, "#ffd166", "#2a9d8f")):
        b += [person(x, 236, .34, SKIN[1], shirt, "#264653", "#5c4033", "short", mood="grin",
                     larm=((-20, -30), (-26, -60)), rarm=((12, 40), (16, 72)),
                     extra=f'<rect x="-18" y="-232" width="36" height="34" rx="4" fill="{hat}"/>'
                           f'<rect x="-28" y="-202" width="56" height="8" rx="3" fill="{hat}"/>')]
    for x, y, c in ((268, 116, "#e63946"), (300, 104, "#ffd166"), (350, 120, "#7209b7")):
        b.append(f'<path d="M{x} {y + 14} Q{x - 4} {y + 40} {x + 4} {y + 70}" fill="none" stroke="#6c757d" stroke-width="1.5"/>'
                 f'<ellipse cx="{x}" cy="{y}" rx="12" ry="15" fill="{c}"/>')
    for _ in range(26):
        x, y = rnd.uniform(250, 374), rnd.uniform(70, 236)
        b.append(f'<rect x="{f(x)}" y="{f(y)}" width="5" height="3" fill="{rnd.choice(["#e63946", "#ffd166", "#2a9d8f", "#f4a261"])}" '
                 f'transform="rotate({rnd.randint(0, 90)} {f(x)} {f(y)})"/>')
    b += ['<path d="M312 66 V242 M246 154 H378" stroke="#fff" stroke-width="6"/>',
          '<rect x="226" y="248" width="172" height="12" fill="#e9ecef"/>',
          # the child dashing across the room
          '<path d="M30 200 H80 M18 230 H74 M36 260 H82" stroke="#adb5bd" stroke-width="5" stroke-linecap="round"/>',
          '<ellipse cx="140" cy="318" rx="40" ry="6" fill="#000" opacity=".12"/>',
          side_runner(140, 300, 1.15, "#e76f51", SKIN[2], "#1b1b1b")]
    return svg(b, "#fdf0d5")


def back_view(x, y, s, shirt, hair, skin, bun=False, arm_up=False):
    """Someone seated with their back to us: shoulders and the back of the head, base at (x, y)."""
    out = [f'<g transform="translate({f(x)} {f(y)}) scale({s})">']
    if arm_up:
        out.append(limb(((22, -52), (34, -96), (30, -134)), shirt, 15) + f'<circle cx="30" cy="-136" r="9" fill="{skin}"/>')
    out += [f'<rect x="-36" y="-56" width="72" height="80" rx="24" fill="{shirt}"/>',
            f'<rect x="-7" y="-64" width="14" height="12" fill="{skin}"/>',
            f'<circle cx="-23" cy="-84" r="6" fill="{skin}"/><circle cx="23" cy="-84" r="6" fill="{skin}"/>',
            f'<circle cx="0" cy="-86" r="24" fill="{hair}"/>']
    if bun:
        out.append(f'<circle cx="0" cy="-108" r="11" fill="{hair}"/>')
    out.append('</g>')
    return "".join(out)


def teach():
    b = ['<rect y="300" width="400" height="100" fill="#d4a373"/>',
         # the board and its pictures
         '<rect x="150" y="40" width="234" height="164" rx="4" fill="#9c6644"/>',
         '<rect x="160" y="50" width="214" height="144" fill="#2d6a4f"/>',
         apple(204, 112, 24),
         '<polygon points="236,112 266,86 296,112" fill="#e76f51"/><rect x="242" y="112" width="48" height="36" fill="#fff"/>'
         '<rect x="260" y="126" width="14" height="22" fill="#9c6644"/>',
         '<circle cx="338" cy="110" r="18" fill="#ffd166"/>',
         '<path d="M338 82 V74 M338 138 V146 M310 110 H302 M366 110 H374 M318 90 L312 84 M358 90 L364 84 '
         'M318 130 L312 136 M358 130 L364 136" stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>',
         '<rect x="166" y="194" width="202" height="8" fill="#9c6644"/>',
         shadow(72, 334, 32),
         person(72, 332, 1.0, SKIN[3], "#e76f51", "#264653", "#1b1b1b", "bun", mood="smile",
                larm=((-12, 40), (-16, 72)), rarm=((24, -20), (52, -42))),
         '<line x1="144" y1="146" x2="182" y2="118" stroke="#7f5539" stroke-width="5" stroke-linecap="round"/>',
         f'<circle cx="146" cy="144" r="8.5" fill="{SKIN[3]}"/>',
         back_view(150, 392, 1.0, "#457b9d", "#adb5bd", SKIN[0]),
         back_view(254, 392, 1.0, "#e9c46a", "#1b1b1b", SKIN[2], bun=True, arm_up=True),
         back_view(352, 392, 1.0, "#6a994e", "#5c4033", SKIN[1])]
    return svg(b, "#e9ecef")


def plane(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<path d="M-120 -40 L-140 -96 H-112 L-80 -40 Z" fill="#457b9d"/>'
            '<path d="M-130 -40 H110 Q140 -40 140 -20 Q140 0 110 0 H-120 Q-140 0 -136 -20 Z" fill="#f8f9fa"/>'
            '<path d="M104 -36 Q124 -34 132 -22 H104 Z" fill="#264653"/>'
            + "".join(f'<circle cx="{-96 + i * 22}" cy="-22" r="5" fill="#4895ef"/>' for i in range(9))
            + '<polygon points="-30,-12 30,-12 -6,40 -34,40" fill="#adb5bd"/>'
            '<path d="M-60 0 V14 M70 0 V14" stroke="#495057" stroke-width="4"/>'
            '<circle cx="-60" cy="18" r="7" fill="#343a40"/><circle cx="70" cy="18" r="7" fill="#343a40"/></g>')


def delayed_by():
    rnd = random.Random(6)
    b = ['<rect y="290" width="400" height="110" fill="#e9ecef"/>',
         '<rect y="306" width="400" height="60" fill="#6c757d"/>',
         '<path d="M0 336 H400" stroke="#fff" stroke-width="4" stroke-dasharray="26 18"/>',
         plane(196, 280, 1.15),
         '<path d="M62 232 Q200 222 350 232" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>',
         # the clock ticking on
         '<circle cx="330" cy="80" r="34" fill="#fff" stroke="#495057" stroke-width="5"/>',
         '<path d="M330 80 V58 M330 80 L348 90" stroke="#264653" stroke-width="4" stroke-linecap="round"/>',
         arc_arrow(330, 80, 48, -150, 60, "#e63946", 5, 14)]
    for _ in range(4):
        x, y = rnd.uniform(20, 380), rnd.uniform(20, 260)
        b.append(f'<path d="M{f(x)} {f(y)} q30 -20 60 0 t60 0" fill="none" stroke="#fff" stroke-width="3" '
                 'stroke-linecap="round" opacity=".7"/>')
    for _ in range(70):
        x, y = rnd.uniform(0, 400), rnd.uniform(0, 390)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(2.5, 5.5))}" fill="#fff"/>')
    return svg(b, "#9aa5b1")


def follows():
    b = ['<rect y="200" width="400" height="200" fill="#a7c957"/>',
         '<ellipse cx="20" cy="290" rx="70" ry="30" fill="#4895ef"/>',
         '<ellipse cx="22" cy="286" rx="50" ry="18" fill="#a8dadc" opacity=".5"/>',
         '<path d="M100 300 Q220 316 390 300" fill="none" stroke="#8a9a5b" stroke-width="3" stroke-dasharray="2 12" '
         'stroke-linecap="round"/>',
         duck(110, 296, 2.4)]
    for k, x in enumerate((196, 250, 304, 358)):
        b.append(duck(x, 300 + k * 1.5, 1.15))
    b += [bush(380, 196, 30), bush(330, 204, 22), bush(140, 200, 18)]
    return svg(b, "#e3f2fd")


def synchronization():
    b = ['<rect y="200" width="400" height="200" fill="#4895ef"/>',
         '<path d="M0 200 H400" stroke="#a8dadc" stroke-width="4"/>']
    for x in (64, 152, 240, 328):
        b += [person(x, 360, .8, SKIN[1], "#e63946", "#264653", "#e63946", "cap", mood="content",
                     larm=((4, -44), (26, -86)), rarm=((20, -40), (46, -78)))]
    b += ['<rect y="252" width="400" height="148" fill="#4895ef"/>']
    for x in (64, 152, 240, 328):
        b.append(f'<ellipse cx="{x}" cy="254" rx="40" ry="7" fill="none" stroke="#caf0f8" stroke-width="3"/>')
    b += ['<path d="M0 300 Q50 292 100 300 T200 300 T300 300 T400 300 M0 350 Q50 342 100 350 T200 350 T300 350 T400 350" '
          'fill="none" stroke="#a8dadc" stroke-width="3" opacity=".7"/>',
          sparkle(110, 60, 12, "#ffd166"), sparkle(200, 40, 9, "#ffd166"), sparkle(290, 60, 12, "#ffd166")]
    return svg(b, "#caf0f8")


def ladder_h(x1, x2, y):
    out = [f'<path d="M{x1} {y - 10} H{x2} M{x1} {y + 10} H{x2}" stroke="#bc6c25" stroke-width="6" stroke-linecap="round"/>']
    for x in range(x1 + 12, x2, 20):
        out.append(f'<path d="M{x} {y - 10} V{y + 10}" stroke="#bc6c25" stroke-width="4"/>')
    return "".join(out)


def borrow():
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         '<rect x="-10" y="150" width="70" height="170" fill="#e9c46a"/><polygon points="-20,150 70,150 -20,90" fill="#bc4749"/>',
         '<rect x="10" y="190" width="30" height="30" fill="#caf0f8"/>',
         '<rect x="340" y="150" width="70" height="170" fill="#90e0ef"/><polygon points="330,150 420,150 420,90" fill="#6d597a"/>',
         '<rect x="360" y="190" width="30" height="30" fill="#fff"/>']
    for x in range(150, 256, 18):
        b.append(f'<path d="M{x - 7} 330 V244 L{x} 234 L{x + 7} 244 V330 Z" fill="#fff"/>')
    b += ['<path d="M140 262 H260 M140 302 H260" stroke="#fff" stroke-width="6"/>',
          shadow(102, 334, 30), shadow(306, 334, 30),
          person(102, 332, 1.0, SKIN[1], "#457b9d", "#264653", "#5c4033", "short", mood="smile",
                 larm=((-12, 40), (-16, 72)), rarm=((26, 20), (52, 14))),
          person(306, 332, 1.0, SKIN[3], "#f4a261", "#264653", "#1b1b1b", "side", mood="grin",
                 larm=((-26, 20), (-52, 14)), rarm=((12, 40), (16, 72))),
          ladder_h(112, 300, 200),
          f'<circle cx="176" cy="200" r="8.5" fill="{SKIN[1]}"/><circle cx="232" cy="200" r="8.5" fill="{SKIN[3]}"/>',
          arrow(150, 120, 262, 120, "#2a9d8f", 6, 16)]
    return svg(b, "#e3f2fd")


def snowman(x, y, k, droop=0.0):
    """A snowman standing on (x, y); droop slumps it to one side as it melts."""
    out = [f'<g transform="translate({f(x)} {f(y)}) scale({k})">',
           '<ellipse cx="0" cy="-30" rx="46" ry="38" fill="#fff"/>',
           f'<ellipse cx="{f(droop * 8)}" cy="-92" rx="34" ry="30" fill="#fff"/>',
           f'<g transform="rotate({f(droop * 22)} 0 -100)"><circle cx="0" cy="-140" r="24" fill="#fff"/>'
           f'<circle cx="-8" cy="-146" r="3" fill="{INK}"/><circle cx="8" cy="-146" r="3" fill="{INK}"/>'
           '<polygon points="0,-140 22,-136 0,-132" fill="#f4a261"/>'
           '<rect x="-20" y="-168" width="40" height="8" fill="#343a40"/><rect x="-13" y="-194" width="26" height="28" '
           'fill="#343a40"/></g>',
           '<circle cx="0" cy="-96" r="3" fill="#343a40"/><circle cx="0" cy="-82" r="3" fill="#343a40"/>',
           '</g>']
    return "".join(out)


def diminish():
    b = ['<rect y="300" width="400" height="100" fill="#e9ecef"/>',
         '<circle cx="350" cy="56" r="30" fill="#ffd166"/>',
         '<path d="M350 12 V2 M350 100 V110 M306 56 H296 M394 56 H404 M319 25 L312 18 M381 87 L388 94 M319 87 L312 94 '
         'M381 25 L388 18" stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>',
         snowman(76, 304, 1.05),
         '<ellipse cx="204" cy="304" rx="52" ry="9" fill="#a8dadc"/>',
         snowman(204, 304, .72, 1.0),
         '<path d="M188 230 v10 M226 246 v10" stroke="#4895ef" stroke-width="4" stroke-linecap="round"/>',
         '<ellipse cx="330" cy="306" rx="60" ry="12" fill="#a8dadc"/>',
         '<ellipse cx="324" cy="298" rx="24" ry="12" fill="#fff"/>',
         '<polygon points="342,300 364,306 342,310" fill="#f4a261"/>',
         '<rect x="296" y="292" width="34" height="7" fill="#343a40" transform="rotate(-14 313 296)"/>'
         '<rect x="300" y="270" width="22" height="24" fill="#343a40" transform="rotate(-14 313 296)"/>',
         arrow(128, 356, 160, 356, "#e76f51", 6, 14), arrow(250, 356, 282, 356, "#e76f51", 6, 14)]
    return svg(b, "#cfe8f3")


def scratchy():
    fuzz = []
    for a in range(-160, -10, 12):
        t = math.radians(a)
        fuzz.append(f'M{f(30 * math.cos(t))} {f(-146 + 8 * math.sin(t))} l{f(5 * math.cos(t))} {f(5 * math.sin(t))}')
    for yy in range(-150, -86, 9):
        fuzz.append(f'M-30 {yy} l-6 -2 M30 {yy} l6 -2')
    for xx in range(-26, 30, 9):
        fuzz.append(f'M{xx} -82 l2 6')
    sweater = (f'<path d="{" ".join(fuzz)}" stroke="#bc6c25" stroke-width="2.5" stroke-linecap="round"/>'
               '<rect x="-16" y="-156" width="32" height="10" rx="5" fill="#e9c46a"/>')
    knit = "".join(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#d4a373"/>'
                   for x in (-16, 0, 16) for y in (-136, -120, -104))
    arms = (f'<g transform="translate(200 342) scale(1.3)">'
            + limb(((22, -146), (36, -152), (26, -170)), "#e9c46a", 15) + f'<circle cx="26" cy="-170" r="8.5" fill="{SKIN[0]}"/>'
            + limb(((-22, -146), (-42, -120), (-40, -96)), "#e9c46a", 15) + f'<circle cx="-40" cy="-96" r="8.5" fill="{SKIN[0]}"/>'
            + '<path d="M-20 -146 l-3 -6 M-26 -132 l-7 -2 M28 -150 l6 -3 M40 -140 l7 0" stroke="#bc6c25" stroke-width="2.5" '
            'stroke-linecap="round"/></g>')
    b = ['<rect y="340" width="400" height="60" fill="#d4a373"/>',
         shadow(200, 344, 44),
         person(200, 342, 1.3, SKIN[0], "#e9c46a", "#457b9d", "#d4a373", "short", mood="frown",
                brows="M-14 -188 L-3 -192 M3 -192 L14 -188",
                larm=((0, 0), (0, 0)), rarm=((0, 0), (0, 0)), extra=knit + sweater),
         arms,
         '<path d="M166 120 l-6 -10 M158 136 l-12 -4 M244 150 l10 -6 M250 164 l12 0" stroke="#e63946" stroke-width="4" '
         'stroke-linecap="round"/>',
         '<path d="M264 96 l14 -6 M268 112 l16 0 M126 214 l-14 -4 M126 230 l-16 2" stroke="#adb5bd" stroke-width="4" '
         'stroke-linecap="round"/>']
    return svg(b, "#fde2e4")


def swimming_dog(x, y):
    """A dog's head and back above the water, swimming left with a stick; head centre (x, y)."""
    return (f'<ellipse cx="{x + 46}" cy="{y + 18}" rx="36" ry="12" fill="#c08552"/>'
            f'<circle cx="{x}" cy="{y}" r="24" fill="#c08552"/>'
            f'<ellipse cx="{x - 24}" cy="{y + 8}" rx="18" ry="12" fill="#e6ccb2"/>'
            f'<circle cx="{x - 40}" cy="{y + 2}" r="6" fill="{INK}"/>'
            f'<circle cx="{x - 8}" cy="{y - 7}" r="4" fill="{INK}"/>'
            f'<path d="M{x + 4} {y - 20} Q{x + 26} {y - 14} {x + 22} {y + 12} Q{x + 10} {y} {x + 2} {y - 10} Z" fill="#7f5539"/>'
            f'<rect x="{x - 64}" y="{y + 12}" width="88" height="9" rx="4" fill="#9c6644" transform="rotate(-6 {x - 20} {y + 16})"/>')


def retrieving():
    b = ['<rect y="216" width="400" height="184" fill="#4895ef"/>',
         '<path d="M0 216 H400" stroke="#a8dadc" stroke-width="4"/>',
         '<path d="M0 250 Q80 240 130 270 Q150 330 120 400 H0 Z" fill="#e9c46a"/>',
         shadow(64, 286, 26),
         person(64, 284, .8, SKIN[0], "#e76f51", "#264653", "#5c4033", "side", mood="grin",
                larm=((-26, -16), (-40, -50)), rarm=((26, -16), (40, -50))),
         swimming_dog(232, 228),
         '<path d="M146 250 Q140 300 150 400 H400 V250 Z" fill="#4895ef"/>',
         '<path d="M190 252 Q232 262 300 252" fill="none" stroke="#caf0f8" stroke-width="4" stroke-linecap="round"/>',
         '<path d="M300 236 Q330 244 360 236 M306 266 Q336 276 372 268" fill="none" stroke="#caf0f8" stroke-width="4" '
         'stroke-linecap="round"/>',
         arrow(270, 170, 180, 170, "#e76f51", 6, 16)]
    return svg(b, "#e3f2fd")


def habitable():
    rnd = random.Random(12)
    b = []
    for _ in range(60):
        b.append(f'<circle cx="{f(rnd.uniform(0, 400))}" cy="{f(rnd.uniform(0, 400))}" r="{f(rnd.uniform(1, 2.6))}" '
                 'fill="#fff" opacity=".8"/>')
    b += ['<circle cx="70" cy="80" r="28" fill="#adb5bd"/><circle cx="60" cy="72" r="6" fill="#8d99ae"/>'
          '<circle cx="80" cy="92" r="5" fill="#8d99ae"/><circle cx="78" cy="66" r="3" fill="#8d99ae"/>',
          '<circle cx="340" cy="334" r="32" fill="#e76f51"/><circle cx="330" cy="326" r="6" fill="#bc4749"/>'
          '<circle cx="352" cy="344" r="7" fill="#bc4749"/>',
          '<circle cx="200" cy="200" r="142" fill="#a8dadc" opacity=".2"/>',
          '<circle cx="200" cy="200" r="122" fill="#a8dadc" opacity=".3"/>',
          '<clipPath id="globe"><circle cx="200" cy="200" r="104"/></clipPath>',
          '<circle cx="200" cy="200" r="104" fill="#4895ef"/>',
          '<g clip-path="url(#globe)">',
          '<path d="M110 130 Q150 100 190 120 Q210 150 180 170 Q160 200 120 190 Q90 160 110 130 Z" fill="#52b788"/>',
          '<path d="M220 200 Q260 180 300 210 Q310 260 270 290 Q240 300 230 260 Q210 230 220 200 Z" fill="#52b788"/>',
          '<path d="M140 250 Q160 240 175 260 Q170 280 150 280 Z" fill="#40916c"/>',
          '<path d="M120 112 Q200 96 280 120" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".85"/>',
          '<path d="M100 230 Q160 216 210 232" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".85"/>',
          '<path d="M230 166 Q280 150 320 170" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".85"/>',
          '<circle cx="250" cy="250" r="110" fill="#14213d" opacity=".18"/>',
          '</g>',
          sparkle(330, 90, 12, "#fff"), sparkle(84, 300, 9, "#fff")]
    return svg(b, "#14213d")


def straw_hat():
    return ('<ellipse cx="0" cy="-196" rx="38" ry="8" fill="#e9c46a"/>'
            '<path d="M-20 -196 Q-20 -224 0 -224 Q20 -224 20 -196 Z" fill="#e9c46a"/>'
            '<rect x="-20" y="-204" width="40" height="7" fill="#bc4749"/>')


def dispute():
    b = ['<rect y="230" width="200" height="170" fill="#e9c46a"/>', '<rect x="200" y="230" width="200" height="170" fill="#6a994e"/>']
    for x in range(14, 200, 26):
        b.append(f'<path d="M{x} 400 V240" stroke="#d4a373" stroke-width="3"/><ellipse cx="{x}" cy="240" rx="5" ry="10" fill="#d4a373"/>')
    for y in range(250, 400, 24):
        b.append(f'<path d="M200 {y} H400" stroke="#386641" stroke-width="5" stroke-dasharray="10 8"/>')
    b += ['<rect x="194" y="200" width="12" height="140" fill="#9c6644"/>',
          '<rect x="186" y="196" width="28" height="8" fill="#7f5539"/>',
          shadow(98, 354, 32), shadow(302, 354, 32),
          person(98, 352, 1.05, SKIN[1], "#457b9d", "#264653", "#5c4033", "short", mood="wide",
                 brows="M-14 -192 L-3 -186 M3 -186 L14 -192",
                 larm=((-12, 40), (-16, 72)), rarm=((26, -8), (46, -16)), extra=straw_hat()),
          person(302, 352, 1.05, SKIN[3], "#bc4749", "#264653", "#1b1b1b", "short", mood="wide",
                 brows="M-14 -192 L-3 -186 M3 -186 L14 -192",
                 larm=((-26, -8), (-46, -16)), rarm=((12, 40), (16, 72)), extra=straw_hat()),
          '<polygon points="210,40 184,90 202,92 180,140 226,78 208,76 228,40" fill="#ffd166" stroke="#e76f51" '
          'stroke-width="4" stroke-linejoin="round"/>']
    return svg(b, "#e3f2fd")


def diver(x, y, k=1.0):
    """A diver swimming right with a torch held out in front; body centre (x, y)."""
    suit = "#264653"
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            + limb(((-30, 0), (-70, 8), (-104, 0)), suit, 14) + limb(((-30, 6), (-68, 22), (-100, 24)), suit, 14)
            + '<polygon points="-100,-8 -132,-22 -128,8 -104,8" fill="#ffd166"/>'
            '<polygon points="-98,16 -128,14 -122,40 -100,32" fill="#ffd166"/>'
            '<rect x="-36" y="-34" width="44" height="16" rx="8" fill="#e9c46a"/>'
            f'<rect x="-44" y="-16" width="70" height="30" rx="14" fill="{suit}"/>'
            + limb(((14, -2), (44, 8), (68, 2)), suit, 12)
            + f'<circle cx="68" cy="2" r="7" fill="{SKIN[1]}"/>'
            '<rect x="70" y="-6" width="26" height="14" rx="3" fill="#6c757d"/><rect x="94" y="-9" width="6" height="20" fill="#adb5bd"/>'
            f'<circle cx="38" cy="-14" r="16" fill="{SKIN[1]}"/>'
            f'<path d="M22 -26 Q38 -36 54 -24 L50 -20 Q38 -28 26 -20 Z" fill="{suit}"/>'
            '<rect x="40" y="-22" width="20" height="13" rx="5" fill="#caf0f8" stroke="#e63946" stroke-width="3"/>'
            '<circle cx="50" cy="-15" r="2.5" fill="#264653"/></g>')


def discover():
    rnd = random.Random(14)
    b = ['<path d="M0 0 H400 V60 Q330 100 260 70 Q200 50 140 80 Q70 110 0 70 Z" fill="#073b4c"/>',
         '<path d="M0 400 H400 V330 Q340 300 290 320 Q220 350 160 320 Q90 290 0 330 Z" fill="#073b4c"/>',
         '<path d="M330 330 l10 -40 l10 40 M360 330 l8 -26 l8 26" fill="#2a9d8f"/>',
         '<polygon points="240,194 300,196 300,252 240,206" fill="#fff3b0" opacity=".35"/>',
         diver(140, 200, 1.0),
         # the never-seen-before glowing fish
         '<circle cx="306" cy="226" r="46" fill="#90e0ef" opacity=".25"/>',
         '<circle cx="306" cy="226" r="30" fill="#90e0ef" opacity=".35"/>',
         '<path d="M330 226 L352 206 L350 246 Z" fill="#c77dff"/>',
         '<ellipse cx="304" cy="226" rx="30" ry="18" fill="#c77dff"/>',
         '<path d="M290 210 Q300 190 316 208" fill="#e0aaff"/>',
         '<path d="M284 210 Q272 182 290 176" fill="none" stroke="#e0aaff" stroke-width="3"/><circle cx="292" cy="176" r="6" fill="#fff3b0"/>',
         '<circle cx="288" cy="222" r="5" fill="#fff"/><circle cx="287" cy="222" r="2.5" fill="#264653"/>',
         '<circle cx="306" cy="234" r="3" fill="#fff3b0"/><circle cx="318" cy="226" r="3" fill="#fff3b0"/><circle cx="312" cy="216" r="2.5" fill="#fff3b0"/>',
         sparkle(352, 182, 9, "#fff3b0"), sparkle(262, 268, 7, "#fff3b0")]
    for k in range(4):
        b.append(f'<circle cx="{178 + k * 4}" cy="{170 - k * 26}" r="{4 + k}" fill="none" stroke="#caf0f8" stroke-width="2"/>')
    for _ in range(14):
        b.append(f'<circle cx="{f(rnd.uniform(0, 400))}" cy="{f(rnd.uniform(110, 300))}" r="1.8" fill="#a8dadc" opacity=".5"/>')
    return svg(b, "#0b525b")


def complex_():
    b = ['<rect x="160" y="0" width="80" height="70" fill="#7f5539"/><rect x="160" y="330" width="80" height="70" fill="#7f5539"/>',
         '<rect x="352" y="186" width="22" height="28" rx="4" fill="#c9a227"/>',
         '<circle cx="200" cy="200" r="160" fill="#e9c46a"/>',
         '<circle cx="200" cy="200" r="144" fill="#f1faee"/>']
    for cx, cy, R, n, rot, c in ((150, 160, 58, 12, 0, "#e9c46a"), (250, 140, 42, 10, 8, "#adb5bd"),
                                 (238, 232, 52, 11, 4, "#d4a373"), (140, 262, 40, 9, 12, "#bc6c25"),
                                 (306, 206, 30, 8, 0, "#e9c46a"), (196, 320, 30, 8, 6, "#adb5bd"),
                                 (98, 190, 26, 7, 0, "#d4a373"), (290, 290, 28, 8, 10, "#bc6c25"),
                                 (200, 78, 26, 7, 4, "#d4a373")):
        b.append(gear(cx, cy, R, n, rot, c))
    for x, y in ((120, 100), (290, 96), (330, 260), (90, 290)):
        b.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#e63946"/><circle cx="{x - 2}" cy="{y - 2}" r="2" fill="#fff"/>')
    return svg(b, "#fdf0d5")


def pretending():
    b = ['<rect y="320" width="400" height="80" fill="#b08968"/>',
         '<rect x="150" y="40" width="110" height="94" fill="#fff"/><rect x="158" y="48" width="94" height="78" fill="#caf0f8"/>',
         '<circle cx="230" cy="74" r="16" fill="#ffd166"/>',
         '<path d="M205 48 V126 M158 87 H252" stroke="#fff" stroke-width="5"/>',
         # the bed
         '<rect x="40" y="150" width="30" height="180" rx="6" fill="#9c6644"/>',
         '<rect x="56" y="250" width="290" height="60" fill="#9c6644"/>',
         '<rect x="56" y="230" width="290" height="40" fill="#fff"/>',
         '<ellipse cx="130" cy="234" rx="60" ry="22" fill="#fff" stroke="#dee2e6" stroke-width="3"/>',
         f'<circle cx="130" cy="212" r="32" fill="{SKIN[1]}"/>',
         '<path d="M98 210 Q96 176 130 176 Q164 176 162 206 Q150 192 128 190 Q108 192 98 210 Z" fill="#5c4033"/>',
         # one eye squeezed shut, the other peeking
         f'<path d="M110 210 Q118 204 126 212 M110 204 L124 208" fill="none" stroke="{INK}" stroke-width="3.5" '
         'stroke-linecap="round"/>',
         f'<circle cx="146" cy="208" r="5.5" fill="#fff"/><circle cx="148" cy="208" r="3" fill="{INK}"/>',
         f'<path d="M122 226 Q132 230 140 224" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>',
         '<path d="M112 244 Q130 236 160 240 Q250 226 346 236 V300 H112 Z" fill="#4895ef"/>',
         '<path d="M112 244 Q130 236 160 240 Q250 226 346 236" fill="none" stroke="#a8dadc" stroke-width="8"/>',
         # the ringing alarm clock
         '<rect x="352" y="250" width="48" height="80" fill="#7f5539"/>',
         '<circle cx="358" cy="208" r="9" fill="#e63946"/><circle cx="394" cy="208" r="9" fill="#e63946"/>',
         '<circle cx="376" cy="226" r="22" fill="#e63946"/><circle cx="376" cy="226" r="16" fill="#fff"/>',
         '<path d="M376 226 V214 M376 226 L386 230" stroke="#264653" stroke-width="3" stroke-linecap="round"/>',
         '<path d="M362 246 L356 252 M390 246 L396 252" stroke="#264653" stroke-width="4" stroke-linecap="round"/>',
         '<path d="M342 196 l-10 -8 M340 214 l-14 0 M352 180 l-6 -12" stroke="#e76f51" stroke-width="4" stroke-linecap="round"/>',
         # school bag waiting by the bed
         '<rect x="290" y="330" width="50" height="58" rx="10" fill="#2a9d8f"/><rect x="300" y="350" width="30" height="20" rx="4" fill="#52b788"/>']
    return svg(b, "#e0e1dd")


def lizard(x, y, k=1.0):
    """A lizard standing on (x, y), facing right."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<path d="M-30 -18 Q-80 -16 -106 -40 Q-80 -4 -30 -4 Z" fill="#2a9d8f"/>'
            + limb(((-22, -8), (-32, 2), (-42, 2)), "#2a9d8f", 7) + limb(((22, -8), (30, 2), (40, 2)), "#2a9d8f", 7)
            + '<ellipse cx="0" cy="-14" rx="38" ry="13" fill="#2a9d8f"/>'
            '<ellipse cx="42" cy="-20" rx="18" ry="11" fill="#2a9d8f"/>'
            + "".join(f'<polygon points="{px - 5},-25 {px},-34 {px + 5},-25" fill="#f4a261"/>' for px in (-24, -10, 4, 18))
            + '<circle cx="-14" cy="-12" r="4" fill="#ffd166"/><circle cx="4" cy="-14" r="4" fill="#ffd166"/>'
            '<circle cx="20" cy="-12" r="3.5" fill="#ffd166"/>'
            f'<circle cx="48" cy="-24" r="3.5" fill="{INK}"/></g>')


def exclusive_to():
    b = ['<rect y="170" width="400" height="230" fill="#4895ef"/>',
         '<path d="M0 170 H400" stroke="#a8dadc" stroke-width="3"/>',
         '<path d="M40 220 Q70 214 100 220 M300 210 Q330 204 360 210 M60 360 Q100 352 140 360 M260 370 Q300 362 340 370" '
         'fill="none" stroke="#a8dadc" stroke-width="3" stroke-linecap="round"/>',
         '<ellipse cx="200" cy="300" rx="130" ry="36" fill="#a8dadc"/>',
         '<ellipse cx="200" cy="292" rx="116" ry="30" fill="#e9c46a"/>',
         '<path d="M262 286 Q256 200 300 150" fill="none" stroke="#9c6644" stroke-width="10" stroke-linecap="round"/>',
         '<path d="M300 150 Q340 140 360 166 M300 150 Q320 116 352 120 M300 150 Q270 120 244 130 M300 150 Q262 150 250 178" '
         'fill="none" stroke="#386641" stroke-width="12" stroke-linecap="round"/>',
         '<ellipse cx="160" cy="288" rx="40" ry="10" fill="#adb5bd"/>',
         lizard(176, 284, 1.25),
         '<circle cx="80" cy="70" r="28" fill="#ffd166"/>']
    return svg(b, "#e3f2fd")


def yield_():
    rnd = random.Random(18)
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>',
         '<rect x="186" y="170" width="28" height="150" fill="#7f5539"/>',
         '<path d="M200 230 L160 190 M200 210 L240 176" stroke="#7f5539" stroke-width="12" stroke-linecap="round"/>',
         '<circle cx="200" cy="130" r="104" fill="#40916c"/>',
         '<circle cx="120" cy="170" r="60" fill="#40916c"/><circle cx="280" cy="170" r="60" fill="#40916c"/>',
         '<circle cx="170" cy="96" r="44" fill="#52b788" opacity=".6"/>']
    pts = []
    while len(pts) < 30:
        x, y = rnd.uniform(78, 322), rnd.uniform(44, 216)
        inside = math.hypot(x - 200, y - 130) < 96 or math.hypot(x - 120, y - 170) < 52 or math.hypot(x - 280, y - 170) < 52
        if inside and all(math.hypot(x - a, y - c) > 26 for a, c in pts):
            pts.append((x, y))
    b += [apple(x, y, 12) for x, y in pts]
    b += ['<path d="M290 330 L330 160 M318 330 L358 170" stroke="#bc6c25" stroke-width="6"/>']
    for k in range(6):
        y = 310 - k * 28
        b.append(f'<path d="M{f(292.4 + (330 - y) * 40 / 170)} {y} H{f(320.4 + (330 - y) * 40 / 170)}" stroke="#bc6c25" '
                 'stroke-width="4"/>')
    b += [crate(26, 330, ["#e63946"]), crate(104, 330, ["#e63946", "#bc4749"]), crate(64, 296, ["#e63946"]),
          crate(212, 330, ["#bc4749", "#e63946"])]
    return svg(b, "#e3f2fd")


def eccentric():
    goggles = ('<rect x="-26" y="-204" width="52" height="7" fill="#495057"/>'
               '<circle cx="-11" cy="-201" r="9" fill="#90e0ef" stroke="#495057" stroke-width="3"/>'
               '<circle cx="11" cy="-201" r="9" fill="#90e0ef" stroke="#495057" stroke-width="3"/>'
               '<path d="M-6 -150 L0 -144 L6 -150 L6 -138 L0 -144 L-6 -138 Z" fill="#e63946"/>')
    socks = ('<rect x="-25" y="-30" width="18" height="26" fill="#e63946"/>'
             '<path d="M-25 -22 H-7 M-25 -13 H-7" stroke="#fff" stroke-width="4"/>'
             '<rect x="7" y="-30" width="18" height="26" fill="#52b788"/>'
             '<circle cx="12" cy="-22" r="2.5" fill="#ffd166"/><circle cx="20" cy="-15" r="2.5" fill="#ffd166"/>'
             '<circle cx="12" cy="-9" r="2.5" fill="#ffd166"/>')
    b = ['<rect y="340" width="400" height="60" fill="#d4a373"/>',
         shadow(200, 344, 44),
         curls(200, 342, 1.3, "#dee2e6", long=False),
         '<g transform="translate(200 342) scale(1.3)">'
         '<path d="M-26 -196 L-44 -210 L-30 -188 Z M26 -196 L44 -212 L30 -188 Z M-10 -206 L-14 -226 L0 -208 Z '
         'M10 -206 L16 -228 L4 -208 Z" fill="#dee2e6"/></g>',
         person(200, 342, 1.3, SKIN[0], "#f8f9fa", "#6c757d", "#dee2e6", "none", mood="grin",
                larm=((-12, 40), (-16, 72)), rarm=((26, -10), (44, -40)), extra=goggles + socks),
         bird(160, 166, "#e63946", "#4895ef", flip=True, k=1.5),
         bird(214, 66, "#52b788", "#ffd166", k=1.4),
         sparkle(320, 110, 10, "#ffd166"), sparkle(80, 240, 8, "#ffd166")]
    return svg(b, "#e8f1f2")


def celebrated():
    b = ['<rect y="320" width="400" height="80" fill="#d6ccc2"/>',
         painting(130, 50, 140, 110, "#caf0f8", "#ffd166", "#52b788", "#2d6a4f", "#c9a227"),
         '<rect x="40" y="70" width="56" height="70" fill="#adb5bd"/><rect x="46" y="76" width="44" height="58" fill="#e5e5e5"/>',
         '<rect x="304" y="70" width="56" height="70" fill="#adb5bd"/><rect x="310" y="76" width="44" height="58" fill="#e5e5e5"/>',
         shadow(200, 344, 34),
         person(200, 342, 1.0, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-20, 30), (-34, 50)), rarm=((24, -20), (40, -50)),
                extra='<ellipse cx="2" cy="-200" rx="26" ry="8" fill="#bc4749"/><circle cx="2" cy="-210" r="4" fill="#bc4749"/>'
                      '<ellipse cx="-60" cy="-96" rx="22" ry="15" fill="#e9c46a"/><circle cx="-70" cy="-100" r="4" fill="#e63946"/>'
                      '<circle cx="-58" cy="-106" r="4" fill="#4895ef"/><circle cx="-48" cy="-98" r="4" fill="#52b788"/>')]
    for x, sk, shirt, hair, style in ((40, SKIN[0], "#e76f51", "#5c4033", "side"), (100, SKIN[3], "#ffd166", "#1b1b1b", "bun"),
                                      (300, SKIN[1], "#457b9d", "#adb5bd", "short"), (360, SKIN[2], "#bc4749", "#1b1b1b", "side")):
        b += [shadow(x, 362, 26),
              person(x, 360, .8, sk, shirt, "#264653", hair, style, mood="grin",
                     larm=((14, 26), (26, 12)), rarm=((-14, 26), (-26, 12)))]
    b += [heart(70, 166, 12), heart(330, 164, 12, "#e76f51"), heart(372, 140, 9),
          sparkle(110, 150, 8, "#ffd166"), sparkle(296, 140, 9, "#ffd166"), sparkle(28, 150, 7, "#ffd166")]
    return svg(b, "#f1faee")


def note(x, y, c=INK, k=1.0):
    """A musical note symbol (a filled head with a flagged stem)."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            f'<ellipse cx="0" cy="0" rx="7" ry="5" fill="{c}" transform="rotate(-20)"/>'
            f'<path d="M6 -2 V-28 Q14 -22 16 -14" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/></g>')


def compose():
    b = ['<rect y="330" width="400" height="70" fill="#b08968"/>',
         # the upright piano with its music sheet
         '<rect x="176" y="120" width="214" height="214" fill="#5c4033"/>',
         '<rect x="170" y="112" width="226" height="12" fill="#7f5539"/>',
         '<rect x="166" y="226" width="234" height="22" fill="#7f5539"/>',
         '<rect x="170" y="228" width="226" height="14" fill="#fff"/>']
    for k in range(17):
        x = 176 + k * 13
        if k % 7 not in (2, 6):
            b.append(f'<rect x="{x + 8}" y="228" width="7" height="8" fill="{INK}"/>')
    b += ['<rect x="230" y="92" width="110" height="88" fill="#fff" stroke="#dee2e6" stroke-width="2"/>',
          '<rect x="226" y="176" width="118" height="8" fill="#7f5539"/>']
    for top in (106, 142):
        for k in range(5):
            b.append(f'<path d="M238 {top + k * 5} H332" stroke="#6c757d" stroke-width="1.2"/>')
    for x, y in ((250, 116), (264, 111), (278, 121), (296, 151), (310, 146)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="3" fill="{INK}"/><path d="M{x + 3.5} {y} V{y - 14}" stroke="{INK}" stroke-width="1.5"/>')
    b += ['<rect x="70" y="268" width="104" height="12" rx="3" fill="#7f5539"/>',
          '<path d="M80 280 V330 M164 280 V330" stroke="#7f5539" stroke-width="8"/>',
          person(118, 356, 1.0, SKIN[2], "#457b9d", "#264653", "#1b1b1b", "side", mood="smile",
                 lleg=((22, 4), (26, 46)), rleg=((34, 4), (38, 46)),
                 larm=((14, 40), (34, 56)), rarm=((50, -10), (96, -46))),
          '<line x1="240" y1="156" x2="226" y2="176" stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>',
          f'<circle cx="236" cy="164" r="8.5" fill="{SKIN[2]}"/>',
          note(256, 70, "#e76f51"), note(300, 52, "#2a9d8f", 1.2), note(350, 74, "#e76f51", .9)]
    return svg(b, "#fdf0d5")


def nugget(x, y, r, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot})">'
            f'<path d="M{-r} 0 Q{-r} {f(-r * .8)} {f(-r * .2)} {-r} Q{f(r * .8)} {f(-r * .9)} {r} {f(-r * .1)} '
            f'Q{f(r * .7)} {f(r * .8)} 0 {f(r * .7)} Q{-r} {f(r * .6)} {-r} 0 Z" fill="#ffd166"/>'
            f'<circle cx="{f(-r * .3)}" cy="{f(-r * .35)}" r="{f(r * .25)}" fill="#fff3b0"/></g>')


def lucrative():
    rnd = random.Random(22)
    b = ['<rect y="330" width="400" height="70" fill="#7f5539"/>',
         '<rect x="20" y="40" width="20" height="290" fill="#9c6644"/><rect x="360" y="40" width="20" height="290" fill="#9c6644"/>',
         '<rect x="10" y="30" width="380" height="22" fill="#9c6644"/>',
         '<path d="M0 352 H400 M0 368 H400" stroke="#adb5bd" stroke-width="5"/>']
    for x in range(10, 400, 36):
        b.append(f'<rect x="{x}" y="346" width="10" height="28" fill="#5c4033"/>')
    pile = []
    for _ in range(36):
        x = rnd.uniform(110, 290)
        top = 214 - 50 * math.sin(math.pi * (x - 100) / 200)
        pile.append(nugget(x, rnd.uniform(top, 226), rnd.uniform(12, 18), rnd.randint(0, 90)))
    b += pile
    b += ['<path d="M90 216 H310 L288 314 H112 Z" fill="#6c757d"/>',
          '<path d="M90 216 H310 L306 234 H94 Z" fill="#495057"/>',
          '<path d="M130 246 V300 M200 246 V300 M270 246 V300" stroke="#495057" stroke-width="5"/>',
          '<circle cx="140" cy="330" r="22" fill="#343a40"/><circle cx="140" cy="330" r="8" fill="#adb5bd"/>',
          '<circle cx="260" cy="330" r="22" fill="#343a40"/><circle cx="260" cy="330" r="8" fill="#adb5bd"/>',
          nugget(330, 324, 14, 20), nugget(70, 328, 12, 60), nugget(316, 260, 12, 10),
          sparkle(150, 140, 14, "#fff"), sparkle(250, 130, 12, "#fff"), sparkle(200, 108, 16, "#fff"),
          sparkle(320, 200, 9, "#fff3b0"), sparkle(76, 190, 10, "#fff3b0")]
    return svg(b, "#3d2c2e")


def sandbag(x, y):
    return (f'<ellipse cx="{x}" cy="{y}" rx="22" ry="10" fill="#d4a373"/>'
            f'<path d="M{x - 14} {y - 2} Q{x} {y + 4} {x + 14} {y - 2}" fill="none" stroke="#b08968" stroke-width="2"/>')


def prepared_for():
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         # the storm rolling in from the left
         '<ellipse cx="60" cy="50" rx="100" ry="44" fill="#495057"/><ellipse cx="140" cy="40" rx="70" ry="36" fill="#6c757d"/>',
         '<path d="M30 100 l-8 24 M60 96 l-8 24 M90 100 l-8 24 M120 90 l-8 24 M44 140 l-8 24 M100 136 l-8 24" '
         'stroke="#4895ef" stroke-width="4" stroke-linecap="round"/>',
         '<polygon points="160,74 144,110 156,110 142,146 176,100 162,100 174,74" fill="#ffd166"/>',
         arrow(196, 60, 250, 60, "#e63946", 6, 16),
         # the house with its windows boarded up
         '<rect x="230" y="160" width="150" height="160" fill="#e9c46a"/>',
         '<polygon points="216,164 305,96 394,164" fill="#bc4749"/>',
         '<rect x="250" y="190" width="44" height="44" fill="#264653"/><rect x="318" y="190" width="44" height="44" fill="#264653"/>',
         '<rect x="290" y="260" width="34" height="60" fill="#7f5539"/>']
    for wx in (250, 318):
        for k, dy in enumerate((194, 208, 222)):
            b.append(f'<rect x="{wx - 6}" y="{dy}" width="56" height="9" fill="#bc6c25" transform="rotate({(-1) ** k * 4} {wx + 22} {dy + 4})"/>')
    for row, y in enumerate((334, 318, 302)):
        for k in range(5 - row):
            b.append(sandbag(40 + row * 22 + k * 44, y))
    b += [shadow(256, 346, 28),
          person(256, 344, .9, SKIN[1], "#f4a261", "#264653", "#5c4033", "short", mood="smile",
                 larm=((-14, 40), (-24, 86)), rarm=((-24, 40), (-48, 86))),
          sandbag(222, 290), f'<circle cx="214" cy="292" r="8" fill="{SKIN[1]}"/><circle cx="232" cy="292" r="8" fill="{SKIN[1]}"/>']
    return svg(b, "#cfd8dc")


def faintly():
    rnd = random.Random(24)
    b = []
    for _ in range(46):
        x, y = rnd.uniform(0, 400), rnd.uniform(0, 270)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(1.4, 2.6))}" fill="#fff" opacity="{f(rnd.uniform(.25, .5))}"/>')
    for x, y in ((90, 80), (300, 60), (220, 150), (60, 200), (340, 190)):
        b.append(sparkle(x, y, 7, "#fff").replace('/>', ' opacity=".4"/>'))
    b += ['<circle cx="300" cy="104" r="26" fill="#f1faee" opacity=".35"/>']
    for y, x, w in ((60, 120, 260), (110, 280, 240), (170, 100, 300), (230, 300, 220)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="{w / 2}" ry="18" fill="#8d99ae" opacity=".35"/>')
    b += ['<path d="M0 300 Q100 260 200 290 T400 280 V400 H0 Z" fill="#0d1b2a"/>',
          '<rect x="60" y="270" width="54" height="40" fill="#0d1b2a"/><polygon points="52,272 87,246 122,272" fill="#0d1b2a"/>',
          '<rect x="78" y="282" width="14" height="12" fill="#ffd166" opacity=".6"/>',
          '<path d="M300 300 V250" stroke="#0d1b2a" stroke-width="8"/><circle cx="300" cy="244" r="22" fill="#0d1b2a"/>']
    return svg(b, "#1d2d44")


def honey_jar(x, y, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot})">'
            '<path d="M-24 -26 Q-30 0 -24 26 H24 Q30 0 24 -26 Z" fill="#f4a261"/>'
            '<rect x="-20" y="-36" width="40" height="12" rx="3" fill="#ffd166"/>'
            '<path d="M-24 -6 H24" stroke="#e76f51" stroke-width="4"/><circle cx="-10" cy="10" r="4" fill="#fff" opacity=".5"/></g>')


def substitute():
    b = ['<rect x="230" y="40" width="130" height="90" fill="#fff"/><rect x="238" y="48" width="114" height="74" fill="#caf0f8"/>',
         person(196, 384, 1.05, SKIN[0], "#fff", "#264653", "#5c4033", "short", mood="smile",
                larm=((-30, -6), (-48, -26)), rarm=((24, 30), (34, 50)),
                extra='<rect x="-20" y="-238" width="40" height="34" rx="12" fill="#fff" stroke="#dee2e6" stroke-width="2"/>'
                      '<rect x="-24" y="-210" width="48" height="12" fill="#fff" stroke="#dee2e6" stroke-width="2"/>'),
         '<rect y="270" width="400" height="130" fill="#d4a373"/><rect y="262" width="400" height="12" fill="#b08968"/>',
         honey_jar(130, 200, 60),
         '<path d="M160 214 Q178 222 184 250 Q188 268 194 286" fill="none" stroke="#f4a261" stroke-width="7" stroke-linecap="round"/>',
         f'<circle cx="126" cy="188" r="9" fill="{SKIN[0]}"/>', bee(80, 140, 20, .9),
         '<path d="M136 270 Q200 340 264 270 Z" fill="#457b9d"/><ellipse cx="200" cy="270" rx="64" ry="12" fill="#a8dadc"/>',
         '<ellipse cx="196" cy="270" rx="22" ry="5" fill="#f4a261"/>',
         # the sugar, left aside
         '<path d="M300 196 H354 L360 266 H294 Z" fill="#f8f9fa" stroke="#dee2e6" stroke-width="2"/>',
         '<path d="M300 196 L310 184 H344 L354 196" fill="#e9ecef"/>',
         '<rect x="304" y="222" width="46" height="14" fill="#4895ef"/>',
         '<rect x="316" y="244" width="12" height="12" fill="#fff" stroke="#adb5bd" stroke-width="2"/>'
         '<rect x="330" y="246" width="12" height="12" fill="#fff" stroke="#adb5bd" stroke-width="2"/>',
         carrow(318, 176, 260, 100, 162, 140, "#e63946", 5, 14)]
    return svg(b, "#fdf0d5")


def foretells():
    b = ['<path d="M40 30 l4 10 l10 4 l-10 4 l-4 10 l-4 -10 l-10 -4 l10 -4 Z" fill="#ffd166" opacity=".6"/>',
         sparkle(350, 60, 10, "#ffd166"), sparkle(60, 120, 7, "#ffd166"),
         '<path d="M320 120 A30 30 0 1 0 350 150 A24 24 0 1 1 320 120 Z" fill="#ffd166" opacity=".7"/>',
         person(200, 340, 1.15, SKIN[2], "#7b2cbf", "#3c096c", "#1b1b1b", "none", mood="down",
                larm=((-30, 40), (-32, 78)), rarm=((30, 40), (32, 78)),
                extra='<path d="M-28 -170 Q-30 -214 0 -214 Q30 -214 28 -170 Q20 -196 0 -196 Q-20 -196 -28 -170 Z" fill="#e63946"/>'
                      '<path d="M-28 -172 Q-40 -140 -30 -120 L-20 -150 Z M28 -172 Q40 -140 30 -120 L20 -150 Z" fill="#e63946"/>'
                      '<circle cx="-24" cy="-160" r="4" fill="#ffd166"/><circle cx="24" cy="-160" r="4" fill="#ffd166"/>'),
         '<rect y="320" width="400" height="80" fill="#5a189a"/>',
         '<path d="M0 320 H400 V336 Q350 350 300 336 Q250 350 200 336 Q150 350 100 336 Q50 350 0 336 Z" fill="#7b2cbf"/>',
         '<path d="M170 322 L176 300 H224 L230 322 Z" fill="#c9a227"/>',
         '<g transform="translate(200 246) scale(.86) translate(-200 -236)">',
         '<circle cx="200" cy="236" r="84" fill="#c77dff" opacity=".25"/>',
         '<clipPath id="ball"><circle cx="200" cy="236" r="66"/></clipPath>',
         '<circle cx="200" cy="236" r="66" fill="#cdb4db"/>',
         '<g clip-path="url(#ball)">',
         '<rect x="130" y="170" width="140" height="70" fill="#9d4edd" opacity=".5"/>',
         '<rect x="150" y="226" width="90" height="50" fill="#6c757d"/>',
         '<path d="M150 226 v-10 h10 v10 h10 v-10 h10 v10 h10 v-10 h10 v10 h10 v-10 h10 v10 h10 v-10 h10 v10" fill="#6c757d"/>',
         '<rect x="152" y="190" width="24" height="40" fill="#6c757d"/><path d="M152 190 v-8 h8 v8 h8 v-8 h8 v8" fill="#6c757d"/>',
         '<g transform="rotate(18 230 230)"><rect x="216" y="184" width="24" height="46" fill="#6c757d"/>'
         '<path d="M216 184 v-8 h8 v8 h8 v-8 h8 v8" fill="#6c757d"/></g>',
         '<path d="M196 230 L204 246 L196 258 L206 276" fill="none" stroke="#343a40" stroke-width="3"/>',
         '<rect x="252" y="214" width="10" height="8" fill="#6c757d" transform="rotate(20 257 218)"/>'
         '<rect x="262" y="240" width="9" height="7" fill="#6c757d" transform="rotate(-15 266 244)"/>'
         '<rect x="246" y="262" width="10" height="8" fill="#6c757d"/>',
         '<rect x="130" y="276" width="140" height="40" fill="#495057"/>',
         '</g>',
         '<circle cx="176" cy="206" r="12" fill="#fff" opacity=".45"/>', '</g>',
         f'<circle cx="138" cy="262" r="10" fill="{SKIN[2]}"/><circle cx="262" cy="262" r="10" fill="{SKIN[2]}"/>',
         '<rect x="40" y="276" width="18" height="44" fill="#fff3b0"/><path d="M49 262 Q56 270 49 276 Q42 270 49 262 Z" fill="#f4a261"/>',
         '<rect x="342" y="276" width="18" height="44" fill="#fff3b0"/><path d="M351 262 Q358 270 351 276 Q344 270 351 262 Z" fill="#f4a261"/>']
    return svg(b, "#240046")


def potted_plant(x, y, top, pot="#bc6c25"):
    out = [f'<path d="M{x} {y - 50} V{top}" stroke="#40916c" stroke-width="6"/>']
    for ly in range(int(y - 70), int(top), -36):
        out.append(f'<ellipse cx="{x - 16}" cy="{ly}" rx="16" ry="7" fill="#52b788" transform="rotate(-25 {x - 16} {ly})"/>'
                   f'<ellipse cx="{x + 16}" cy="{ly - 14}" rx="16" ry="7" fill="#52b788" transform="rotate(25 {x + 16} {ly - 14})"/>')
    out.append(f'<ellipse cx="{x}" cy="{top}" rx="10" ry="14" fill="#52b788"/>')
    out.append(f'<path d="M{x - 34} {y - 54} H{x + 34} L{x + 26} {y} H{x - 26} Z" fill="{pot}"/>'
               f'<rect x="{x - 38}" y="{y - 60}" width="76" height="12" rx="3" fill="{pot}"/>')
    return "".join(out)


def compared():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         potted_plant(100, 334, 74), potted_plant(300, 334, 220, "#e76f51"),
         '<rect x="184" y="56" width="32" height="278" rx="3" fill="#ffd166"/>']
    for k, y in enumerate(range(68, 330, 13)):
        w = 14 if k % 5 == 0 else 8
        b.append(f'<path d="M184 {y} h{w}" stroke="#bc6c25" stroke-width="2.5"/>')
    b += ['<path d="M112 66 H184 M216 212 H290" stroke="#e63946" stroke-width="3" stroke-dasharray="7 6"/>',
          '<circle cx="184" cy="66" r="5" fill="#e63946"/><circle cx="216" cy="212" r="5" fill="#e63946"/>',
          arrow(236, 200, 236, 84, "#e63946", 4, 12), arrow(236, 84, 236, 200, "#e63946", 4, 12)]
    return svg(b, "#e8f1f2")


def pranks():
    b = ['<rect y="320" width="400" height="80" fill="#b08968"/>',
         '<rect x="40" y="40" width="220" height="110" fill="#2d6a4f" stroke="#9c6644" stroke-width="8"/>',
         # the chair
         '<rect x="150" y="160" width="12" height="110" fill="#7f5539"/>',
         '<rect x="150" y="256" width="100" height="12" fill="#9c6644"/>',
         '<path d="M156 268 V330 M244 268 V330" stroke="#7f5539" stroke-width="8"/>',
         # the whoopee cushion going down on the seat
         '<ellipse cx="208" cy="248" rx="34" ry="10" fill="#ff8fab"/>',
         '<path d="M240 246 Q252 242 256 250 L252 254 Q246 250 240 252 Z" fill="#ff8fab"/>',
         shadow(310, 334, 30),
         person(310, 332, .8, SKIN[1], "#ffd166", "#264653", "#5c4033", "side", mood="sly",
                larm=((-34, 10), (-65, 44)), rarm=((-40, 30), (-89, 51)))]
    for x, sk, shirt, hair, style in ((60, SKIN[3], "#4895ef", "#1b1b1b", "bun"), (106, SKIN[0], "#e76f51", "#e9c46a", "short")):
        b += [person(x, 340, .7, sk, shirt, "#264653", hair, style, mood="closed",
                     larm=((-12, 40), (-16, 72)), rarm=((4, -4), (-22, -18)),
                     extra=f'<circle cx="0" cy="-163" r="9" fill="{sk}"/>')]
    b += [sparkle(40, 190, 7, "#ffd166"), sparkle(140, 186, 6, "#ffd166")]
    return svg(b, "#fefae0")


def venerate():
    b = ['<rect y="300" width="400" height="100" fill="#9c6644"/>',
         # the shrine
         '<rect x="90" y="60" width="220" height="200" fill="#7f5539"/>',
         '<rect x="100" y="70" width="200" height="170" fill="#bc6c25"/>',
         '<rect x="80" y="236" width="240" height="16" fill="#5c4033"/>']
    for x in (130, 210):
        b.append(f'<rect x="{x}" y="88" width="60" height="74" fill="#e9c46a"/><rect x="{x + 6}" y="94" width="48" height="62" fill="#dee2e6"/>'
                 f'<circle cx="{x + 30}" cy="118" r="11" fill="#8d99ae"/><path d="M{x + 12} 156 Q{x + 30} 128 {x + 48} 156 Z" fill="#8d99ae"/>')
    for x in (114, 286):
        b.append(f'<rect x="{x - 7}" y="196" width="14" height="40" fill="#fff3b0"/>'
                 f'<path d="M{x} 178 Q{x + 8} 188 {x} 196 Q{x - 8} 188 {x} 178 Z" fill="#f4a261"/>'
                 f'<circle cx="{x}" cy="188" r="16" fill="#ffd166" opacity=".3"/>')
    b += ['<path d="M150 236 L144 200 H164 L158 236 Z" fill="#457b9d"/>',
          '<circle cx="146" cy="190" r="8" fill="#e63946"/><circle cx="158" cy="186" r="8" fill="#ffd166"/><circle cx="152" cy="178" r="7" fill="#e63946"/>',
          '<path d="M250 236 L244 200 H264 L258 236 Z" fill="#457b9d"/>',
          '<circle cx="246" cy="190" r="8" fill="#ffd166"/><circle cx="258" cy="186" r="8" fill="#e63946"/><circle cx="252" cy="178" r="7" fill="#ffd166"/>',
          '<rect x="190" y="220" width="20" height="16" fill="#5c4033"/>',
          '<path d="M200 220 V196" stroke="#6c757d" stroke-width="2"/>',
          '<path d="M200 194 Q192 184 200 174 Q208 164 200 154" fill="none" stroke="#adb5bd" stroke-width="2.5" opacity=".8"/>',
          back_view(110, 392, 1.1, "#457b9d", "#5c4033", SKIN[1]),
          back_view(200, 392, .8, "#e76f51", "#1b1b1b", SKIN[1], bun=True),
          back_view(290, 392, 1.1, "#2a9d8f", "#adb5bd", SKIN[1])]
    return svg(b, "#f2e8cf")


def cheap():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         shadow(120, 344, 30),
         person(120, 342, 1.05, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "short", mood="frown",
                brows="M-14 -188 L-3 -192 M3 -192 L14 -188",
                larm=((30, 40), (75, 45)), rarm=((40, 10), (85, 32))),
         # the broken toy robot, its price tag showing a single small coin
         '<rect x="176" y="200" width="56" height="60" rx="6" fill="#4cc9f0"/>',
         '<circle cx="192" cy="222" r="5" fill="#ffd166"/><circle cx="214" cy="222" r="5" fill="#e63946"/>',
         '<path d="M222 200 L212 218 L222 230 L214 248" fill="none" stroke="#264653" stroke-width="3"/>',
         '<path d="M192 200 V190 L198 194 L204 186 L210 194 L216 190 V200 Z" fill="#adb5bd"/>',
         '<path d="M232 236 L252 250" stroke="#264653" stroke-width="2"/>',
         '<rect x="248" y="244" width="30" height="20" rx="3" fill="#fff" stroke="#adb5bd" stroke-width="2" transform="rotate(14 263 254)"/>',
         '<circle cx="263" cy="254" r="6" fill="#e9c46a" stroke="#c9a227" stroke-width="2"/>',
         f'<circle cx="176" cy="236" r="9" fill="{SKIN[2]}"/><circle cx="232" cy="222" r="9" fill="{SKIN[2]}"/>',
         # the bits that fell off
         '<rect x="290" y="306" width="40" height="34" rx="5" fill="#4cc9f0" transform="rotate(-20 310 323)"/>',
         '<circle cx="302" cy="320" r="4" fill="#264653"/><circle cx="316" cy="316" r="4" fill="#264653"/>',
         '<path d="M312 304 L316 290" stroke="#264653" stroke-width="3"/><circle cx="317" cy="286" r="5" fill="#e63946"/>',
         '<rect x="344" y="328" width="34" height="12" rx="5" fill="#4cc9f0" transform="rotate(12 361 334)"/>',
         '<path d="M250 336 l10 -6 l4 8 Z M272 340 l6 -8 l6 6 Z" fill="#4cc9f0"/>']
    return svg(b, "#e8f1f2")


def crossed_arms(shirt, edge, skin):
    """Folded arms for person(): draw as extra with the person's arms hanging straight down."""
    return (limb(((-22, -146), (-30, -112), (16, -114)), edge, 19) + limb(((-22, -146), (-30, -112), (16, -114)), shirt, 15)
            + limb(((22, -146), (30, -122), (-16, -124)), edge, 19) + limb(((22, -146), (30, -122), (-16, -124)), shirt, 15)
            + f'<circle cx="18" cy="-114" r="8.5" fill="{skin}"/><circle cx="-18" cy="-124" r="8.5" fill="{skin}"/>')


def skeptical():
    b = ['<rect y="330" width="400" height="70" fill="#ced4da"/>',
         shadow(110, 334, 34), shadow(300, 334, 34),
         person(110, 332, 1.05, SKIN[0], "#e76f51", "#264653", "#e9c46a", "side", mood="grin",
                larm=((-30, -20), (-50, -54)), rarm=((30, -20), (50, -54))),
         '<path d="M154 92 V82 Q154 76 160 76 H168 Q174 76 174 82 V92 Q182 98 182 110 V150 H146 V110 Q146 98 154 92 Z" fill="#a8dadc"/>',
         '<rect x="150" y="116" width="28" height="18" fill="#e63946"/><rect x="156" y="68" width="16" height="10" rx="2" fill="#2a9d8f"/>',
         f'<circle cx="164" cy="150" r="9" fill="{SKIN[0]}"/>',
         sparkle(132, 78, 10, "#ffd166"), sparkle(196, 64, 12, "#ffd166"), sparkle(40, 90, 9, "#ffd166"),
         '<path d="M24 140 l-14 -6 M24 160 l-16 0 M196 150 l14 -6 M196 170 l16 0" stroke="#adb5bd" stroke-width="4" '
         'stroke-linecap="round"/>',
         person(300, 332, 1.05, SKIN[3], "#457b9d", "#264653", "#1b1b1b", "short", mood="left",
                brows="M-14 -189 L-3 -189 M3 -194 Q9 -202 15 -195",
                larm=((0, 0), (0, 0)), rarm=((0, 0), (0, 0)),
                extra=crossed_arms("#457b9d", "#2f5f80", SKIN[3]))]
    return svg(b, "#f8f9fa")


def pith_helmet():
    return ('<ellipse cx="0" cy="-196" rx="34" ry="7" fill="#e9d8a6"/>'
            '<path d="M-22 -196 Q-22 -224 0 -224 Q22 -224 22 -196 Z" fill="#e9d8a6"/>'
            '<rect x="-22" y="-204" width="44" height="5" fill="#bc6c25"/>')


def impenetrable():
    rnd = random.Random(32)
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         '<path d="M30 400 Q80 360 150 340 L170 330 L190 340 Q120 360 100 400 Z" fill="#d4a373"/>']
    for x in (170, 230, 290, 350, 395):
        b.append(f'<rect x="{x - 10}" y="0" width="20" height="340" fill="#5c4033"/>')
    for _ in range(170):
        x, y = rnd.uniform(160, 420), rnd.uniform(-20, 350)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rnd.uniform(14, 30))}" '
                 f'fill="{rnd.choice(["#1b4332", "#2d6a4f", "#40916c", "#2d6a4f", "#52b788"])}"/>')
    for x in range(176, 400, 26):
        top = rnd.uniform(0, 40)
        d = f'M{x} {f(top)} Q{x + 12} {f(top + 80)} {x - 4} {f(top + 160)} T{x + 4} {f(top + 300)}'
        b.append(f'<path d="{d}" fill="none" stroke="#386641" stroke-width="5"/>')
        for k in range(4):
            ly = top + 50 + k * 64
            b.append(f'<ellipse cx="{x + 8}" cy="{f(ly)}" rx="10" ry="5" fill="#80b918" transform="rotate(30 {x + 8} {f(ly)})"/>')
    for x, shirt, sk, tool in ((46, "#bc6c25", SKIN[1], False), (126, "#6a994e", SKIN[3], True)):
        extra = pith_helmet()
        if tool:
            extra += ('<rect x="56" y="-178" width="8" height="58" rx="3" fill="#adb5bd" transform="rotate(30 60 -120)"/>'
                      '<rect x="56" y="-124" width="8" height="18" fill="#5c4033" transform="rotate(30 60 -120)"/>')
        b += [shadow(x, 344, 26),
              person(x, 342, .85, sk, shirt, "#7f5539", "#5c4033", "short", mood="side",
                     brows="M-14 -190 L-3 -192 M3 -192 L14 -190",
                     larm=((-12, 40), (-16, 72)), rarm=((22, 10), (38, 26)) if tool else ((12, 40), (16, 72)),
                     extra=extra)]
    return svg(b, "#cfe8d5")


def magnitude():
    rnd = random.Random(33)
    pts = []
    for k in range(0, 156, 6):
        x = 24 + k
        pts.append((x, 200 + rnd.uniform(-4, 4)))
    amp = [30, 70, 90, 80, 96, 60, 84, 40]
    x = 180
    for k, a in enumerate(amp):
        pts.append((x, 200 - a if k % 2 == 0 else 200 + a))
        x += 18
    pts.append((330, 200))
    trace = " ".join(f"{f(px)},{f(py)}" for px, py in pts)
    b = ['<rect x="16" y="90" width="324" height="220" fill="#fff"/>']
    for y in range(110, 310, 25):
        b.append(f'<path d="M16 {y} H340" stroke="#e9ecef" stroke-width="2"/>')
    b += [f'<polyline points="{trace}" fill="none" stroke="#e63946" stroke-width="4" stroke-linejoin="round"/>',
          '<ellipse cx="350" cy="200" rx="22" ry="110" fill="#6c757d"/><ellipse cx="344" cy="200" rx="8" ry="100" fill="#adb5bd"/>',
          '<rect x="280" y="20" width="110" height="50" rx="6" fill="#495057"/>',
          '<path d="M330 70 L330 196" stroke="#343a40" stroke-width="6"/>',
          '<polygon points="324,190 336,190 330,204" fill="#264653"/>',
          '<rect y="330" width="400" height="70" fill="#9c6644"/>',
          '<path d="M160 330 L176 350 L166 366 L186 400 H200 L182 366 L194 350 L178 330 Z" fill="#3d2c2e"/>',
          '<g transform="rotate(-8 80 330)"><rect x="50" y="290" width="60" height="40" fill="#e9c46a"/>'
          '<polygon points="42,292 80,262 118,292" fill="#bc4749"/></g>',
          '<path d="M34 276 l-12 -4 M34 290 l-14 0 M128 268 l12 -4 M128 282 l14 0" stroke="#495057" stroke-width="3" '
          'stroke-linecap="round"/>']
    return svg(b, "#e9ecef")


def experiment():
    b = [person(336, 384, 1.1, SKIN[1], "#f8f9fa", "#264653", "#5c4033", "bun", mood="smile",
                larm=((-24, 20), (-40, 40)), rarm=((-20, 30), (-58, 46)),
                extra='<rect x="-60" y="-128" width="38" height="48" rx="3" fill="#bc6c25"/>'
                      '<rect x="-56" y="-122" width="30" height="38" fill="#fff"/>'
                      '<path d="M-52 -112 h20 M-52 -102 h16 M-52 -92 h20" stroke="#adb5bd" stroke-width="2"/>'
                      '<path d="M-28 -106 L-42 -94" stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>'),
         '<rect y="300" width="400" height="100" fill="#adb5bd"/><rect y="296" width="400" height="10" fill="#6c757d"/>',
         # the lamp over the first plant
         '<path d="M30 300 V90 L90 80" fill="none" stroke="#495057" stroke-width="6" stroke-linejoin="round"/>',
         '<polygon points="70,74 112,84 106,104 64,94" fill="#ffd166"/>',
         '<polygon points="70,98 104,104 150,296 30,296" fill="#fff3b0" opacity=".45"/>',
         potted_plant(90, 296, 120),
         # the dark box over the second
         '<rect x="166" y="150" width="120" height="146" fill="#343a40"/>',
         '<path d="M226 250 V230 Q226 200 210 210 M226 236 Q240 216 252 232" fill="none" stroke="#a3b18a" stroke-width="5" '
         'stroke-linecap="round"/>',
         '<ellipse cx="210" cy="214" rx="10" ry="5" fill="#ccd5ae"/><ellipse cx="252" cy="234" rx="10" ry="5" fill="#ccd5ae"/>',
         '<path d="M192 242 H260 L254 296 H198 Z" fill="#bc6c25"/>']
    return svg(b, "#e8f1f2")


def mitigate():
    b = ['<path d="M0 176 Q40 166 80 176 T160 172 Q176 172 178 200 L190 400 H0 Z" fill="#4895ef"/>',
         '<path d="M0 220 Q30 210 60 220 T120 220 M0 270 Q30 260 60 270 T120 270 M0 320 Q30 310 60 320 T120 320" '
         'fill="none" stroke="#a8dadc" stroke-width="4"/>',
         arrow(30, 150, 120, 150, "#e63946", 6, 16),
         '<path d="M150 400 L160 270 Q170 250 200 248 H400 V400 Z" fill="#9c6644"/>',
         '<path d="M160 270 Q170 250 200 248 H400 V262 H200 Q176 262 170 280 Z" fill="#6a994e"/>']
    for x in (186, 228, 270):
        b.append(f'<path d="M{x} 264 q-10 14 -22 24 M{x} 264 q10 16 18 26 M{x} 264 v34" fill="none" stroke="#5c4033" stroke-width="2.5"/>'
                 f'<rect x="{x - 6}" y="160" width="12" height="100" fill="#7f5539"/>'
                 + bush(x, 150, 30))
    b += ['<path d="M164 168 l-6 -10 M172 172 l2 -12 M178 178 l8 -8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
          '<rect x="316" y="196" width="60" height="54" fill="#e9c46a"/><polygon points="306,198 346,166 386,198" fill="#bc4749"/>',
          '<rect x="340" y="220" width="16" height="30" fill="#7f5539"/>',
          '<circle cx="350" cy="60" r="26" fill="#ffd166"/>']
    return svg(b, "#cfe8f3")


def deciding():
    b = ['<rect y="170" width="400" height="230" fill="#a7c957"/>',
         '<path d="M170 400 L188 300 Q190 270 160 250 L60 200 H90 L196 256 Q210 266 224 256 L330 200 H360 L248 262 Q222 280 226 300 L250 400 Z" '
         'fill="#e9d8a6"/>',
         # two different colleges
         '<rect x="20" y="96" width="110" height="80" fill="#e5e5e5"/>',
         '<path d="M40 96 Q75 40 110 96 Z" fill="#457b9d"/>',
         '<path d="M36 112 V170 M58 112 V170 M80 112 V170 M102 112 V170 M120 112 V170" stroke="#adb5bd" stroke-width="7"/>',
         '<rect x="12" y="172" width="126" height="8" fill="#adb5bd"/>',
         '<rect x="272" y="104" width="112" height="76" fill="#bc4749"/>',
         '<rect x="312" y="56" width="32" height="50" fill="#9d0208"/><polygon points="306,58 328,22 350,58" fill="#264653"/>',
         '<circle cx="328" cy="76" r="9" fill="#fff"/>']
    for x in (284, 306, 350, 368):
        b.append(f'<rect x="{x - 6}" y="122" width="12" height="18" fill="#fff3b0"/><rect x="{x - 6}" y="152" width="12" height="18" fill="#fff3b0"/>')
    b += [shadow(206, 364, 30),
          person(206, 362, 1.05, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "bun", mood="left",
                 brows="M-14 -190 L-3 -188 M3 -192 L14 -194",
                 larm=((-12, 40), (-16, 72)), rarm=((6, 20), (-10, -4)),
                 extra='<rect x="-30" y="-150" width="12" height="54" rx="5" fill="#e76f51"/>'),
          f'<circle cx="226" cy="204" r="9" fill="{SKIN[2]}"/>',
          '<circle cx="250" cy="148" r="4" fill="#adb5bd"/><circle cx="262" cy="134" r="6" fill="#adb5bd"/>']
    return svg(b, "#e3f2fd")


def nervous_about():
    b = ['<rect y="320" width="400" height="80" fill="#3d2c2e"/>',
         '<rect x="230" y="0" width="170" height="320" fill="#fff3b0" opacity=".25"/>',
         '<path d="M220 0 H260 Q240 160 270 320 H220 Z" fill="#9d0208"/>',
         '<path d="M234 40 Q244 160 236 300" fill="none" stroke="#6a040f" stroke-width="5"/>',
         '<path d="M330 320 V200" stroke="#adb5bd" stroke-width="4"/><ellipse cx="330" cy="194" rx="7" ry="10" fill="#343a40"/>',
         shadow(120, 334, 30),
         person(120, 332, 1.1, SKIN[1], "#4895ef", "#264653", "#5c4033", "side", mood="wide",
                brows="M-14 -188 L-3 -192 M3 -192 L14 -188",
                lleg=((2, 44), (-6, 86)), rleg=((-2, 44), (6, 86)),
                larm=((-24, 34), (-36, 60)), rarm=((10, -4), (-18, -18)),
                extra=f'<circle cx="2" cy="-164" r="8.5" fill="{SKIN[1]}" stroke="#c68642" stroke-width="2"/>'
                      '<path d="M-18 -200 q-4 8 0 10 q4 -2 0 -10 Z M20 -194 q-4 8 0 10 q4 -2 0 -10 Z" fill="#90e0ef"/>'
                      '<rect x="-74" y="-112" width="34" height="44" fill="#fff" stroke="#dee2e6" stroke-width="2" transform="rotate(-10 -57 -90)"/>'),
         '<path d="M84 280 l-10 -4 M84 292 l-12 0 M156 280 l10 -4 M156 292 l12 0" stroke="#adb5bd" stroke-width="3" '
         'stroke-linecap="round"/>',
         '<path d="M50 200 l-8 -4 M48 216 l-10 2" stroke="#adb5bd" stroke-width="3" stroke-linecap="round"/>']
    return svg(b, "#5c4d3c")


def familiarize():
    b = ['<rect y="320" width="400" height="80" fill="#adb5bd"/>',
         '<rect x="250" y="236" width="140" height="12" fill="#9c6644"/><path d="M262 248 V320 M378 248 V320" stroke="#7f5539" stroke-width="7"/>',
         '<rect x="290" y="176" width="70" height="50" rx="4" fill="#343a40"/><rect x="296" y="182" width="58" height="38" fill="#4895ef"/>',
         '<rect x="318" y="226" width="14" height="10" fill="#343a40"/>',
         '<rect x="350" y="80" width="40" height="66" rx="4" fill="#6c757d"/><rect x="358" y="90" width="24" height="18" fill="#343a40"/>'
         '<rect x="362" y="120" width="16" height="16" fill="#fff"/>',
         '<rect x="270" y="60" width="50" height="40" fill="#fff"/><rect x="276" y="66" width="38" height="28" fill="#caf0f8"/>',
         shadow(196, 334, 30),
         person(196, 332, 1.0, SKIN[3], "#e76f51", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-12, 40), (-16, 72)), rarm=((30, -16), (64, -36))),
         shadow(86, 344, 30),
         person(86, 342, .95, SKIN[0], "#457b9d", "#264653", "#e9c46a", "bun", mood="smile",
                larm=((-12, 30), (-20, 50)), rarm=((12, 30), (20, 50)),
                extra='<path d="M-10 -156 L-4 -126 M10 -156 L4 -126" stroke="#e63946" stroke-width="2"/>'
                      '<rect x="-8" y="-128" width="16" height="20" rx="2" fill="#fff" stroke="#adb5bd" stroke-width="2"/>'
                      '<rect x="-38" y="-100" width="76" height="44" fill="#d4a373"/>'
                      '<path d="M-38 -86 H38" stroke="#b08968" stroke-width="3"/>'
                      '<path d="M-20 -100 V-120 M-20 -112 l-10 -8 M-20 -116 l8 -10" stroke="#40916c" stroke-width="4" stroke-linecap="round"/>'
                      '<rect x="0" y="-116" width="20" height="16" fill="#e9c46a"/>'
                      f'<circle cx="-40" cy="-92" r="8.5" fill="{SKIN[0]}"/><circle cx="40" cy="-92" r="8.5" fill="{SKIN[0]}"/>')]
    return svg(b, "#f1faee")


def admonish():
    b = ['<rect y="320" width="400" height="80" fill="#b08968"/>',
         '<rect x="10" y="20" width="380" height="200" fill="#7f5539"/>']
    rnd = random.Random(39)
    colors = ["#e63946", "#2a9d8f", "#e9c46a", "#457b9d", "#f4a261", "#6a994e"]
    for top in (30, 96, 162):
        x = 18
        while x < 380:
            w = rnd.randint(12, 20)
            h = rnd.randint(44, 56)
            b.append(f'<rect x="{x}" y="{top + 56 - h}" width="{w}" height="{h}" fill="{rnd.choice(colors)}"/>')
            x += w + 2
        b.append(f'<rect x="10" y="{top + 56}" width="380" height="10" fill="#5c4033"/>')
    for x, sk, shirt, hair, style in ((60, SKIN[2], "#ffd166", "#1b1b1b", "short"), (148, SKIN[0], "#e76f51", "#5c4033", "bun")):
        b += [person(x, 380, .9, sk, shirt, "#264653", hair, style, mood="wide",
                     larm=((-20, 10), (-40, -10)), rarm=((20, 10), (40, -10)))]
    b += ['<rect x="10" y="290" width="200" height="14" fill="#9c6644"/><path d="M24 304 V330 M196 304 V330" stroke="#7f5539" stroke-width="8"/>',
          '<path d="M30 180 l-12 -8 M30 196 l-14 0 M178 180 l12 -8 M178 196 l14 0" stroke="#e63946" '
          'stroke-width="4" stroke-linecap="round"/>',
          shadow(304, 334, 32),
          person(304, 332, 1.1, SKIN[1], "#6d597a", "#264653", "#adb5bd", "bun", mood="left",
                 brows="M-14 -192 L-3 -187 M3 -187 L14 -192",
                 larm=((-12, 40), (-16, 72)), rarm=((0, 10), (-14, 4)),
                 extra=f'<rect x="-3" y="-178" width="7" height="22" rx="3" fill="{SKIN[1]}" stroke="#c68642" stroke-width="1.5"/>'
                       f'<circle cx="2" cy="-154" r="8.5" fill="{SKIN[1]}"/>'
                       '<circle cx="-8" cy="-180" r="8" fill="none" stroke="#264653" stroke-width="2.5"/>'
                       '<circle cx="12" cy="-180" r="8" fill="none" stroke="#264653" stroke-width="2.5"/>')]
    return svg(b, "#f2e8cf")


def useful():
    tools = (
        (-14, '<path d="M30 -10 H190 Q170 14 30 10 Z" fill="#ced4da"/><path d="M30 -10 H190" stroke="#adb5bd" stroke-width="3"/>'),
        (-44, '<path d="M30 -6 L140 -14 L140 -2 Z M30 6 L140 14 L140 2 Z" fill="#ced4da"/>'
              '<circle cx="34" cy="0" r="6" fill="#adb5bd"/>'),
        (-76, '<rect x="30" y="-5" width="120" height="10" fill="#ced4da"/><rect x="146" y="-8" width="12" height="16" fill="#adb5bd"/>'),
        (-108, '<path d="M30 -9 H110 Q124 -9 124 0 Q124 9 110 9 H30 Z" fill="#ced4da"/>'
               '<circle cx="106" cy="0" r="5" fill="#fde2e4"/>'))
    b = ['<circle cx="200" cy="210" r="170" fill="#fde2e4"/>']
    for ang, shape in tools:
        b.append(f'<g transform="translate(118 280) rotate({ang})" stroke="#8d99ae" stroke-width="1.5">{shape}</g>')
    b += ['<rect x="96" y="260" width="240" height="44" rx="22" fill="#e63946"/>',
          '<rect x="104" y="268" width="224" height="10" rx="5" fill="#ff6b6b" opacity=".6"/>',
          '<circle cx="118" cy="282" r="9" fill="#adb5bd"/><circle cx="316" cy="282" r="9" fill="#adb5bd"/>',
          sparkle(330, 120, 14, "#ffd166"), sparkle(70, 120, 10, "#ffd166"), sparkle(360, 220, 8, "#ffd166")]
    return svg(b, "#fff8f0")


def traditional():
    b = ['<rect y="320" width="400" height="80" fill="#d4a373"/>',
         '<rect x="10" y="190" width="90" height="130" fill="#f8edeb"/><polygon points="0,194 55,140 110,194" fill="#9c6644"/>',
         '<path d="M10 220 H100 M55 194 V320 M20 194 L90 320" stroke="#7f5539" stroke-width="5"/>',
         '<rect x="300" y="200" width="90" height="120" fill="#f8edeb"/><polygon points="290,204 345,150 400,204" fill="#9c6644"/>',
         '<path d="M300 230 H390 M345 204 V320 M310 204 L380 320" stroke="#7f5539" stroke-width="5"/>',
         '<path d="M0 40 Q100 80 200 50 T400 50" fill="none" stroke="#6c757d" stroke-width="2"/>']
    for k in range(13):
        x = 10 + k * 30
        y = 40 + 40 * math.sin(math.pi * x / 200) * .5 if x < 200 else 50 + 22 * math.sin(math.pi * (x - 200) / 200)
        c = ("#e63946", "#ffd166", "#2a9d8f", "#4895ef")[k % 4]
        b.append(f'<polygon points="{f(x - 9)},{f(y)} {f(x + 9)},{f(y)} {f(x)},{f(y + 20)}" fill="{c}"/>')
    wreath = "".join(f'<circle cx="{f(24 * math.cos(math.radians(a)))}" cy="{f(-182 + 24 * math.sin(math.radians(a)))}" r="6" '
                     f'fill="{c}"/>' for a, c in ((-160, "#e63946"), (-130, "#ffd166"), (-100, "#4895ef"), (-70, "#e63946"),
                                                  (-40, "#ffd166"), (-10, "#4895ef")))
    skirt = ('<path d="M-26 -110 L-50 -34 Q0 -24 50 -34 L26 -110 Z" fill="#e63946"/>'
             '<path d="M-48 -44 Q0 -34 48 -44" fill="none" stroke="#ffd166" stroke-width="5"/>'
             '<path d="M-46 -52 Q0 -42 46 -52" fill="none" stroke="#2a9d8f" stroke-width="4"/>'
             '<path d="M-20 -150 L-10 -110 H10 L20 -150" fill="none" stroke="#264653" stroke-width="6"/>'
             '<circle cx="0" cy="-138" r="3" fill="#ffd166"/><circle cx="0" cy="-124" r="3" fill="#ffd166"/>')
    vest = ('<path d="M-28 -152 H-8 V-90 H-28 Z M8 -152 H28 V-90 H8 Z" fill="#bc4749"/>'
            '<circle cx="-18" cy="-130" r="3" fill="#ffd166"/><circle cx="-18" cy="-112" r="3" fill="#ffd166"/>'
            '<circle cx="18" cy="-130" r="3" fill="#ffd166"/><circle cx="18" cy="-112" r="3" fill="#ffd166"/>'
            '<rect x="-29" y="-96" width="58" height="10" fill="#2a9d8f"/>'
            '<ellipse cx="0" cy="-200" rx="30" ry="6" fill="#264653"/><rect x="-18" y="-220" width="36" height="20" rx="6" fill="#264653"/>'
            '<rect x="-18" y="-206" width="36" height="5" fill="#e63946"/>')
    b += [shadow(144, 344, 34), shadow(256, 344, 34),
          person(144, 342, 1.05, SKIN[0], "#fff", "#e63946", "#bc6c25", "bun", mood="grin", long_hair=True,
                 larm=((-30, 10), (-50, 30)), rarm=((20, -30), (31, -62)), lleg=((-6, 44), (-10, 86)),
                 rleg=((10, 40), (24, 80)), extra=skirt + wreath),
          person(256, 342, 1.05, SKIN[1], "#fff", "#264653", "#5c4033", "short", mood="grin",
                 larm=((-20, -30), (-31, -62)), rarm=((30, 10), (50, 30)), lleg=((-12, 40), (-26, 80)),
                 rleg=((6, 44), (10, 86)), extra=vest),
          sparkle(200, 100, 10, "#ffd166"), sparkle(110, 120, 7, "#ffd166"), sparkle(300, 116, 8, "#ffd166")]
    return svg(b, "#e3f2fd")


def useless():
    b = ['<rect y="320" width="400" height="80" fill="#22223b"/>',
         '<rect x="290" y="60" width="80" height="100" fill="#2b2d42"/><path d="M330 60 V160 M290 110 H370" stroke="#1b1b2f" stroke-width="5"/>',
         shadow(110, 334, 30),
         person(110, 332, 1.05, SKIN[1], "#457b9d", "#264653", "#5c4033", "side", mood="frown",
                brows="M-14 -188 L-3 -192 M3 -192 L14 -188",
                larm=((-12, 40), (-16, 72)), rarm=((30, 10), (68, 10))),
         # where the light should be
         '<polygon points="270,174 400,110 400,290 270,206" fill="none" stroke="#6c757d" stroke-width="3" stroke-dasharray="10 8"/>',
         # the torch, opened up and empty
         '<rect x="170" y="176" width="80" height="26" rx="4" fill="#6c757d"/>',
         '<rect x="190" y="182" width="44" height="14" rx="3" fill="#1b1b2f"/>',
         '<polygon points="250,172 272,164 272,214 250,206" fill="#6c757d"/>',
         '<rect x="270" y="164" width="6" height="50" fill="#495057"/>',
         '<ellipse cx="170" cy="189" rx="5" ry="13" fill="#1b1b2f"/>',
         f'<circle cx="214" cy="198" r="9" fill="{SKIN[1]}"/>',
         '<rect x="160" y="320" width="30" height="20" rx="4" fill="#6c757d" transform="rotate(20 175 330)"/>',
         '<path d="M84 140 l-10 -6 M84 156 l-12 0" stroke="#6c757d" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#1b1b2f")


def mock():
    patch = ('<rect x="-20" y="-130" width="14" height="14" fill="#e9c46a" transform="rotate(10 -13 -123)"/>'
             '<rect x="6" y="-60" width="12" height="12" fill="#bc6c25"/>')
    b = ['<rect y="330" width="400" height="70" fill="#a7c957"/>',
         shadow(320, 344, 28),
         person(320, 342, .95, SKIN[2], "#adb5bd", "#6c757d", "#1b1b1b", "short", mood="cry",
                larm=((-12, 40), (-16, 72)), rarm=((12, 40), (16, 72)), extra=patch)]
    for x, sk, shirt, hair, style, point in ((50, SKIN[0], "#e63946", "#e9c46a", "bun", False),
                                             (120, SKIN[3], "#ffd166", "#1b1b1b", "short", False),
                                             (200, SKIN[1], "#2a9d8f", "#5c4033", "side", True)):
        b += [shadow(x, 344, 24),
              person(x, 342, .8, sk, shirt, "#264653", hair, style, mood="grin",
                     larm=((-6, 40), (6, 64)) if point else ((6, 36), (20, 58)),
                     rarm=((30, -16), (62, -26)) if point else ((-6, 36), (-20, 58)))]
    return svg(b, "#e3f2fd")


def rousing():
    b = ['<rect y="320" width="400" height="80" fill="#6c757d"/>']
    for x in range(0, 400, 50):
        b.append(f'<rect x="{x + 2}" y="40" width="46" height="280" fill="#4895ef"/>'
                 f'<path d="M{x + 12} 60 h26 M{x + 12} 68 h26 M{x + 12} 76 h26" stroke="#3a7bd5" stroke-width="3"/>'
                 f'<rect x="{x + 38}" y="170" width="5" height="22" rx="2" fill="#adb5bd"/>')
    b += ['<rect y="290" width="400" height="16" fill="#9c6644"/>',
          shadow(100, 344, 34),
          person(100, 342, 1.15, SKIN[1], "#e63946", "#264653", "#5c4033", "cap", mood="wide",
                 brows="M-14 -192 L-3 -188 M3 -188 L14 -192",
                 larm=((-20, -30), (-24, -70)), rarm=((12, 40), (16, 72)),
                 extra='<path d="M0 -156 L-10 -130" stroke="#ffd166" stroke-width="2"/><rect x="-16" y="-132" width="12" height="8" rx="3" fill="#adb5bd"/>'),
          '<path d="M136 140 l14 -6 M138 152 l18 0 M136 164 l14 6" stroke="#e76f51" stroke-width="4" stroke-linecap="round"/>']
    for x, sk in ((220, SKIN[3]), (290, SKIN[0]), (360, SKIN[2])):
        b += [shadow(x, 360, 26),
              person(x, 358, .9, sk, "#2a9d8f", "#fff", "#1b1b1b", "short", mood="grin",
                     larm=((-24, -30), (-34, -70)), rarm=((24, -30), (34, -70)),
                     extra='<circle cx="0" cy="-120" r="10" fill="#fff"/>')]
    b += [sparkle(250, 60, 12, "#ffd166"), sparkle(330, 50, 10, "#ffd166"), sparkle(190, 80, 8, "#ffd166")]
    return svg(b, "#e9ecef")


def owl(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<polygon points="-34,-96 -24,-128 -12,-100" fill="#7f5539"/><polygon points="34,-96 24,-128 12,-100" fill="#7f5539"/>'
            '<ellipse cx="0" cy="-50" rx="42" ry="56" fill="#9c6644"/>'
            '<ellipse cx="0" cy="-30" rx="26" ry="32" fill="#e6ccb2"/>'
            '<circle cx="-17" cy="-80" r="17" fill="#ede0d4"/><circle cx="17" cy="-80" r="17" fill="#ede0d4"/>'
            '<circle cx="-17" cy="-80" r="12" fill="#ffd166"/><circle cx="17" cy="-80" r="12" fill="#ffd166"/>'
            f'<circle cx="-12" cy="-76" r="6" fill="{INK}"/><circle cx="22" cy="-76" r="6" fill="{INK}"/>'
            '<polygon points="-6,-66 6,-66 0,-54" fill="#f4a261"/>'
            '<path d="M-14 4 v8 M-6 4 v8 M6 4 v8 M14 4 v8" stroke="#f4a261" stroke-width="4" stroke-linecap="round"/></g>')


def hearing():
    rnd = random.Random(45)
    b = ['<circle cx="340" cy="60" r="28" fill="#f1faee"/>',
         '<rect y="330" width="400" height="70" fill="#1b4332"/>',
         '<path d="M0 150 Q100 140 200 156" fill="none" stroke="#5c4033" stroke-width="14" stroke-linecap="round"/>',
         owl(110, 144, 1.0)]
    for _ in range(26):
        x = rnd.uniform(200, 400)
        b.append(f'<path d="M{f(x)} 340 q{f(rnd.uniform(-8, 8))} -30 {f(rnd.uniform(-6, 6))} -{f(rnd.uniform(30, 56))}" '
                 'fill="none" stroke="#2d6a4f" stroke-width="5" stroke-linecap="round"/>')
    b += ['<ellipse cx="300" cy="320" rx="22" ry="14" fill="#adb5bd"/>',
          '<circle cx="280" cy="312" r="10" fill="#adb5bd"/><circle cx="276" cy="300" r="6" fill="#ced4da"/>',
          f'<circle cx="272" cy="312" r="2.5" fill="{INK}"/><circle cx="270" cy="316" r="2" fill="#e5989b"/>',
          '<path d="M322 322 Q350 330 344 310" fill="none" stroke="#adb5bd" stroke-width="3"/>']
    for r in (40, 64, 88):
        b.append(f'<path d="M{f(280 - r * math.cos(math.radians(40)))} {f(304 - r * math.sin(math.radians(40)))} '
                 f'A{r} {r} 0 0 1 {f(280 - r * math.cos(math.radians(80)))} {f(304 - r * math.sin(math.radians(80)))}" '
                 'fill="none" stroke="#ffd166" stroke-width="4" stroke-linecap="round" opacity=".85"/>')
    return svg(b, "#1d2d44")


def avoid():
    b = ['<rect width="400" height="400" fill="#a7c957"/>',
         '<polygon points="150,0 250,0 330,400 70,400" fill="#d4a373"/>',
         '<ellipse cx="200" cy="250" rx="96" ry="44" fill="#7f5539"/>',
         '<ellipse cx="196" cy="248" rx="70" ry="28" fill="#5c4033"/>',
         '<circle cx="110" cy="236" r="6" fill="#7f5539"/><circle cx="290" cy="268" r="5" fill="#7f5539"/>',
         '<path d="M170 240 q10 -4 20 0 M210 254 q10 -4 20 0" fill="none" stroke="#9c6644" stroke-width="3"/>',
         carrow(150, 384, 440, 270, 250, 112, "#fff", 4, 14),
         bush(30, 80, 30), bush(370, 60, 26), bush(20, 340, 24)]
    for k, (x, y) in enumerate(((150, 380), (180, 352), (240, 330), (300, 300))):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="11" fill="#9c6644" transform="rotate({40 + k * 10} {x} {y})"/>')
    b += [shadow(330, 236, 26),
          person(330, 234, .78, SKIN[2], "#e76f51", "#264653", "#1b1b1b", "cap", mood="side",
                 larm=((-12, 40), (-16, 72)), rarm=((16, 36), (30, 62)),
                 lleg=((-14, 40), (-26, 80)), rleg=((10, 44), (18, 86)),
                 extra='<rect x="-34" y="-150" width="16" height="56" rx="6" fill="#2a9d8f"/>'),
          '<path d="M354 186 L370 240" stroke="#495057" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#a7c957")


def innovative():
    scene = ('<rect x="0" y="0" width="160" height="200" fill="#caf0f8"/><circle cx="110" cy="50" r="18" fill="#ffd166"/>'
             '<path d="M0 140 Q50 100 90 130 T160 120 V200 H0 Z" fill="#52b788"/>')
    b = ['<circle cx="200" cy="210" r="170" fill="#ede7f6"/>',
         # folded shut ...
         '<rect x="42" y="160" width="62" height="100" rx="10" fill="#264653"/>',
         '<rect x="50" y="168" width="46" height="84" rx="4" fill="#caf0f8"/><circle cx="73" cy="176" r="3" fill="#264653"/>',
         '<rect x="104" y="170" width="8" height="80" rx="3" fill="#495057"/>',
         arrow(126, 210, 166, 210, "#7209b7", 5, 14),
         # ... and opened out like a book
         '<g transform="translate(272 214) scale(.78) translate(-200 -203)">',
         '<clipPath id="lft"><polygon points="128,124 196,104 196,300 128,280"/></clipPath>',
         '<clipPath id="rgt"><polygon points="204,104 272,124 272,280 204,300"/></clipPath>',
         '<polygon points="118,114 200,90 200,316 118,292" fill="#264653"/>',
         '<polygon points="200,90 282,114 282,292 200,316" fill="#264653"/>',
         f'<g clip-path="url(#lft)"><g transform="translate(120 100)">{scene}</g></g>',
         f'<g clip-path="url(#rgt)"><g transform="translate(120 100)">{scene}</g></g>',
         '<path d="M200 90 V316" stroke="#495057" stroke-width="6"/>',
         '<circle cx="162" cy="116" r="4" fill="#264653"/><circle cx="238" cy="116" r="4" fill="#264653"/>',
         '<rect x="282" y="150" width="6" height="34" rx="2" fill="#495057"/>',
         carrow(136, 76, 200, 30, 264, 76, "#7209b7", 5, 14), '</g>',
         sparkle(356, 90, 14, "#ffd166"), sparkle(70, 110, 10, "#ffd166"), sparkle(360, 320, 9, "#ffd166")]
    return svg(b, "#f8f9fa")


def occupying():
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         '<rect x="190" y="250" width="20" height="90" fill="#7f5539"/>',
         '<path d="M110 250 V170 Q110 110 200 110 Q290 110 290 170 V250 Z" fill="#6c757d"/>',
         '<path d="M124 250 V174 Q124 126 200 126 Q276 126 276 174 V250 Z" fill="#343a40"/>',
         '<path d="M110 250 H290 L300 290 H100 Z" fill="#adb5bd"/>',
         '<rect x="296" y="140" width="8" height="70" fill="#e63946"/><rect x="304" y="140" width="30" height="20" fill="#e63946"/>',
         # the nest and its hungry chicks
         '<ellipse cx="200" cy="236" rx="70" ry="18" fill="#9c6644"/>']
    for x in (154, 200, 246):
        b.append(f'<circle cx="{x}" cy="212" r="16" fill="#ffd166"/>'
                 f'<polygon points="{x - 9},202 {x + 9},202 {x},188" fill="#f4a261"/><polygon points="{x - 7},204 {x + 7},204 {x},214" fill="#f4a261"/>'
                 f'<circle cx="{x - 7}" cy="206" r="2.2" fill="{INK}"/><circle cx="{x + 7}" cy="206" r="2.2" fill="{INK}"/>')
    b += ['<path d="M136 230 l20 10 M170 244 l26 -6 M214 240 l24 6 M246 230 l18 8 M150 246 l30 2" stroke="#7f5539" '
          'stroke-width="3" stroke-linecap="round"/>',
          bird(200, 110, "#457b9d", "#264653", k=1.7),
          '<path d="M240 66 q6 6 0 12 q-6 6 0 12" fill="none" stroke="#e76f51" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#e3f2fd")


def neutral():
    b = ['<rect y="330" width="400" height="70" fill="#ced4da"/>']
    for x, sk, shirt, side in ((40, SKIN[1], "#e63946", 1), (100, SKIN[3], "#e63946", 1),
                               (300, SKIN[0], "#4895ef", -1), (360, SKIN[2], "#4895ef", -1)):
        inner = x in (100, 300)
        arm = ((26 * side, -10), (48 * side, -20)) if inner else ((-14 * side, -30), (-20 * side, -64))
        down = ((12 * side, 40), (16 * side, 72))
        b += [shadow(x, 344, 22),
              person(x, 342, .8, sk, shirt, "#264653", "#1b1b1b", "short", mood="wide",
                     brows="M-14 -192 L-3 -186 M3 -186 L14 -192",
                     larm=down if (side > 0) == inner else arm, rarm=arm if (side > 0) == inner else down)]
    b += [shadow(200, 344, 28),
          person(200, 342, 1.0, SKIN[1], "#adb5bd", "#495057", "#5c4033", "side", mood="content",
                 larm=((-12, 40), (-16, 72)), rarm=((12, 40), (16, 72))),
          # a level balance over the middle
          '<path d="M200 60 V120" stroke="#6c757d" stroke-width="5"/><path d="M150 70 H250" stroke="#6c757d" stroke-width="5" '
          'stroke-linecap="round"/>',
          '<path d="M150 70 L136 100 M150 70 L164 100 M250 70 L236 100 M250 70 L264 100" stroke="#6c757d" stroke-width="2"/>',
          '<path d="M132 100 H168 Q150 116 132 100 Z M232 100 H268 Q250 116 232 100 Z" fill="#e9c46a"/>',
          '<rect x="186" y="118" width="28" height="6" rx="3" fill="#6c757d"/>']
    return svg(b, "#f8f9fa")


def accidental():
    b = ['<rect y="280" width="400" height="120" fill="#adb5bd"/><rect y="276" width="400" height="10" fill="#6c757d"/>',
         person(110, 390, 1.15, SKIN[0], "#f8f9fa", "#264653", "#5c4033", "short", mood="wide",
                larm=((-30, -20), (-44, -60)), rarm=((30, -20), (44, -60)),
                extra='<rect x="-26" y="-210" width="52" height="14" rx="7" fill="#90e0ef" stroke="#495057" stroke-width="3"/>'),
         '<rect y="280" width="400" height="120" fill="#adb5bd"/><rect y="276" width="400" height="10" fill="#6c757d"/>',
         # the flask fizzing over in new colours
         '<path d="M250 140 V190 L210 270 Q206 280 218 280 H322 Q334 280 330 270 L290 190 V140 Z" fill="#e9ecef" opacity=".9"/>',
         '<path d="M232 226 H308 L330 270 Q334 280 322 280 H218 Q206 280 210 270 Z" fill="#c77dff"/>',
         '<path d="M240 206 H300 L308 226 H232 Z" fill="#ff8fab"/>',
         '<rect x="244" y="132" width="52" height="10" rx="3" fill="#dee2e6"/>']
    for x, y, r, c in ((270, 120, 18, "#ff8fab"), (252, 100, 14, "#ffd166"), (288, 96, 16, "#52b788"), (270, 76, 14, "#4cc9f0"),
                       (300, 120, 11, "#c77dff"), (240, 124, 10, "#4cc9f0"), (310, 70, 9, "#ff8fab"), (236, 72, 8, "#52b788")):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>')
    b += ['<path d="M246 138 h10 v26 a5 5 0 0 1 -10 0 Z M284 138 h10 v16 a5 5 0 0 1 -10 0 Z" fill="#ff8fab"/>',
          # the bottle knocked over beside it
          '<g transform="rotate(-80 352 268)"><rect x="340" y="230" width="24" height="40" rx="4" fill="#4cc9f0"/>'
          '<rect x="346" y="218" width="12" height="14" fill="#4cc9f0"/></g>',
          '<ellipse cx="338" cy="280" rx="22" ry="4" fill="#4cc9f0"/>',
          sparkle(340, 60, 12, "#ffd166"), sparkle(206, 90, 10, "#ffd166"), sparkle(352, 140, 8, "#ffd166")]
    return svg(b, "#e8f1f2")


PICTURES = {
    "accentuate": accentuate,
    "vacate": vacate,
    "running to": running_to,
    "teach": teach,
    "delayed by": delayed_by,
    "follows": follows,
    "synchronization": synchronization,
    "borrow": borrow,
    "diminish": diminish,
    "scratchy": scratchy,
    "retrieving": retrieving,
    "habitable": habitable,
    "dispute": dispute,
    "discover": discover,
    "complex": complex_,
    "pretending": pretending,
    "exclusive to": exclusive_to,
    "yield": yield_,
    "eccentric": eccentric,
    "celebrated": celebrated,
    "compose": compose,
    "lucrative": lucrative,
    "prepared for": prepared_for,
    "faintly": faintly,
    "substitute": substitute,
    "foretells": foretells,
    "compared": compared,
    "pranks": pranks,
    "venerate": venerate,
    "cheap": cheap,
    "skeptical": skeptical,
    "impenetrable": impenetrable,
    "magnitude": magnitude,
    "experiment": experiment,
    "mitigate": mitigate,
    "deciding": deciding,
    "nervous about": nervous_about,
    "familiarize": familiarize,
    "admonish": admonish,
    "useful": useful,
    "traditional": traditional,
    "useless": useless,
    "mock": mock,
    "rousing": rousing,
    "hearing": hearing,
    "avoid": avoid,
    "innovative": innovative,
    "occupying": occupying,
    "neutral": neutral,
    "accidental": accidental,
}
