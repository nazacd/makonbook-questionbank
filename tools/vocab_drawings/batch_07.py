"""Batch 7: drawings 281-330 (each function returns one SVG; PICTURES maps word -> function).

The figures and small shapes come from batch_01.py to batch_06.py.
"""

import math
import random

from batch_01 import bird
from batch_02 import SKIN, heart, limb, monkey, person, shadow, sparkle
from batch_03 import dog
from batch_04 import barking_dog, pointing_arm
from batch_05 import hard_hat
from batch_06 import back_view, crossed_arms, note, painting
from common import INK, arrow, bush, f, svg


def amusing():
    b = ['<rect y="320" width="400" height="80" fill="#d4a373"/>',
         dog(110, 334, 1.0),
         # the sock stuck over its head
         '<path d="M100 228 L106 122 Q106 98 130 98 H214 Q238 98 238 117 Q238 136 214 136 H174 L180 228 Z" fill="#4895ef"/>',
         '<path d="M106 136 L106 122 Q106 98 130 98 H136 Q120 110 126 136 Z" fill="#e63946"/>',
         '<path d="M214 98 Q238 98 238 117 Q238 136 214 136 Q224 117 214 98 Z" fill="#e63946"/>',
         '<path d="M101 204 L179 204 L180 228 L100 228 Z" fill="#e9ecef"/>',
         '<path d="M112 206 V226 M124 206 V226 M136 206 V226 M148 206 V226 M160 206 V226 M172 206 V226" stroke="#ced4da" stroke-width="3"/>',
         '<path d="M40 250 l-10 -6 M40 266 l-12 0" stroke="#adb5bd" stroke-width="4" stroke-linecap="round"/>',
         shadow(232, 344, 20),
         person(232, 342, .62, SKIN[1], "#ffd166", "#264653", "#5c4033", "bun", mood="grin",
                larm=((-12, 40), (-16, 72)), rarm=((-4, 36), (-20, 60))),
         shadow(296, 344, 28),
         person(296, 342, 1.0, SKIN[1], "#e76f51", "#264653", "#5c4033", "short", mood="grin",
                larm=((-30, -14), (-60, -24)), rarm=((-4, 36), (-20, 58))),
         shadow(362, 344, 26),
         person(362, 342, .95, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "bun", mood="grin", long_hair=True,
                larm=((10, 36), (24, 58)), rarm=((-4, 36), (-20, 58))),
         sparkle(270, 70, 9, "#ffd166"), sparkle(330, 96, 11, "#ffd166"), sparkle(60, 120, 8, "#ffd166")]
    return svg(b, "#fdf0d5")


def frond(x, y, ang, length, open_=True, n=6):
    a = math.radians(ang)
    ex, ey = x + length * math.cos(a), y + length * math.sin(a)
    out = [f'<path d="M{f(x)} {f(y)} L{f(ex)} {f(ey)}" stroke="#40916c" stroke-width="3"/>']
    for k in range(1, n + 1):
        t = k / (n + .5)
        px, py = x + (ex - x) * t, y + (ey - y) * t
        for side in (-1, 1):
            if open_:
                rot = ang + side * 70
                d = 9
            else:
                rot = ang + side * 12
                d = 3
            r = math.radians(ang + side * 90)
            cx, cy = px + d * math.cos(r), py + d * math.sin(r)
            out.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="9" ry="4" fill="{"#52b788" if open_ else "#74c69d"}" '
                       f'transform="rotate({f(rot)} {f(cx)} {f(cy)})"/>')
    return "".join(out)


def sensitive():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         '<path d="M150 340 Q146 240 170 140" fill="none" stroke="#40916c" stroke-width="6"/>',
         frond(152, 300, 200, 90), frond(150, 260, -150, 96), frond(156, 216, 196, 92),
         frond(162, 180, -160, 84), frond(168, 150, -60, 80), frond(160, 236, -10, 90),
         frond(166, 190, 30, 100, open_=False),
         '<path d="M118 352 H186 L178 400 H126 Z" fill="#bc6c25"/><rect x="112" y="340" width="80" height="14" rx="3" fill="#bc6c25"/>',
         pointing_arm(410, 226, 296, 236, "#457b9d", SKIN[1]),
         '<path d="M240 196 l8 -12 M258 206 l14 -6 M226 186 l2 -14" stroke="#e76f51" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#e8f5e9")


def detects():
    b = ['<rect width="400" height="34" fill="#dee2e6"/>',
         '<rect y="300" width="400" height="100" fill="#d4a373"/>',
         '<rect y="292" width="400" height="12" fill="#b08968"/>',
         # the toaster with its burnt toast
         '<rect x="56" y="230" width="100" height="64" rx="16" fill="#adb5bd"/>',
         '<rect x="72" y="206" width="26" height="34" rx="5" fill="#3d2c2e"/><rect x="112" y="206" width="26" height="34" rx="5" fill="#3d2c2e"/>',
         '<rect x="56" y="244" width="100" height="10" fill="#8d99ae"/>']
    for k, (x, y, r) in enumerate(((104, 186, 14), (118, 160, 18), (136, 132, 22), (158, 104, 24), (178, 78, 22))):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#adb5bd" opacity="{f(.75 - k * .08)}"/>')
    b += ['<rect x="176" y="34" width="48" height="10" fill="#ced4da"/>',
          '<ellipse cx="200" cy="50" rx="56" ry="16" fill="#f8f9fa" stroke="#ced4da" stroke-width="3"/>',
          '<circle cx="224" cy="52" r="7" fill="#e63946"/>',
          '<circle cx="224" cy="52" r="18" fill="#e63946" opacity=".25"/>',
          '<path d="M262 50 h20 M256 70 l14 12 M228 78 l2 18 M144 70 l-14 12" stroke="#e63946" stroke-width="5" '
          'stroke-linecap="round"/>']
    return svg(b, "#f1faee")


def regret():
    b = ['<rect y="320" width="400" height="80" fill="#b08968"/>',
         '<rect x="30" y="200" width="110" height="12" fill="#7f5539"/><path d="M44 212 V320 M126 212 V320" stroke="#7f5539" stroke-width="8"/>',
         '<ellipse cx="200" cy="336" rx="74" ry="10" fill="#a8dadc"/>',
         '<path d="M176 340 Q164 320 172 300 L182 290 L190 302 L200 286 L210 300 L220 290 L228 300 Q236 320 224 340 Z" fill="#4895ef"/>',
         '<path d="M170 312 H230" stroke="#fff" stroke-width="5"/>',
         '<path d="M136 342 Q132 322 146 312 L156 326 L150 342 Z" fill="#4895ef"/>',
         '<path d="M246 340 Q252 318 270 314 L268 332 L258 342 Z" fill="#4895ef"/>',
         '<path d="M148 318 L154 326 M254 322 L266 320" stroke="#fff" stroke-width="4"/>',
         '<path d="M196 262 Q192 276 200 282 L206 270 Z" fill="#4895ef"/>',
         '<path d="M120 334 Q140 320 170 326" fill="none" stroke="#40916c" stroke-width="4"/>',
         '<path d="M240 340 Q260 324 280 330" fill="none" stroke="#40916c" stroke-width="4"/>',
         '<circle cx="118" cy="332" r="9" fill="#e63946"/><circle cx="282" cy="330" r="9" fill="#ffd166"/>',
         shadow(320, 334, 30),
         person(320, 332, 1.05, SKIN[0], "#6d597a", "#264653", "#5c4033", "side", mood="frown",
                brows="M-14 -188 L-3 -193 M3 -193 L14 -188",
                larm=((-14, 40), (-18, 72)), rarm=((10, -30), (-6, -58)))]
    return svg(b, "#e9ecef")


def visible():
    rnd = random.Random(5)
    b = []
    for _ in range(50):
        b.append(f'<circle cx="{f(rnd.uniform(0, 400))}" cy="{f(rnd.uniform(0, 280))}" r="{f(rnd.uniform(1, 2))}" '
                 'fill="#fff" opacity=".6"/>')
    b += ['<circle cx="300" cy="90" r="40" fill="#ffd166" opacity=".18"/>',
          '<circle cx="300" cy="90" r="26" fill="#ffd166" opacity=".3"/>',
          '<circle cx="300" cy="90" r="15" fill="#fff3b0"/>',
          sparkle(300, 90, 34, "#fff3b0").replace('/>', ' opacity=".7"/>'),
          '<path d="M0 320 Q120 270 260 300 T400 290 V400 H0 Z" fill="#2d6a4f"/>',
          shadow(130, 312, 28),
          person(130, 310, .95, SKIN[2], "#e9c46a", "#264653", "#1b1b1b", "bun", mood="grin",
                 larm=((-12, 40), (-16, 72)), rarm=((26, -40), (56, -84)))]
    return svg(b, "#14213d")


def food_truck(x, y, w, color, open_=True):
    """A food truck parked with its wheels on y, serving hatch facing us; left edge x."""
    return (f'<rect x="{x}" y="{y - 130}" width="{w}" height="110" rx="10" fill="{color}"/>'
            f'<rect x="{x + w - 40}" y="{y - 100}" width="40" height="80" rx="8" fill="{color}"/>'
            f'<rect x="{x + w - 34}" y="{y - 94}" width="26" height="26" rx="4" fill="#caf0f8"/>'
            f'<rect x="{x + 14}" y="{y - 110}" width="{w - 70}" height="46" fill="#264653"/>'
            + (f'<path d="M{x + 6} {y - 112} H{x + w - 50} L{x + w - 44} {y - 96} H{x} Z" fill="#fff"/>' if open_ else "")
            + f'<rect x="{x + 8}" y="{y - 64}" width="{w - 58}" height="8" fill="#e9ecef"/>'
            f'<circle cx="{x + 34}" cy="{y - 18}" r="16" fill="#343a40"/><circle cx="{x + w - 30}" cy="{y - 18}" r="16" fill="#343a40"/>'
            f'<circle cx="{x + 34}" cy="{y - 18}" r="6" fill="#adb5bd"/><circle cx="{x + w - 30}" cy="{y - 18}" r="6" fill="#adb5bd"/>')


def popularity():
    b = ['<rect y="250" width="400" height="150" fill="#ced4da"/>',
         food_truck(10, 252, 150, "#adb5bd", open_=False),
         f'<circle cx="60" cy="168" r="14" fill="{SKIN[0]}"/><path d="M48 170 H72" stroke="{INK}" stroke-width="2"/>'
         f'<circle cx="55" cy="164" r="2" fill="{INK}"/><circle cx="65" cy="164" r="2" fill="{INK}"/>',
         food_truck(220, 252, 170, "#e76f51"),
         f'<circle cx="272" cy="168" r="14" fill="{SKIN[2]}"/><path d="M264 172 Q272 178 280 172" fill="none" stroke="{INK}" stroke-width="2"/>'
         f'<circle cx="267" cy="164" r="2" fill="{INK}"/><circle cx="277" cy="164" r="2" fill="{INK}"/>',
         heart(250, 76, 12), heart(300, 60, 9, "#e76f51"), heart(340, 84, 11),
         sparkle(370, 50, 9, "#ffd166")]
    line = ((262, 300, SKIN[0], "#457b9d"), (236, 314, SKIN[3], "#2a9d8f"), (210, 326, SKIN[1], "#e9c46a"),
            (184, 338, SKIN[2], "#bc4749"), (158, 350, SKIN[0], "#6a994e"), (132, 362, SKIN[3], "#f4a261"),
            (106, 374, SKIN[1], "#7209b7"), (80, 386, SKIN[2], "#4895ef"), (54, 398, SKIN[0], "#e63946"))
    for x, y, sk, shirt in line:
        b.append(person(x, y, .52, sk, shirt, "#264653", "#5c4033", "short", mood="smile"))
    return svg(b, "#e3f2fd")


def melodic():
    b = ['<path d="M0 330 Q100 280 200 320 T400 300 V400 H0 Z" fill="#95d5b2"/>',
         '<path d="M0 360 Q140 320 260 356 T400 350 V400 H0 Z" fill="#52b788"/>',
         '<path d="M0 260 Q80 250 150 262 L190 250" fill="none" stroke="#7f5539" stroke-width="12" stroke-linecap="round"/>',
         '<ellipse cx="172" cy="244" rx="12" ry="6" fill="#52b788" transform="rotate(-30 172 244)"/>',
         bird(110, 254, "#e76f51", "#bc4749", k=2.6),
         '<polygon points="152,190 170,196 152,200" fill="#f4a261"/>',
         '<path d="M170 190 Q220 150 260 170 T340 120 T400 90" fill="none" stroke="#ffd166" stroke-width="3" '
         'stroke-dasharray="2 8" stroke-linecap="round"/>',
         note(204, 168, "#2a9d8f"), note(250, 152, "#7209b7", 1.2), note(296, 140, "#e76f51"), note(346, 104, "#2a9d8f", 1.1),
         sparkle(320, 190, 8, "#ffd166"), sparkle(230, 100, 7, "#ffd166")]
    return svg(b, "#fff1e6")


def sandwich_half(x, y, rot=0, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({k})">'
            '<polygon points="-22,14 22,14 -22,-22" fill="#e9c46a"/>'
            '<polygon points="-18,10 14,10 -18,-16" fill="#fff3b0"/>'
            '<path d="M-18 4 L6 4" stroke="#52b788" stroke-width="4"/><path d="M-18 -2 L-2 -2" stroke="#e63946" stroke-width="4"/></g>')


def generous():
    b = ['<rect y="330" width="400" height="70" fill="#a7c957"/>',
         shadow(120, 344, 28),
         person(120, 342, 1.0, SKIN[2], "#e76f51", "#264653", "#1b1b1b", "bun", mood="grin",
                larm=((-12, 30), (-6, 50)), rarm=((30, 0), (62, -6))),
         sandwich_half(210, 186, -20),
         '<rect x="20" y="300" width="60" height="34" rx="4" fill="#e76f51"/>',
         '<rect x="26" y="306" width="48" height="22" fill="#e9ecef"/>',
         '<path d="M20 300 L28 270 H80 L80 300 Z" fill="#f4a261"/>',
         sandwich_half(50, 312, 0, .7),
         shadow(290, 344, 28),
         person(290, 342, .95, SKIN[0], "#4895ef", "#264653", "#e9c46a", "short", mood="grin",
                larm=((-30, 0), (-60, -6)), rarm=((12, 40), (16, 72))),
         f'<circle cx="230" cy="192" r="8" fill="{SKIN[0]}"/>',
         # the empty lunchbox
         '<rect x="330" y="300" width="60" height="34" rx="4" fill="#2a9d8f"/>',
         '<rect x="336" y="306" width="48" height="22" fill="#e9ecef"/>',
         '<path d="M330 300 L338 270 H390 L390 300 Z" fill="#52b788"/>',
         heart(200, 120, 14), heart(240, 96, 9, "#ff8fab")]
    return svg(b, "#fefae0")


def simulate():
    rnd = random.Random(9)
    b = ['<rect y="320" width="400" height="80" fill="#22223b"/>',
         '<rect x="20" y="24" width="360" height="190" rx="10" fill="#495057"/>',
         '<rect x="30" y="34" width="340" height="170" fill="#4a5568"/>',
         '<path d="M30 160 L370 130 V204 H30 Z" fill="#2d6a4f"/>',
         '<ellipse cx="120" cy="60" rx="110" ry="36" fill="#2b2d42"/><ellipse cx="290" cy="56" rx="110" ry="34" fill="#343a40"/>',
         '<polygon points="230,70 210,112 226,112 206,156 254,98 236,98 252,70" fill="#ffd166"/>']
    for _ in range(26):
        x, y = rnd.uniform(36, 360), rnd.uniform(90, 190)
        b.append(f'<path d="M{f(x)} {f(y)} l-6 14" stroke="#90e0ef" stroke-width="2.5" stroke-linecap="round"/>')
    b += ['<path d="M120 34 V204 M280 34 V204" stroke="#495057" stroke-width="6"/>',
          '<rect x="10" y="212" width="380" height="70" rx="8" fill="#343a40"/>']
    for x in (60, 110, 290, 340):
        b.append(f'<circle cx="{x}" cy="244" r="17" fill="#212529" stroke="#adb5bd" stroke-width="3"/>'
                 f'<path d="M{x} 244 l9 -9" stroke="#52b788" stroke-width="3" stroke-linecap="round"/>')
    b += ['<rect x="170" y="226" width="60" height="36" rx="4" fill="#4895ef" opacity=".6"/>',
          back_view(200, 400, 1.3, "#457b9d", "#5c4033", SKIN[1]),
          '<path d="M172 286 Q200 256 228 286" fill="none" stroke="#212529" stroke-width="6"/>',
          '<rect x="162" y="280" width="12" height="22" rx="5" fill="#212529"/><rect x="226" y="280" width="12" height="22" rx="5" fill="#212529"/>',
          '<path d="M150 392 Q150 380 160 380 H170" fill="none" stroke="#343a40" stroke-width="10"/>',
          '<path d="M30 320 L10 400 M370 320 L390 400" stroke="#6c757d" stroke-width="10"/>']
    return svg(b, "#2b2d42")


def demonstrate():
    b = ['<rect y="300" width="400" height="100" fill="#d4a373"/>',
         '<rect x="40" y="30" width="320" height="110" fill="#2d6a4f" stroke="#9c6644" stroke-width="8"/>',
         shadow(80, 304, 26),
         person(80, 302, .85, SKIN[3], "#4895ef", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-12, 40), (-16, 72)), rarm=((30, 0), (60, 4))),
         shadow(330, 304, 26),
         person(330, 302, .85, SKIN[0], "#e9c46a", "#264653", "#bc6c25", "bun", mood="wide",
                larm=((-30, -10), (-50, -40)), rarm=((12, 40), (16, 72))),
         '<rect x="120" y="250" width="170" height="14" fill="#9c6644"/><path d="M134 264 V320 M276 264 V320" stroke="#7f5539" stroke-width="8"/>',
         # the volcano and its foam
         '<polygon points="148,250 262,250 222,170 188,170" fill="#9c6644"/>',
         '<polygon points="188,170 222,170 214,184 196,184" fill="#7f5539"/>',
         '<path d="M188 172 Q178 196 170 214 Q164 226 174 226 Q182 214 192 196 Q196 216 204 214 Q206 200 214 190 '
         'Q222 214 232 228 Q242 230 238 216 Q230 196 222 172 Z" fill="#e63946"/>',
         '<circle cx="194" cy="164" r="14" fill="#e63946"/><circle cx="214" cy="158" r="16" fill="#f4a261"/>'
         '<circle cx="202" cy="142" r="12" fill="#e63946"/><circle cx="222" cy="136" r="9" fill="#f4a261"/>'
         '<circle cx="184" cy="146" r="8" fill="#f4a261"/>'
         '<circle cx="208" cy="150" r="4" fill="#fff" opacity=".6"/><circle cx="192" cy="160" r="3" fill="#fff" opacity=".6"/>',
         sparkle(250, 110, 8, "#ffd166"), sparkle(160, 120, 7, "#ffd166"),
         back_view(100, 410, .9, "#6a994e", "#5c4033", SKIN[1]),
         back_view(200, 410, .9, "#e76f51", "#1b1b1b", SKIN[3], bun=True),
         back_view(300, 410, .9, "#457b9d", "#e9c46a", SKIN[0])]
    return svg(b, "#e9ecef")


def organized():
    b = ['<rect y="270" width="400" height="130" fill="#b08968"/>',
         '<rect y="262" width="400" height="14" fill="#9c6644"/>']
    for r in range(2):
        for c in range(4):
            col = ("#ffd166", "#90e0ef", "#ff8fab", "#b7e4c7")[(r + c) % 4]
            b.append(f'<rect x="{224 + c * 38}" y="{40 + r * 38}" width="30" height="30" fill="{col}"/>')
    for k, col in enumerate(("#e63946", "#f4a261", "#ffd166", "#52b788", "#4895ef", "#7209b7")):
        b.append(f'<rect x="{42 + k * 18}" y="{176 + (k % 2) * 4}" width="14" height="{86 - (k % 2) * 4}" fill="{col}"/>')
    b += ['<path d="M36 262 V196 H156 V262" fill="none" stroke="#6c757d" stroke-width="6"/>',
          '<rect x="180" y="210" width="36" height="52" fill="#457b9d"/>']
    for k, col in enumerate(("#e63946", "#ffd166", "#2a9d8f", "#4895ef")):
        x = 186 + k * 8
        b.append(f'<rect x="{x}" y="176" width="6" height="40" fill="{col}"/><polygon points="{x},176 {x + 6},176 {x + 3},168" fill="#f4d58d"/>')
    for k in range(5):
        b.append(f'<rect x="236" y="{252 - k * 7}" width="70" height="6" fill="#fff" stroke="#dee2e6" stroke-width="1"/>')
    b += ['<rect x="234" y="216" width="74" height="8" fill="#e9c46a"/>',
          '<path d="M370 262 V160 L330 120" fill="none" stroke="#495057" stroke-width="6" stroke-linejoin="round"/>',
          '<polygon points="314,104 346,118 334,142 300,128" fill="#2a9d8f"/>',
          '<rect x="320" y="254" width="70" height="8" fill="#ffd166"/>',
          '<rect x="0" y="300" width="400" height="6" fill="#9c6644"/>',
          '<rect x="40" y="316" width="150" height="60" fill="#9c6644"/><rect x="210" y="316" width="150" height="60" fill="#9c6644"/>',
          '<rect x="100" y="340" width="30" height="8" rx="3" fill="#ffd166"/><rect x="270" y="340" width="30" height="8" rx="3" fill="#ffd166"/>',
          sparkle(176, 110, 10, "#ffd166"), sparkle(380, 60, 8, "#ffd166")]
    return svg(b, "#f1faee")


def carefully():
    rnd = random.Random(12)
    b = ['<rect y="200" width="400" height="200" fill="#bc6c25"/>',
         '<rect x="40" y="214" width="320" height="170" fill="#9c6644"/>',
         '<path d="M40 214 H360" stroke="#7f5539" stroke-width="4"/>',
         '<path d="M146 214 V384 M253 214 V384 M40 298 H360" stroke="#fff" stroke-width="1.5" opacity=".7"/>',
         # the pot, half out of the earth
         '<path d="M240 360 Q220 330 232 300 Q240 284 256 280 V266 H284 V280 Q300 284 308 300 Q320 330 300 360 Z" fill="#e76f51"/>',
         '<path d="M234 306 H306" stroke="#f4a261" stroke-width="6"/>',
         '<circle cx="246" cy="322" r="3.5" fill="#7f5539"/><circle cx="262" cy="322" r="3.5" fill="#7f5539"/>'
         '<circle cx="278" cy="322" r="3.5" fill="#7f5539"/><circle cx="294" cy="322" r="3.5" fill="#7f5539"/>',
         '<path d="M40 340 Q140 330 220 334 Q270 326 360 336 V384 H40 Z" fill="#7f5539"/>']
    for _ in range(10):
        b.append(f'<circle cx="{f(rnd.uniform(250, 300))}" cy="{f(rnd.uniform(240, 270))}" r="2" fill="#d4a373"/>')
    b += [person(150, 395, .9, SKIN[1], "#6a994e", "#7f5539", "#5c4033", "short", mood="down",
                 lleg=((-2, 44), (-40, 46)), rleg=((30, 6), (34, 46)),
                 larm=((10, 40), (20, 60)), rarm=((30, 20), (66, 40)),
                 extra='<ellipse cx="0" cy="-196" rx="38" ry="8" fill="#e9d8a6"/>'
                       '<path d="M-22 -196 Q-22 -222 0 -222 Q22 -222 22 -196 Z" fill="#e9d8a6"/>'),
          '<rect x="212" y="282" width="34" height="8" rx="3" fill="#7f5539" transform="rotate(30 228 286)"/>',
          '<path d="M244 296 l10 6 M246 290 l12 2 M246 302 l8 8" stroke="#e9c46a" stroke-width="4" stroke-linecap="round"/>',
          f'<circle cx="219" cy="300" r="8" fill="{SKIN[1]}"/>',
          '<path d="M330 172 H380 L372 200 H338 Z" fill="#6c757d"/>',
          '<path d="M332 174 Q355 146 378 174" fill="none" stroke="#495057" stroke-width="3"/>']
    return svg(b, "#e3f2fd")


def startle():
    b = ['<rect y="300" width="400" height="100" fill="#d4a373"/>',
         '<rect x="70" y="316" width="90" height="26" rx="13" fill="#52b788"/>',
         '<rect x="70" y="316" width="90" height="10" rx="5" fill="#74c69d"/>',
         '<circle cx="90" cy="332" r="2" fill="#2d6a4f"/><circle cx="114" cy="328" r="2" fill="#2d6a4f"/><circle cx="138" cy="334" r="2" fill="#2d6a4f"/>',
         '<path d="M236 220 V284 M256 226 V294 M276 220 V284" stroke="#adb5bd" stroke-width="4" stroke-linecap="round" stroke-dasharray="12 8"/>',
         # the shocked cat, all four legs off the floor
         '<path d="M296 140 Q330 100 340 60" fill="none" stroke="#6c757d" stroke-width="16" stroke-linecap="round"/>',
         '<path d="M330 92 l12 -4 M336 76 l12 0 M326 108 l12 -2 M320 82 l-10 -6 M314 100 l-10 -2" stroke="#6c757d" stroke-width="4" stroke-linecap="round"/>',
         limb(((220, 174), (212, 212)), "#6c757d", 11), limb(((240, 180), (238, 218)), "#6c757d", 11),
         limb(((278, 178), (282, 214)), "#6c757d", 11), limb(((296, 170), (306, 206)), "#6c757d", 11),
         '<path d="M206 170 Q210 110 256 108 Q300 106 304 160 Q300 186 256 184 Q216 186 206 170 Z" fill="#6c757d"/>']
    for a in range(200, 345, 18):
        t = math.radians(a)
        x, y = 256 + 50 * math.cos(t), 150 + 42 * math.sin(t)
        b.append(f'<path d="M{f(x)} {f(y)} l{f(10 * math.cos(t))} {f(10 * math.sin(t))}" stroke="#6c757d" stroke-width="5" stroke-linecap="round"/>')
    b += ['<circle cx="190" cy="140" r="30" fill="#6c757d"/>',
          '<path d="M168 122 L164 92 L186 112 Z M198 112 L214 92 L214 122 Z" fill="#6c757d"/>',
          '<circle cx="178" cy="136" r="9" fill="#fff"/><circle cx="200" cy="136" r="9" fill="#fff"/>',
          f'<circle cx="176" cy="138" r="3" fill="{INK}"/><circle cx="198" cy="138" r="3" fill="{INK}"/>',
          '<ellipse cx="188" cy="158" rx="5" ry="6" fill="#9d0208"/>',
          '<path d="M164 152 l-20 -4 M164 158 l-20 4 M212 152 l20 -4 M212 158 l20 4" stroke="#dee2e6" stroke-width="2"/>',
          '<path d="M144 112 l-14 -8 M140 132 l-16 0 M226 96 l10 -12" stroke="#e63946" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#fdf0d5")


def distant_from():
    b = ['<path d="M0 190 Q100 170 200 186 T400 176 V400 H0 Z" fill="#b7e4c7"/>',
         '<path d="M0 240 Q120 214 240 236 T400 226 V400 H0 Z" fill="#95d5b2"/>',
         '<path d="M0 300 Q140 270 280 296 T400 290 V400 H0 Z" fill="#74c69d"/>',
         '<path d="M90 352 Q180 300 140 270 Q110 240 220 228 Q300 218 330 186" fill="none" stroke="#d4a373" stroke-width="5" '
         'stroke-dasharray="10 8" stroke-linecap="round"/>',
         # the far-off hospital
         '<rect x="320" y="150" width="40" height="32" fill="#fff"/><rect x="332" y="140" width="16" height="12" fill="#fff"/>',
         '<path d="M340 157 V175 M331 166 H349" stroke="#2a9d8f" stroke-width="5"/>',
         '<ellipse cx="120" cy="60" rx="50" ry="18" fill="#fff"/><ellipse cx="280" cy="70" rx="40" ry="14" fill="#fff"/>']
    for x, y, c in ((40, 352, "#e9c46a"), (78, 366, "#f4a261"), (116, 352, "#e76f51"), (60, 336, "#ffd166")):
        b.append(f'<rect x="{x - 14}" y="{y - 22}" width="28" height="22" fill="{c}"/>'
                 f'<polygon points="{x - 18},{y - 20} {x},{y - 36} {x + 18},{y - 20}" fill="#9c6644"/>'
                 f'<rect x="{x - 4}" y="{y - 12}" width="8" height="12" fill="#7f5539"/>')
    b += [arrow(150, 330, 300, 140, "#e63946", 4, 14), arrow(300, 140, 150, 330, "#e63946", 4, 14)]
    return svg(b, "#e3f2fd")


def envelope(x, y, rot=0, c="#fff"):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot})"><rect x="-22" y="-14" width="44" height="28" fill="{c}" '
            'stroke="#dee2e6" stroke-width="2"/><path d="M-22 -14 L0 2 L22 -14" fill="none" stroke="#ced4da" stroke-width="2"/></g>')


def photo(x, y, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot})"><rect x="-18" y="-22" width="36" height="44" fill="#fff" '
            'stroke="#dee2e6" stroke-width="2"/><rect x="-14" y="-18" width="28" height="28" fill="#a8dadc"/>'
            '<path d="M-14 10 L-4 -2 L4 6 L8 2 L14 10 Z" fill="#6a994e"/></g>')


def full_of():
    rnd = random.Random(15)
    b = ['<rect y="300" width="400" height="100" fill="#9c6644"/>',
         '<polygon points="90,210 310,210 330,96 110,96" fill="#7f5539"/>',
         '<polygon points="102,200 298,200 314,108 118,108" fill="#5c4033"/>']
    items = []
    for _ in range(26):
        x, y = rnd.uniform(100, 300), rnd.uniform(170, 220)
        items.append(envelope(x, y, rnd.randint(-30, 30), rnd.choice(["#fff", "#fdf0d5", "#fff3b0"])) if rnd.random() < .6
                     else photo(x, y, rnd.randint(-30, 30)))
    b += items
    b += ['<rect x="86" y="214" width="228" height="96" rx="6" fill="#9c6644"/>',
          '<path d="M86 236 H314 M86 284 H314" stroke="#6c757d" stroke-width="6"/>',
          '<rect x="186" y="228" width="28" height="24" rx="3" fill="#c9a227"/>',
          envelope(60, 330, -20), photo(340, 334, 16), envelope(330, 290, 10, "#fdf0d5"), photo(70, 296, -10)]
    return svg(b, "#e9d8c4")


def grocery_bag(x, y):
    return (f'<path d="M{x - 28} {y - 30} L{x - 4} {y - 70} L{x + 6} {y - 66} L{x - 14} {y - 30} Z" fill="#e9c46a"/>'
            f'<path d="M{x + 6} {y - 30} L{x + 18} {y - 66} L{x + 22} {y - 30} Z" fill="#f4a261"/>'
            f'<path d="M{x + 16} {y - 66} l-4 -10 M{x + 18} {y - 66} l2 -12 M{x + 20} {y - 66} l6 -8" stroke="#52b788" stroke-width="3"/>'
            f'<circle cx="{x - 2}" cy="{y - 34}" r="10" fill="#e63946"/>'
            f'<path d="M{x - 34} {y - 36} H{x + 34} L{x + 28} {y + 20} H{x - 28} Z" fill="#d4a373"/>')


def appreciated():
    b = ['<rect y="330" width="400" height="70" fill="#a7c957"/>',
         '<rect x="0" y="60" width="200" height="270" fill="#e9c46a"/>',
         '<rect x="30" y="120" width="100" height="210" fill="#5c4033"/>',
         shadow(70, 344, 26),
         person(70, 342, .95, SKIN[3], "#e76f51", "#264653", "#1b1b1b", "bun", mood="grin",
                larm=((-12, 40), (-16, 72)), rarm=((14, 20), (-6, 30))),
         shadow(146, 344, 22),
         person(146, 342, .9, SKIN[3], "#457b9d", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-12, 40), (-16, 72)), rarm=((32, 10), (62, 4))),
         shadow(116, 352, 16),
         person(112, 350, .55, SKIN[3], "#ffd166", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-20, -30), (-26, -60)), rarm=((20, -30), (26, -60))),
         shadow(300, 344, 28),
         person(300, 342, 1.0, SKIN[0], "#2a9d8f", "#264653", "#bc6c25", "side", mood="smile",
                larm=((-30, 14), (-60, 20)), rarm=((12, 40), (16, 72)),
                extra='<rect x="-28" y="-156" width="56" height="16" fill="#ffd166" opacity=".9"/>'),
         grocery_bag(234, 246),
         heart(160, 120, 14), heart(200, 90, 10, "#ff8fab"), heart(240, 126, 12)]
    return svg(b, "#e3f2fd")


def healthy():
    b = ['<rect width="400" height="400" fill="#e8f1f2"/>',
         '<rect x="40" y="70" width="12" height="260" rx="5" fill="#adb5bd"/>',
         '<path d="M36 70 V120 M46 70 V120 M56 70 V120" stroke="#adb5bd" stroke-width="4"/>',
         '<rect x="350" y="70" width="12" height="260" rx="5" fill="#adb5bd"/><path d="M350 70 Q372 120 362 190 H350 Z" fill="#adb5bd"/>',
         '<circle cx="200" cy="200" r="140" fill="#fff" stroke="#dee2e6" stroke-width="4"/>',
         '<circle cx="200" cy="200" r="112" fill="none" stroke="#e9ecef" stroke-width="3"/>',
         # salmon
         '<path d="M150 130 Q200 100 250 130 Q240 170 200 168 Q160 168 150 130 Z" fill="#f4a261"/>',
         '<path d="M170 128 Q176 146 172 160 M196 120 Q202 140 196 164 M222 122 Q228 142 222 162" fill="none" stroke="#fff" stroke-width="3"/>']
    for x, y in ((136, 220), (160, 240), (128, 252)):
        b.append(f'<rect x="{x - 4}" y="{y}" width="8" height="18" fill="#52b788"/>'
                 f'<circle cx="{x - 8}" cy="{y}" r="10" fill="#2d6a4f"/><circle cx="{x + 8}" cy="{y}" r="10" fill="#2d6a4f"/>'
                 f'<circle cx="{x}" cy="{y - 8}" r="11" fill="#40916c"/>')
    for k in range(4):
        b.append(f'<rect x="{214 + k * 8}" y="{196 + k * 4}" width="58" height="9" rx="4" fill="#f77f00" transform="rotate(25 240 210)"/>')
    b += ['<ellipse cx="206" cy="270" rx="40" ry="24" fill="#f8f1e5"/>']
    rnd = random.Random(3)
    for _ in range(18):
        b.append(f'<ellipse cx="{f(rnd.uniform(176, 236))}" cy="{f(rnd.uniform(256, 284))}" rx="3" ry="1.6" fill="#e9d8a6"/>')
    b += ['<circle cx="276" cy="262" r="16" fill="#e63946"/><circle cx="288" cy="236" r="12" fill="#7209b7"/>'
          '<circle cx="300" cy="256" r="10" fill="#7209b7"/><circle cx="270" cy="236" r="9" fill="#e63946"/>',
          '<circle cx="104" cy="190" r="16" fill="#ffd166"/><circle cx="104" cy="190" r="10" fill="#fff3b0"/>']
    return svg(b, "#e8f1f2")


def decisive():
    b = ['<rect y="230" width="400" height="170" fill="#4895ef"/>',
         '<path d="M0 250 Q40 240 80 250 T160 250 T240 250 T320 250 T400 250" fill="none" stroke="#a8dadc" stroke-width="3"/>',
         '<path d="M0 270 H400 L380 400 H20 Z" fill="#9c6644"/>',
         '<path d="M0 290 H400 M0 320 H400 M0 350 H400" stroke="#7f5539" stroke-width="3"/>',
         '<rect x="226" y="20" width="10" height="260" fill="#7f5539"/>',
         '<path d="M240 30 Q330 70 330 150 L240 160 Z" fill="#f8f9fa"/>',
         '<path d="M226 40 L130 170" stroke="#bc6c25" stroke-width="3"/>',
         shadow(100, 324, 30),
         person(100, 322, 1.05, SKIN[1], "#264653", "#264653", "#adb5bd", "short", mood="flat",
                brows="M-14 -190 L-3 -186 M3 -186 L14 -190",
                larm=((-12, 40), (-16, 72)), rarm=((36, -24), (76, -40)),
                extra='<rect x="-24" y="-214" width="48" height="16" rx="4" fill="#fff"/>'
                      '<rect x="-30" y="-202" width="60" height="7" rx="3" fill="#264653"/>'
                      '<circle cx="0" cy="-206" r="4" fill="#ffd166"/>'
                      '<path d="M-26 -150 H-14 M14 -150 H26" stroke="#ffd166" stroke-width="4"/>'),
         arrow(300, 110, 380, 96, "#e63946", 7, 18),
         # the crew hauling on the lines
         shadow(270, 344, 24),
         person(270, 342, .8, SKIN[3], "#e63946", "#f8f9fa", "#1b1b1b", "short", mood="grin", rot=-12,
                larm=((-12, -40), (-30, -76)), rarm=((12, -40), (-14, -84)),
                lleg=((-14, 40), (-30, 80)), rleg=((14, 40), (26, 84))),
         '<path d="M238 166 L226 50" stroke="#bc6c25" stroke-width="3"/>',
         shadow(350, 344, 24),
         person(350, 342, .8, SKIN[0], "#4895ef", "#f8f9fa", "#bc6c25", "side", mood="grin",
                larm=((-20, 30), (-16, 38)), rarm=((20, 30), (16, 38)),
                lleg=((-14, 40), (-26, 84)), rleg=((14, 40), (26, 84))),
         '<circle cx="350" cy="252" r="30" fill="none" stroke="#7f5539" stroke-width="7"/>',
         '<path d="M350 214 V290 M312 252 H388 M323 225 L377 279 M377 225 L323 279" stroke="#7f5539" stroke-width="5"/>',
         f'<circle cx="320" cy="256" r="7" fill="{SKIN[0]}"/><circle cx="380" cy="256" r="7" fill="{SKIN[0]}"/>']
    return svg(b, "#cfe8f3")


def headscarf(color):
    return (f'<path d="M-30 -170 Q-32 -214 0 -214 Q32 -214 30 -170 Q32 -146 20 -136 H-20 Q-32 -146 -30 -170 Z '
            f'M-17 -176 A17 19 0 1 0 17 -176 A17 19 0 1 0 -17 -176 Z" fill="{color}" fill-rule="evenodd"/>')


def tolerance():
    b = ['<circle cx="200" cy="200" r="170" fill="#fff1e6"/>',
         '<rect y="330" width="400" height="70" fill="#a7c957"/>',
         heart(200, 90, 26)]
    kids = ((42, SKIN[3], "#e63946", "#1b1b1b", "bun", ""), (106, SKIN[0], "#4895ef", "#e9c46a", "side", ""),
            (170, SKIN[2], "#ffd166", "#1b1b1b", "none", headscarf("#2a9d8f")), (234, SKIN[1], "#7209b7", "#5c4033", "short", ""),
            (298, SKIN[3], "#52b788", "#1b1b1b", "short", ""), (362, SKIN[1], "#f4a261", "#bc6c25", "bun", ""))
    for k, (x, sk, shirt, hair, style, extra) in enumerate(kids):
        y = 340 + (6 if k in (0, 5) else 0)
        b += [shadow(x, y + 2, 20),
              person(x, y, .74, sk, shirt, "#264653", hair, style, mood="grin",
                     larm=((-16, 30), (-21, 46)) if k else ((-12, 40), (-16, 72)),
                     rarm=((16, 30), (21, 46)) if k < 5 else ((12, 40), (16, 72)), extra=extra)]
    return svg(b, "#e3f2fd")


def blended():
    b = ['<rect y="300" width="400" height="100" fill="#b08968"/><rect y="292" width="400" height="12" fill="#9c6644"/>',
         '<rect x="130" y="250" width="110" height="46" rx="8" fill="#495057"/>',
         '<circle cx="185" cy="274" r="8" fill="#e63946"/>',
         '<path d="M140 250 L130 90 H240 L230 250 Z" fill="#e5f6ff" opacity=".9"/>',
         '<path d="M142 236 L136 140 H234 L228 236 Z" fill="#ff8fab"/>',
         '<path d="M150 200 Q185 150 220 200 Q185 230 150 200 Z" fill="#ffafcc"/>',
         '<path d="M160 170 Q185 150 210 172" fill="none" stroke="#ffc2d1" stroke-width="5"/>',
         '<circle cx="168" cy="216" r="5" fill="#e63946"/><circle cx="206" cy="160" r="4" fill="#fff3b0"/>',
         '<rect x="124" y="78" width="122" height="16" rx="5" fill="#343a40"/>',
         '<path d="M250 140 l14 -6 M252 160 l16 0 M250 180 l14 6" stroke="#adb5bd" stroke-width="4" stroke-linecap="round"/>',
         # what went in
         '<path d="M20 230 Q60 206 110 214 Q74 230 24 240 Z" fill="#ffd166"/><path d="M106 212 l6 -4" stroke="#7f5539" stroke-width="4"/>',
         '<path d="M40 286 Q30 262 50 256 Q70 262 60 286 Q50 296 40 286 Z" fill="#e63946"/>',
         '<path d="M40 258 Q50 246 60 258 Q50 254 40 258 Z" fill="#52b788"/>',
         '<path d="M76 290 Q72 268 88 264 Q104 270 98 290 Q88 298 76 290 Z" fill="#e63946"/>',
         '<path d="M78 266 Q88 254 98 266 Q88 262 78 266 Z" fill="#52b788"/>',
         '<circle cx="46" cy="272" r="1.6" fill="#fff3b0"/><circle cx="54" cy="280" r="1.6" fill="#fff3b0"/><circle cx="50" cy="266" r="1.6" fill="#fff3b0"/>'
         '<circle cx="84" cy="278" r="1.6" fill="#fff3b0"/><circle cx="92" cy="284" r="1.6" fill="#fff3b0"/><circle cx="90" cy="272" r="1.6" fill="#fff3b0"/>',
         # and the smoothie it made
         '<path d="M290 190 H350 L342 292 H298 Z" fill="#ff8fab"/>',
         '<path d="M290 190 H350 L349 206 H291 Z" fill="#ffafcc"/>',
         '<path d="M326 192 L346 130" stroke="#4895ef" stroke-width="6" stroke-linecap="round"/>',
         '<circle cx="356" cy="196" r="10" fill="#e63946"/>',
         sparkle(370, 160, 8, "#ffd166")]
    return svg(b, "#fdf0d5")


def tiny_house(x, y, c):
    return (f'<rect x="{x - 12}" y="{y - 18}" width="24" height="18" fill="{c}"/>'
            f'<polygon points="{x - 16},{y - 16} {x},{y - 30} {x + 16},{y - 16}" fill="#9c6644"/>')


def disseminate():
    b = ['<path d="M0 250 Q100 220 200 250 T400 240 V400 H0 Z" fill="#95d5b2"/>',
         '<path d="M0 320 Q120 290 240 320 T400 316 V400 H0 Z" fill="#74c69d"/>']
    for r in (50, 90, 130, 170):
        b.append(f'<circle cx="200" cy="96" r="{r}" fill="none" stroke="#e63946" stroke-width="4" stroke-dasharray="14 10" '
                 f'opacity="{f(1 - r / 220)}"/>')
    b += ['<path d="M200 90 L170 300 M200 90 L230 300 M178 240 H222 M184 190 H216 M190 140 H210 M178 240 L216 190 M184 190 L210 140" '
          'stroke="#6c757d" stroke-width="5" stroke-linecap="round"/>',
          '<circle cx="200" cy="90" r="9" fill="#e63946"/>']
    for x, y in ((40, 252), (66, 258), (340, 250), (366, 244), (60, 336), (86, 344), (316, 330), (344, 338), (130, 380), (270, 384)):
        b.append(tiny_house(x, y, ("#e9c46a", "#f4a261", "#fff", "#e76f51")[(x + y) % 4]))
    return svg(b, "#e3f2fd")


def bowl(x, y, rot, fill, dots):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot})">'
            + "".join(f'<circle cx="{dx}" cy="{dy}" r="6" fill="{dots}"/>' for dx, dy in ((-14, -6), (0, -9), (14, -6), (-6, -14), (8, -15)))
            + f'<path d="M-30 -4 H30 Q28 26 0 26 Q-28 26 -30 -4 Z" fill="{fill}"/></g>')


def combined():
    b = ['<rect y="300" width="400" height="100" fill="#adb5bd"/><rect y="292" width="400" height="12" fill="#6c757d"/>',
         person(200, 384, 1.05, SKIN[2], "#fff", "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-34, 0), (-62, -6)), rarm=((34, 0), (62, -6)),
                extra='<rect x="-20" y="-238" width="40" height="34" rx="12" fill="#fff" stroke="#dee2e6" stroke-width="2"/>'
                      '<rect x="-24" y="-210" width="48" height="12" fill="#fff" stroke="#dee2e6" stroke-width="2"/>'),
         bowl(118, 212, 35, "#457b9d", "#52b788"), bowl(282, 212, -35, "#e76f51", "#e63946")]
    for k in range(4):
        b.append(f'<circle cx="{150 + k * 8}" cy="{232 + k * 12}" r="5" fill="#52b788"/>'
                 f'<circle cx="{250 - k * 8}" cy="{232 + k * 12}" r="5" fill="#e63946"/>')
    b += ['<rect x="128" y="276" width="144" height="66" rx="8" fill="#495057"/>',
          '<rect x="116" y="270" width="168" height="12" rx="5" fill="#343a40"/>',
          '<path d="M116 300 h-12 M284 300 h12" stroke="#343a40" stroke-width="8" stroke-linecap="round"/>']
    for k, c in enumerate(("#52b788", "#e63946", "#52b788", "#e63946", "#52b788", "#e63946", "#52b788")):
        b.append(f'<circle cx="{146 + k * 18}" cy="{270 - (k % 2) * 5}" r="7" fill="{c}"/>')
    b += [f'<circle cx="114" cy="230" r="9" fill="{SKIN[2]}"/><circle cx="286" cy="230" r="9" fill="{SKIN[2]}"/>',]
    return svg(b, "#fdf0d5")


def suitcase_sitter(x, sk, shirt, hair, style, mood, larm, rarm, case):
    return (f'<rect x="{x - 34}" y="290" width="68" height="56" rx="8" fill="{case}"/>'
            f'<path d="M{x - 12} 290 V280 H{x + 12} V290" fill="none" stroke="#495057" stroke-width="4"/>'
            + person(x, 376, .9, sk, shirt, "#264653", hair, style, mood=mood,
                     brows="M-14 -188 L-3 -192 M3 -192 L14 -188",
                     lleg=((-10, 8), (-12, 48)), rleg=((10, 8), (12, 48)), larm=larm, rarm=rarm))


def distressed():
    b = ['<rect y="340" width="400" height="60" fill="#adb5bd"/>',
         '<rect x="150" y="30" width="250" height="200" fill="#dee2e6"/>',
         '<rect x="160" y="40" width="230" height="180" fill="#caf0f8"/>',
         '<rect x="160" y="170" width="230" height="50" fill="#adb5bd"/>',
         '<g transform="translate(276 160) scale(.55)">'
         '<path d="M-120 -40 L-140 -96 H-112 L-80 -40 Z" fill="#457b9d"/>'
         '<path d="M-130 -40 H110 Q140 -40 140 -20 Q140 0 110 0 H-120 Q-140 0 -136 -20 Z" fill="#f8f9fa"/>'
         + "".join(f'<circle cx="{-96 + i * 22}" cy="-22" r="5" fill="#4895ef"/>' for i in range(9))
         + '<path d="M-60 0 V14 M70 0 V14" stroke="#495057" stroke-width="4"/>'
         '<circle cx="-60" cy="18" r="7" fill="#343a40"/><circle cx="70" cy="18" r="7" fill="#343a40"/></g>',
         '<path d="M275 40 V220 M160 130 H390" stroke="#dee2e6" stroke-width="6"/>',
         # the departures board, one flight in red
         '<rect x="10" y="30" width="126" height="100" rx="4" fill="#212529"/>',
         '<rect x="20" y="42" width="106" height="12" fill="#ffd166"/><rect x="20" y="62" width="106" height="12" fill="#ffd166"/>',
         '<rect x="20" y="82" width="106" height="12" fill="#e63946"/><rect x="20" y="102" width="106" height="12" fill="#ffd166"/>',
         suitcase_sitter(70, SKIN[1], "#e76f51", "#5c4033", "side", "frown",
                         ((10, -30), (-6, -58)), ((-14, 30), (-28, 40)), "#7209b7"),
         suitcase_sitter(200, SKIN[3], "#2a9d8f", "#1b1b1b", "bun", "wide",
                         ((-10, -30), (6, -58)), ((10, -30), (-6, -58)), "#e63946"),
         suitcase_sitter(330, SKIN[0], "#457b9d", "#e9c46a", "short", "frown",
                         ((14, 30), (28, 40)), ((-14, 30), (-28, 40)), "#2a9d8f")]
    return svg(b, "#f1faee")


def ant(x, y, k=1.0, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({k})">'
            f'<path d="M-6 0 l-4 5 M-6 0 l-4 -5 M0 0 l0 6 M0 0 l0 -6 M6 0 l4 5 M6 0 l4 -5" stroke="{INK}" stroke-width="1.5"/>'
            f'<circle cx="-7" cy="0" r="4" fill="{INK}"/><circle cx="0" cy="0" r="3" fill="{INK}"/><circle cx="7" cy="0" r="3.5" fill="{INK}"/>'
            f'<path d="M9 -2 l5 -5 M9 2 l5 5" stroke="{INK}" stroke-width="1.2"/></g>')


def curiosity():
    b = ['<rect y="250" width="400" height="150" fill="#a7c957"/>',
         bush(40, 240, 30), bush(370, 236, 26), bush(330, 246, 18),
         '<path d="M290 330 Q330 270 370 330 Z" fill="#bc6c25"/>',
         '<circle cx="330" cy="304" r="5" fill="#7f5539"/>']
    for k in range(6):
        b.append(ant(200 + k * 18, 340 - k * 4, .8, -10))
    b += [person(110, 402, .95, SKIN[2], "#ffd166", "#264653", "#1b1b1b", "bun", mood="wide",
                 lleg=((-2, 44), (-40, 46)), rleg=((30, 6), (34, 46)),
                 larm=((10, 40), (20, 60)), rarm=((40, 30), (74, 50))),
          '<path d="M184 336 L206 320" stroke="#7f5539" stroke-width="8" stroke-linecap="round"/>',
          f'<circle cx="182" cy="338" r="8" fill="{SKIN[2]}"/>',
          '<circle cx="232" cy="298" r="34" fill="#caf0f8" opacity=".75" stroke="#495057" stroke-width="6"/>',
          ant(232, 300, 2.6, -10),
          sparkle(276, 250, 8, "#ffd166"), sparkle(190, 250, 6, "#ffd166")]
    return svg(b, "#e3f2fd")


def steady():
    b = ['<rect y="340" width="400" height="60" fill="#a7c957"/>',
         bush(80, 340, 18), bush(320, 340, 16), bush(200, 344, 12),
         '<rect x="10" y="250" width="12" height="150" fill="#7f5539"/><rect x="378" y="250" width="12" height="150" fill="#7f5539"/>',
         '<path d="M16 254 H384" stroke="#495057" stroke-width="4"/>',
         person(200, 254, .9, SKIN[1], "#e63946", "#264653", "#5c4033", "bun", mood="content",
                larm=((-24, 10), (-40, 20)), rarm=((24, 10), (40, 20)),
                lleg=((-2, 44), (-2, 86)), rleg=((2, 44), (2, 86))),
         '<path d="M40 150 Q200 136 360 150" fill="none" stroke="#9c6644" stroke-width="6" stroke-linecap="round"/>',
         '<circle cx="40" cy="150" r="9" fill="#ffd166"/><circle cx="360" cy="150" r="9" fill="#ffd166"/>',
         f'<circle cx="144" cy="141" r="7.5" fill="{SKIN[1]}"/><circle cx="256" cy="141" r="7.5" fill="{SKIN[1]}"/>',
         '<ellipse cx="80" cy="60" rx="40" ry="14" fill="#fff"/><ellipse cx="320" cy="76" rx="34" ry="12" fill="#fff"/>']
    return svg(b, "#cfe8f3")


def dumbbell(x, y, rot=0, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({k})">'
            '<rect x="-24" y="-3" width="48" height="6" fill="#6c757d"/>'
            '<rect x="-30" y="-14" width="12" height="28" rx="3" fill="#343a40"/><rect x="18" y="-14" width="12" height="28" rx="3" fill="#343a40"/></g>')


def strengthen():
    sk = SKIN[2]
    tank = ('<rect x="-28" y="-150" width="56" height="66" rx="14" fill="#e63946"/>'
            f'<circle cx="44" cy="-158" r="12" fill="{sk}"/>')
    b = ['<rect y="340" width="400" height="60" fill="#adb5bd"/>',
         shadow(200, 344, 36),
         person(200, 342, 1.2, sk, sk, "#264653", "#1b1b1b", "short", mood="grin",
                larm=((-12, 40), (-16, 72)), rarm=((36, -4), (42, -44)), extra=tank),
         dumbbell(276, 112, 0, 1.1), dumbbell(176, 262, 0, 1.0),
         arrow(300, 210, 300, 150, "#2a9d8f", 6, 14), arrow(330, 220, 330, 160, "#2a9d8f", 6, 14),
         sparkle(340, 96, 10, "#ffd166"), sparkle(360, 130, 7, "#ffd166")]
    return svg(b, "#e8f1f2")


def harbinger():
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>',
         '<path d="M0 300 Q60 290 120 304 Q90 330 30 326 Q0 322 0 300 Z" fill="#fff"/>',
         '<path d="M240 330 Q300 316 360 330 Q330 350 270 348 Z" fill="#fff"/>',
         '<path d="M130 316 q3 6 0 8 q-3 -2 0 -8 Z M366 300 q3 6 0 8 q-3 -2 0 -8 Z" fill="#90e0ef"/>',
         '<circle cx="340" cy="70" r="30" fill="#ffd166"/>',
         '<path d="M0 150 Q100 140 190 158" fill="none" stroke="#7f5539" stroke-width="12" stroke-linecap="round"/>',
         '<path d="M30 146 Q40 130 60 136 M120 150 Q130 132 150 138" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>',
         bird(110, 150, "#7f5539", "#5c4033", k=2.4),
         '<ellipse cx="114" cy="122" rx="20" ry="14" fill="#f77f00"/>',
         '<polygon points="148,90 166,96 148,100" fill="#f4a261"/>',
         note(190, 96, "#2a9d8f"), note(230, 74, "#e76f51", 1.1), note(270, 100, "#2a9d8f", .9)]
    for x, c in ((70, "#9d4edd"), (110, "#ffd166"), (180, "#9d4edd"), (220, "#ffffff"), (300, "#ffd166"), (350, "#9d4edd")):
        b.append(f'<path d="M{x} 340 V316" stroke="#40916c" stroke-width="3"/>'
                 f'<path d="M{x - 7} 316 Q{x - 8} 300 {x} 294 Q{x + 8} 300 {x + 7} 316 Z" fill="{c}"/>'
                 f'<ellipse cx="{x - 6}" cy="334" rx="6" ry="2.5" fill="#52b788" transform="rotate(-30 {x - 6} 334)"/>')
    return svg(b, "#e3f2fd")


def bold():
    rnd = random.Random(28)
    b = ['<ellipse cx="300" cy="50" rx="140" ry="50" fill="#343a40"/><ellipse cx="380" cy="110" rx="90" ry="40" fill="#495057"/>',
         '<polygon points="330,100 306,150 322,150 300,200 344,138 328,138 346,100" fill="#ffd166"/>']
    for _ in range(26):
        x, y = rnd.uniform(220, 400), rnd.uniform(100, 380)
        b.append(f'<path d="M{f(x)} {f(y)} l-10 18" stroke="#90e0ef" stroke-width="2.5" stroke-linecap="round"/>')
    b += ['<path d="M0 300 H270 L282 400 H0 Z" fill="#6c757d"/>', '<path d="M0 300 H270" stroke="#52b788" stroke-width="8"/>',
          '<path d="M270 300 L290 400 H400 V360 Q330 370 290 340 Z" fill="#4895ef"/>',
          shadow(214, 304, 30),
          person(214, 302, 1.15, SKIN[3], "#9c6644", "#7f5539", "#1b1b1b", "short", mood="flat",
                 brows="M-14 -190 L-3 -186 M3 -186 L14 -190",
                 larm=((-22, 30), (-8, 54)), rarm=((22, 30), (8, 54)),
                 extra='<path d="M-28 -150 Q-60 -110 -96 -100 Q-70 -90 -56 -84 Q-80 -70 -90 -60 Q-50 -64 -30 -84 Z" fill="#9c6644"/>'
                       '<path d="M0 -150 V-84" stroke="#7f5539" stroke-width="3"/>'
                       '<ellipse cx="0" cy="-198" rx="36" ry="7" fill="#7f5539"/>'
                       '<path d="M-20 -198 Q-20 -220 0 -220 Q20 -220 20 -198 Z" fill="#7f5539"/>'),
          '<path d="M60 120 h40 M40 160 h56 M70 200 h36" stroke="#adb5bd" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#8d99ae")


def mystifying():
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         '<rect x="150" y="300" width="100" height="20" fill="#7f5539"/>',
         '<rect x="156" y="200" width="88" height="50" fill="#f8f9fa" stroke="#dee2e6" stroke-width="3"/>',
         '<rect x="156" y="250" width="88" height="50" fill="#f8f9fa" stroke="#dee2e6" stroke-width="3"/>',
         '<rect x="148" y="190" width="104" height="12" fill="#e9c46a"/>',
         '<rect x="184" y="286" width="32" height="8" rx="3" fill="#343a40"/>',
         shadow(80, 334, 28),
         person(80, 332, 1.0, SKIN[1], "#f8f9fa", "#264653", "#5c4033", "side", mood="side",
                brows="M-14 -190 L-3 -190 M3 -196 Q9 -202 15 -195",
                larm=((-12, 40), (-16, 72)), rarm=((10, -30), (-6, -58))),
         shadow(320, 334, 28),
         person(320, 332, 1.0, SKIN[3], "#f8f9fa", "#264653", "#1b1b1b", "bun", mood="left",
                brows="M-15 -195 Q-9 -202 -3 -196 M3 -190 L14 -190",
                larm=((-14, 4), (-26, 0)), rarm=((-10, -30), (6, -58)))]
    # the empty comb frame she holds up
    cells = []
    for r in range(4):
        for c in range(4):
            cx, cy = 206 + c * 14 + (r % 2) * 7, 156 + r * 12
            pts = " ".join(f"{f(cx + 7 * math.cos(math.radians(30 + 60 * i)))},{f(cy + 7 * math.sin(math.radians(30 + 60 * i)))}" for i in range(6))
            cells.append(f'<polygon points="{pts}" fill="#ffd166" stroke="#e9c46a" stroke-width="2"/>')
    b += ['<rect x="196" y="144" width="76" height="58" fill="#bc6c25"/>'] + cells
    b += [f'<circle cx="272" cy="186" r="8" fill="{SKIN[3]}"/>']
    return svg(b, "#e3f2fd")


def succumb():
    b = ['<rect y="300" width="400" height="100" fill="#d4a373"/>',
         '<path d="M20 340 l18 6 l10 -8 l16 10 l12 -4 M140 372 l14 -8 l12 6 l18 -6 l8 8 M250 340 l12 10 l16 -4 l10 12 M300 384 l16 -6 l14 6 l20 -8" fill="none" '
         'stroke="#9c6644" stroke-width="3"/>',
         '<circle cx="320" cy="80" r="44" fill="#ffd166"/><circle cx="320" cy="80" r="62" fill="#ffd166" opacity=".3"/>',
         # the drooping sapling
         '<path d="M180 310 Q178 230 200 200 Q230 170 250 210" fill="none" stroke="#7f5539" stroke-width="10" stroke-linecap="round"/>',
         '<path d="M200 220 Q170 214 160 236" fill="none" stroke="#7f5539" stroke-width="5" stroke-linecap="round"/>']
    for x, y, rot in ((252, 222, 70), (240, 236, 100), (262, 238, 60), (160, 246, 110), (170, 250, 80)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="15" fill="#bc6c25" transform="rotate({rot} {x} {y})"/>')
    b += ['<ellipse cx="220" cy="318" rx="8" ry="4" fill="#bc6c25"/><ellipse cx="150" cy="320" rx="8" ry="4" fill="#e9c46a"/>',
          '<rect x="60" y="120" width="18" height="120" rx="9" fill="#fff" stroke="#adb5bd" stroke-width="3"/>',
          '<rect x="64" y="134" width="10" height="100" rx="5" fill="#e63946"/><circle cx="69" cy="244" r="16" fill="#e63946"/>',
          ]
    return svg(b, "#fde2c8")


def assertive():
    b = ['<rect y="320" width="400" height="80" fill="#adb5bd"/>',
         '<rect x="190" y="40" width="170" height="110" fill="#fff" stroke="#dee2e6" stroke-width="4"/>',
         '<rect x="214" y="100" width="24" height="40" fill="#4895ef"/><rect x="250" y="80" width="24" height="60" fill="#52b788"/>'
         '<rect x="286" y="60" width="24" height="80" fill="#e76f51"/><rect x="322" y="90" width="24" height="50" fill="#ffd166"/>']
    for x, sk, shirt, hair, style in ((210, SKIN[0], "#457b9d", "#5c4033", "short"), (280, SKIN[3], "#e9c46a", "#1b1b1b", "bun"),
                                      (350, SKIN[1], "#6a994e", "#adb5bd", "side")):
        b.append(person(x, 350, .8, sk, shirt, "#264653", hair, style, mood="left"))
    b += ['<rect x="170" y="252" width="230" height="16" fill="#9c6644"/><rect x="180" y="268" width="210" height="60" fill="#7f5539"/>',
          '<rect x="200" y="240" width="30" height="14" fill="#fff"/><rect x="270" y="240" width="30" height="14" fill="#fff"/>',
          shadow(86, 334, 32),
          person(86, 332, 1.15, SKIN[2], "#bc4749", "#264653", "#1b1b1b", "bun", mood="smile",
                 brows="M-14 -190 L-3 -188 M3 -188 L14 -190",
                 larm=((-22, 30), (-8, 54)), rarm=((34, -10), (66, -18)))]
    return svg(b, "#f1faee")


def binoculars():
    return ('<rect x="-20" y="-188" width="16" height="18" rx="4" fill="#343a40"/><rect x="4" y="-188" width="16" height="18" rx="4" fill="#343a40"/>'
            '<rect x="-6" y="-184" width="12" height="8" fill="#343a40"/>'
            '<circle cx="-12" cy="-186" r="5" fill="#90e0ef"/><circle cx="12" cy="-186" r="5" fill="#90e0ef"/>')


def watched():
    rnd = random.Random(32)
    b = ['<rect y="250" width="400" height="150" fill="#e9c46a"/>',
         '<circle cx="330" cy="70" r="30" fill="#ffd166"/>',
         '<path d="M300 260 Q312 150 330 130 Q348 150 362 260 Z" fill="#bc6c25"/>',
         '<circle cx="320" cy="200" r="5" fill="#7f5539"/>',
         monkey(250, 268, k=.9),
         '<path d="M276 220 L318 200" stroke="#7f5539" stroke-width="4" stroke-linecap="round"/>',
         person(60, 330, .9, SKIN[1], "#6a994e", "#264653", "#5c4033", "short", mood="flat",
                larm=((-6, 20), (12, -30)), rarm=((6, 20), (-12, -30)), extra=binoculars()),
         person(140, 336, .85, SKIN[3], "#a3b18a", "#264653", "#1b1b1b", "bun", mood="side",
                larm=((10, 30), (30, 24)), rarm=((12, 30), (30, 34)),
                extra='<rect x="4" y="-130" width="34" height="26" fill="#fff" stroke="#adb5bd" stroke-width="2"/>'
                      '<path d="M10 -122 h22 M10 -114 h16" stroke="#adb5bd" stroke-width="2"/>')]
    for _ in range(90):
        x = rnd.uniform(0, 210)
        h = rnd.uniform(150, 215)
        b.append(f'<path d="M{f(x)} 400 Q{f(x + rnd.uniform(-10, 10))} {f(400 - h / 2)} {f(x + rnd.uniform(-14, 14))} {f(400 - h)}" '
                 f'fill="none" stroke="{rnd.choice(["#a3b18a", "#bc8a5f", "#ccd5ae"])}" stroke-width="5" stroke-linecap="round"/>')
    return svg(b, "#e3f2fd")


def extensive():
    b = ['<path d="M0 120 Q100 96 200 112 T400 104 V140 H0 Z" fill="#8d99ae"/>',
         '<rect y="130" width="400" height="270" fill="#6c9bcf"/>']
    for y in range(160, 400, 34):
        b.append(f'<path d="M0 {y} Q50 {y - 6} 100 {y} T200 {y} T300 {y} T400 {y}" fill="none" stroke="#a8dadc" stroke-width="3" opacity=".7"/>')
    for x, y, k in ((60, 230, 1.0), (300, 200, .7), (180, 300, 1.2), (350, 330, 1.0)):
        b.append(f'<polygon points="{x - 30 * k},{y} {x},{y - 26 * k} {x + 30 * k},{y}" fill="#bc4749"/>'
                 f'<rect x="{x - 22 * k}" y="{y}" width="{44 * k}" height="{8 * k}" fill="#e9c46a"/>')
    for x, y, r in ((120, 180, 16), (240, 160, 12), (90, 330, 20), (270, 250, 14), (380, 170, 12)):
        b.append(bush(x, y, r))
    b += ['<path d="M150 214 H260" stroke="#adb5bd" stroke-width="6"/>',
          '<path d="M160 214 V224 M190 214 V224 M220 214 V224 M250 214 V224" stroke="#adb5bd" stroke-width="4"/>',
          '<rect x="22" y="270" width="6" height="30" fill="#6c757d"/><rect x="10" y="256" width="30" height="18" rx="3" fill="#ffd166"/>']
    return svg(b, "#adb5bd")


def easel(x, y, w, h):
    return (f'<path d="M{x + w * .2} {y + h + 70} L{x + w * .35} {y - 10} M{x + w * .8} {y + h + 70} L{x + w * .65} {y - 10}" '
            'stroke="#7f5539" stroke-width="7" stroke-linecap="round"/>'
            f'<rect x="{x - 4}" y="{y + h + 4}" width="{w + 8}" height="8" fill="#7f5539"/>')


def revise():
    b = ['<rect y="330" width="400" height="70" fill="#d6ccc2"/>',
         easel(30, 120, 110, 86),
         painting(30, 120, 110, 86, "#adb5bd", "#8d99ae", "#6c757d", "#495057"),
         arrow(150, 170, 186, 170, "#e63946", 5, 14),
         easel(196, 70, 170, 136),
         painting(196, 70, 170, 136, "#caf0f8", "#ffd166", "#52b788", "#2d6a4f"),
         '<path d="M196 70 H260 L240 206 H196 Z" fill="#adb5bd"/>',
         '<path d="M196 170 Q226 150 250 168 L240 206 H196 Z" fill="#6c757d"/>',
         person(330, 412, 1.1, SKIN[1], "#457b9d", "#264653", "#5c4033", "short", mood="smile",
                larm=((-30, -20), (-62, -40)), rarm=((12, 40), (16, 72)),
                extra='<ellipse cx="2" cy="-200" rx="26" ry="8" fill="#bc4749"/>'),
         '<path d="M238 207 L248 176" stroke="#7f5539" stroke-width="5" stroke-linecap="round"/>',
         '<path d="M248 176 l2 -8" stroke="#52b788" stroke-width="8" stroke-linecap="round"/>',
         f'<circle cx="238" cy="207" r="9" fill="{SKIN[1]}"/>',
         '<rect y="330" width="400" height="70" fill="#d6ccc2"/>',
         sparkle(300, 50, 10, "#ffd166")]
    return svg(b, "#f8f9fa")


def inspecting():
    b = ['<rect y="0" width="400" height="320" fill="#ced4da"/>']
    for r in range(8):
        for c in range(6):
            x = c * 72 - (36 if r % 2 else 0)
            b.append(f'<rect x="{x + 2}" y="{r * 40 + 2}" width="68" height="36" fill="#dee2e6"/>')
    b += ['<rect y="320" width="400" height="80" fill="#6c757d"/>',
          '<polygon points="170,190 260,120 360,200 360,270 260,300 170,214" fill="#fff3b0" opacity=".55"/>',
          '<path d="M286 40 L276 90 L296 130 L280 180 L300 230 L290 290 L298 320 M296 130 L326 150 M280 180 L250 196 M300 230 L330 252" '
          'fill="none" stroke="#343a40" stroke-width="5" stroke-linejoin="round"/>',
          shadow(100, 334, 30),
          person(100, 332, 1.05, SKIN[3], "#f4a261", "#264653", "#1b1b1b", "short", mood="side",
                 larm=((-14, 30), (-6, 52)), rarm=((30, 0), (62, -4)),
                 extra=hard_hat("#ffd166") + '<rect x="-26" y="-112" width="30" height="38" rx="2" fill="#bc6c25"/>'
                       '<rect x="-22" y="-106" width="22" height="28" fill="#fff"/>'),
          '<rect x="166" y="184" width="28" height="16" rx="3" fill="#495057" transform="rotate(-10 180 192)"/>',
          f'<circle cx="166" cy="194" r="9" fill="{SKIN[3]}"/>']
    return svg(b, "#ced4da")


def vigilance():
    rnd = random.Random(36)
    b = ['<rect y="150" width="400" height="140" fill="#4895ef"/>',
         '<path d="M0 290 Q200 270 400 290 V400 H0 Z" fill="#f2cc8f"/>']
    for y in (180, 220, 260):
        b.append(f'<path d="M140 {y} Q170 {y - 6} 200 {y} T260 {y} T320 {y} T400 {y}" fill="none" stroke="#a8dadc" stroke-width="3"/>')
    for x, y, sk, cap in ((220, 210, SKIN[0], "#e63946"), (290, 240, SKIN[3], "#ffd166"), (350, 196, SKIN[1], "#2a9d8f")):
        b.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{sk}"/><path d="M{x - 11} {y - 2} Q{x} {y - 18} {x + 11} {y - 2} Z" fill="{cap}"/>'
                 f'<path d="M{x + 8} {y} q12 -14 18 -4" fill="none" stroke="{sk}" stroke-width="5" stroke-linecap="round"/>'
                 f'<ellipse cx="{x}" cy="{y + 9}" rx="18" ry="4" fill="none" stroke="#caf0f8" stroke-width="2"/>')
    b += ['<path d="M50 380 L80 190 M130 380 L100 190 M60 320 H120 M68 260 H112" stroke="#f8f9fa" stroke-width="8" stroke-linecap="round"/>',
          '<rect x="60" y="180" width="62" height="12" fill="#e63946"/>',
          person(90, 254, .85, SKIN[2], "#e63946", "#e63946", "#1b1b1b", "short", mood="flat",
                 lleg=((-8, 10), (-12, 48)), rleg=((8, 10), (12, 48)),
                 larm=((10, -6), (22, -30)), rarm=((-10, -6), (2, -30)), extra=binoculars()),
          '<path d="M130 110 L210 90 M130 120 L210 200" stroke="#ffd166" stroke-width="3" stroke-dasharray="6 6"/>']
    return svg(b, "#cfe8f3")


def signal_flag(x, y, rot):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot})">'
            '<path d="M0 0 V-60" stroke="#7f5539" stroke-width="5" stroke-linecap="round"/>'
            '<rect x="0" y="-60" width="40" height="34" fill="#ffd166"/><polygon points="0,-60 40,-60 0,-26" fill="#e63946"/></g>')


def signaling():
    b = ['<rect y="180" width="400" height="220" fill="#4895ef"/>',
         '<path d="M0 220 Q60 212 120 220 T240 220 T360 220 T480 220" fill="none" stroke="#a8dadc" stroke-width="3"/>',
         '<path d="M300 186 H370 L362 198 H308 Z" fill="#f8f9fa"/><path d="M334 186 V150 L356 182 Z" fill="#fff"/>',
         '<circle cx="320" cy="180" r="4" fill="#264653"/>',
         '<path d="M0 290 H270 L250 400 H0 Z" fill="#9c6644"/>',
         '<path d="M0 300 H266" stroke="#f8f9fa" stroke-width="6"/>',
         shadow(130, 334, 30),
         person(130, 332, 1.05, SKIN[1], "#f8f9fa", "#264653", "#5c4033", "short", mood="grin",
                larm=((-24, -30), (-40, -62)), rarm=((24, -30), (40, -62)),
                extra='<rect x="-24" y="-218" width="48" height="16" rx="6" fill="#fff"/><rect x="-28" y="-206" width="56" height="5" fill="#264653"/>'
                      '<path d="M-28 -150 H28" stroke="#264653" stroke-width="8"/>'),
         signal_flag(66, 140, -30), signal_flag(194, 140, 30),
         '<path d="M240 120 L300 160" stroke="#ffd166" stroke-width="3" stroke-dasharray="6 6"/>']
    return svg(b, "#e3f2fd")


def weaken():
    b = ['<rect y="300" width="400" height="100" fill="#d4a373"/>',
         '<path d="M20 340 l18 6 l10 -8 l16 10 l12 -4 M140 372 l14 -8 l12 6 l18 -6 l8 8 M250 340 l12 10 l16 -4 l10 12 M300 384 l16 -6 l14 6 l20 -8" fill="none" '
         'stroke="#9c6644" stroke-width="3"/>',
         '<circle cx="80" cy="80" r="40" fill="#ffd166"/>',
         '<g transform="rotate(24 210 310)">',
         '<path d="M196 310 V150 L224 150 V310 Z" fill="#7f5539"/>',
         '<path d="M210 300 L206 260 L214 220 L208 180" fill="none" stroke="#3d2c2e" stroke-width="4"/>',
         '<path d="M210 160 L170 100 M210 170 L260 110 M186 124 L170 120 M246 126 L266 136 M210 150 V96" stroke="#7f5539" stroke-width="8" '
         'stroke-linecap="round"/>',
         '</g>',
         '<path d="M196 312 q-16 4 -24 14 M222 312 q18 2 26 12" fill="none" stroke="#7f5539" stroke-width="6" stroke-linecap="round"/>',
         '<ellipse cx="300" cy="320" rx="8" ry="4" fill="#bc6c25"/><ellipse cx="330" cy="310" rx="8" ry="4" fill="#e9c46a" transform="rotate(30 330 310)"/>']
    return svg(b, "#fde2c8")


def mortarboard():
    return ('<polygon points="-34,-206 0,-222 34,-206 0,-192" fill="#264653"/>'
            '<rect x="-18" y="-204" width="36" height="12" fill="#264653"/>'
            '<path d="M0 -206 L24 -200 V-180" stroke="#ffd166" stroke-width="3" fill="none"/>')


def receive():
    b = ['<rect y="300" width="400" height="100" fill="#9c6644"/>',
         '<path d="M0 0 H60 Q70 150 40 300 H0 Z M400 0 H340 Q330 150 360 300 H400 Z" fill="#9d0208"/>',
         '<polygon points="140,0 180,0 230,300 90,300" fill="#fff3b0" opacity=".25"/>',
         shadow(120, 304, 30),
         person(120, 302, 1.05, SKIN[2], "#264653", "#264653", "#1b1b1b", "bun", mood="grin",
                larm=((-12, 40), (-16, 72)), rarm=((32, 4), (64, 0)), extra=mortarboard()),
         shadow(280, 304, 30),
         person(280, 302, 1.05, SKIN[0], "#6d597a", "#264653", "#adb5bd", "short", mood="smile",
                larm=((-32, 4), (-64, 0)), rarm=((12, 40), (16, 72))),
         '<rect x="172" y="134" width="56" height="16" rx="8" fill="#fff" stroke="#dee2e6" stroke-width="2"/>',
         '<path d="M196 134 V150 M204 134 V150" stroke="#e63946" stroke-width="4"/>',
         '<path d="M200 150 l-8 14 M200 150 l8 14" stroke="#e63946" stroke-width="3"/>',
         f'<circle cx="176" cy="142" r="8" fill="{SKIN[2]}"/><circle cx="224" cy="142" r="8" fill="{SKIN[0]}"/>',
         sparkle(200, 96, 10, "#ffd166"), sparkle(160, 76, 7, "#ffd166"), sparkle(244, 82, 8, "#ffd166")]
    for k in range(8):
        x = 25 + k * 50
        b.append(f'<circle cx="{x}" cy="366" r="20" fill="#14213d"/><rect x="{x - 26}" y="376" width="52" height="30" rx="12" fill="#14213d"/>')
    return svg(b, "#3d405b")


def delivery_truck(x, y):
    return (f'<rect x="{x}" y="{y - 120}" width="150" height="100" rx="6" fill="#f8f9fa"/>'
            f'<path d="M{x + 150} {y - 90} H{x + 196} L{x + 220} {y - 56} V{y - 20} H{x + 150} Z" fill="#e76f51"/>'
            f'<path d="M{x + 160} {y - 82} H{x + 192} L{x + 208} {y - 58} H{x + 160} Z" fill="#caf0f8"/>'
            f'<rect x="{x + 50}" y="{y - 96}" width="50" height="44" fill="#d4a373"/>'
            f'<path d="M{x + 50} {y - 80} H{x + 100} M{x + 75} {y - 96} V{y - 80}" stroke="#9c6644" stroke-width="3"/>'
            f'<circle cx="{x + 40}" cy="{y - 16}" r="18" fill="#343a40"/><circle cx="{x + 180}" cy="{y - 16}" r="18" fill="#343a40"/>'
            f'<circle cx="{x + 40}" cy="{y - 16}" r="7" fill="#adb5bd"/><circle cx="{x + 180}" cy="{y - 16}" r="7" fill="#adb5bd"/>')


def impede():
    rnd = random.Random(40)
    b = ['<rect y="280" width="400" height="120" fill="#e9ecef"/>',
         '<path d="M0 300 H400 V360 H0 Z" fill="#adb5bd"/>',
         delivery_truck(10, 344),
         '<path d="M250 360 Q246 250 300 220 Q340 196 370 230 Q404 250 400 280 V360 Z" fill="#fff"/>',
         '<path d="M260 300 Q300 270 340 290 M300 250 Q330 236 360 252" fill="none" stroke="#dee2e6" stroke-width="4"/>']
    for _ in range(60):
        b.append(f'<circle cx="{f(rnd.uniform(0, 400))}" cy="{f(rnd.uniform(0, 300))}" r="{f(rnd.uniform(2, 5))}" fill="#fff"/>')
    b += ['<path d="M10 224 H160 Q170 210 150 206 H20 Q0 210 10 224 Z" fill="#fff"/>']
    return svg(b, "#8d99ae")


def contracted():
    b = ['<circle cx="200" cy="220" r="130" fill="none" stroke="#adb5bd" stroke-width="4" stroke-dasharray="12 10"/>',
         '<circle cx="200" cy="220" r="94" fill="none" stroke="#6c757d" stroke-width="30"/>',
         '<circle cx="200" cy="220" r="94" fill="none" stroke="#ced4da" stroke-width="10"/>',
         '<path d="M150 150 A86 86 0 0 1 250 150" fill="none" stroke="#fff" stroke-width="4" opacity=".7"/>']
    for a in (0, 90, 180, 270, 45, 135, 225, 315):
        t = math.radians(a)
        b.append(arrow(200 + 156 * math.cos(t), 220 + 156 * math.sin(t), 200 + 120 * math.cos(t), 220 + 120 * math.sin(t),
                       "#e63946", 5, 12))
    for x, y, r in ((170, 90, 12), (186, 70, 16), (206, 52, 14), (230, 76, 10), (214, 34, 10)):
        b.append(f'<circle cx="{x}" cy="{y - 30}" r="{r}" fill="#e9ecef"/>')
    return svg(b, "#cfe8f3")


def veg_bag(x, y, c, dots):
    rnd = random.Random(int(x * 7 + y))
    out = [f'<rect x="{x}" y="{y}" width="64" height="40" rx="10" fill="{c}" opacity=".85"/>',
           f'<rect x="{x + 6}" y="{y - 4}" width="52" height="8" rx="3" fill="#e9ecef"/>']
    for _ in range(9):
        out.append(f'<circle cx="{f(x + rnd.uniform(10, 54))}" cy="{f(y + rnd.uniform(10, 34))}" r="4" fill="{dots}"/>')
    return "".join(out)


def icicles(x, y, w):
    return "".join(f'<polygon points="{x + k * 16},{y} {x + k * 16 + 10},{y} {x + k * 16 + 5},{y + 8 + (k % 3) * 4}" fill="#fff"/>'
                   for k in range(int(w // 16)))


def preserve():
    b = ['<rect y="350" width="400" height="50" fill="#adb5bd"/>',
         '<rect x="60" y="30" width="230" height="330" rx="12" fill="#e9ecef"/>',
         '<rect x="74" y="44" width="202" height="302" rx="6" fill="#caf0f8"/>',
         '<path d="M290 40 L370 70 V330 L290 356 Z" fill="#dee2e6"/>',
         '<rect x="350" y="170" width="8" height="60" rx="3" fill="#adb5bd"/>',
         '<path d="M74 140 H276 M74 240 H276" stroke="#a8dadc" stroke-width="6"/>',
         veg_bag(84, 94, "#2d6a4f", "#80b918"), veg_bag(160, 94, "#ffd166", "#f4a261"),
         veg_bag(84, 194, "#e76f51", "#f77f00"), veg_bag(160, 194, "#80b918", "#ffd166"),
         veg_bag(84, 294, "#bc4749", "#e63946"), veg_bag(160, 294, "#2d6a4f", "#80b918"),
         '<rect x="74" y="44" width="202" height="8" fill="#fff"/>',
         icicles(80, 52, 194), icicles(80, 146, 194), icicles(80, 246, 194),
         '<circle cx="250" cy="110" r="10" fill="#fff" opacity=".6"/><circle cx="262" cy="100" r="7" fill="#fff" opacity=".5"/>',
         '<circle cx="250" cy="210" r="9" fill="#fff" opacity=".6"/><circle cx="250" cy="310" r="10" fill="#fff" opacity=".6"/>']
    return svg(b, "#f1faee")


def bull(x, y, k=1.0):
    """A big bull standing on (x, y), facing left."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<path d="M90 -110 Q118 -100 116 -60" fill="none" stroke="#3d2c2e" stroke-width="6" stroke-linecap="round"/>'
            '<path d="M-50 -60 V0 M-26 -60 V0 M50 -60 V0 M74 -60 V0" stroke="#3d2c2e" stroke-width="18" stroke-linecap="round"/>'
            '<ellipse cx="14" cy="-104" rx="90" ry="58" fill="#5c4033"/>'
            '<ellipse cx="-70" cy="-120" rx="40" ry="38" fill="#5c4033"/>'
            '<path d="M-96 -146 Q-124 -150 -122 -176 Q-110 -158 -90 -158 Z M-48 -150 Q-24 -160 -18 -184 Q-38 -168 -56 -160 Z" fill="#f8f9fa"/>'
            '<ellipse cx="-96" cy="-100" rx="24" ry="18" fill="#9c6644"/>'
            f'<circle cx="-106" cy="-100" r="3.5" fill="{INK}"/><circle cx="-90" cy="-100" r="3.5" fill="{INK}"/>'
            f'<circle cx="-74" cy="-132" r="5" fill="{INK}"/>'
            f'<path d="M-88 -142 L-62 -136" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            '<circle cx="-132" cy="-108" r="7" fill="#e9ecef" opacity=".8"/><circle cx="-146" cy="-114" r="5" fill="#e9ecef" opacity=".7"/></g>')


def defied():
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         bull(270, 336, .92),
         barking_dog(60, 334, .55),
         '<path d="M136 270 l14 -6 M138 284 l16 0 M136 298 l14 6" stroke="#e76f51" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#e3f2fd")


def leaf(x, y, rot, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({k})">'
            '<path d="M-50 0 Q0 -36 50 0 Q0 36 -50 0 Z" fill="#52b788"/><path d="M-50 0 H50" stroke="#2d6a4f" stroke-width="3"/></g>')


def big_butterfly(x, y):
    return (f'<g transform="translate({x} {y})">'
            '<ellipse cx="-34" cy="-24" rx="38" ry="28" fill="#f4a261" transform="rotate(-20 -34 -24)"/>'
            '<ellipse cx="34" cy="-24" rx="38" ry="28" fill="#f4a261" transform="rotate(20 34 -24)"/>'
            '<ellipse cx="-24" cy="24" rx="24" ry="18" fill="#e76f51"/><ellipse cx="24" cy="24" rx="24" ry="18" fill="#e76f51"/>'
            '<circle cx="-40" cy="-26" r="8" fill="#ffd166"/><circle cx="40" cy="-26" r="8" fill="#ffd166"/>'
            f'<ellipse cx="0" cy="0" rx="7" ry="36" fill="{INK}"/>'
            f'<path d="M-3 -34 Q-10 -56 -22 -58 M3 -34 Q10 -56 22 -58" fill="none" stroke="{INK}" stroke-width="3"/>'
            f'<circle cx="-22" cy="-58" r="4" fill="{INK}"/><circle cx="22" cy="-58" r="4" fill="{INK}"/></g>')


def transformed():
    b = ['<path d="M0 90 Q200 70 400 96" fill="none" stroke="#7f5539" stroke-width="10" stroke-linecap="round"/>',
         leaf(80, 290, 0, 1.2),
         # caterpillar on its leaf
         '<circle cx="50" cy="268" r="10" fill="#80b918"/><circle cx="66" cy="264" r="11" fill="#80b918"/>'
         '<circle cx="84" cy="262" r="11" fill="#80b918"/><circle cx="102" cy="264" r="11" fill="#80b918"/>'
         '<circle cx="120" cy="260" r="12" fill="#80b918"/>',
         f'<circle cx="124" cy="256" r="2.5" fill="{INK}"/><path d="M120 248 l-2 -10 M126 248 l4 -9" stroke="{INK}" stroke-width="2"/>',
         arrow(140, 200, 172, 200, "#e63946", 5, 14),
         # the chrysalis hanging from the branch
         '<path d="M200 82 V112" stroke="#7f5539" stroke-width="3"/>',
         '<path d="M200 112 Q228 140 216 190 Q200 216 184 190 Q172 140 200 112 Z" fill="#a3b18a"/>',
         '<path d="M188 150 Q200 156 212 150 M186 170 Q200 176 214 170" fill="none" stroke="#6a994e" stroke-width="3"/>',
         arrow(230, 200, 262, 200, "#e63946", 5, 14),
         big_butterfly(314, 200),
         sparkle(370, 140, 9, "#ffd166"), sparkle(290, 260, 7, "#ffd166")]
    return svg(b, "#e8f5e9")


def ineffective():
    rnd = random.Random(45)
    b = ['<rect y="330" width="400" height="70" fill="#6c757d"/>',
         '<ellipse cx="200" cy="350" rx="110" ry="14" fill="#90e0ef" opacity=".7"/>']
    for _ in range(110):
        x, y = rnd.uniform(0, 400), rnd.uniform(0, 330)
        b.append(f'<path d="M{f(x)} {f(y)} l-6 16" stroke="#90e0ef" stroke-width="3" stroke-linecap="round"/>')
    b += ['<ellipse cx="200" cy="6" rx="210" ry="34" fill="#495057"/>',
          person(200, 346, 1.15, SKIN[1], "#e9c46a", "#264653", "#5c4033", "short", mood="frown",
                 brows="M-14 -188 L-3 -192 M3 -192 L14 -188",
                 larm=((-12, 40), (-16, 72)), rarm=((24, -20), (20, -60))),
          '<path d="M224 74 V122" stroke="#495057" stroke-width="3"/>',
          '<path d="M204 76 Q224 58 244 76 Z" fill="#e63946"/>',
          '<path d="M176 136 q-3 8 0 10 q3 -2 0 -10 Z M220 160 q-3 8 0 10 q3 -2 0 -10 Z M172 230 q-3 8 0 10 q3 -2 0 -10 Z '
          'M228 250 q-3 8 0 10 q3 -2 0 -10 Z M196 300 q-3 8 0 10 q3 -2 0 -10 Z" fill="#4895ef"/>']
    return svg(b, "#8d99ae")


def efficient():
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>',
         '<circle cx="70" cy="70" r="34" fill="#ffd166"/>',
         '<path d="M70 20 V10 M70 120 V130 M20 70 H10 M120 70 H130 M35 35 L28 28 M105 105 L112 112 M35 105 L28 112 M105 35 L112 28" '
         'stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>',
         '<rect x="120" y="200" width="160" height="110" fill="#f8edeb"/>',
         '<polygon points="100,206 200,124 300,206" fill="#bc4749"/>',
         '<rect x="186" y="250" width="32" height="60" fill="#7f5539"/>',
         '<rect x="136" y="226" width="34" height="30" fill="#caf0f8"/><rect x="232" y="226" width="34" height="30" fill="#caf0f8"/>']
    for k in range(3):
        x0 = 128 + k * 26
        b.append(f'<polygon points="{x0},{196 - k * 21} {x0 + 24},{176 - k * 21} {x0 + 44},{192 - k * 21} {x0 + 20},{212 - k * 21}" '
                 'fill="#264653" stroke="#4895ef" stroke-width="2"/>')
    b += [# the wind turbine
          '<path d="M340 310 L346 130 H350 L356 310 Z" fill="#f8f9fa"/>']
    for a in (-90, 30, 150):
        t = math.radians(a)
        b.append(f'<path d="M348 130 L{f(348 + 70 * math.cos(t) - 6 * math.sin(t))} {f(130 + 70 * math.sin(t) + 6 * math.cos(t))} '
                 f'L{f(348 + 70 * math.cos(t))} {f(130 + 70 * math.sin(t))} Z" fill="#f8f9fa" stroke="#adb5bd" stroke-width="2"/>')
    b += ['<circle cx="348" cy="130" r="7" fill="#adb5bd"/>',
          sparkle(200, 96, 10, "#ffd166")]
    return svg(b, "#e3f2fd")


def imitate():
    tune = (("#e63946", 0, 0), ("#2a9d8f", 30, -14), ("#7209b7", 60, 4))
    b = ['<path d="M0 140 Q120 130 220 146" fill="none" stroke="#7f5539" stroke-width="12" stroke-linecap="round"/>',
         '<path d="M400 300 Q260 290 150 306" fill="none" stroke="#7f5539" stroke-width="12" stroke-linecap="round"/>',
         bird(110, 140, "#457b9d", "#264653", k=2.2),
         '<polygon points="146,88 162,94 146,98" fill="#f4a261"/>']
    for c, dx, dy in tune:
        b.append(note(186 + dx, 90 + dy, c, 1.1))
    for k, x in enumerate((210, 268, 326)):
        b.append(bird(x, 300, "#a8dadc", "#457b9d", k=1.1))
        b.append(f'<polygon points="{x + 18},{271} {x + 26},{273} {x + 18},{276}" fill="#f4a261"/>')
    for c, dx, dy in tune:
        b.append(note(218 + dx * 1.2, 230 + dy * .6, c, .8))
    b += ['<path d="M200 130 Q240 170 230 196" fill="none" stroke="#adb5bd" stroke-width="3" stroke-dasharray="6 6"/>',
          arrow(232, 186, 232, 204, "#adb5bd", 3, 10)]
    return svg(b, "#fff1e6")


def competent():
    b = ['<rect y="330" width="400" height="70" fill="#dee2e6"/>',
         '<rect x="20" y="40" width="80" height="100" fill="#fff" stroke="#dee2e6" stroke-width="3"/>',
         '<path d="M60 70 V110 M40 90 H80" stroke="#2a9d8f" stroke-width="10"/>',
         '<rect x="60" y="262" width="80" height="12" rx="4" fill="#9c6644"/><path d="M70 274 V330 M130 274 V330" stroke="#7f5539" stroke-width="7"/>',
         person(110, 350, .95, SKIN[3], "#ffd166", "#264653", "#1b1b1b", "short", mood="smile",
                lleg=((22, 4), (26, 46)), rleg=((32, 4), (36, 46)),
                larm=((14, 40), (30, 56)), rarm=((34, 10), (74, 14))),
         shadow(280, 334, 30),
         person(280, 332, 1.05, SKIN[1], "#2a9d8f", "#2a9d8f", "#5c4033", "bun", mood="smile",
                larm=((-30, 20), (-64, 30)), rarm=((-20, 40), (-58, 44))),
         # the bandage going on
         '<rect x="166" y="198" width="40" height="18" rx="5" fill="#fff"/>',
         '<path d="M174 198 l6 18 M186 198 l6 18 M198 198 l6 18" stroke="#dee2e6" stroke-width="2"/>',
         '<circle cx="222" cy="214" r="12" fill="#fff" stroke="#dee2e6" stroke-width="2"/><circle cx="222" cy="214" r="4" fill="#dee2e6"/>',
         '<path d="M206 206 L214 210" stroke="#fff" stroke-width="8"/>',
         '<rect x="320" y="290" width="60" height="40" rx="5" fill="#f8f9fa" stroke="#adb5bd" stroke-width="2"/>'
         '<path d="M350 298 V322 M338 310 H362" stroke="#2a9d8f" stroke-width="6"/>',
         f'<circle cx="216" cy="198" r="8" fill="{SKIN[1]}"/><circle cx="230" cy="222" r="8" fill="{SKIN[1]}"/>']
    return svg(b, "#f1faee")


def offended():
    hat = ('<path d="M-30 -196 Q-36 -250 0 -252 Q36 -250 30 -196 Z" fill="#7209b7"/>'
           '<ellipse cx="0" cy="-196" rx="46" ry="9" fill="#7209b7"/>'
           '<rect x="-30" y="-212" width="60" height="10" fill="#ffd166"/>'
           '<circle cx="22" cy="-226" r="12" fill="#ff8fab"/><circle cx="22" cy="-226" r="5" fill="#ffd166"/>'
           '<path d="M-20 -240 Q-50 -290 -6 -296" fill="none" stroke="#2a9d8f" stroke-width="8" stroke-linecap="round"/>')
    b = ['<rect y="330" width="400" height="70" fill="#d6ccc2"/>',
         shadow(110, 344, 30),
         person(110, 342, 1.0, SKIN[0], "#e76f51", "#264653", "#e9c46a", "short", mood="grin",
                larm=((-4, 36), (8, 58)), rarm=((30, -16), (64, -30))),
         '<path d="M80 150 l-12 -8 M78 166 l-14 0" stroke="#e76f51" stroke-width="4" stroke-linecap="round"/>',
         shadow(290, 344, 30),
         person(290, 342, 1.05, SKIN[2], "#2a9d8f", "#264653", "#1b1b1b", "bun", mood="sidenm",
                brows="M-14 -186 L-3 -192 M3 -192 L14 -186", rot=-6,
                larm=((0, 0), (0, 0)), rarm=((0, 0), (0, 0)),
                extra=crossed_arms("#2a9d8f", "#21867a", SKIN[2]) + hat
                      + f'<path d="M-2 -163 Q5 -169 12 -163" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'),
         '<path d="M330 120 l12 -10 M336 136 l16 -4" stroke="#e63946" stroke-width="4" stroke-linecap="round"/>']
    return svg(b, "#f8f9fa")


def counteract():
    b = ['<rect y="320" width="400" height="80" fill="#6c757d"/>',
         '<rect x="250" y="120" width="150" height="200" fill="#9c6644"/>',
         '<rect x="276" y="150" width="40" height="40" fill="#343a40"/><rect x="336" y="150" width="40" height="40" fill="#343a40"/>',
         '<path d="M240 320 Q230 250 270 220 Q260 260 290 250 Q280 190 330 160 Q324 210 350 220 Q360 180 390 160 Q400 220 400 320 Z" fill="#e63946"/>',
         '<path d="M270 320 Q266 270 296 250 Q296 280 318 270 Q316 230 346 210 Q346 250 370 250 Q384 280 380 320 Z" fill="#f77f00"/>',
         '<path d="M300 320 Q300 290 322 280 Q326 300 344 290 Q356 300 352 320 Z" fill="#ffd166"/>',
         shadow(90, 334, 30),
         person(90, 332, 1.05, SKIN[1], "#343a40", "#343a40", "#5c4033", "short", mood="flat",
                brows="M-14 -190 L-3 -188 M3 -188 L14 -190",
                larm=((26, 10), (50, 4)), rarm=((30, 0), (60, -6)),
                extra='<path d="M-30 -194 Q-32 -224 0 -226 Q32 -224 30 -194 Z" fill="#e63946"/>'
                      '<ellipse cx="0" cy="-194" rx="38" ry="7" fill="#e63946"/>'
                      '<path d="M-28 -120 H28 M-28 -100 H28" stroke="#ffd166" stroke-width="6"/>'),
         '<path d="M150 190 L176 178" stroke="#495057" stroke-width="12" stroke-linecap="round"/>',
         '<path d="M30 340 Q60 300 130 200 L150 190" fill="none" stroke="#e63946" stroke-width="10" stroke-linecap="round"/>',
         '<path d="M178 176 Q250 110 300 230" fill="none" stroke="#4895ef" stroke-width="16" stroke-linecap="round"/>',
         '<path d="M180 176 Q250 118 296 226" fill="none" stroke="#a8dadc" stroke-width="5" stroke-linecap="round"/>',
         '<circle cx="300" cy="236" r="14" fill="#90e0ef"/><circle cx="314" cy="226" r="10" fill="#caf0f8"/>',
         '<circle cx="262" cy="160" r="16" fill="#e9ecef" opacity=".85"/><circle cx="284" cy="140" r="12" fill="#e9ecef" opacity=".8"/>']
    return svg(b, "#cfd8dc")


PICTURES = {
    "amusing": amusing,
    "sensitive": sensitive,
    "detects": detects,
    "regret": regret,
    "visible": visible,
    "popularity": popularity,
    "melodic": melodic,
    "generous": generous,
    "simulate": simulate,
    "demonstrate": demonstrate,
    "organized": organized,
    "carefully": carefully,
    "startle": startle,
    "distant from": distant_from,
    "full of": full_of,
    "appreciated": appreciated,
    "healthy": healthy,
    "decisive": decisive,
    "tolerance": tolerance,
    "blended": blended,
    "disseminate": disseminate,
    "combined": combined,
    "distressed": distressed,
    "curiosity": curiosity,
    "steady": steady,
    "strengthen": strengthen,
    "harbinger": harbinger,
    "bold": bold,
    "mystifying": mystifying,
    "succumb": succumb,
    "assertive": assertive,
    "watched": watched,
    "extensive": extensive,
    "revise": revise,
    "inspecting": inspecting,
    "vigilance": vigilance,
    "signaling": signaling,
    "weaken": weaken,
    "receive": receive,
    "impede": impede,
    "contracted": contracted,
    "preserve": preserve,
    "defied": defied,
    "transformed": transformed,
    "ineffective": ineffective,
    "efficient": efficient,
    "imitate": imitate,
    "competent": competent,
    "offended": offended,
    "counteract": counteract,
}
