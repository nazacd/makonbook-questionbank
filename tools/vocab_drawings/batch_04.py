"""Batch 4: drawings 131-180 (each function returns one SVG; PICTURES maps word -> function).

The figures and small shapes come from batch_02.py and batch_03.py.
"""

import math
import random

from batch_02 import SKIN, heart, limb, person, puzzle_piece, shadow, sheep, sparkle, star
from batch_03 import bicycle, cyclist, dog, side_runner, thumbs_up
from common import INK, arrow, arc_arrow, bush, carrow, f, pine, svg


def phone(x, y, k=1.0, glow=True):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            + ('<circle cx="0" cy="0" r="16" fill="#caf0f8" opacity=".6"/>' if glow else "")
            + f'<rect x="-7" y="-11" width="14" height="22" rx="3" fill="{INK}"/>'
            '<rect x="-5" y="-8" width="10" height="15" fill="#4895ef"/></g>')


def bottle(x, y, cap=True):
    return (f'<path d="M{x - 13} {y} V{y - 50} Q{x - 13} {y - 62} {x - 6} {y - 66} V{y - 78} H{x + 6} V{y - 66} '
            f'Q{x + 13} {y - 62} {x + 13} {y - 50} V{y} Z" fill="#a8dadc"/>'
            f'<rect x="{x - 9}" y="{y - 40}" width="18" height="16" fill="#2a9d8f"/>'
            + (f'<rect x="{x - 8}" y="{y - 86}" width="16" height="10" rx="2" fill="#e63946"/>' if cap else ""))


# ---------------------------------------------------------------------------------------------

def repetitive():
    b = ['<rect y="330" width="400" height="70" fill="#ced4da"/>',
         person(200, 300, 1.0, SKIN[1], "#457b9d", "#264653", "#5c4033", "cap", mood="down",
                larm=((-12, 40), (-14, 72)), rarm=((24, 30), (40, 58))),
         '<rect x="10" y="250" width="380" height="22" rx="11" fill="#495057"/>',
         '<circle cx="24" cy="261" r="8" fill="#6c757d"/><circle cx="376" cy="261" r="8" fill="#6c757d"/>',
         '<rect x="40" y="272" width="10" height="60" fill="#6c757d"/><rect x="350" y="272" width="10" height="60" '
         'fill="#6c757d"/>']
    for k, x in enumerate(range(40, 380, 46)):
        b.append(bottle(x, 250, cap=x > 230))
    b += [f'<circle cx="244" cy="160" r="8.5" fill="{SKIN[1]}"/>',
          '<rect x="236" y="150" width="16" height="10" rx="2" fill="#e63946"/>',
          arc_arrow(320, 90, 30, 200, 520, "#e76f51", 5, 13),
          '<path d="M110 290 l-16 -8 M300 290 l16 -8" stroke="#adb5bd" stroke-width="3" stroke-linecap="round"/>']
    return svg(b, "#e9ecef")


def ubiquitous():
    b = ['<rect x="0" y="40" width="90" height="230" fill="#adb5bd"/>', '<rect x="100" y="80" width="80" height="190" fill="#ced4da"/>',
         '<rect x="190" y="20" width="100" height="250" fill="#adb5bd"/>', '<rect x="300" y="70" width="100" height="200" '
         'fill="#ced4da"/>']
    for bx, by, w, h in ((0, 40, 90, 230), (100, 80, 80, 190), (190, 20, 100, 250), (300, 70, 100, 200)):
        for yy in range(by + 16, by + h - 30, 34):
            for xx in range(bx + 12, bx + w - 16, 26):
                b.append(f'<rect x="{xx}" y="{yy}" width="14" height="18" fill="#e9ecef"/>')
    b += ['<rect y="270" width="400" height="130" fill="#dee2e6"/>']
    people = ((40, 330, .62, SKIN[0], "#e76f51"), (110, 314, .55, SKIN[3], "#2a9d8f"), (180, 340, .66, SKIN[1], "#457b9d"),
              (250, 316, .55, SKIN[2], "#e9c46a"), (320, 336, .64, SKIN[0], "#f4a261"), (370, 304, .5, SKIN[3], "#a7c957"),
              (80, 388, .7, SKIN[2], "#264653"), (290, 392, .72, SKIN[1], "#e63946"))
    for x, y, s, sk, c in sorted(people, key=lambda p: p[1]):
        b += [shadow(x, y + 2, 24 * s / .6, 4),
              person(x, y, s, sk, c, "#495057", "#3e2723", "short", mood="down",
                     larm=((-6, 30), (14, 36)), rarm=((6, 30), (-14, 36))),
              phone(x, y - 108 * s, s * 1.4)]
    return svg(b, "#e3f2fd")


def complaining():
    b = ['<rect y="320" width="400" height="80" fill="#d4a373"/>',
         person(110, 330, 1.05, SKIN[0], "#e76f51", "#264653", "#7f5539", "short", mood="angry",
                larm=((-12, 30), (-14, 56)), rarm=((40, 8), (80, 18))),
         '<rect x="40" y="250" width="240" height="14" rx="4" fill="#7f5539"/>',
         '<rect x="56" y="264" width="10" height="60" fill="#6f4518"/><rect x="254" y="264" width="10" height="60" '
         'fill="#6f4518"/>',
         '<ellipse cx="200" cy="246" rx="48" ry="10" fill="#fff" stroke="#ced4da" stroke-width="3"/>',
         '<ellipse cx="200" cy="240" rx="30" ry="10" fill="#e9c46a"/><ellipse cx="190" cy="236" rx="12" ry="6" fill="#a7c957"/>',
         '<path d="M178 222 l-4 -14 M200 220 v-16 M222 222 l4 -14" stroke="#4895ef" stroke-width="3" stroke-linecap="round"/>',
         sparkle(180, 200, 6, "#a8dadc"), sparkle(224, 196, 6, "#a8dadc"),
         '<path d="M90 120 l-12 -10 M110 112 l-2 -16 M130 118 l10 -12" stroke="#e63946" stroke-width="4" '
         'stroke-linecap="round"/>',
         shadow(320, 334, 34),
         person(320, 332, 1.05, SKIN[3], "#fff", "#264653", "#1b1b1b", "short", mood="flat",
                brows="M-14 -192 Q-8 -196 -2 -192 M2 -192 Q8 -196 14 -192",
                larm=((-20, 24), (-26, 4)), rarm=((12, 40), (14, 72)),
                extra='<rect x="-50" y="-150" width="22" height="28" rx="2" fill="#fff" stroke="#adb5bd" stroke-width="2"/>')]
    return svg(b, "#fdf6ec")


def barking_dog(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<ellipse cx="0" cy="4" rx="56" ry="7" fill="#000" opacity=".12"/>'
            '<path d="M-50 -60 Q-70 -84 -62 -96" fill="none" stroke="#7f5539" stroke-width="10" stroke-linecap="round"/>'
            '<path d="M-40 -40 V0 M-24 -40 V0 M26 -40 V0 M42 -40 V0" stroke="#7f5539" stroke-width="13" stroke-linecap="round"/>'
            '<ellipse cx="0" cy="-58" rx="56" ry="30" fill="#9c6644"/>'
            '<circle cx="54" cy="-92" r="28" fill="#9c6644"/>'
            '<path d="M44 -114 L36 -136 L58 -118 Z" fill="#7f5539"/>'
            '<path d="M66 -104 L112 -104 L112 -88 L70 -84 Z" fill="#9c6644"/>'
            '<path d="M70 -78 L108 -62 L100 -48 L66 -64 Z" fill="#7f5539"/>'
            '<path d="M70 -84 L112 -88 L108 -62 L70 -78 Z" fill="#9d0208"/>'
            '<path d="M78 -86 l5 10 l5 -10 M94 -87 l5 10 l5 -10 M80 -74 l4 -9 l4 9 M94 -68 l4 -9 l4 9" fill="#fff"/>'
            f'<circle cx="112" cy="-100" r="7" fill="{INK}"/>'
            f'<circle cx="60" cy="-100" r="4" fill="{INK}"/>'
            f'<path d="M50 -110 L68 -104" stroke="{INK}" stroke-width="4" stroke-linecap="round"/></g>')


def aggressive():
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>',
         barking_dog(90, 340, 1.1)]
    for x in range(196, 270, 22):
        b.append(f'<rect x="{x}" y="196" width="10" height="150" rx="3" fill="#adb5bd"/>')
    b += ['<rect x="190" y="214" width="84" height="8" fill="#adb5bd"/><rect x="190" y="306" width="84" height="8" '
          'fill="#adb5bd"/>',
          '<path d="M222 172 l14 -12 M228 188 h18 M222 206 l14 10" stroke="#e63946" stroke-width="5" '
          'stroke-linecap="round" opacity=".0"/>',
          '<path d="M276 210 l14 -10 M280 228 h18" stroke="#e63946" stroke-width="5" stroke-linecap="round"/>',
          shadow(330, 364, 34),
          person(330, 362, 1.05, SKIN[2], "#457b9d", "#264653", "#1b1b1b", "cap", mood="wide",
                 larm=((-24, -16), (-40, -40)), rarm=((12, 40), (16, 72)), rot=8),
          '<path d="M290 230 L360 300" stroke="#7f5539" stroke-width="5"/>',
          '<rect x="330" y="276" width="50" height="40" rx="6" fill="#7f5539"/>',
          '<rect x="342" y="282" width="26" height="16" fill="#fff"/>']
    return svg(b, "#e3f2fd")


def chef_hat():
    return ('<path d="M-22 -192 H22 V-206 Q36 -214 30 -232 Q24 -246 10 -240 Q4 -256 -10 -246 Q-24 -250 -28 -234 '
            'Q-38 -218 -22 -206 Z" fill="#fff" stroke="#dee2e6" stroke-width="2"/>')


def managed():
    b = ['<rect y="320" width="400" height="80" fill="#ced4da"/>',
         '<rect x="0" y="180" width="400" height="10" fill="#adb5bd"/>',
         # stove on the left, chopping board on the right
         '<rect x="10" y="230" width="110" height="100" fill="#6c757d"/>', '<rect x="10" y="226" width="110" height="10" fill="#495057"/>',
         '<path d="M30 226 V196 H70 V226" fill="#adb5bd"/>', '<path d="M42 192 q-4 -10 0 -18 M58 192 q4 -10 0 -18" '
         'fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>',
         '<rect x="290" y="236" width="110" height="94" fill="#9c6b3c"/>', '<rect x="300" y="226" width="80" height="12" rx="3" '
         'fill="#e6ccb2"/>',
         '<circle cx="330" cy="222" r="7" fill="#e76f51"/><circle cx="350" cy="222" r="7" fill="#a7c957"/>',
         person(64, 344, .7, SKIN[0], "#fff", "#264653", "#7f5539", "short", mood="smile",
                larm=((-12, 40), (-14, 70)), rarm=((16, 20), (24, 0))),
         person(340, 344, .7, SKIN[3], "#fff", "#264653", "#1b1b1b", "short", mood="smile",
                larm=((-16, 20), (-24, 0)), rarm=((12, 40), (14, 70))),
         shadow(200, 354, 40),
         # the head chef in the middle, directing
         person(200, 352, 1.15, SKIN[1], "#fff", "#264653", "#5c4033", "short", mood="grin",
                larm=((-40, -10), (-84, -10)), rarm=((40, -10), (84, -10)), extra=chef_hat()),
         '<path d="M190 210 h20" stroke="#e63946" stroke-width="6"/>',
         '<path d="M60 152 l-12 -8 M56 170 h-14 M340 152 l12 -8 M344 170 h14" stroke="#6c757d" stroke-width="3" '
         'stroke-linecap="round"/>']
    return svg(b, "#f8f9fa")


def physical():
    b = ['<rect y="250" width="400" height="150" fill="#a7c957"/>', '<circle cx="340" cy="56" r="28" fill="#ffd166"/>',
         bush(40, 246, 30), bush(380, 244, 26),
         # jumping rope
         '<path d="M60 220 Q70 380 160 220" fill="none" stroke="#e63946" stroke-width="4"/>',
         shadow(110, 360, 24, 5),
         person(110, 330, .7, SKIN[2], "#f4a261", "#457b9d", "#1b1b1b", "bun", mood="grin",
                larm=((-22, 30), (-38, 48)), rarm=((22, 30), (38, 48)), lleg=((-6, 40), (-10, 70)),
                rleg=((6, 40), (10, 70))),
         # runner
         shadow(250, 302, 30, 5), side_runner(250, 296, .95, "#2a9d8f", SKIN[0], "#7f5539"),
         # soccer
         shadow(310, 384, 26, 5),
         person(310, 382, .75, SKIN[1], "#e76f51", "#264653", "#5c4033", "short", mood="grin",
                larm=((-30, 10), (-50, 4)), rarm=((24, 30), (34, 60)), lleg=((-4, 44), (-4, 86)),
                rleg=((30, 30), (60, 40))),
         '<circle cx="368" cy="350" r="12" fill="#fff" stroke="#264653" stroke-width="2"/>',
         '<polygon points="368,344 373,348 371,354 365,354 363,348" fill="#264653"/>',
         '<path d="M180 230 h-26 M184 250 h-34" stroke="#fff" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#cfe8f3")


def fox(x, y, k, coat, belly, flip=False, outline="none"):
    sgn = -1 if flip else 1
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sgn * k)} {k})" stroke="{outline}" stroke-width="1.5">'
            '<ellipse cx="0" cy="4" rx="54" ry="6" fill="#000" opacity=".1"/>'
            f'<path d="M-40 -30 Q-90 -30 -96 -64 Q-80 -50 -46 -46 Z" fill="{coat}"/>'
            f'<path d="M-96 -64 Q-92 -52 -84 -50 Q-94 -50 -96 -64 Z" fill="{belly}"/>'
            f'<path d="M-28 -26 V0 M-12 -26 V0 M18 -26 V0 M32 -26 V0" stroke="{coat}" stroke-width="10" stroke-linecap="round"/>'
            f'<ellipse cx="0" cy="-36" rx="46" ry="24" fill="{coat}"/>'
            f'<circle cx="44" cy="-58" r="20" fill="{coat}"/>'
            f'<path d="M32 -72 L34 -96 L48 -76 Z M48 -76 L60 -94 L60 -70 Z" fill="{coat}"/>'
            f'<path d="M58 -62 L84 -52 L60 -44 Z" fill="{coat}"/>'
            f'<ellipse cx="40" cy="-46" rx="14" ry="8" fill="{belly}"/>'
            f'<circle cx="84" cy="-52" r="4" fill="{INK}"/><circle cx="52" cy="-62" r="3.5" fill="{INK}"/></g>')


def adapt_to():
    rnd = random.Random(2)
    b = ['<rect width="200" height="400" fill="#cfe8f3"/>', '<rect x="200" width="200" height="400" fill="#dbe7f0"/>',
         '<rect y="250" width="200" height="150" fill="#a7c957"/>', '<rect x="200" y="250" width="200" height="150" fill="#fff"/>',
         '<path d="M200 250 Q260 236 330 246 T400 240 V250 Z" fill="#fff"/>',
         bush(40, 244, 26), pine(150, 254, 80),
         pine(300, 254, 110, "#ced4da"),
         fox(100, 320, .9, "#e76f51", "#fefae0"), fox(310, 320, .9, "#f8f9fa", "#e9ecef", outline="#ced4da"),
         '<circle cx="342" cy="273" r="0" fill="none"/>']
    for _ in range(40):
        x, y = rnd.uniform(205, 395), rnd.uniform(5, 240)
        b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{rnd.choice((2, 2.5, 3))}" fill="#fff"/>')
    b += ['<path d="M200 0 V400" stroke="#fff" stroke-width="4" stroke-dasharray="10 8"/>',
          arrow(160, 120, 240, 120, INK, 6, 16)]
    return svg(b, "#cfe8f3")


def agree_with():
    b = ['<rect y="330" width="400" height="70" fill="#e9d8c4"/>']
    for x, sk, c, hair, style in ((80, SKIN[0], "#e76f51", "#7f5539", "bun"), (200, SKIN[3], "#2a9d8f", "#1b1b1b", "short"),
                                  (320, SKIN[1], "#457b9d", "#5c4033", "side")):
        b.append(person(x, 340, 1.0, sk, c, "#264653", hair, style, mood="grin",
                        larm=((-12, 40), (-14, 70)), rarm=((26, 0), (30, -24))))
        b.append(thumbs_up(x + 50, 172, 1.0, sk))
    b += ['<rect x="20" y="250" width="360" height="16" rx="4" fill="#7f5539"/>',
          '<rect x="40" y="266" width="12" height="70" fill="#6f4518"/><rect x="348" y="266" width="12" height="70" fill="#6f4518"/>',
          '<circle cx="200" cy="40" r="26" fill="#52b788"/>',
          '<path d="M186 40 L196 50 L216 30" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" '
          'stroke-linejoin="round"/>']
    return svg(b, "#f1faee")


def mountain_view(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#bde0fe"/>'
            f'<polygon points="{x},{y + h} {x + w * .35},{y + h * .3} {x + w * .55},{y + h * .55} {x + w * .75},{y + h * .2} '
            f'{x + w},{y + h * .6} {x + w},{y + h}" fill="#6d597a"/>'
            f'<polygon points="{x + w * .75},{y + h * .2} {x + w * .83},{y + h * .33} {x + w * .75},{y + h * .3} '
            f'{x + w * .68},{y + h * .32}" fill="#fff"/>'
            f'<rect x="{x}" y="{y + h * .85}" width="{w}" height="{h * .15}" fill="#52b788"/>')


def adjusted():
    b = ['<rect x="20" y="40" width="160" height="130" rx="8" fill="#343a40"/>',
         f'<g filter="url(#blur)">{mountain_view(30, 50, 140, 110)}</g>',
         '<rect x="220" y="40" width="160" height="130" rx="8" fill="#343a40"/>', mountain_view(230, 50, 140, 110),
         arrow(184, 105, 216, 105, INK, 5, 12),
         # lens with the focus ring being turned
         '<rect x="120" y="230" width="160" height="110" rx="14" fill="#495057"/>',
         '<rect x="150" y="230" width="20" height="110" fill="#6c757d"/>']
    for y in range(236, 336, 10):
        b.append(f'<line x1="150" y1="{y}" x2="170" y2="{y}" stroke="#343a40" stroke-width="3"/>')
    b += ['<ellipse cx="280" cy="285" rx="20" ry="55" fill="#264653"/>',
          '<ellipse cx="280" cy="285" rx="12" ry="40" fill="#4895ef" opacity=".7"/>',
          '<rect x="40" y="250" width="80" height="70" rx="10" fill="#343a40"/>',
          f'<ellipse cx="160" cy="226" rx="16" ry="12" fill="{SKIN[1]}"/>',
          f'<ellipse cx="160" cy="344" rx="16" ry="12" fill="{SKIN[1]}"/>',
          carrow(190, 220, 210, 285, 190, 352, "#e76f51", 5, 14)]
    return svg(b, "#fdf6ec", '<filter id="blur" x="-10%" y="-10%" width="120%" height="120%">'
               '<feGaussianBlur stdDeviation="6"/></filter>')



def bus(x, y, k=1.0, color="#ffd166", flip=False):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(-k if flip else k)} {k})">'
            f'<rect x="-90" y="-96" width="180" height="84" rx="12" fill="{color}"/>'
            '<rect x="-90" y="-34" width="180" height="8" fill="#264653"/>'
            + "".join(f'<rect x="{xx}" y="-84" width="30" height="28" rx="3" fill="#caf0f8"/>' for xx in (-76, -38, 0))
            + '<rect x="44" y="-84" width="30" height="64" rx="3" fill="#caf0f8"/>'
            '<path d="M59 -84 V-20" stroke="#264653" stroke-width="2"/>'
            '<circle cx="-56" cy="-10" r="16" fill="#343a40"/><circle cx="-56" cy="-10" r="6" fill="#adb5bd"/>'
            '<circle cx="54" cy="-10" r="16" fill="#343a40"/><circle cx="54" cy="-10" r="6" fill="#adb5bd"/></g>')


def convenient():
    b = ['<rect y="330" width="400" height="70" fill="#adb5bd"/>', '<rect y="320" width="400" height="14" fill="#dee2e6"/>',
         # the school door
         '<rect x="0" y="80" width="170" height="242" fill="#e76f51"/>', '<polygon points="0,84 85,30 170,84" fill="#9d0208"/>',
         '<rect x="60" y="210" width="60" height="112" fill="#7f5539"/>', '<rect x="66" y="216" width="22" height="100" fill="#9c6b3c"/>',
         '<rect x="20" y="110" width="40" height="40" fill="#caf0f8"/><rect x="110" y="110" width="40" height="40" fill="#caf0f8"/>',
         '<circle cx="85" cy="60" r="12" fill="#fff"/><path d="M85 52 V60 H91" fill="none" stroke="#264653" stroke-width="2"/>',
         bus(310, 344, 1.0, flip=True),
         # the stop, right at the door
         '<rect x="180" y="200" width="6" height="122" fill="#6c757d"/>',
         '<rect x="164" y="186" width="38" height="28" rx="4" fill="#4895ef"/>',
         '<rect x="172" y="192" width="22" height="12" rx="3" fill="#fff"/>',
         person(130, 334, .62, SKIN[2], "#f4a261", "#457b9d", "#1b1b1b", "short", mood="grin",
                larm=((-12, 40), (-14, 70)), rarm=((12, 40), (16, 70))),
         person(252, 328, .62, SKIN[0], "#a7c957", "#264653", "#7f5539", "bun", mood="grin",
                larm=((-12, 40), (-14, 70)), rarm=((12, 40), (16, 70))),
         '<path d="M126 372 H240" stroke="#264653" stroke-width="3"/><path d="M126 364 V380 M240 364 V380" stroke="#264653" '
         'stroke-width="3"/>']
    return svg(b, "#cfe8f3")


def weather_icons(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<circle cx="-50" cy="-20" r="16" fill="#ffd166"/>'
            '<ellipse cx="10" cy="-26" rx="22" ry="12" fill="#fff"/><ellipse cx="0" cy="-32" rx="12" ry="10" fill="#fff"/>'
            '<ellipse cx="56" cy="10" rx="22" ry="12" fill="#adb5bd"/>'
            '<path d="M46 26 l-4 10 M58 26 l-4 10 M70 26 l-4 10" stroke="#4895ef" stroke-width="3" stroke-linecap="round"/>'
            '<circle cx="-20" cy="34" r="12" fill="#ffd166"/><ellipse cx="-8" cy="40" rx="18" ry="10" fill="#fff"/></g>')


def prediction():
    b = ['<rect y="340" width="400" height="60" fill="#ced4da"/>',
         '<rect x="20" y="40" width="260" height="210" rx="8" fill="#457b9d"/>',
         '<path d="M50 120 Q70 70 130 80 Q170 60 210 90 Q260 100 250 160 Q240 220 170 210 Q130 236 90 210 Q40 190 50 120 Z" '
         'fill="#a7c957"/>',
         weather_icons(150, 140, 1.3),
         '<rect x="140" y="250" width="20" height="90" fill="#6c757d"/>',
         shadow(330, 344, 34),
         person(330, 342, 1.05, SKIN[3], "#e9c46a", "#264653", "#1b1b1b", "bun", mood="grin",
                larm=((-30, -20), (-60, -40)), rarm=((12, 40), (14, 72))),
         '<line x1="268" y1="148" x2="232" y2="128" stroke="#7f5539" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#f1faee")


def urge():
    b = ['<rect y="230" width="400" height="170" fill="#e76f51"/>',
         '<path d="M0 290 H400 M0 350 H400" stroke="#fff" stroke-width="4" opacity=".7"/>',
         '<rect y="200" width="400" height="34" fill="#a7c957"/>',
         shadow(150, 342, 40, 5), side_runner(150, 330, 1.25, "#457b9d", SKIN[0], "#e9c46a", mood="tense"),
         '<path d="M150 110 Q144 122 150 126 Q156 122 150 110 Z" fill="#8ecae6"/>',
         '<path d="M174 100 Q168 112 174 116 Q180 112 174 100 Z" fill="#8ecae6"/>',
         shadow(320, 236, 30, 5),
         person(320, 234, .95, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "cap", mood="wide",
                larm=((-30, -24), (-50, -60)), rarm=((30, -24), (50, -60))),
         '<path d="M246 34 l-12 -8 M244 54 h-16 M394 34 l-6 -10" stroke="#264653" stroke-width="3" stroke-linecap="round"/>',
         '<path d="M262 52 q-6 -10 0 -20 M380 52 q6 -10 0 -20" fill="none" stroke="#264653" stroke-width="3"/>',
         arrow(230, 280, 300, 280, "#fff", 6, 16)]
    return svg(b, "#e3f2fd")


def perceive():
    rnd = random.Random(9)
    b = ['<rect width="400" height="400" fill="#1d2d44"/>']
    for _ in range(30):
        b.append(f'<circle cx="{f(rnd.uniform(0, 400))}" cy="{f(rnd.uniform(0, 200))}" r="1.5" fill="#fff" opacity=".7"/>')
    b += ['<circle cx="330" cy="60" r="24" fill="#fefae0"/>',
          '<path d="M0 340 Q200 320 400 340 V400 H0Z" fill="#2d6a4f"/>',
          '<rect x="40" y="0" width="30" height="340" fill="#3e2723"/>',
          '<path d="M60 160 H180" stroke="#3e2723" stroke-width="14" stroke-linecap="round"/>',
          # the owl
          '<ellipse cx="130" cy="120" rx="40" ry="48" fill="#8d6e63"/>',
          '<ellipse cx="130" cy="134" rx="24" ry="30" fill="#d7b899"/>',
          '<polygon points="96,82 104,58 118,78" fill="#8d6e63"/><polygon points="164,82 156,58 142,78" fill="#8d6e63"/>',
          '<circle cx="114" cy="98" r="15" fill="#fff3b0"/><circle cx="146" cy="98" r="15" fill="#fff3b0"/>',
          '<circle cx="114" cy="98" r="22" fill="#ffd166" opacity=".3"/><circle cx="146" cy="98" r="22" fill="#ffd166" opacity=".3"/>',
          '<circle cx="118" cy="102" r="7" fill="#1b1b1b"/><circle cx="150" cy="102" r="7" fill="#1b1b1b"/>',
          '<polygon points="126,108 134,108 130,120" fill="#f4a261"/>',
          '<path d="M112 162 v8 M124 162 v8 M136 162 v8 M148 162 v8" stroke="#f4a261" stroke-width="3"/>',
          # sight lines to the tiny mouse
          '<path d="M160 104 L330 330 M160 104 L346 330" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="7 7" opacity=".8"/>',
          '<circle cx="338" cy="334" r="20" fill="#ffd166" opacity=".2"/>',
          '<ellipse cx="338" cy="336" rx="9" ry="6" fill="#adb5bd"/><circle cx="346" cy="333" r="4" fill="#adb5bd"/>',
          '<circle cx="344" cy="329" r="2.5" fill="#ced4da"/>',
          '<path d="M329 337 q-8 4 -12 -2" fill="none" stroke="#adb5bd" stroke-width="1.5"/>']
    return svg(b, "#1d2d44")


def hard_hat(color="#ffd166"):
    return (f'<path d="M-26 -186 Q-26 -210 0 -210 Q26 -210 26 -186 Z" fill="{color}"/>'
            f'<rect x="-30" y="-190" width="60" height="7" rx="3" fill="{color}"/>')


def staged():
    signs = (
        # hard hat
        '<path d="M-14 6 Q-14 -12 0 -12 Q14 -12 14 6 Z" fill="#ffd166"/><rect x="-18" y="4" width="36" height="6" '
        'rx="3" fill="#ffd166"/>',
        # first-aid cross
        '<path d="M-6 -16 H6 V-6 H16 V6 H6 V16 H-6 V6 H-16 V-6 H-6 Z" fill="#52b788"/>',
        # shield with a tick
        '<path d="M0 -18 L16 -12 Q16 8 0 18 Q-16 8 -16 -12 Z" fill="#4895ef"/>'
        '<path d="M-7 0 L-2 6 L8 -6" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" '
        'stroke-linejoin="round"/>',
        # care for the workers
        heart(0, 2, 16))
    b = [# the factory
         '<rect x="30" y="140" width="340" height="170" fill="#b8c0c8"/>',
         '<polygon points="30,140 30,100 98,140 98,100 166,140 166,100 234,140 234,100 302,140 302,100 370,140" '
         'fill="#8d99ae"/>',
         '<rect x="300" y="40" width="30" height="80" fill="#6c757d"/>',
         '<circle cx="320" cy="30" r="14" fill="#ced4da"/><circle cx="338" cy="16" r="12" fill="#dee2e6"/>'
         '<circle cx="358" cy="8" r="10" fill="#e9ecef"/>']
    for x in range(52, 360, 56):
        b.append(f'<rect x="{x}" y="164" width="36" height="28" rx="3" fill="#457b9d"/>')
    b += ['<rect x="170" y="230" width="60" height="80" fill="#6c757d"/>',
          '<rect y="300" width="400" height="100" fill="#ced4da"/>']
    workers = ((52, SKIN[1], "#e76f51", "#ffd166", "wide"), (140, SKIN[3], "#2a9d8f", "#f4a261", "angry"),
               (228, SKIN[0], "#457b9d", "#ffd166", "wide"), (316, SKIN[2], "#e9c46a", "#f4a261", "angry"))
    for (x, sk, shirt, hat, mood), sign in zip(workers, signs):
        held = ('<line x1="40" y1="-140" x2="40" y2="-252" stroke="#9c6b3c" stroke-width="6" stroke-linecap="round"/>'
                '<rect x="0" y="-306" width="80" height="58" rx="4" fill="#fff" stroke="#adb5bd" stroke-width="3"/>'
                f'<g transform="translate(40 -277)">{sign}</g>'
                f'<circle cx="40" cy="-196" r="8.5" fill="{sk}"/>' + hard_hat(hat))
        b += [shadow(x, 354, 30),
              person(x, 352, .88, sk, shirt, "#264653", "#1b1b1b", "none", mood=mood,
                     larm=((-14, 40), (-16, 72)), rarm=((14, -18), (18, -50)), extra=held)]
    return svg(b, "#cfe8f3")



def arduous():
    rnd = random.Random(12)
    b = ['<polygon points="0,400 0,330 400,100 400,400" fill="#e9ecef"/>',
         '<polygon points="0,400 0,350 400,120 400,400" fill="#caf0f8"/>',
         '<path d="M60 350 L120 316 M200 268 L260 236 M300 214 L360 180" stroke="#a8dadc" stroke-width="4"/>']
    for x, y, s, c in ((140, 262, .75, "#e63946"), (290, 176, .75, "#f4a261")):
        b += [person(x, y, s, SKIN[1], c, "#264653", "#1b1b1b", "cap", mood="shut", rot=22,
                     brows="M-14 -190 L-3 -186 M3 -186 L14 -190",
                     larm=((30, 16), (58, 22)), rarm=((18, 18), (34, 22)), lleg=((-10, 40), (-24, 80)),
                     rleg=((14, 36), (20, 76)))]
    b += ['<path d="M190 176 Q232 196 268 136" fill="none" stroke="#ffd166" stroke-width="4"/>']
    for _ in range(26):
        x, y = rnd.uniform(0, 400), rnd.uniform(0, 300)
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 30)}" y2="{f(y + 6)}" stroke="#fff" stroke-width="3" '
                 'stroke-linecap="round" opacity=".9"/>')
    return svg(b, "#8d99ae")


def plate(x, y, k=1.0, food=None):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<ellipse cx="0" cy="0" rx="26" ry="7" fill="#fff" stroke="#ced4da" stroke-width="2"/>'
            + (f'<ellipse cx="0" cy="-4" rx="12" ry="6" fill="{food}"/>' if food else "") + '</g>')


def overwhelmed():
    rnd = random.Random(3)
    foods = ["#e76f51", "#a7c957", "#e9c46a", "#9c6644", None]
    b = ['<rect y="340" width="400" height="60" fill="#d4a373"/>', shadow(200, 344, 40),
         person(200, 342, 1.0, SKIN[0], "#fff", "#264653", "#7f5539", "short", mood="wide",
                brows="M-14 -192 Q-8 -198 -2 -193 M2 -193 Q8 -198 14 -192",
                larm=((-34, -10), (-62, -24)), rarm=((34, -10), (62, -24)),
                extra=f'<path d="M-9 -152 L0 -146 L9 -152 L9 -142 L0 -146 L-9 -142 Z" fill="{INK}"/>')]
    for cx in (116, 284):
        for k in range(7):
            b.append(plate(cx + rnd.uniform(-5, 5), 160 - k * 12, 1.1, rnd.choice(foods)))
    for x, y, r in ((60, 50, -20), (340, 40, 30), (200, 30, 10)):
        b.append(f'<g transform="rotate({r} {x} {y})">' + plate(x, y, 1.0, "#e76f51") + '</g>')
    b += ['<path d="M250 90 Q244 102 250 106 Q256 102 250 90 Z" fill="#8ecae6"/>',
          # the order slips piling up
          '<rect x="300" y="260" width="90" height="12" fill="#7f5539"/>']
    for k in range(6):
        b.append(f'<rect x="{310 + rnd.uniform(-6, 6)}" y="{250 - k * 12}" width="44" height="30" fill="#fff" '
                 f'stroke="#ced4da" stroke-width="2" transform="rotate({rnd.uniform(-15, 15)} 332 {260 - k * 12})"/>')
    b += [f'<path d="M30 270 l40 -10 M20 300 l50 0" stroke="#adb5bd" stroke-width="0"/>']
    return svg(b, "#fdf6ec")


def protective():
    rnd = random.Random(5)
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         '<ellipse cx="90" cy="40" rx="120" ry="40" fill="#adb5bd"/><ellipse cx="320" cy="34" rx="120" ry="36" fill="#8d99ae"/>']
    for _ in range(40):
        x, y = rnd.uniform(0, 400), rnd.uniform(60, 320)
        if 60 < x < 340 and y > 150:
            continue
        b.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(x - 4)}" y2="{f(y + 14)}" stroke="#4895ef" stroke-width="3" '
                 'stroke-linecap="round"/>')
    b += [shadow(200, 326, 140, 8),
          # wings spread wide like a roof
          '<path d="M200 190 Q120 150 50 230 Q40 260 70 320 L120 300 Q140 260 200 250 Z" fill="#c08552"/>',
          '<path d="M200 190 Q280 150 350 230 Q360 260 330 320 L280 300 Q260 260 200 250 Z" fill="#c08552"/>',
          '<path d="M60 250 L110 236 M66 280 L120 260 M340 250 L290 236 M334 280 L280 260" stroke="#9c6644" stroke-width="4"/>',
          '<ellipse cx="200" cy="240" rx="70" ry="60" fill="#e6ccb2"/>',
          '<circle cx="200" cy="150" r="34" fill="#e6ccb2"/>',
          '<path d="M186 118 Q190 100 200 112 Q206 98 214 114" fill="#e63946"/>',
          '<polygon points="194,156 206,156 200,172" fill="#f4a261"/>', '<path d="M194 172 q6 10 12 0" fill="#e63946"/>',
          f'<circle cx="188" cy="146" r="4" fill="{INK}"/><circle cx="212" cy="146" r="4" fill="{INK}"/>']
    for x in (110, 160, 240, 290):
        b += [f'<circle cx="{x}" cy="306" r="16" fill="#ffd166"/>', f'<circle cx="{x + 6}" cy="302" r="2.5" fill="{INK}"/>',
              f'<polygon points="{x + 14},{304} {x + 22},{306} {x + 14},{309}" fill="#f4a261"/>']
    return svg(b, "#dbe7f0")


def predictable():
    b = ['<rect y="300" width="400" height="100" fill="#e9d8c4"/>']
    xs = list(range(30, 380, 32))
    for k, x in enumerate(xs):
        if k < 5:
            rot = 62
        elif k == 5:
            rot = 32
        else:
            rot = 0
        b.append(f'<g transform="rotate({rot} {x + 14} 300)"><rect x="{x}" y="230" width="14" height="70" rx="3" fill="#264653"/>'
                 f'<circle cx="{x + 7}" cy="248" r="3" fill="#fff"/><circle cx="{x + 7}" cy="282" r="3" fill="#fff"/>'
                 f'<line x1="{x + 2}" y1="265" x2="{x + 12}" y2="265" stroke="#fff" stroke-width="2"/></g>')
    b += [arrow(40, 150, 370, 150, "#e76f51", 6, 18)]
    for x in xs[6:]:
        b.append(f'<path d="M{x + 7} 222 Q{x + 34} 222 {x + 40} 262" fill="none" stroke="#6c757d" stroke-width="3" '
                 'stroke-dasharray="5 5" stroke-linecap="round"/>'
                 f'<polygon points="{x + 34},258 {x + 46},258 {x + 41},270" fill="#6c757d"/>')
    return svg(b, "#fdf6ec")


def ignored():
    b = ['<rect y="300" width="400" height="100" fill="#8d6e63"/>',
         '<rect x="260" y="40" width="110" height="90" fill="#1d2d44"/><circle cx="330" cy="70" r="14" fill="#fefae0"/>',
         # bed with someone under the covers, pillow pressed over their head
         '<rect x="20" y="220" width="250" height="60" rx="10" fill="#457b9d"/>',
         '<rect x="10" y="180" width="20" height="130" rx="6" fill="#7f5539"/><rect x="262" y="230" width="16" height="80" '
         'rx="6" fill="#7f5539"/>',
         '<path d="M90 236 Q160 180 262 226 V250 H90 Z" fill="#a8dadc"/>',
         f'<circle cx="68" cy="206" r="22" fill="{SKIN[1]}"/>',
         '<ellipse cx="66" cy="188" rx="46" ry="20" fill="#fff" stroke="#dee2e6" stroke-width="3"/>',
         f'<circle cx="104" cy="192" r="9" fill="{SKIN[1]}"/>',
         # the ringing alarm clock
         '<rect x="290" y="250" width="80" height="54" rx="4" fill="#9c6b3c"/>',
         '<circle cx="330" cy="212" r="30" fill="#e63946"/><circle cx="330" cy="212" r="22" fill="#fff"/>',
         '<path d="M330 212 V198 M330 212 L340 218" stroke="#264653" stroke-width="3" stroke-linecap="round"/>',
         '<circle cx="306" cy="182" r="10" fill="#e9c46a"/><circle cx="354" cy="182" r="10" fill="#e9c46a"/>',
         '<path d="M316 246 l-6 6 M344 246 l6 6" stroke="#264653" stroke-width="4" stroke-linecap="round"/>',
         '<path d="M288 186 q-12 4 -14 20 M372 186 q12 4 14 20 M280 172 q-18 6 -20 34 M380 172 q18 6 20 34" fill="none" '
         'stroke="#e63946" stroke-width="3.5" stroke-linecap="round"/>',
         '<path d="M84 150 h12 l-12 12 h12 M104 126 h16 l-16 16 h16" fill="none" stroke="#264653" stroke-width="3" '
         'stroke-linejoin="round"/>']
    return svg(b, "#ffe8cc")


def avoided():
    b = ['<rect x="110" y="0" width="180" height="400" fill="#495057"/>',
         '<path d="M200 0 V400" stroke="#ffd166" stroke-width="4" stroke-dasharray="24 18"/>',
         bush(50, 80, 30), bush(60, 300, 34), bush(350, 160, 32), bush(340, 340, 26),
         '<ellipse cx="248" cy="210" rx="34" ry="22" fill="#212529"/><ellipse cx="248" cy="214" rx="24" ry="14" fill="#343a40"/>',
         '<path d="M250 390 C 250 300, 150 260, 150 210 C 150 160, 250 120, 250 30" fill="none" stroke="#fff" stroke-width="3" '
         'stroke-dasharray="8 8"/>',
         '<g transform="rotate(-20 156 190)"><rect x="132" y="150" width="48" height="80" rx="12" fill="#e63946"/>'
         '<rect x="138" y="164" width="36" height="18" rx="4" fill="#caf0f8"/>'
         '<rect x="138" y="204" width="36" height="14" rx="4" fill="#caf0f8"/></g>',
         arrow(250, 70, 250, 26, "#fff", 3, 11)]
    return svg(b, "#a7c957")



def impractical():
    shoe = ('<path d="M-12 -12 L2 -2 L16 2 Q19 7 14 7 L-4 7 Z" fill="#e63946"/>'
            '<line x1="-10" y1="-8" x2="-11" y2="8" stroke="#e63946" stroke-width="3"/>')
    b = ['<polygon points="0,260 120,110 210,190 300,90 400,220 400,400 0,400" fill="#9a8c98"/>',
         '<polygon points="300,90 326,124 312,128 300,116 288,130 276,122" fill="#fff"/>',
         '<path d="M0 320 Q200 290 400 320 V400 H0Z" fill="#b08968"/>']
    for x, y, rx in ((40, 330, 30), (130, 324, 22), (300, 320, 34), (370, 336, 24), (230, 350, 20)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{rx * .55}" fill="#6c757d"/>'
                 f'<ellipse cx="{x - rx * .3}" cy="{y - rx * .2}" rx="{rx * .4}" ry="{rx * .2}" fill="#adb5bd"/>')
    hiker = ('<g transform="translate(190 336) scale(1.6)">'
             '<rect x="-24" y="-138" width="18" height="44" rx="5" fill="#2a9d8f"/>'
             + limb(((0, -80), (-8, -44), (-16, -12)), "#457b9d", 12)
             + limb(((0, -80), (14, -44), (18, -12)), "#457b9d", 12)
             + f'<g transform="translate(-16 -10)">{shoe}</g><g transform="translate(20 -10)">{shoe}</g>'
             + limb(((0, -82), (4, -126)), "#f4a261", 22)
             + limb(((4, -124), (-20, -112), (-38, -124)), "#f4a261", 9) + f'<circle cx="-40" cy="-125" r="5" fill="{SKIN[0]}"/>'
             + limb(((4, -124), (26, -110), (42, -124)), "#f4a261", 9) + f'<circle cx="44" cy="-125" r="5" fill="{SKIN[0]}"/>'
             + f'<circle cx="10" cy="-146" r="15" fill="{SKIN[0]}"/>'
             '<path d="M-4 -150 Q-4 -166 10 -165 Q24 -164 24 -152 Q12 -158 2 -148 Z" fill="#7f5539"/>'
             f'<circle cx="17" cy="-148" r="2.5" fill="{INK}"/>'
             f'<path d="M12 -156 L20 -158" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'
             f'<path d="M14 -138 Q18 -141 22 -138" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/></g>')
    b += [shadow(196, 340, 36), hiker,
          '<path d="M110 120 q-10 6 -8 18 M282 120 q10 6 8 18 M120 100 q-14 8 -12 26 M272 100 q14 8 12 26" fill="none" '
          'stroke="#264653" stroke-width="3" stroke-linecap="round"/>',
          '<path d="M218 300 Q212 312 218 316 Q224 312 218 300 Z" fill="#8ecae6" opacity=".0"/>',
          '<path d="M236 80 Q230 92 236 96 Q242 92 236 80 Z" fill="#8ecae6"/>']
    return svg(b, "#cfe8f3")


def cat_side(x, y, k=1.0, flip=False, color="#6c757d"):
    sgn = -1 if flip else 1
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sgn * k)} {k})">'
            f'<path d="M-40 -10 Q-48 -60 -52 -98" fill="none" stroke="{color}" stroke-width="14" stroke-linecap="round"/>'
            '<path d="M-58 -96 l-4 -10 M-52 -100 v-12 M-46 -96 l4 -10" stroke="' + color + '" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M-34 0 V-40 M-22 0 V-46 M22 0 V-46 M34 0 V-40" stroke="{color}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-44 -40 Q-30 -100 0 -100 Q30 -100 44 -40 Q0 -52 -44 -40 Z" fill="{color}"/>'
            '<path d="M-30 -86 l-6 -10 M-14 -98 l-4 -12 M2 -100 v-12 M18 -96 l4 -12 M32 -84 l8 -10" stroke="' + color
            + '" stroke-width="4" stroke-linecap="round"/>'
            f'<circle cx="54" cy="-60" r="22" fill="{color}"/>'
            f'<path d="M38 -76 L40 -98 L54 -82 Z M58 -82 L70 -98 L70 -74 Z" fill="{color}"/>'
            '<path d="M60 -56 Q72 -52 76 -46 Q66 -40 60 -46 Z" fill="#9d0208"/>'
            '<path d="M64 -54 l2 5 l2 -5 M70 -50 l2 5 l2 -4" fill="#fff"/>'
            '<ellipse cx="62" cy="-68" rx="5" ry="3" fill="#ffd166"/>'
            f'<path d="M56 -76 L68 -72" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M70 -60 l14 -4 M70 -56 l14 2" stroke="#fff" stroke-width="1.5"/></g>')


def despise():
    b = ['<circle cx="330" cy="60" r="26" fill="#fefae0"/>',
         '<rect y="300" width="400" height="100" fill="#52796f"/>']
    for x in range(0, 400, 40):
        b.append(f'<rect x="{x + 4}" y="236" width="32" height="70" fill="#b08968"/>')
    b += ['<rect y="226" width="400" height="14" fill="#9c6b3c"/>',
          cat_side(110, 228, 1.1, False, "#495057"), cat_side(290, 228, 1.1, True, "#e76f51"),
          '<polygon points="200,110 188,136 200,134 190,160 214,128 202,130 212,110" fill="#ffd166"/>',
          '<path d="M176 120 l-8 -8 M224 120 l8 -8" stroke="#ffd166" stroke-width="3" stroke-linecap="round"/>']
    return svg(b, "#cdb4db")


def rabbit(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<ellipse cx="0" cy="-14" rx="22" ry="14" fill="#adb5bd"/>'
            '<circle cx="18" cy="-26" r="11" fill="#adb5bd"/>'
            '<ellipse cx="14" cy="-46" rx="4" ry="13" fill="#adb5bd" transform="rotate(-15 14 -46)"/>'
            '<ellipse cx="22" cy="-46" rx="4" ry="13" fill="#adb5bd" transform="rotate(10 22 -46)"/>'
            '<circle cx="-22" cy="-16" r="6" fill="#fff"/>'
            f'<path d="M18 -26 q3 2 6 0" fill="none" stroke="{INK}" stroke-width="2"/></g>')


def provide():
    b = ['<circle cx="340" cy="56" r="34" fill="#ffd166"/>']
    for a in range(0, 360, 30):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(340 + 44 * ca)}" y1="{f(56 + 44 * sa)}" x2="{f(340 + 58 * ca)}" y2="{f(56 + 58 * sa)}" '
                 'stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>')
    b += ['<rect y="270" width="400" height="130" fill="#e9c46a"/>',
          '<ellipse cx="170" cy="330" rx="160" ry="44" fill="#6a994e"/>',
          '<path d="M150 330 L158 170 H184 L192 330 Z" fill="#7f5539"/>']
    for x, y, r in ((170, 130, 96), (90, 170, 60), (250, 170, 64), (120, 90, 56), (220, 80, 60)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#2d6a4f"/>')
    for x, y, r in ((150, 110, 40), (230, 140, 26), (90, 160, 22)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#40916c"/>')
    b += [sheep(80, 344, k=.8), dog(250, 350, .62), rabbit(120, 370, .9), rabbit(310, 360, .7),
          '<path d="M350 310 q-6 -6 0 -12 t0 -12 t0 -12 M372 310 q-6 -6 0 -12 t0 -12 t0 -12" fill="none" '
          'stroke="#f4a261" stroke-width="3" stroke-linecap="round"/>']
    return svg(b, "#fff3b0")


def banana_peel(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<ellipse cx="0" cy="4" rx="24" ry="5" fill="#000" opacity=".12"/>'
            '<path d="M0 0 Q-26 -2 -30 -14 Q-14 -10 -2 -8 Z" fill="#ffd166"/>'
            '<path d="M0 0 Q24 -4 30 -16 Q14 -10 2 -8 Z" fill="#ffd166"/>'
            '<path d="M0 0 Q-4 -18 -2 -28 Q6 -16 4 -2 Z" fill="#ffd166"/>'
            '<rect x="-4" y="-6" width="8" height="8" rx="2" fill="#e9c46a"/>'
            '<path d="M-2 -28 l0 -5" stroke="#7f5539" stroke-width="3" stroke-linecap="round"/></g>')


def overlook():
    b = ['<rect y="320" width="400" height="80" fill="#ced4da"/>',
         '<path d="M290 70 q12 -10 24 0 q12 -10 24 0" fill="none" stroke="#264653" stroke-width="4" stroke-linecap="round"/>',
         '<ellipse cx="90" cy="60" rx="50" ry="16" fill="#fff"/>',
         shadow(160, 334, 36),
         person(160, 332, 1.1, SKIN[2], "#e9c46a", "#457b9d", "#1b1b1b", "short", mood="up",
                larm=((-14, 40), (-18, 72)), rarm=((24, -20), (40, -50)),
                lleg=((-6, 44), (-12, 86)), rleg=((24, 34), (40, 70))),
         banana_peel(244, 336, 1.3),
         '<path d="M206 300 Q226 296 236 314" fill="none" stroke="#e63946" stroke-width="3" stroke-dasharray="5 5"/>',
         '<path d="M200 140 L280 80" stroke="#6c757d" stroke-width="2" stroke-dasharray="6 6"/>']
    return svg(b, "#e3f2fd")


def creativity():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         # the cardboard robot
         '<rect x="190" y="250" width="30" height="80" fill="#c08552"/><rect x="250" y="250" width="30" height="80" fill="#c08552"/>',
         '<rect x="170" y="150" width="130" height="110" fill="#d4a373" stroke="#b08968" stroke-width="3"/>',
         '<rect x="190" y="70" width="90" height="74" fill="#e6ccb2" stroke="#b08968" stroke-width="3"/>',
         '<circle cx="215" cy="104" r="12" fill="#e63946"/><circle cx="255" cy="104" r="12" fill="#4895ef"/>',
         '<rect x="216" y="124" width="38" height="8" rx="3" fill="#264653"/>',
         '<path d="M235 70 V46" stroke="#6c757d" stroke-width="4"/><circle cx="235" cy="42" r="7" fill="#ffd166"/>',
         '<rect x="300" y="170" width="60" height="20" fill="#c08552"/><rect x="110" y="170" width="60" height="20" fill="#c08552"/>',
         '<circle cx="210" cy="190" r="9" fill="#2a9d8f"/><circle cx="235" cy="190" r="9" fill="#ffd166"/>'
         '<circle cx="260" cy="190" r="9" fill="#e76f51"/>',
         '<rect x="200" y="216" width="70" height="24" rx="4" fill="#a8dadc"/>',
         '<path d="M206 228 h10 M226 228 h10 M246 228 h10" stroke="#264653" stroke-width="3"/>',
         # the young builder adding a cap
         shadow(80, 344, 30),
         person(80, 342, .82, SKIN[3], "#a7c957", "#457b9d", "#1b1b1b", "bun", mood="grin",
                larm=((-12, 40), (-14, 70)), rarm=((24, 0), (44, -6))),
         '<circle cx="120" cy="186" r="8" fill="#e63946"/>',
         '<rect x="320" y="300" width="22" height="32" rx="4" fill="#fff"/><rect x="326" y="290" width="10" height="12" '
         'fill="#e76f51"/>',
         '<circle cx="80" cy="70" r="20" fill="#ffd166"/><rect x="72" y="88" width="16" height="12" rx="2" fill="#adb5bd"/>']
    for a in range(-150, -20, 30):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(80 + 28 * ca)}" y1="{f(70 + 28 * sa)}" x2="{f(80 + 40 * ca)}" y2="{f(70 + 40 * sa)}" '
                 'stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>')
    return svg(b, "#fdf6ec")


def excited_about():
    b = ['<rect y="320" width="400" height="80" fill="#adb5bd"/>', '<rect y="300" width="400" height="22" fill="#dee2e6"/>',
         '<circle cx="60" cy="60" r="26" fill="#ffd166"/>',
         bus(300, 340, .95),
         '<path d="M180 270 h-24 M184 290 h-34" stroke="#fff" stroke-width="4" stroke-linecap="round"/>']
    for x, y, sk, c, hair, style in ((50, 280, SKIN[0], "#e76f51", "#7f5539", "bun"),
                                     (120, 268, SKIN[3], "#2a9d8f", "#1b1b1b", "short"),
                                     (190, 284, SKIN[1], "#e9c46a", "#5c4033", "side")):
        b += [shadow(x, 318, 22, 4),
              person(x, y, .7, sk, c, "#457b9d", hair, style, mood="grin",
                     larm=((-24, -30), (-36, -66)), rarm=((24, -30), (36, -66)),
                     lleg=((-10, 34), (-6, 66)), rleg=((10, 34), (6, 66)))]
    b += [star(90, 110, 9), star(160, 96, 7), star(30, 140, 6)]
    return svg(b, "#e3f2fd")


def recollect():
    b = ['<rect y="340" width="400" height="60" fill="#e9d8c4"/>',
         # the thought: himself as a boy on a bike
         '<circle cx="150" cy="170" r="8" fill="#fff" stroke="#ced4da" stroke-width="2"/>',
         '<circle cx="170" cy="140" r="12" fill="#fff" stroke="#ced4da" stroke-width="2"/>',
         '<ellipse cx="280" cy="90" rx="110" ry="80" fill="#fff" stroke="#ced4da" stroke-width="3"/>',
         '<g opacity=".85">', '<rect x="186" y="128" width="190" height="16" fill="#a7c957"/>',
         cyclist(280, 140, "#e63946", "#e76f51", SKIN[0], "#7f5539", False, .62, happy=True), '</g>',
         '<rect x="34" y="230" width="20" height="110" fill="#7f5539"/>',
         shadow(100, 344, 40),
         person(100, 342, 1.0, SKIN[0], "#8d6e63", "#495057", "#dee2e6", "short", mood="smile",
                larm=((-12, 40), (-14, 70)), rarm=((30, 20), (46, 10)),
                extra=(f'<circle cx="-8" cy="-180" r="7" fill="none" stroke="{INK}" stroke-width="2"/>'
                       f'<circle cx="8" cy="-180" r="7" fill="none" stroke="{INK}" stroke-width="2"/>')),
         '<g transform="rotate(-12 160 216)"><rect x="140" y="196" width="44" height="40" rx="2" fill="#fff"/>'
         '<rect x="146" y="202" width="32" height="24" fill="#d4a373" opacity=".7"/></g>',
         f'<circle cx="146" cy="225" r="8.5" fill="{SKIN[0]}"/>']
    return svg(b, "#fdf6ec")


def accurate():
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         '<path d="M150 330 L180 280 M250 330 L220 280" stroke="#7f5539" stroke-width="8" stroke-linecap="round"/>']
    for r, c in ((110, "#fff"), (88, "#e63946"), (66, "#fff"), (44, "#e63946"), (22, "#ffd166")):
        b.append(f'<circle cx="200" cy="180" r="{r}" fill="{c}"/>')
    b += ['<circle cx="200" cy="180" r="110" fill="none" stroke="#adb5bd" stroke-width="3"/>',
          '<line x1="200" y1="180" x2="370" y2="80" stroke="#7f5539" stroke-width="6" stroke-linecap="round"/>',
          '<polygon points="356,78 382,62 386,74 366,88" fill="#2a9d8f"/><polygon points="360,92 386,92 380,104 364,100" '
          'fill="#2a9d8f"/>',
          '<circle cx="200" cy="180" r="5" fill="#264653"/>',
          sparkle(160, 140, 10, "#fff"), sparkle(240, 220, 8, "#fff"),
          '<path d="M172 170 l-12 -4 M176 196 l-12 6 M206 152 l2 -12" stroke="#264653" stroke-width="3" '
          'stroke-linecap="round"/>']
    return svg(b, "#e3f2fd")


def inadvertently():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         person(200, 330, 1.1, SKIN[0], "#457b9d", "#264653", "#7f5539", "short", mood="wide",
                brows="M-14 -192 Q-8 -198 -2 -193 M2 -193 Q8 -198 14 -192",
                larm=((-30, 16), (-74, 24)), rarm=((40, 40), (24, 64))),
         '<rect x="20" y="250" width="360" height="14" rx="4" fill="#7f5539"/>',
         '<rect x="40" y="264" width="12" height="70" fill="#6f4518"/><rect x="348" y="264" width="12" height="70" fill="#6f4518"/>',
         # bread on the left, the glass going over on the right
         '<path d="M60 250 Q60 228 90 226 Q122 228 122 250 Z" fill="#e9c46a"/>',
         '<path d="M72 236 l8 -6 M92 234 l8 -6" stroke="#c08552" stroke-width="3" stroke-linecap="round"/>',
         '<g transform="rotate(60 272 250)"><path d="M258 210 H286 L282 250 H262 Z" fill="#caf0f8" stroke="#8ecae6" '
         'stroke-width="3"/><path d="M260 226 H284 L282 250 H262 Z" fill="#f4a261"/></g>',
         '<path d="M300 244 Q330 240 340 250 Q360 252 370 250" fill="none" stroke="#f4a261" stroke-width="8" '
         'stroke-linecap="round"/>',
         '<circle cx="350" cy="236" r="4" fill="#f4a261"/><circle cx="330" cy="228" r="3" fill="#f4a261"/>',
         '<path d="M368 258 Q370 280 366 290" fill="none" stroke="#f4a261" stroke-width="5" stroke-linecap="round"/>',
         '<path d="M244 210 l10 -8 M250 226 l12 -2" stroke="#e63946" stroke-width="3" stroke-linecap="round"/>']
    return svg(b, "#fdf6ec")


def persist():
    b = ['<rect y="0" width="400" height="200" fill="#cfe8f3"/>', '<circle cx="330" cy="60" r="30" fill="#ffd166"/>',
         '<rect x="0" y="120" width="400" height="80" fill="#e9d8c4"/>',
         '<rect x="40" y="140" width="50" height="40" fill="#caf0f8"/><rect x="310" y="140" width="50" height="40" fill="#caf0f8"/>',
         # the pavement, seen from above at an angle
         '<polygon points="0,200 400,200 400,400 0,400" fill="#adb5bd"/>',
         '<path d="M0 260 H400 M0 330 H400 M120 200 L80 400 M280 200 L320 400" stroke="#8d99ae" stroke-width="4"/>',
         '<path d="M150 400 L176 366 L168 346 L196 326 L204 302 L226 282 L222 262 L246 236 L240 214" fill="none" '
         'stroke="#495057" stroke-width="6" stroke-linejoin="round"/>',
         # the little plant pushing up through the crack
         '<ellipse cx="204" cy="304" rx="16" ry="5" fill="#495057"/>',
         '<path d="M204 304 Q200 250 208 196" fill="none" stroke="#52b788" stroke-width="7" stroke-linecap="round"/>',
         '<path d="M203 260 Q170 240 160 252 Q176 272 203 260 Z" fill="#52b788"/>',
         '<path d="M206 228 Q238 204 250 216 Q234 236 206 228 Z" fill="#40916c"/>',
         '<path d="M208 198 Q202 178 214 168 Q220 186 208 198 Z" fill="#a7c957"/>',
         arrow(270, 290, 270, 200, "#2a9d8f", 5, 14), sparkle(150, 200, 9, "#ffd166")]
    return svg(b, "#cfe8f3")


def bulb(x, y, k=1.0, lit=True, rot=0):
    glass = "#ffd166" if lit else "#adb5bd"
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({k})">'
            + ('<circle cx="0" cy="-30" r="44" fill="#fff3b0" opacity=".6"/>' if lit else "")
            + f'<circle cx="0" cy="-34" r="28" fill="{glass}"/>'
            f'<path d="M-14 -16 H14 L10 4 H-10 Z" fill="{glass}"/>'
            '<rect x="-12" y="4" width="24" height="18" rx="3" fill="#6c757d"/>'
            '<path d="M-12 10 H12 M-12 16 H12" stroke="#495057" stroke-width="2"/>'
            + ('<path d="M-9 -34 q2.25 -6 4.5 0 t4.5 0 t4.5 0 t4.5 0" fill="none" stroke="#e76f51" stroke-width="3" '
               'stroke-linecap="round"/>' if lit else
               '<path d="M-8 -48 L0 -36 L-6 -28 L4 -18" fill="none" stroke="#495057" stroke-width="3"/>')
            + '</g>')


def replace():
    b = ['<rect x="180" y="0" width="40" height="40" fill="#adb5bd"/>',
         '<line x1="200" y1="0" x2="200" y2="40" stroke="#495057" stroke-width="6"/>',
         '<rect x="184" y="40" width="32" height="24" rx="4" fill="#495057"/>',
         bulb(200, 96, 1.4, True, 180),
         # the old, burnt-out bulb in a hand on its way out
         bulb(90, 300, 1.1, False, 160),
         f'<path d="M0 360 Q50 340 80 330" fill="none" stroke="#457b9d" stroke-width="30" stroke-linecap="round"/>',
         f'<ellipse cx="88" cy="326" rx="18" ry="16" fill="{SKIN[1]}"/>',
         carrow(120, 250, 150, 200, 160, 160, "#2a9d8f", 5, 14),
         carrow(250, 200, 300, 260, 250, 320, "#e76f51", 5, 14)]
    return svg(b, "#3d405b")


def koala(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<ellipse cx="0" cy="0" rx="40" ry="50" fill="#adb5bd"/>'
            '<ellipse cx="6" cy="10" rx="22" ry="30" fill="#dee2e6"/>'
            '<circle cx="-32" cy="-74" r="22" fill="#adb5bd"/><circle cx="32" cy="-74" r="22" fill="#adb5bd"/>'
            '<circle cx="-32" cy="-74" r="12" fill="#f1f3f5"/><circle cx="32" cy="-74" r="12" fill="#f1f3f5"/>'
            '<circle cx="0" cy="-56" r="38" fill="#adb5bd"/>'
            '<ellipse cx="0" cy="-48" rx="12" ry="16" fill="#343a40"/>'
            f'<path d="M-20 -66 q6 -6 12 0 M8 -66 q6 -6 12 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            '</g>')


def clinging_to():
    rnd = random.Random(4)
    b = ['<rect y="340" width="400" height="60" fill="#a7c957"/>',
         '<path d="M150 400 L160 0 H230 L240 400 Z" fill="#9c6644"/>',
         '<path d="M180 60 Q190 200 176 360" stroke="#7f5539" stroke-width="4" fill="none"/>',
         koala(160, 200, 1.1),
         # its arms and legs wrapped round the trunk
         '<path d="M140 150 Q200 130 236 160" fill="none" stroke="#adb5bd" stroke-width="20" stroke-linecap="round"/>',
         '<path d="M140 250 Q200 236 236 262" fill="none" stroke="#adb5bd" stroke-width="20" stroke-linecap="round"/>',
         '<circle cx="236" cy="160" r="12" fill="#6c757d"/><circle cx="236" cy="262" r="12" fill="#6c757d"/>']
    for y in (60, 110, 300, 360):
        b.append(f'<path d="M260 {y} q40 -12 80 0 t60 -4" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
    for _ in range(7):
        x, y = rnd.uniform(270, 390), rnd.uniform(40, 320)
        b.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="10" ry="5" fill="#52b788" transform="rotate({rnd.randint(-40, 40)} '
                 f'{f(x)} {f(y)})"/>')
    b += ['<path d="M20 120 q30 -10 60 0 M10 220 q40 -10 80 0" fill="none" stroke="#fff" stroke-width="4" '
          'stroke-linecap="round"/>']
    return svg(b, "#cfe8f3")



def pointing_arm(x1, y1, x2, y2, sleeve, skin):
    a = math.atan2(y2 - y1, x2 - x1)
    fx, fy = x2 + 22 * math.cos(a), y2 + 22 * math.sin(a)
    return (f'<line x1="{x1}" y1="{y1}" x2="{f(x2)}" y2="{f(y2)}" stroke="{sleeve}" stroke-width="26" stroke-linecap="round"/>'
            f'<circle cx="{f(x2)}" cy="{f(y2)}" r="14" fill="{skin}"/>'
            f'<line x1="{f(x2)}" y1="{f(y2)}" x2="{f(fx)}" y2="{f(fy)}" stroke="{skin}" stroke-width="8" stroke-linecap="round"/>')


def blamed():
    b = ['<rect y="300" width="400" height="100" fill="#d4a373"/>',
         dog(190, 330, 1.05),
         '<path d="M216 210 Q224 194 240 196" fill="none" stroke="#7f5539" stroke-width="0"/>',
         '<path d="M178 196 Q172 208 178 212 Q184 208 178 196 Z" fill="#8ecae6"/>',
         # the chewed shoe
         '<path d="M250 330 V300 Q252 290 262 290 H280 Q284 304 300 308 Q324 312 326 330 Z" fill="#e63946"/>',
         '<path d="M262 290 l4 8 l4 -8 l4 8 l4 -8 M300 308 l2 8 l4 -6 l4 6" fill="none" stroke="#d4a373" stroke-width="3"/>',
         '<rect x="248" y="326" width="80" height="8" rx="3" fill="#fff"/>',
         '<circle cx="240" cy="350" r="4" fill="#fff"/><circle cx="330" cy="344" r="3" fill="#fff"/>',
         pointing_arm(0, 90, 90, 140, "#457b9d", SKIN[0]),
         pointing_arm(400, 80, 310, 140, "#e76f51", SKIN[3]),
         pointing_arm(0, 250, 70, 240, "#2a9d8f", SKIN[1]),
         pointing_arm(400, 230, 350, 220, "#e9c46a", SKIN[2])]
    return svg(b, "#fdf0d5")


def gathering():
    rnd = random.Random(8)
    b = ['<rect y="280" width="400" height="120" fill="#a7c957"/>',
         '<path d="M0 40 Q100 80 200 50 T400 40" fill="none" stroke="#6c757d" stroke-width="2"/>']
    for k in range(13):
        x = k * 32 + 8
        y = 40 + 18 * math.sin(k / 12 * 2 * math.pi) + 12
        b.append(f'<circle cx="{x}" cy="{f(y)}" r="6" fill="#ffd166"/>')
    people = ((60, SKIN[0], "#e76f51", "#dee2e6", "bun"), (120, SKIN[3], "#2a9d8f", "#1b1b1b", "short"),
              (180, SKIN[1], "#e9c46a", "#7f5539", "side"), (240, SKIN[2], "#457b9d", "#1b1b1b", "bun"),
              (300, SKIN[0], "#f4a261", "#e9c46a", "short"), (355, SKIN[1], "#a7c957", "#5c4033", "short"))
    for x, sk, c, hair, style in people:
        b.append(person(x, 330, .85, sk, c, "#264653", hair, style, mood="grin" if x % 120 else "smile",
                        larm=((-10, 30), (2, 40)), rarm=((10, 30), (-2, 40))))
    b += ['<rect x="10" y="246" width="380" height="20" rx="4" fill="#fff"/>',
          '<rect x="10" y="262" width="380" height="60" fill="#e9ecef"/>',
          '<path d="M10 266 H390" stroke="#e63946" stroke-width="4" stroke-dasharray="20 20"/>']
    for x in range(40, 380, 54):
        b.append(f'<ellipse cx="{x}" cy="248" rx="18" ry="5" fill="#fff" stroke="#ced4da" stroke-width="2"/>'
                 f'<circle cx="{x}" cy="244" r="7" fill="{rnd.choice(("#e76f51", "#a7c957", "#e9c46a", "#9c6644"))}"/>')
    b += ['<path d="M190 240 V218 Q200 210 210 218 V240 Z" fill="#c8743a"/>',
          '<rect x="30" y="322" width="10" height="40" fill="#adb5bd"/><rect x="360" y="322" width="10" height="40" '
          'fill="#adb5bd"/>']
    return svg(b, "#fde2c8")


def hesitant():
    b = ['<rect x="0" y="0" width="400" height="260" fill="#e9ecef"/>',
         '<rect x="200" y="260" width="200" height="140" fill="#4895ef"/>',
         '<path d="M210 300 q20 -8 40 0 t40 0 t40 0 t40 0 M210 340 q20 -8 40 0 t40 0 t40 0 t40 0" fill="none" '
         'stroke="#a8dadc" stroke-width="3"/>',
         '<rect x="0" y="250" width="200" height="150" fill="#dee2e6"/>',
         '<rect x="0" y="250" width="210" height="14" fill="#fff"/>',
         '<ellipse cx="232" cy="266" rx="20" ry="5" fill="none" stroke="#fff" stroke-width="3"/>',
         '<ellipse cx="232" cy="266" rx="34" ry="9" fill="none" stroke="#fff" stroke-width="2" opacity=".7"/>',
         shadow(140, 256, 30, 5),
         person(140, 254, .95, SKIN[2], "#e63946", "#264653", "#1b1b1b", "short", mood="frown",
                brows="M-14 -186 L-4 -191 M4 -191 L14 -186",
                larm=((10, 26), (34, 22)), rarm=((-10, 26), (-34, 22)),
                lleg=((-4, 44), (-4, 86)), rleg=((40, 36), (84, 86))),
         '<path d="M196 110 Q190 122 196 126 Q202 122 196 110 Z" fill="#8ecae6"/>']
    return svg(b, "#e9ecef")


def neglected():
    rnd = random.Random(14)
    b = ['<rect y="250" width="400" height="150" fill="#a3a380"/>',
         # broken fence
         '<path d="M10 250 V190 L20 180 L30 190 V250 M60 250 V200 L70 186 L76 196 V250 M150 250 L130 196 L140 186 L156 246 '
         'M330 250 V190 L340 180 L350 190 V250 M370 250 V214 L378 204" fill="#b08968" stroke="#8d6e63" stroke-width="3"/>',
         '<path d="M0 210 H90 M310 212 H400" stroke="#8d6e63" stroke-width="6"/>',
         '<path d="M90 206 L130 230" stroke="#8d6e63" stroke-width="6"/>',
         # the dry, cracked fountain
         '<path d="M120 330 H280 L268 280 H132 Z" fill="#ced4da"/>', '<rect x="114" y="270" width="172" height="14" rx="4" fill="#adb5bd"/>',
         '<rect x="190" y="200" width="20" height="72" fill="#ced4da"/>',
         '<path d="M156 240 Q200 256 244 240 L240 230 H160 Z" fill="#adb5bd"/>',
         '<path d="M150 290 L170 306 L162 320 M240 286 L226 300 L236 316 M196 210 L204 226 L198 240" fill="none" '
         'stroke="#6c757d" stroke-width="3"/>',
         '<path d="M140 276 H260" stroke="#8d6e63" stroke-width="4"/>']
    for _ in range(90):
        x = rnd.uniform(0, 400)
        y0 = rnd.uniform(330, 400)
        h = rnd.uniform(30, 90)
        b.append(f'<path d="M{f(x)} {f(y0)} Q{f(x + rnd.uniform(-10, 10))} {f(y0 - h * .6)} {f(x + rnd.uniform(-16, 16))} '
                 f'{f(y0 - h)}" fill="none" stroke="{rnd.choice(("#6a994e", "#a7c957", "#8a9a5b", "#bc6c25"))}" '
                 'stroke-width="4" stroke-linecap="round"/>')
    b += ['<path d="M360 250 V140 M360 180 L330 150 M360 200 L390 170" stroke="#5c4033" stroke-width="6" '
          'stroke-linecap="round" fill="none"/>',
          '<path d="M30 30 L70 70 M50 30 L50 70 M30 50 H70 M36 36 L64 64" stroke="#adb5bd" stroke-width="1.5" opacity=".0"/>']
    return svg(b, "#cfd8dc")


def inventive():
    b = ['<rect y="330" width="400" height="70" fill="#8d6e63"/>',
         '<rect x="20" y="40" width="160" height="10" fill="#9c6b3c"/>',
         '<circle cx="50" cy="30" r="10" fill="#6c757d"/><circle cx="90" cy="26" r="14" fill="#adb5bd"/>',
         # pedal bike on a stand
         '<path d="M70 330 L90 300 M150 330 L130 300" stroke="#495057" stroke-width="6"/>',
         cyclist(120, 300, "#e76f51", "#2a9d8f", SKIN[1], "#e9c46a", False, 1.2, happy=True),
         # belt from the back wheel to the pump
         '<path d="M66 264 L250 250 M66 300 L250 286" stroke="#343a40" stroke-width="4"/>',
         '<circle cx="250" cy="268" r="18" fill="#adb5bd" stroke="#495057" stroke-width="4"/>',
         '<rect x="240" y="200" width="60" height="130" rx="6" fill="#457b9d"/>',
         '<path d="M300 220 H350 V250" fill="none" stroke="#6c757d" stroke-width="12"/>',
         '<path d="M350 256 Q348 290 356 312" fill="none" stroke="#4895ef" stroke-width="10" stroke-linecap="round"/>',
         '<path d="M330 312 H380 L374 340 H336 Z" fill="#adb5bd"/><ellipse cx="355" cy="312" rx="25" ry="6" fill="#4895ef"/>',
         '<circle cx="190" cy="80" r="18" fill="#ffd166"/><rect x="183" y="96" width="14" height="10" rx="2" fill="#adb5bd"/>',
         sparkle(230, 80, 9, "#ffd166"), sparkle(150, 70, 7, "#ffd166")]
    return svg(b, "#fdf0d5")


def satisfying():
    n, s0, ox, oy = 3, 90, 65, 50
    rnd = random.Random(4)
    right = [[rnd.choice((1, -1)) for _ in range(n)] for _ in range(n)]
    down = [[rnd.choice((1, -1)) for _ in range(n)] for _ in range(n)]

    def edges(c, r):
        return (0 if r == 0 else -down[r - 1][c], 0 if c == n - 1 else right[r][c],
                0 if r == n - 1 else down[r][c], 0 if c == 0 else -right[r][c - 1])
    colors = ("#a8dadc", "#52b788", "#40916c")
    b = ['<rect x="50" y="35" width="300" height="300" rx="10" fill="#d4a373"/>']
    for r in range(n):
        for c in range(n):
            if (c, r) != (2, 2):
                col = "#ffd166" if (c, r) == (2, 0) else colors[r]
                b.append(puzzle_piece(ox + c * s0, oy + r * s0, s0, edges(c, r), col, "#fff", 3))
    b += [f'<g transform="translate(14 -30) rotate(-8 290 290)">'
          f'{puzzle_piece(ox + 2 * s0, oy + 2 * s0, s0, edges(2, 2), colors[2], "#fff", 3)}</g>',
          f'<path d="M400 330 Q360 320 340 300" fill="none" stroke="#457b9d" stroke-width="30" stroke-linecap="round"/>',
          f'<ellipse cx="332" cy="292" rx="22" ry="18" fill="{SKIN[1]}"/>',
          arrow(250, 236, 262, 260, INK, 4, 12),
          sparkle(40, 30, 12, "#ffd166"), sparkle(370, 60, 10, "#ffd166"), sparkle(30, 360, 8, "#ffd166")]
    return svg(b, "#f1faee")


def possessions():
    b = ['<rect y="320" width="400" height="80" fill="#adb5bd"/>',
         # the truck, back open
         '<rect x="20" y="110" width="260" height="200" rx="6" fill="#fff" stroke="#ced4da" stroke-width="4"/>',
         '<rect x="30" y="120" width="240" height="180" fill="#e9ecef"/>',
         '<path d="M280 180 H340 Q370 182 380 230 V300 H280 Z" fill="#e63946"/>',
         '<path d="M292 192 H336 Q356 196 362 230 H292 Z" fill="#caf0f8"/>',
         '<circle cx="90" cy="316" r="24" fill="#343a40"/><circle cx="90" cy="316" r="9" fill="#adb5bd"/>',
         '<circle cx="320" cy="316" r="24" fill="#343a40"/><circle cx="320" cy="316" r="9" fill="#adb5bd"/>',
         # what is inside
         '<rect x="40" y="246" width="110" height="40" rx="10" fill="#457b9d"/><rect x="40" y="226" width="22" height="60" rx="8" '
         'fill="#457b9d"/><rect x="128" y="226" width="22" height="60" rx="8" fill="#457b9d"/>',
         '<rect x="44" y="160" width="50" height="50" fill="#d4a373"/><rect x="100" y="180" width="40" height="40" fill="#c08552"/>',
         '<rect x="50" y="130" width="40" height="30" fill="#c08552"/>',
         '<path d="M64 160 V210 M120 180 V220" stroke="#e9c46a" stroke-width="4"/>',
         '<line x1="200" y1="290" x2="200" y2="170" stroke="#6c757d" stroke-width="4"/>',
         '<path d="M180 170 H220 L210 140 H190 Z" fill="#ffd166"/>',
         '<rect x="186" y="284" width="28" height="6" fill="#6c757d"/>',
         '<g transform="translate(225 285) scale(.45)">' + bicycle("#2a9d8f") + '</g>',
         '<path d="M240 200 V230 M240 210 L226 196 M240 216 L254 202" stroke="#52b788" stroke-width="4" fill="none"/>',
         '<rect x="230" y="230" width="20" height="18" fill="#e76f51"/>']
    return svg(b, "#cfe8f3")


def coincidence():
    outfit = ('<path d="M-28 -140 H28 M-28 -124 H28 M-28 -108 H28 M-28 -92 H28" stroke="#fff" stroke-width="5"/>'
              '<ellipse cx="0" cy="-198" rx="30" ry="6" fill="#264653"/>'
              '<path d="M-18 -198 Q-18 -220 0 -220 Q18 -220 18 -198 Z" fill="#264653"/>')
    b = ['<rect y="320" width="400" height="80" fill="#ced4da"/>',
         '<rect x="0" y="40" width="400" height="280" fill="#f2e9e4"/>',
         '<rect x="190" y="40" width="20" height="280" fill="#adb5bd" opacity=".5"/>',
         '<rect x="196" y="90" width="8" height="232" fill="#495057"/><circle cx="200" cy="86" r="14" fill="#ffd166"/>',
         shadow(110, 334, 36), shadow(290, 334, 36),
         person(110, 332, 1.1, SKIN[0], "#e63946", "#457b9d", "#7f5539", "none", mood="wide",
                larm=((-12, 40), (-14, 72)), rarm=((20, -20), (30, -50)), extra=outfit),
         person(290, 332, 1.1, SKIN[3], "#e63946", "#457b9d", "#1b1b1b", "none", mood="wide",
                larm=((-20, -20), (-30, -50)), rarm=((12, 40), (14, 72)), extra=outfit),
         '<path d="M150 60 l-6 -14 M166 56 v-16 M234 56 v-16 M250 60 l6 -14" stroke="#e76f51" stroke-width="4" '
         'stroke-linecap="round"/>']
    return svg(b, "#f2e9e4")


def impressive():
    b = ['<rect width="400" height="150" fill="#a8dadc"/>',
         '<rect y="150" width="400" height="40" fill="#4895ef"/>', '<rect y="186" width="400" height="214" fill="#f1dca7"/>',
         '<circle cx="60" cy="50" r="24" fill="#ffd166"/>']
    sand, dark = "#e0c48c", "#c9a227"
    for x, y, w, h in ((100, 180, 40, 150), (260, 180, 40, 150), (170, 110, 60, 220), (60, 240, 30, 90), (310, 240, 30, 90)):
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{sand}"/>')
        for k in range(int(w // 12)):
            b.append(f'<rect x="{x + k * 12 + 1}" y="{y - 10}" width="8" height="10" fill="{sand}"/>')
        b.append(f'<line x1="{x + w / 2}" y1="{y - 10}" x2="{x + w / 2}" y2="{y - 40}" stroke="#7f5539" stroke-width="2"/>'
                 f'<polygon points="{x + w / 2},{y - 40} {x + w / 2 + 18},{y - 34} {x + w / 2},{y - 28}" fill="#e63946"/>')
    b += ['<rect x="40" y="260" width="320" height="70" fill="#d4a373"/>',
          '<path d="M180 330 V296 Q200 276 220 296 V330 Z" fill="#9c6b3c"/>',
          '<path d="M140 220 Q150 206 160 220 M240 220 Q250 206 260 220" fill="none" stroke="#9c6b3c" stroke-width="5"/>',
          '<rect x="186" y="160" width="28" height="30" rx="14" fill="#9c6b3c"/>']
    for x, sk, c in ((40, SKIN[0], "#e76f51"), (330, SKIN[3], "#2a9d8f"), (370, SKIN[1], "#e9c46a")):
        b.append(person(x, 380, .42, sk, c, "#457b9d", "#3e2723", "short", mood="wide",
                        larm=((-20, -24), (-30, -54)), rarm=((20, -24), (30, -54))))
    b += [sparkle(140, 90, 10, "#fff"), sparkle(290, 120, 8, "#fff")]
    return svg(b, "#a8dadc")


def latent():
    b = ['<rect y="0" width="400" height="160" fill="#cfe8f3"/>', '<circle cx="330" cy="60" r="28" fill="#ffd166"/>',
         '<rect y="160" width="400" height="20" fill="#6a994e"/>',
         '<rect y="180" width="400" height="220" fill="#7f5539"/>',
         '<rect y="260" width="400" height="140" fill="#6f4518"/>']
    rnd = random.Random(2)
    for _ in range(26):
        x, y = rnd.uniform(0, 400), rnd.uniform(190, 395)
        b.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{rnd.choice((3, 4, 6))}" ry="3" fill="#9c6644"/>')
    b += [# the future plant, not there yet
          '<path d="M200 160 Q196 110 202 60" fill="none" stroke="#2d6a4f" stroke-width="4" stroke-dasharray="8 7"/>',
          '<path d="M200 120 Q170 100 156 112 Q172 132 200 120 Z M202 90 Q236 70 248 84 Q232 104 202 90 Z" fill="none" '
          'stroke="#2d6a4f" stroke-width="3" stroke-dasharray="7 6"/>',
          '<circle cx="202" cy="50" r="16" fill="none" stroke="#2d6a4f" stroke-width="3" stroke-dasharray="7 6"/>',
          # the seed, already sprouting underground
          '<ellipse cx="200" cy="270" rx="26" ry="18" fill="#e9c46a"/>',
          '<path d="M196 256 Q192 226 204 206" fill="none" stroke="#a7c957" stroke-width="5" stroke-linecap="round"/>',
          '<path d="M202 212 Q216 200 224 206 Q214 220 202 212 Z" fill="#a7c957"/>',
          '<path d="M186 284 q-12 14 -26 18 M200 288 q2 16 -4 26 M214 284 q14 12 28 14" fill="none" stroke="#e6ccb2" '
          'stroke-width="3" stroke-linecap="round"/>',
          '<circle cx="200" cy="260" r="56" fill="none" stroke="#ffd166" stroke-width="3" stroke-dasharray="6 6"/>']
    return svg(b, "#cfe8f3")


def momentous():
    rnd = random.Random(10)
    colors = ["#e63946", "#ffd166", "#2a9d8f", "#4895ef", "#f4a261"]
    b = ['<rect y="320" width="400" height="80" fill="#9c6b3c"/>']
    for k in range(9):
        x = 22 + k * 45
        b.append(person(x, 270, .55, SKIN[k % 4], colors[k % 5], "#264653", "#3e2723", "short", mood="grin",
                        larm=((-20, -24), (-30, -54)), rarm=((20, -24), (30, -54))))
    for _ in range(40):
        x, y = rnd.uniform(0, 400), rnd.uniform(0, 160)
        b.append(f'<rect x="{f(x)}" y="{f(y)}" width="8" height="4" fill="{rnd.choice(colors)}" '
                 f'transform="rotate({rnd.randint(0, 180)} {f(x)} {f(y)})"/>')
    b += [person(130, 380, 1.1, SKIN[1], "#343a40", "#343a40", "#adb5bd", "short", mood="grin",
                 larm=((-12, 40), (-14, 72)), rarm=((30, 20), (60, 26)),
                 extra='<path d="M-6 -156 L0 -110 L6 -156 Z" fill="#e63946"/>'),
          person(270, 380, 1.1, SKIN[3], "#264653", "#264653", "#1b1b1b", "short", mood="grin",
                 larm=((-30, 20), (-60, 26)), rarm=((12, 40), (14, 72)),
                 extra='<path d="M-6 -156 L0 -110 L6 -156 Z" fill="#457b9d"/>'),
          '<rect x="186" y="210" width="28" height="22" rx="10" fill="#e0ac69"/>',
          '<rect x="184" y="218" width="32" height="18" rx="9" fill="#8d5524" opacity=".85"/>',
          '<rect x="60" y="292" width="280" height="14" rx="4" fill="#7f5539"/>',
          '<rect x="150" y="270" width="100" height="24" fill="#fff" transform="rotate(-4 200 282)"/>',
          '<path d="M162 284 q10 -10 18 0 t16 0 M210 286 q8 -10 16 0 t14 -2" fill="none" stroke="#264653" stroke-width="2"/>']
    return svg(b, "#fde2c8")


def decorate():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         '<rect x="0" y="320" width="400" height="10" fill="#b08968"/>',
         # paintings already up
         '<rect x="30" y="60" width="70" height="56" fill="#fff" stroke="#e9c46a" stroke-width="4"/>',
         '<circle cx="80" cy="78" r="9" fill="#e63946"/><path d="M34 112 L56 86 L76 112 Z" fill="#52b788"/>',
         '<rect x="290" y="70" width="80" height="60" fill="#fff" stroke="#4895ef" stroke-width="4"/>',
         '<path d="M300 120 Q320 80 340 120 Q350 90 360 120" fill="none" stroke="#f4a261" stroke-width="5"/>',
         # a paper chain across the top
         ]
    for k in range(14):
        x = 10 + k * 28
        y = 24 + 14 * math.sin(k / 13 * math.pi)
        b.append(f'<ellipse cx="{x}" cy="{f(y)}" rx="14" ry="8" fill="none" stroke="{("#e63946", "#ffd166", "#2a9d8f", "#4895ef")[k % 4]}" '
                 'stroke-width="5"/>')
    b += [# a student on a stool hanging a new painting
          '<rect x="140" y="290" width="70" height="12" rx="3" fill="#7f5539"/>',
          '<rect x="148" y="302" width="8" height="30" fill="#6f4518"/><rect x="194" y="302" width="8" height="30" fill="#6f4518"/>',
          person(176, 290, .85, SKIN[2], "#a7c957", "#457b9d", "#1b1b1b", "bun", mood="grin",
                 larm=((-20, -36), (-26, -70)), rarm=((20, -36), (26, -70))),
          '<rect x="138" y="44" width="84" height="62" fill="#fff" stroke="#e76f51" stroke-width="4" '
          'transform="rotate(-4 180 75)"/>',
          '<circle cx="166" cy="68" r="11" fill="#ffd166"/><path d="M148 100 Q180 74 212 98" fill="#4895ef"/>',
          shadow(300, 334, 30),
          person(300, 332, .85, SKIN[0], "#e76f51", "#264653", "#7f5539", "short", mood="smile",
                 larm=((-20, -10), (-40, -24)), rarm=((12, 40), (14, 72)))]
    for k in range(6):
        t = k / 5
        x, y = 246 - 8 * k, 186 - 24 * k + 6 * math.sin(t * math.pi)
        b.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="8" ry="13" fill="none" '
                 f'stroke="{("#e63946", "#ffd166", "#2a9d8f")[k % 3]}" stroke-width="4"/>')
    b += []
    return svg(b, "#fdf6ec")


def fuse():
    b = ['<rect y="300" width="400" height="100" fill="#6c757d"/>',
         '<ellipse cx="200" cy="300" rx="200" ry="40" fill="#f4a261" opacity=".25"/>',
         # two rods carrying hot glass into one another
         '<line x1="0" y1="220" x2="150" y2="200" stroke="#adb5bd" stroke-width="8" stroke-linecap="round"/>',
         '<line x1="400" y1="180" x2="250" y2="200" stroke="#adb5bd" stroke-width="8" stroke-linecap="round"/>',
         '<ellipse cx="200" cy="200" rx="90" ry="64" fill="#ffd166" opacity=".35"/>',
         '<circle cx="168" cy="200" r="42" fill="#f77f00"/>',
         '<circle cx="232" cy="200" r="42" fill="#e63946"/>',
         '<path d="M200 168 Q186 200 200 232 Q214 200 200 168 Z" fill="#ffd166"/>',
         '<ellipse cx="154" cy="182" rx="12" ry="7" fill="#ffd166"/>',
         arrow(40, 160, 100, 152, "#ffd166", 5, 14), arrow(360, 132, 300, 140, "#ffd166", 5, 14),
         sparkle(200, 120, 12, "#ffd166"), sparkle(150, 270, 8, "#ffd166"), sparkle(260, 266, 9, "#ffd166"),
         '<path d="M190 110 l-8 -14 M212 110 l8 -14" stroke="#ffd166" stroke-width="3" stroke-linecap="round"/>']
    return svg(b, "#3d405b")


def carrying():
    rnd = random.Random(3)
    colors = ["#e63946", "#2a9d8f", "#ffd166", "#4895ef", "#f4a261", "#6a994e"]
    b = ['<rect y="250" width="400" height="150" fill="#457b9d"/>',
         '<circle cx="70" cy="70" r="28" fill="#ffd166"/>',
         '<path d="M20 290 L380 290 L350 340 H60 Z" fill="#264653"/>',
         '<rect x="20" y="284" width="360" height="10" fill="#e63946"/>',
         '<rect x="300" y="200" width="54" height="84" fill="#fff"/>',
         '<rect x="308" y="212" width="38" height="12" fill="#a8dadc"/>',
         '<rect x="318" y="176" width="14" height="26" fill="#e76f51"/>']
    for r in range(4):
        for c in range(6):
            x, y = 40 + c * 42, 254 - r * 26
            if r == 3 and c in (0, 5):
                continue
            b.append(f'<rect x="{x}" y="{y}" width="40" height="24" fill="{rnd.choice(colors)}"/>'
                     f'<path d="M{x + 10} {y + 3} V{y + 21} M{x + 20} {y + 3} V{y + 21} M{x + 30} {y + 3} V{y + 21}" '
                     'stroke="#000" stroke-width="1.5" opacity=".2"/>')
    b += ['<path d="M0 340 Q50 330 100 340 T200 340 T300 340 T400 340 V400 H0 Z" fill="#4895ef"/>',
          '<path d="M0 370 Q50 360 100 370 T200 370 T300 370 T400 370" fill="none" stroke="#a8dadc" stroke-width="4"/>']
    return svg(b, "#cfe8f3")


def awkward():
    b = ['<rect y="330" width="400" height="70" fill="#e9d8c4"/>', shadow(130, 334, 36), shadow(270, 334, 36),
         person(130, 332, 1.1, SKIN[0], "#457b9d", "#264653", "#7f5539", "short", mood="shut",
                brows="M-14 -188 L-4 -192 M4 -192 L14 -188",
                larm=((-12, 40), (-14, 72)), rarm=((30, 20), (60, 20)),
                extra='<circle cx="-14" cy="-170" r="5" fill="#e5989b" opacity=".9"/>'
                      '<circle cx="14" cy="-170" r="5" fill="#e5989b" opacity=".9"/>'),
         person(270, 332, 1.1, SKIN[3], "#e9c46a", "#457b9d", "#1b1b1b", "bun", mood="shut",
                brows="M-14 -188 L-4 -192 M4 -192 L14 -188",
                larm=((-40, -6), (-64, -30)), rarm=((40, -6), (64, -30)),
                extra='<circle cx="-14" cy="-170" r="5" fill="#e5989b" opacity=".9"/>'
                      '<circle cx="14" cy="-170" r="5" fill="#e5989b" opacity=".9"/>'),
         '<path d="M104 100 Q98 112 104 116 Q110 112 104 100 Z" fill="#8ecae6"/>',
         '<path d="M300 90 Q294 102 300 106 Q306 102 300 90 Z" fill="#8ecae6"/>']
    return svg(b, "#f2e9e4")


def butterfly(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<ellipse cx="-14" cy="-10" rx="16" ry="12" fill="#f4a261" transform="rotate(-20 -14 -10)"/>'
            '<ellipse cx="14" cy="-10" rx="16" ry="12" fill="#f4a261" transform="rotate(20 14 -10)"/>'
            '<ellipse cx="-10" cy="10" rx="10" ry="8" fill="#e76f51"/><ellipse cx="10" cy="10" rx="10" ry="8" fill="#e76f51"/>'
            f'<ellipse cx="0" cy="0" rx="3" ry="16" fill="{INK}"/>'
            f'<path d="M0 -14 l-6 -10 M0 -14 l6 -10" stroke="{INK}" stroke-width="2"/></g>')


def elusive():
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>', '<circle cx="60" cy="56" r="26" fill="#ffd166"/>',
         bush(380, 296, 30),
         '<path d="M60 220 C 120 120, 200 220, 250 140 S 320 60, 340 110" fill="none" stroke="#6c757d" stroke-width="3" '
         'stroke-dasharray="8 8"/>',
         butterfly(346, 100, 1.4),
         shadow(140, 334, 40),
         person(140, 332, 1.05, SKIN[1], "#e76f51", "#457b9d", "#5c4033", "short", mood="wide", rot=10,
                larm=((-12, 40), (-14, 72)), rarm=((30, -20), (50, -50)),
                lleg=((-14, 40), (-26, 80)), rleg=((14, 40), (26, 80))),
         '<line x1="204" y1="160" x2="270" y2="110" stroke="#9c6b3c" stroke-width="6" stroke-linecap="round"/>',
         '<ellipse cx="290" cy="100" rx="26" ry="20" fill="#fff" opacity=".6" stroke="#adb5bd" stroke-width="3" '
         'transform="rotate(-36 290 100)"/>',
         '<path d="M318 120 l8 -6 M322 134 l10 -2" stroke="#6c757d" stroke-width="3" stroke-linecap="round"/>']
    return svg(b, "#cfe8f3")


def involuntarily():
    b = ['<rect y="330" width="400" height="70" fill="#ced4da"/>',
         # exam table
         '<rect x="40" y="250" width="180" height="20" rx="6" fill="#4895ef"/>',
         '<rect x="50" y="270" width="12" height="62" fill="#6c757d"/><rect x="196" y="270" width="12" height="62" fill="#6c757d"/>',
         # the patient, side on, sitting at the edge
         limb(((120, 246), (128, 172)), "#e9c46a", 30),
         limb(((128, 176), (160, 210), (180, 196)), "#e9c46a", 11), f'<circle cx="182" cy="194" r="6" fill="{SKIN[0]}"/>',
         f'<circle cx="134" cy="146" r="22" fill="{SKIN[0]}"/>',
         '<path d="M112 146 Q110 120 134 122 Q154 122 156 140 Q140 132 120 150 Z" fill="#7f5539"/>',
         '<circle cx="146" cy="142" r="5" fill="#fff"/><circle cx="147" cy="142" r="2.5" fill="#264653"/>',
         '<ellipse cx="148" cy="158" rx="4" ry="5" fill="#264653"/>',
         limb(((120, 246), (208, 248)), "#457b9d", 18),
         '<path d="M208 248 L234 296" stroke="#457b9d" stroke-width="16" stroke-linecap="round" stroke-dasharray="4 8" '
         'opacity=".35"/>',
         limb(((208, 248), (244, 196)), "#457b9d", 16), f'<ellipse cx="250" cy="188" rx="14" ry="7" fill="{INK}" '
         'transform="rotate(-55 250 188)"/>',
         '<path d="M262 168 l12 -10 M270 186 l16 -4 M250 160 l4 -14" stroke="#e76f51" stroke-width="4" stroke-linecap="round"/>',
         arc_arrow(208, 248, 62, 70, -40, "#2a9d8f", 4, 12),
         # the doctor with the reflex hammer
         shadow(348, 334, 34),
         person(348, 332, 1.05, SKIN[3], "#fff", "#264653", "#1b1b1b", "short", mood="smile",
                larm=((-46, 50), (-94, 79)), rarm=((12, 40), (14, 72))),
         '<line x1="250" y1="262" x2="222" y2="252" stroke="#6c757d" stroke-width="5" stroke-linecap="round"/>',
         '<polygon points="212,242 226,246 216,260" fill="#e63946"/>']
    return svg(b, "#e3f2fd")


def reflect():
    hills = ('<polygon points="0,200 70,90 120,150 190,50 260,140 310,80 400,190 400,200" fill="#6d597a"/>'
             '<polygon points="190,50 216,84 200,90 190,80 176,94 166,86" fill="#fff"/>'
             '<polygon points="70,90 88,118 76,116 70,108 60,118 56,112" fill="#fff"/>'
             '<polygon points="310,80 330,108 316,110 310,100 300,112 294,104" fill="#fff"/>'
             + pine(30, 200, 50, "#2d6a4f") + pine(370, 200, 56, "#2d6a4f") + pine(340, 200, 40, "#2d6a4f"))
    b = ['<rect width="400" height="200" fill="#bde0fe"/>', '<circle cx="90" cy="40" r="20" fill="#fff3b0"/>',
         hills,
         '<rect y="200" width="400" height="200" fill="#a8dadc"/>',
         f'<g transform="translate(0 400) scale(1 -1)" opacity=".55">{hills}<circle cx="90" cy="40" r="20" fill="#fff3b0"/></g>',
         '<path d="M40 240 H120 M220 260 H330 M80 320 H180 M250 350 H350" stroke="#fff" stroke-width="3" '
         'stroke-linecap="round" opacity=".7"/>',
         '<path d="M0 200 H400" stroke="#fff" stroke-width="3" opacity=".8"/>']
    return svg(b, "#bde0fe")


PICTURES = {
    "repetitive": repetitive,
    "ubiquitous": ubiquitous,
    "complaining": complaining,
    "aggressive": aggressive,
    "managed": managed,
    "physical": physical,
    "adapt to": adapt_to,
    "agree with": agree_with,
    "adjusted": adjusted,
    "convenient": convenient,
    "prediction": prediction,
    "urge": urge,
    "perceive": perceive,
    "staged": staged,
    "arduous": arduous,
    "overwhelmed": overwhelmed,
    "protective": protective,
    "predictable": predictable,
    "ignored": ignored,
    "avoided": avoided,
    "impractical": impractical,
    "despise": despise,
    "provide": provide,
    "overlook": overlook,
    "creativity": creativity,
    "excited about": excited_about,
    "recollect": recollect,
    "accurate": accurate,
    "inadvertently": inadvertently,
    "persist": persist,
    "replace": replace,
    "clinging to": clinging_to,
    "blamed": blamed,
    "gathering": gathering,
    "hesitant": hesitant,
    "neglected": neglected,
    "inventive": inventive,
    "satisfying": satisfying,
    "possessions": possessions,
    "coincidence": coincidence,
    "impressive": impressive,
    "latent": latent,
    "momentous": momentous,
    "decorate": decorate,
    "fuse": fuse,
    "carrying": carrying,
    "awkward": awkward,
    "elusive": elusive,
    "involuntarily": involuntarily,
    "reflect": reflect,
}
