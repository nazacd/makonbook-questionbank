"""Batch 2: drawings 31-80 (each function returns one SVG; PICTURES maps word -> function)."""

import math
import random

from common import INK, arrow, bush, carrow, f, svg, zzz

SKIN = ("#f1c27d", "#e0ac69", "#c68642", "#8d5524")


def limb(pts, color, w=14):
    return (f'<polyline points="{" ".join(f"{f(x)},{f(y)}" for x, y in pts)}" fill="none" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def shadow(x, y, rx, ry=6, o=.15):
    return f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(ry)}" fill="#000" opacity="{o}"/>'


def face(kind="smile", brows=None):
    """Eyes and mouth for a head of radius 22 centred at (0, -178)."""
    out = []
    if kind in ("closed", "content"):
        out.append(f'<path d="M-13 -179 Q-8 -174 -3 -179 M3 -179 Q8 -174 13 -179" fill="none" stroke="{INK}" '
                   'stroke-width="3" stroke-linecap="round"/>')
    elif kind == "wide":
        out.append(f'<circle cx="-8" cy="-181" r="5" fill="#fff"/><circle cx="8" cy="-181" r="5" fill="#fff"/>'
                   f'<circle cx="-8" cy="-181" r="2.6" fill="{INK}"/><circle cx="8" cy="-181" r="2.6" fill="{INK}"/>')
    elif kind in ("side", "sidenm"):
        out.append(f'<circle cx="-4" cy="-180" r="3" fill="{INK}"/><circle cx="12" cy="-180" r="3" fill="{INK}"/>')
    elif kind == "sly":
        out.append('<circle cx="-8" cy="-180" r="5.5" fill="#fff"/><circle cx="8" cy="-180" r="5.5" fill="#fff"/>'
                   f'<circle cx="-5" cy="-179" r="3" fill="{INK}"/><circle cx="11" cy="-179" r="3" fill="{INK}"/>'
                   f'<path d="M-14 -182 H-2 M2 -182 H14" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    elif kind == "left":
        out.append(f'<circle cx="-12" cy="-180" r="3" fill="{INK}"/><circle cx="4" cy="-180" r="3" fill="{INK}"/>')
    else:
        out.append(f'<circle cx="-8" cy="-180" r="3" fill="{INK}"/><circle cx="8" cy="-180" r="3" fill="{INK}"/>')
    mouth = {"smile": "M-7 -168 Q0 -161 7 -168", "closed": "M-7 -168 Q0 -162 7 -168",
             "content": "M-7 -168 Q0 -162 7 -168", "flat": "M-6 -166 H6", "side": "M-2 -166 Q4 -168 10 -165",
             "grin": None, "wide": None, "shut": "M-7 -166 Q0 -169 7 -166",
             "left": "M-10 -166 H2", "sidenm": None,
             "sly": "M-7 -167 Q1 -164 8 -170"}[kind]
    if kind == "grin":
        out.append('<path d="M-9 -170 Q0 -158 9 -170 Z" fill="#fff" stroke="#264653" stroke-width="2.5" '
                   'stroke-linejoin="round"/>')
    elif kind == "wide":
        out.append(f'<ellipse cx="0" cy="-164" rx="5" ry="6.5" fill="{INK}"/>')
    elif mouth is None:
        pass
    else:
        out.append(f'<path d="{mouth}" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    if brows:
        out.append(f'<path d="{brows}" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    if kind in ("smile", "closed", "content", "grin"):
        out.append('<circle cx="-14" cy="-170" r="4" fill="#e5989b" opacity=".6"/>'
                   '<circle cx="14" cy="-170" r="4" fill="#e5989b" opacity=".6"/>')
    return "".join(out)


HAIR = {
    "short": "M-23 -176 Q-25 -204 0 -203 Q25 -204 23 -176 Q16 -192 0 -191 Q-14 -192 -23 -176 Z",
    "side": "M-23 -174 Q-26 -206 2 -203 Q26 -202 23 -178 Q8 -186 -6 -192 Q-14 -186 -23 -174 Z",
    "bun": "M-23 -176 Q-25 -204 0 -203 Q25 -204 23 -176 Q16 -194 0 -194 Q-16 -194 -23 -176 Z",
    "cap": "M-24 -180 Q-24 -206 0 -206 Q24 -206 24 -180 Z",
}


def person(x, y, s=1.0, skin=SKIN[0], shirt="#2a9d8f", pants="#264653", hair="#5c4033", style="short",
           larm=((-12, 40), (-16, 76)), rarm=((12, 40), (16, 76)), lleg=((-4, 44), (-4, 86)),
           rleg=((4, 44), (4, 86)), mood="smile", brows=None, extra="", front="", rot=0, long_hair=False,
           skirt=False, tiptoe=False):
    """A simple standing figure about 200*s tall, feet at (x, y). Arm points are relative to the
    shoulders ((-22, -146) and (22, -146)); leg points relative to the hips ((-12, -88), (12, -88))."""
    def path(start, pts):
        return [start] + [(start[0] + dx, start[1] + dy) for dx, dy in pts]
    la, ra = path((-22, -146), larm), path((22, -146), rarm)
    ll, rl = path((-12, -88), lleg), path((12, -88), rleg)
    g = [f'<g transform="translate({f(x)} {f(y)}) scale({s}) rotate({rot} 0 -100)">']
    if long_hair:
        g.append(f'<path d="M-25 -180 Q-28 -140 -20 -128 H20 Q28 -140 25 -180 Z" fill="{hair}"/>')
    for lg in (ll, rl):
        g.append(limb(lg, pants, 17))
        fx, fy = lg[-1]
        if tiptoe:
            g.append(f'<ellipse cx="{f(fx)}" cy="{f(fy + 4)}" rx="6" ry="11" fill="{INK}"/>')
        else:
            g.append(f'<ellipse cx="{f(fx + (3 if lg is rl else -3))}" cy="{f(fy + 2)}" rx="12" ry="6" fill="{INK}"/>')
    if skirt:
        g.append(f'<path d="M-26 -110 L-34 -62 H34 L26 -110 Z" fill="{pants}"/>')
    g.append(f'<rect x="-28" y="-156" width="56" height="72" rx="16" fill="{shirt}"/>')
    g.append(f'<rect x="-6" y="-160" width="12" height="10" fill="{skin}"/>')
    for arm in (la, ra):
        g.append(limb(arm, shirt, 15))
        hx, hy = arm[-1]
        g.append(f'<circle cx="{f(hx)}" cy="{f(hy)}" r="8.5" fill="{skin}"/>')
    g.append(f'<circle cx="0" cy="-178" r="22" fill="{skin}"/>')
    if style != "none":
        g.append(f'<path d="{HAIR[style]}" fill="{hair}"/>')
        if style == "bun":
            g.append(f'<circle cx="0" cy="-206" r="10" fill="{hair}"/>')
    g.append(face(mood, brows))
    g.append(extra)
    g.append('</g>')
    return "".join(g) + front


def sparkle(x, y, r, color="#fff"):
    return (f'<path d="M{f(x)} {f(y - r)} Q{f(x + r * .18)} {f(y - r * .18)} {f(x + r)} {f(y)} '
            f'Q{f(x + r * .18)} {f(y + r * .18)} {f(x)} {f(y + r)} Q{f(x - r * .18)} {f(y + r * .18)} {f(x - r)} {f(y)} '
            f'Q{f(x - r * .18)} {f(y - r * .18)} {f(x)} {f(y - r)} Z" fill="{color}"/>')


def heart(x, y, s, color="#e63946"):
    return (f'<path d="M{f(x)} {f(y + s * .9)} C{f(x - s * 1.4)} {f(y)}, {f(x - s * .8)} {f(y - s * 1.1)}, {f(x)} '
            f'{f(y - s * .35)} C{f(x + s * .8)} {f(y - s * 1.1)}, {f(x + s * 1.4)} {f(y)}, {f(x)} {f(y + s * .9)} Z" '
            f'fill="{color}"/>')


def star(x, y, r, color="#ffd166", k=.45, rot=-90):
    pts = " ".join(f"{f(x + (r if i % 2 == 0 else r * k) * math.cos(math.radians(rot + i * 36)))},"
                   f"{f(y + (r if i % 2 == 0 else r * k) * math.sin(math.radians(rot + i * 36)))}" for i in range(10))
    return f'<polygon points="{pts}" fill="{color}"/>'


def flower(x, y, r, petal, center="#ffd166", n=6, rot=0):
    out = []
    for i in range(n):
        a = math.radians(rot + i * 360 / n)
        out.append(f'<circle cx="{f(x + r * math.cos(a))}" cy="{f(y + r * math.sin(a))}" r="{f(r * .72)}" '
                   f'fill="{petal}"/>')
    out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r * .6)}" fill="{center}"/>')
    return "".join(out)


def puzzle_piece(x, y, s, edges, color, stroke="#fff", sw=3):
    """A jigsaw piece with its square body at (x, y), side s. edges = (top, right, bottom, left),
    each 1 (tab out), -1 (slot in) or 0 (flat), walking clockwise."""
    pts = [(x, y), (x + s, y), (x + s, y + s), (x, y + s)]
    d = f"M{f(x)} {f(y)}"
    for i, e in enumerate(edges):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 4]
        dx, dy = (x2 - x1) / s, (y2 - y1) / s
        nx, ny = dy, -dx  # outward normal for a clockwise walk
        if e == 0:
            d += f" L{f(x2)} {f(y2)}"
            continue
        p = lambda t, n: (x1 + dx * s * t + nx * s * n * e, y1 + dy * s * t + ny * s * n * e)
        pts_ = [p(.42, 0), p(.42, .07), p(.58, .07), p(.58, 0)]
        d += (f" L{f(pts_[0][0])} {f(pts_[0][1])} L{f(pts_[1][0])} {f(pts_[1][1])} "
              f"A{f(s * .13)} {f(s * .13)} 0 1 {1 if e > 0 else 0} {f(pts_[2][0])} {f(pts_[2][1])} "
              f"L{f(pts_[3][0])} {f(pts_[3][1])} L{f(x2)} {f(y2)}")
    return f'<path d="{d} Z" fill="{color}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'


# ---------------------------------------------------------------------------------------------

def skepticism_toward():
    bottle = ('<g transform="translate(150 120) rotate(-12)">'
              '<rect x="-20" y="-30" width="40" height="64" rx="10" fill="#2a9d8f"/>'
              '<rect x="-8" y="-50" width="16" height="22" fill="#2a9d8f"/>'
              '<rect x="-11" y="-60" width="22" height="12" rx="3" fill="#e9c46a"/>'
              '<rect x="-12" y="-20" width="8" height="40" rx="4" fill="#fff" opacity=".5"/></g>')
    b = ['<rect y="320" width="400" height="80" fill="#e9d8c4"/>', shadow(110, 322, 50), shadow(300, 322, 50),
         person(110, 318, 1.15, SKIN[1], "#e9c46a", "#7f5539", "#264653", "side",
                larm=((-14, 34), (-20, 70)), rarm=((30, -10), (34, -46)), mood="grin",
                brows="M-14 -192 L-3 -190 M3 -190 L14 -192"),
         bottle]
    for x, y, r in ((112, 60, 12), (196, 82, 9), (186, 46, 7), (122, 160, 6)):
        b.append(sparkle(x, y, r, "#ffd166"))
    # the doubter, arms folded across the chest
    fold = ('<rect x="-30" y="-128" width="60" height="16" rx="8" fill="#457b9d"/>'
            '<rect x="-30" y="-122" width="60" height="14" rx="7" fill="#3d6a8c"/>'
            f'<circle cx="-28" cy="-120" r="7" fill="{SKIN[2]}"/><circle cx="28" cy="-118" r="7" fill="{SKIN[2]}"/>')
    b.append(person(300, 318, 1.15, SKIN[2], "#457b9d", "#264653", "#e9c46a", "short",
                    larm=((-4, 22),), rarm=((4, 22),), mood="side",
                    brows="M-12 -186 L0 -185 M5 -192 Q12 -199 19 -191", extra=fold))
    return svg(b, "#f6efe6")


def careful():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         '<path d="M0 352 H400 M0 378 H400" stroke="#c08552" stroke-width="3"/>', shadow(170, 334, 40)]
    b.append(person(170, 318, .95, SKIN[0], "#fff", "#264653", "#264653", "short",
                    larm=((-34, 0), (-72, -8)), rarm=((30, -22), (38, -64)),
                    lleg=((-2, 44), (0, 90)), rleg=((2, 44), (4, 90)), mood="shut", tiptoe=True,
                    brows="M-14 -192 L-3 -188 M3 -188 L14 -192",
                    extra=f'<path d="M-9 -152 L0 -146 L9 -152 L9 -142 L0 -146 L-9 -142 Z" fill="{INK}"/>'))
    tray_y = 128
    b.append(f'<rect x="166" y="{tray_y}" width="150" height="8" rx="4" fill="#adb5bd"/>')
    for row, n in enumerate((4, 3, 2, 1)):
        for k in range(n):
            gx = 241 - (n - 1) * 16 + k * 32 + row * 3
            gy = tray_y - row * 30
            b.append(f'<path d="M{gx - 13} {gy - 28} L{gx - 10} {gy} H{gx + 10} L{gx + 13} {gy - 28} Z" '
                     'fill="#caf0f8" stroke="#8ecae6" stroke-width="3" stroke-linejoin="round"/>'
                     f'<path d="M{gx - 6} {gy - 23} V{gy - 8}" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
    b += ['<path d="M190 34 q-12 14 0 28 M300 30 q12 14 0 28" fill="none" stroke="#6c757d" stroke-width="3" '
          'stroke-linecap="round"/>',
          '<path d="M140 128 Q133 142 140 146 Q147 142 140 128 Z" fill="#8ecae6"/>']
    return svg(b, "#fdf6ec")


def assistance():
    b = ['<circle cx="340" cy="60" r="32" fill="#ffd166"/>',
         '<path d="M0 400 V140 Q60 128 150 132 L236 138 L248 400 Z" fill="#8d6e63"/>',
         '<path d="M0 140 Q60 128 150 132 L236 138 L238 152 Q120 144 0 154 Z" fill="#6a994e"/>',
         '<path d="M40 220 L90 210 M30 300 L110 280 M140 250 L190 270 M60 360 L150 340 M170 330 L220 350" '
         'stroke="#7f5539" stroke-width="4" stroke-linecap="round"/>',
         # helper lying on the clifftop, reaching down
         limb(((70, 116), (130, 118)), "#264653", 17), limb(((70, 126), (130, 124)), "#264653", 17),
         f'<ellipse cx="62" cy="121" rx="7" ry="12" fill="{INK}"/>',
         '<rect x="120" y="102" width="82" height="34" rx="14" fill="#e76f51"/>',
         limb(((196, 126), (226, 170), (240, 200)), "#e76f51", 15),
         f'<circle cx="222" cy="100" r="22" fill="{SKIN[2]}"/>',
         '<path d="M200 98 Q198 74 222 76 Q246 76 244 98 Q232 86 222 86 Q210 86 200 98 Z" fill="#1b1b1b"/>',
         f'<circle cx="215" cy="104" r="3" fill="{INK}"/><circle cx="231" cy="104" r="3" fill="{INK}"/>',
         f'<path d="M215 113 Q223 120 231 113" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>']
    # climber hanging below, holding on
    b.append(person(272, 372, .8, SKIN[0], "#2a9d8f", "#457b9d", "#e9c46a", "side",
                    larm=((-14, -34), (-18, -65)), rarm=((24, 30), (44, 40)),
                    lleg=((-12, 40), (-30, 66)), rleg=((8, 42), (2, 86)), mood="grin",
                    extra='<rect x="20" y="-150" width="20" height="48" rx="8" fill="#f4a261"/>'))
    b += [f'<circle cx="242" cy="203" r="9" fill="{SKIN[2]}"/>', arrow(340, 330, 340, 230, INK, 6, 18)]
    return svg(b, "#cfe8f3")


def scrutinize():
    b = ['<polygon points="70,46 126,46 330,340 -60,340" fill="#fff3b0" opacity=".5"/>',
         '<path d="M56 24 H140 L126 58 H70 Z" fill="#457b9d"/>',
         '<rect x="92" y="0" width="12" height="26" fill="#457b9d"/>',
         '<rect x="200" y="250" width="180" height="120" rx="50" fill="#6c757d"/>',
         f'<circle cx="290" cy="170" r="82" fill="{SKIN[1]}"/>',
         '<path d="M208 160 Q205 80 290 84 Q375 80 372 160 Q352 112 290 112 Q228 112 208 160 Z" fill="#adb5bd"/>',
         f'<circle cx="320" cy="176" r="7" fill="{INK}"/>',
         f'<path d="M306 152 L334 160" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>',
         f'<path d="M234 150 L262 142" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>',
         f'<path d="M282 220 Q294 214 306 220" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>',
         # the loupe over one eye
         '<circle cx="254" cy="178" r="36" fill="#1b1b1b"/>',
         '<circle cx="254" cy="178" r="27" fill="#fff"/>',
         '<circle cx="254" cy="178" r="16" fill="#457b9d"/><circle cx="254" cy="178" r="8" fill="#1b1b1b"/>',
         '<circle cx="247" cy="171" r="4" fill="#fff"/>',
         '<rect y="330" width="400" height="70" fill="#7f5539"/>', '<rect y="330" width="400" height="8" fill="#9c6b3c"/>',
         # the gem held in tweezers right in front of the loupe
         '<path d="M118 346 L178 268 M136 350 L186 274" stroke="#ced4da" stroke-width="7" stroke-linecap="round"/>',
         '<polygon points="160,222 210,222 226,240 185,286 144,240" fill="#4895ef"/>',
         '<polygon points="160,222 210,222 198,240 172,240" fill="#a8dadc"/>',
         '<polygon points="144,240 172,240 185,286" fill="#457b9d"/>',
         '<polygon points="198,240 226,240 185,286" fill="#3a86ff"/>',
         sparkle(232, 214, 11), sparkle(140, 214, 8)]
    return svg(b, "#3d405b")



def restricted():
    b = ['<rect y="330" width="400" height="70" fill="#c9ada7"/>',
         '<rect x="120" y="60" width="160" height="272" fill="#9a8c98"/>',
         '<rect x="136" y="76" width="128" height="256" fill="#4a4e69"/>',
         '<circle cx="200" cy="150" r="44" fill="#e63946"/>',
         '<rect x="170" y="141" width="60" height="18" rx="4" fill="#fff"/>',
         shadow(90, 336, 26, 6), shadow(310, 336, 26, 6),
         '<path d="M90 222 Q200 290 310 222" fill="none" stroke="#9d0208" stroke-width="13" stroke-linecap="round"/>',
         '<path d="M90 218 Q200 284 310 218" fill="none" stroke="#e63946" stroke-width="5" stroke-linecap="round" '
         'opacity=".6"/>']
    for x in (90, 310):
        b += [f'<rect x="{x - 5}" y="212" width="10" height="118" fill="#c9a227"/>',
              f'<ellipse cx="{x}" cy="332" rx="24" ry="7" fill="#c9a227"/>',
              f'<circle cx="{x}" cy="210" r="11" fill="#e9c46a"/>']
    b.append(person(352, 380, .5, SKIN[1], "#f4a261", "#457b9d", "#5c4033", "short",
                    mood="flat", brows="M-14 -188 L-4 -192 M4 -192 L14 -188"))
    b.append(shadow(352, 382, 18, 4))
    b.append(person(48, 380, .5, SKIN[3], "#a7c957", "#264653", "#1b1b1b", "short",
                    mood="flat", brows="M-14 -188 L-4 -192 M4 -192 L14 -188"))
    b.append(shadow(48, 382, 18, 4))
    return svg(b, "#f2e9e4")


def cherished():
    album = ('<g transform="rotate(-8 0 -118)"><rect x="-34" y="-146" width="68" height="54" rx="5" fill="#7f5539"/>'
             '<rect x="-27" y="-139" width="40" height="34" rx="3" fill="#e9c46a"/>'
             '<circle cx="-15" cy="-126" r="7" fill="#f4a261"/><circle cx="2" cy="-126" r="7" fill="#e76f51"/>'
             '<rect x="25" y="-146" width="5" height="54" fill="#5c4033"/></g>')
    arms = (limb(((-22, -146), (-34, -122), (8, -108)), "#e76f51", 15) + f'<circle cx="12" cy="-108" r="8.5" fill="{SKIN[0]}"/>'
            + limb(((22, -146), (34, -126), (-4, -124)), "#e76f51", 15) + f'<circle cx="-8" cy="-124" r="8.5" fill="{SKIN[0]}"/>')
    glasses = (f'<circle cx="-8" cy="-180" r="7" fill="none" stroke="{INK}" stroke-width="2"/>'
               f'<circle cx="8" cy="-180" r="7" fill="none" stroke="{INK}" stroke-width="2"/>'
               f'<path d="M-1 -180 H1" stroke="{INK}" stroke-width="2"/>')
    b = ['<circle cx="200" cy="200" r="150" fill="#fde2c8"/>',
         '<rect y="340" width="400" height="60" fill="#e9c46a" opacity=".5"/>', shadow(200, 344, 60),
         person(200, 340, 1.4, SKIN[0], "#e76f51", "#457b9d", "#dee2e6", "bun", larm=((0, 10),), rarm=((0, 10),),
                mood="closed", extra=album + arms + glasses, skirt=True,
                lleg=((-4, 44), (-4, 86)), rleg=((4, 44), (4, 86)))]
    b += [heart(80, 110, 18), heart(320, 90, 22), heart(340, 180, 14, "#f4a261"), heart(60, 200, 13, "#f4a261"),
          heart(300, 40, 11, "#e76f51")]
    return svg(b, "#fff8f0")


def enthusiasm_for():
    rnd = random.Random(21)
    b = [f'<circle cx="{f(rnd.uniform(10, 390))}" cy="{f(rnd.uniform(10, 260))}" r="{rnd.choice((1.5, 2, 2.5))}" '
         'fill="#fff" opacity=".8"/>' for _ in range(40)]
    b += [star(70, 60, 14), star(330, 50, 11), star(360, 150, 9), star(40, 180, 9), star(200, 30, 8),
          '<circle cx="290" cy="90" r="26" fill="#fefae0"/><circle cx="302" cy="82" r="22" fill="#2b2d5c"/>',
          '<path d="M0 340 Q200 320 400 340 V400 H0Z" fill="#2d6a4f"/>']
    # telescope on a tripod
    b += ['<path d="M290 340 L320 250 L350 340 M320 250 V340" fill="none" stroke="#adb5bd" stroke-width="7" '
          'stroke-linecap="round"/>',
          '<g transform="rotate(-38 320 250)"><rect x="268" y="232" width="110" height="34" rx="8" fill="#e9c46a"/>'
          '<rect x="372" y="226" width="16" height="46" rx="5" fill="#f4a261"/>'
          '<rect x="254" y="238" width="18" height="22" rx="4" fill="#f4a261"/></g>']
    b += [shadow(150, 344, 34, 6, .25),
          person(150, 300, .9, SKIN[2], "#e76f51", "#457b9d", "#1b1b1b", "short",
                 larm=((-26, -30), (-44, -66)), rarm=((26, -30), (44, -66)),
                 lleg=((-14, 34), (-8, 66)), rleg=((14, 34), (8, 66)), mood="grin"),
          '<path d="M120 318 v14 M150 316 v18 M180 318 v14" stroke="#a7c957" stroke-width="4" stroke-linecap="round"/>',
          sparkle(90, 120, 10, "#ffd166"), sparkle(214, 112, 10, "#ffd166")]
    return svg(b, "#2b2d5c")


def publicity():
    b = ['<polygon points="160,0 240,0 330,320 70,320" fill="#fff3b0" opacity=".35"/>',
         '<rect y="300" width="400" height="100" fill="#7f5539"/>',
         '<rect y="300" width="400" height="12" fill="#9c6b3c"/>', shadow(200, 304, 40)]
    for x, y, r in ((60, 80, 40), (340, 70, 44), (40, 230, 34), (360, 220, 38), (110, 30, 26), (290, 150, 26)):
        b.append(star(x, y, r, "#fff", .35, rot=-90 + r))
        b.append(star(x, y, r * .55, "#ffd166", .4, rot=-72 + r))
    b.append(person(200, 300, 1.0, SKIN[1], "#2a9d8f", "#264653", "#5c4033", "side",
                    larm=((-14, 36), (-16, 72)), rarm=((26, -26), (40, -60)), mood="grin"))
    # microphones pushed in from both sides
    for x1, y1, x2, y2 in ((0, 170, 150, 140), (400, 150, 252, 132), (20, 300, 158, 170), (380, 290, 244, 166)):
        a = math.atan2(y2 - y1, x2 - x1)
        b.append(f'<line x1="{x1}" y1="{y1}" x2="{f(x2 - 14 * math.cos(a))}" y2="{f(y2 - 14 * math.sin(a))}" '
                 f'stroke="#343a40" stroke-width="9" stroke-linecap="round"/>')
        b.append(f'<circle cx="{f(x2)}" cy="{f(y2)}" r="13" fill="#6c757d"/>')
    # cameras at the bottom
    for x in (40, 130, 270, 360):
        b += [f'<rect x="{x - 34}" y="340" width="68" height="46" rx="8" fill="#343a40"/>',
              f'<rect x="{x - 16}" y="332" width="24" height="12" rx="3" fill="#343a40"/>',
              f'<circle cx="{x}" cy="364" r="15" fill="#6c757d"/><circle cx="{x}" cy="364" r="8" fill="#1b1b1b"/>',
              f'<circle cx="{x - 4}" cy="360" r="3" fill="#fff" opacity=".7"/>']
    return svg(b, "#5c4d7d")


def overshadowed_by():
    b = ['<circle cx="50" cy="50" r="30" fill="#ffd166"/>',
         '<rect y="290" width="400" height="110" fill="#a7c957"/>',
         '<polygon points="112,300 150,292 400,300 400,400 250,400" fill="#264653" opacity=".35"/>',
         '<path d="M112 300 L118 150 H142 L148 300 Z" fill="#7f5539"/>',
         '<ellipse cx="130" cy="300" rx="30" ry="6" fill="#5c4033" opacity=".4"/>']
    for x, y, r in ((130, 110, 72), (80, 150, 46), (182, 150, 50), (100, 70, 44), (165, 70, 46), (132, 40, 40)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#2d6a4f"/>')
    for x, y, r in ((112, 92, 30), (160, 60, 20), (72, 140, 18)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#40916c"/>')
    # the small flower, drooping in the shade
    b += [shadow(310, 362, 18, 4),
          '<path d="M310 362 Q314 316 298 290 Q288 276 270 280" fill="none" stroke="#52796f" stroke-width="6" '
          'stroke-linecap="round"/>',
          '<ellipse cx="300" cy="336" rx="16" ry="6" fill="#52796f" transform="rotate(-30 300 336)"/>',
          '<ellipse cx="322" cy="330" rx="16" ry="6" fill="#52796f" transform="rotate(30 322 330)"/>',
          flower(266, 288, 14, "#b392ac", "#adb5bd", 5, 30)]
    return svg(b, "#cfe8f3")


def surprise_at():
    rnd = random.Random(14)
    colors = ["#e63946", "#ffd166", "#2a9d8f", "#4895ef", "#f4a261", "#a7c957"]
    b = ['<rect y="340" width="400" height="60" fill="#e9c46a" opacity=".45"/>', shadow(250, 344, 40)]
    b.append(person(255, 340, 1.0, SKIN[3], "#457b9d", "#264653", "#1b1b1b", "short", rot=-10,
                    larm=((-30, -20), (-46, -54)), rarm=((30, -20), (46, -54)), mood="wide",
                    brows="M-14 -192 Q-8 -198 -2 -193 M2 -193 Q8 -198 14 -192"))
    for _ in range(30):
        a = rnd.uniform(-160, -20)
        d = rnd.uniform(40, 150)
        x, y = 120 + d * math.cos(math.radians(a)), 228 + d * math.sin(math.radians(a))
        c = rnd.choice(colors)
        if x > 200:
            continue
        if rnd.random() < .5:
            b.append(f'<rect x="{f(x)}" y="{f(y)}" width="9" height="5" fill="{c}" '
                     f'transform="rotate({rnd.randint(0, 180)} {f(x)} {f(y)})"/>')
        else:
            b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="4" fill="{c}"/>')
    b += [shadow(120, 342, 52),
          '<rect x="70" y="250" width="100" height="90" fill="#e76f51"/>',
          '<rect x="112" y="250" width="16" height="90" fill="#ffd166"/>',
          '<g transform="rotate(-30 70 236)"><rect x="60" y="226" width="120" height="24" fill="#f4a261"/>'
          '<rect x="112" y="226" width="16" height="24" fill="#ffd166"/></g>',
          '<path d="M60 220 l-14 -12 M72 200 l-6 -16 M180 236 l16 -6" stroke="#6c757d" stroke-width="3" '
          'stroke-linecap="round"/>']
    return svg(b, "#fff4e6")


def vague():
    town = ('<rect x="70" y="150" width="70" height="200" fill="#6c757d"/>'
            '<polygon points="60,150 105,90 150,150" fill="#6c757d"/>'
            '<rect x="160" y="80" width="80" height="270" fill="#495057"/>'
            '<rect x="194" y="40" width="12" height="40" fill="#495057"/>'
            '<rect x="250" y="180" width="90" height="170" fill="#6c757d"/>'
            + "".join(f'<rect x="{x}" y="{y}" width="14" height="20" fill="#ced4da"/>'
                      for x in (176, 210) for y in (110, 160, 210, 260))
            + "".join(f'<rect x="{x}" y="{y}" width="14" height="18" fill="#ced4da"/>' for x in (266, 304)
                      for y in (210, 260)))
    b = [f'<g filter="url(#fog)" opacity=".75">{town}</g>',
         '<rect y="340" width="400" height="60" fill="#adb5bd"/>']
    for y, o in ((120, .55), (200, .65), (280, .6), (330, .7)):
        b.append(f'<ellipse cx="200" cy="{y}" rx="260" ry="26" fill="#fff" opacity="{o}" filter="url(#soft)"/>')
    return svg(b, "#dfe5ea", '<filter id="fog" x="-20%" y="-20%" width="140%" height="140%">'
               '<feGaussianBlur stdDeviation="9"/></filter>'
               '<filter id="soft" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="10"/>'
               '</filter>')


def struggling():
    turtle = ('<ellipse cx="0" cy="-6" rx="54" ry="8" fill="#000" opacity=".15"/>'
              '<path d="M-60 -12 Q-74 -10 -78 -2" fill="none" stroke="#6a994e" stroke-width="9" stroke-linecap="round"/>'
              f'<path d="M-36 -18 L-50 0 M-12 -18 L-20 0 M14 -18 L22 0 M36 -20 L50 -2" stroke="#6a994e" '
              'stroke-width="13" stroke-linecap="round"/>'
              '<path d="M-58 -16 Q-50 -76 0 -78 Q48 -76 56 -16 Z" fill="#2d6a4f"/>'
              '<path d="M-30 -60 L-10 -50 L-14 -24 M10 -50 L30 -60 M-10 -50 H10 L14 -24 M30 -60 L36 -24" '
              'fill="none" stroke="#52b788" stroke-width="4"/>'
              '<path d="M44 -36 Q70 -50 80 -32" fill="none" stroke="#6a994e" stroke-width="16" stroke-linecap="round"/>'
              '<circle cx="86" cy="-36" r="15" fill="#6a994e"/>'
              f'<path d="M86 -44 l7 3 M86 -41 l7 -3" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>'
              f'<path d="M88 -28 h8" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>')
    rock = ('<circle cx="160" cy="-62" r="62" fill="#8d99ae"/><circle cx="140" cy="-82" r="22" fill="#adb5bd"/>'
            '<path d="M180 -40 l14 -10 M150 -30 l8 6" stroke="#6c757d" stroke-width="4" stroke-linecap="round"/>')
    b = ['<circle cx="340" cy="60" r="30" fill="#ffd166"/>',
         '<polygon points="0,400 0,330 400,150 400,400" fill="#a7c957"/>',
         '<polygon points="0,400 0,350 400,170 400,400" fill="#90be6d"/>',
         f'<g transform="translate(125 294) rotate(-24)">{turtle}{rock}'
         '<path d="M70 -100 Q64 -88 70 -84 Q76 -88 70 -100 Z" fill="#8ecae6"/>'
         '<path d="M50 -110 Q44 -98 50 -94 Q56 -98 50 -110 Z" fill="#8ecae6"/>'
         '</g>']
    return svg(b, "#e3f2fd")



def paper(x, y, rot, w=44, h=56, c="#fff"):
    return (f'<g transform="rotate({rot} {x} {y})"><rect x="{f(x - w / 2)}" y="{f(y - h / 2)}" width="{w}" height="{h}" '
            f'fill="{c}" stroke="#ced4da" stroke-width="2"/>'
            f'<path d="M{f(x - w / 2 + 8)} {f(y - h / 2 + 12)} h{w - 16} M{f(x - w / 2 + 8)} {f(y - h / 2 + 22)} '
            f'h{w - 20} M{f(x - w / 2 + 8)} {f(y - h / 2 + 32)} h{w - 16}" stroke="#adb5bd" stroke-width="2.5"/></g>')


def disorganized():
    b = ['<rect y="330" width="400" height="70" fill="#d4a373"/>',
         '<rect x="40" y="210" width="320" height="16" rx="3" fill="#7f5539"/>',
         '<rect x="54" y="226" width="14" height="110" fill="#6f4518"/>',
         '<rect x="230" y="226" width="116" height="110" fill="#8d6e63"/>',
         '<rect x="238" y="236" width="100" height="40" fill="#6f4518"/>',
         # a drawer pulled out, overflowing
         '<rect x="226" y="284" width="140" height="40" fill="#9c6b3c"/>',
         paper(262, 280, -20, 36, 30), paper(312, 278, 25, 36, 30),
         '<rect x="236" y="296" width="120" height="28" fill="#b08968"/>',
         '<rect x="286" y="306" width="22" height="6" rx="3" fill="#5c4033"/>',
         # a crooked pile of books
         '<g transform="rotate(-8 90 210)"><rect x="60" y="190" width="80" height="20" fill="#e76f51"/></g>',
         '<g transform="rotate(10 95 180)"><rect x="58" y="170" width="76" height="20" fill="#2a9d8f"/></g>',
         '<g transform="rotate(-16 100 152)"><rect x="66" y="142" width="70" height="20" fill="#e9c46a"/></g>',
         '<g transform="rotate(22 104 126)"><rect x="76" y="118" width="62" height="18" fill="#457b9d"/></g>',
         # papers everywhere
         paper(190, 194, -14), paper(250, 190, 18), paper(300, 196, -6), paper(120, 352, 30), paper(200, 356, -12),
         paper(320, 354, 70), paper(40, 300, -40),
         # a tipped mug, spilling over the edge
         '<path d="M336 210 H362 V250 Q362 258 358 262 Q354 256 354 246 V214 Z" fill="#7f5539"/>',
         '<ellipse cx="350" cy="210" rx="16" ry="3" fill="#7f5539"/>',
         '<rect x="300" y="186" width="40" height="24" rx="5" fill="#e63946"/>',
         '<ellipse cx="340" cy="198" rx="4" ry="11" fill="#5c4033"/>',
         '<path d="M310 186 Q318 172 328 186" fill="none" stroke="#e63946" stroke-width="5"/>',
         # a tangle of cable
         '<path d="M150 210 C 150 240, 120 240, 130 260 C 140 290, 190 250, 170 280 C 150 310, 110 280, 120 310 '
         'C 128 334, 160 300, 180 330 C 190 344, 150 350, 140 340" fill="none" stroke="#343a40" stroke-width="4" '
         'stroke-linecap="round"/>']
    return svg(b, "#fdf0d5")


def nurture():
    b = ['<circle cx="340" cy="60" r="34" fill="#ffd166"/>']
    for a in range(0, 360, 30):
        r1, r2 = 44, 58
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(340 + r1 * ca)}" y1="{f(60 + r1 * sa)}" x2="{f(340 + r2 * ca)}" y2="{f(60 + r2 * sa)}" '
                 'stroke="#ffd166" stroke-width="5" stroke-linecap="round"/>')
    b += ['<polygon points="300,90 390,180 260,380 140,380" fill="#fff3b0" opacity=".45"/>',
          '<rect y="352" width="400" height="48" fill="#ddb892"/>', shadow(220, 356, 60),
          '<path d="M160 280 H280 L268 356 H172 Z" fill="#e76f51"/>',
          '<rect x="152" y="270" width="136" height="22" rx="4" fill="#f4a261"/>',
          '<ellipse cx="220" cy="272" rx="60" ry="5" fill="#7f5539"/>',
          '<path d="M220 272 Q218 236 222 214" fill="none" stroke="#52b788" stroke-width="6" stroke-linecap="round"/>',
          '<path d="M221 236 Q196 220 186 230 Q200 246 221 236 Z" fill="#52b788"/>',
          '<path d="M222 222 Q248 200 258 212 Q244 230 222 222 Z" fill="#40916c"/>']
    for x, y in ((180, 168), (196, 190), (176, 204), (204, 150), (188, 226), (164, 186)):
        b.append(f'<path d="M{x} {y - 9} Q{x - 6} {y} {x} {y + 3} Q{x + 6} {y} {x} {y - 9} Z" fill="#4895ef"/>')
    b += ['<g transform="rotate(30 100 110)">'
          '<path d="M40 80 H140 L130 150 H50 Z" fill="#2a9d8f"/>'
          '<path d="M140 92 L210 70 L214 82 L140 112 Z" fill="#2a9d8f"/>'
          '<ellipse cx="214" cy="76" rx="8" ry="14" fill="#264653"/>'
          '<path d="M52 92 Q20 100 30 130 Q36 150 50 140" fill="none" stroke="#2a9d8f" stroke-width="10"/>'
          '<rect x="58" y="96" width="10" height="40" rx="5" fill="#fff" opacity=".4"/></g>',
          f'<circle cx="44" cy="96" r="13" fill="{SKIN[1]}"/>',
          heart(290, 220, 16), heart(140, 300, 11, "#f4a261")]
    return svg(b, "#e8f5e9")


def advice():
    b = ['<rect width="190" height="210" fill="#adb5bd"/>',
         '<ellipse cx="90" cy="60" rx="80" ry="34" fill="#6c757d"/><ellipse cx="150" cy="80" rx="60" ry="26" fill="#6c757d"/>',
         '<path d="M70 96 l-10 22 M100 96 l-10 22 M130 100 l-10 22" stroke="#457b9d" stroke-width="3" '
         'stroke-linecap="round"/>',
         '<circle cx="320" cy="70" r="32" fill="#ffd166"/>',
         '<path d="M0 210 Q100 186 200 204 T400 196 V400 H0Z" fill="#a7c957"/>',
         '<path d="M0 210 Q60 196 150 204 L190 206 V400 H0 Z" fill="#8a9a5b"/>',
         '<path d="M246 400 L262 300 Q240 240 140 200 L160 196 Q262 236 276 286 Q300 236 360 196 L376 200 '
         'Q300 252 290 300 L318 400 Z" fill="#e6ccb2"/>',
         '<path d="M40 214 L52 160 L62 214 Z M80 216 L96 150 L110 216 Z" fill="#495057"/>',
         bush(340, 196, 20), bush(380, 210, 16), bush(290, 186, 14)]
    b += [shadow(90, 382, 24, 5), shadow(176, 384, 32, 6),
          person(90, 380, .66, SKIN[0], "#e9c46a", "#457b9d", "#7f5539", "side", mood="side"),
          person(176, 382, 1.0, SKIN[2], "#2a9d8f", "#264653", "#dee2e6", "short",
                 larm=((-26, 30), (-44, 54)), rarm=((40, -30), (84, -60)), mood="smile"),
          arrow(280, 160, 330, 136, "#e76f51", 6, 16)]
    return svg(b, "#e3f2fd")


def inspect():
    b = ['<rect y="330" width="400" height="70" fill="#adb5bd"/>', shadow(170, 332, 160, 8),
         # car seen from the side, hood raised at the front
         '<path d="M14 310 V262 Q16 244 40 242 L90 238 L132 186 H214 L240 238 H312 Q328 240 328 262 V310 Z" '
         'fill="#e63946"/>',
         '<path d="M142 196 H206 L226 236 H142 Z M100 236 L134 196 H136 V236 Z" fill="#caf0f8"/>',
         '<rect x="14" y="270" width="314" height="8" fill="#9d0208"/>',
         '<rect x="240" y="228" width="84" height="14" fill="#343a40"/>',
         '<rect x="250" y="210" width="30" height="22" rx="4" fill="#6c757d"/>',
         '<rect x="286" y="216" width="26" height="16" rx="3" fill="#adb5bd"/>',
         '<circle cx="300" cy="212" r="7" fill="#e9c46a"/>',
         '<polygon points="234,238 248,234 324,128 300,116" fill="#c1121f"/>',
         '<circle cx="84" cy="310" r="30" fill="#343a40"/><circle cx="84" cy="310" r="13" fill="#adb5bd"/>',
         '<circle cx="268" cy="310" r="30" fill="#343a40"/><circle cx="268" cy="310" r="13" fill="#adb5bd"/>',
         # the beam of the flashlight on the engine
         '<polygon points="286,204 236,226 300,240" fill="#fff3b0" opacity=".8"/>']
    b.append(shadow(356, 334, 26, 5))
    b.append(person(356, 332, .8, SKIN[3], "#457b9d", "#457b9d", "#1b1b1b", "cap", mood="left",
                    larm=((-18, 0), (-34, -12)), rarm=((12, 40), (14, 74)),
                    brows="M-18 -190 L-6 -192 M2 -192 L12 -190"))
    b.append('<g transform="rotate(-24 310 204)"><rect x="286" y="198" width="28" height="13" rx="4" fill="#ffd166"/>'
             '<rect x="281" y="195" width="8" height="19" rx="2" fill="#f4a261"/></g>'
             f'<circle cx="310" cy="205" r="7" fill="{SKIN[3]}"/>')
    return svg(b, "#e9f1f7")


def lift():
    b = ['<rect y="340" width="400" height="60" fill="#ced4da"/>', shadow(200, 344, 50)]
    b.append(person(200, 340, 1.0, SKIN[1], "#e76f51", "#264653", "#5c4033", "short",
                    larm=((-30, -24), (-30, -62)), rarm=((30, -24), (30, -62)),
                    lleg=((-14, 44), (-16, 86)), rleg=((14, 44), (16, 86)), mood="grin",
                    brows="M-15 -192 L-4 -188 M4 -188 L15 -192"))
    b += ['<rect x="118" y="38" width="164" height="104" rx="6" fill="#d4a373"/>',
          '<rect x="190" y="38" width="20" height="104" fill="#e9c46a"/>',
          '<rect x="118" y="38" width="164" height="14" fill="#c08552"/>',
          f'<circle cx="148" cy="138" r="9" fill="{SKIN[1]}"/><circle cx="252" cy="138" r="9" fill="{SKIN[1]}"/>',
          arrow(60, 300, 60, 120, "#2a9d8f", 8, 22), arrow(340, 300, 340, 120, "#2a9d8f", 8, 22)]
    return svg(b, "#f1faee")


def overlooked():
    b = ['<rect y="320" width="400" height="80" fill="#8d6e63"/>',
         '<polygon points="84,156 0,96 0,236" fill="#fff3b0" opacity=".85"/>',
         shadow(160, 324, 40)]
    b.append(person(160, 322, 1.0, SKIN[0], "#2a9d8f", "#264653", "#7f5539", "side", mood="left",
                    larm=((-30, 0), (-44, -20)), rarm=((10, 40), (14, 76)),
                    brows="M-20 -190 L-8 -194 M0 -194 L10 -190"))
    b += ['<rect x="88" y="148" width="34" height="16" rx="5" fill="#495057"/>'
          '<rect x="82" y="144" width="10" height="24" rx="2" fill="#adb5bd"/>',
          f'<circle cx="104" cy="156" r="8.5" fill="{SKIN[0]}"/>',
          # table with the keys, right behind
          '<rect x="260" y="250" width="120" height="12" rx="3" fill="#7f5539"/>',
          '<rect x="270" y="262" width="10" height="60" fill="#6f4518"/><rect x="360" y="262" width="10" height="60" '
          'fill="#6f4518"/>',
          '<g transform="translate(320 240) scale(1.5) translate(-320 -240)">'
          '<circle cx="318" cy="238" r="12" fill="none" stroke="#e9c46a" stroke-width="5"/>'
          '<path d="M328 244 L352 244 M344 244 v6 M350 244 v6" stroke="#e9c46a" stroke-width="7" '
          'stroke-linecap="round"/>'
          '<path d="M306 246 L294 234 M294 234 l-5 5" stroke="#adb5bd" stroke-width="6" stroke-linecap="round"/></g>',
          sparkle(304, 210, 9, "#ffd166"), sparkle(358, 222, 7, "#ffd166"), sparkle(330, 196, 6, "#ffd166")]
    return svg(b, "#3d405b")


def evidence():
    b = ['<rect width="400" height="400" fill="#b08968"/>']
    b += [f'<path d="M0 {y} H400" stroke="#9c6b3c" stroke-width="3"/>' for y in (70, 150, 230, 310, 390)]
    # plaster cast of a footprint
    b += ['<rect x="30" y="40" width="150" height="190" rx="12" fill="#e9ecef" transform="rotate(-8 105 135)"/>',
          '<g transform="rotate(-8 105 135)"><path d="M90 72 Q130 64 134 100 Q138 140 126 160 L124 196 Q118 214 100 210 '
          'Q84 206 86 186 L88 150 Q72 120 74 96 Q76 76 90 72 Z" fill="#adb5bd"/>'
          '<path d="M86 100 h40 M84 122 h46 M92 186 h28" stroke="#ced4da" stroke-width="5"/></g>',
          # fingerprint card
          '<rect x="226" y="40" width="140" height="110" rx="6" fill="#fff" transform="rotate(6 296 95)"/>']
    for k, cx in enumerate((262, 330)):
        for r in range(6, 34, 6):
            b.append(f'<ellipse cx="{cx}" cy="{98 + k * 7}" rx="{r * .75}" ry="{r}" fill="none" stroke="#264653" '
                     'stroke-width="2.5" stroke-dasharray="14 4"/>')
    # muddy boot
    b += ['<path d="M216 210 H262 V290 Q300 296 330 306 Q352 314 350 336 H210 Z" fill="#6f4518"/>',
          '<rect x="208" y="336" width="146" height="14" rx="5" fill="#3e2723"/>',
          '<path d="M210 314 Q240 300 262 318 Q300 300 350 320 L352 336 H210 Z" fill="#8d6e63"/>',
          '<circle cx="232" cy="330" r="6" fill="#8d6e63"/><circle cx="300" cy="340" r="5" fill="#8d6e63"/>',
          '<path d="M216 230 H262 M216 250 H262" stroke="#3e2723" stroke-width="3"/>',
          # magnifying glass over the fingerprints
          '<line x1="90" y1="246" x2="44" y2="300" stroke="#264653" stroke-width="18" stroke-linecap="round"/>',
          '<circle cx="128" cy="196" r="56" fill="#caf0f8" opacity=".35"/>',
          f'<circle cx="128" cy="196" r="56" fill="none" stroke="{INK}" stroke-width="10"/>',
          '<path d="M98 164 A40 40 0 0 1 130 152" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>']
    for x, y, r in ((70, 360, -20), (130, 330, -10)):
        b.append(f'<g transform="rotate({r} {x} {y})"><ellipse cx="{x}" cy="{y}" rx="13" ry="22" fill="#6f4518"/>'
                 f'<ellipse cx="{x}" cy="{y + 30}" rx="10" ry="12" fill="#6f4518"/></g>')
    return svg(b, "#b08968")


def buttress():
    stone, dark = "#d6ccc2", "#b8a99a"
    b = ['<rect y="350" width="400" height="50" fill="#a7c957"/>',
         # the tall nave in the middle
         f'<rect x="150" y="110" width="100" height="240" fill="{stone}"/>',
         f'<polygon points="140,112 200,40 260,112" fill="#8d6e63"/>',
         f'<path d="M184 170 V140 Q200 116 216 140 V170 Z M184 260 V220 Q200 196 216 220 V260 Z" fill="#457b9d"/>',
         '<path d="M188 300 V350 H212 V300 Q200 284 188 300 Z" fill="#7f5539"/>']
    for side in (-1, 1):
        px = 200 + side * 150
        b += [f'<rect x="{px - 22}" y="150" width="44" height="200" fill="{dark}"/>',
              f'<polygon points="{px - 26},150 {px},120 {px + 26},150" fill="#8d6e63"/>',
              f'<rect x="{px - 30}" y="300" width="60" height="50" fill="{dark}"/>',
              f'<path d="M{px - side * 22} 170 Q{200 + side * 90} 150 {200 + side * 50} 150 L{200 + side * 50} 182 '
              f'Q{200 + side * 90} 182 {px - side * 22} 220 Z" fill="{dark}"/>',
              f'<path d="M{px - side * 22} 270 Q{200 + side * 90} 250 {200 + side * 50} 250 L{200 + side * 50} 282 '
              f'Q{200 + side * 90} 282 {px - side * 22} 320 Z" fill="{dark}"/>',
              arrow(px - side * 26, 196, 200 + side * 62, 166, "#e76f51", 6, 16),
              arrow(px - side * 26, 296, 200 + side * 62, 266, "#e76f51", 6, 16)]
    return svg(b, "#e3f2fd")


def profusion_of():
    rnd = random.Random(31)
    colors = ["#e63946", "#ffd166", "#f4a261", "#e76f51", "#fff", "#4895ef", "#8338ec", "#ff8fab"]
    b = ['<path d="M0 120 Q120 96 220 112 T400 104 V400 H0Z" fill="#a7c957"/>',
         '<path d="M0 180 Q150 160 260 176 T400 170 V400 H0Z" fill="#90be6d"/>',
         '<circle cx="330" cy="50" r="26" fill="#ffd166"/>']
    pts = []
    while len(pts) < 190:
        y = rnd.uniform(118, 392)
        x = rnd.uniform(8, 392)
        r = 3 + (y - 110) / 280 * 10
        if all(math.hypot(x - px, y - py) > (r + pr) * 1.05 for px, py, pr in pts):
            pts.append((x, y, r))
    pts.sort(key=lambda p: p[1])
    for x, y, r in pts:
        b.append(f'<path d="M{f(x)} {f(y)} v{f(r * 1.6)}" stroke="#40916c" stroke-width="{f(r * .3)}"/>')
        b.append(flower(x, y, r * .7, rnd.choice(colors), "#ffd166" if rnd.random() < .7 else "#7f5539",
                        rnd.choice((5, 6)), rnd.uniform(0, 60)))
    return svg(b, "#cfe8f3")


def canvas_art(x, y, w, h, wobble=0):
    """A little landscape painting (sun over hills) in the box (x, y, w, h)."""
    j = lambda v: v * wobble
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#caf0f8"/>'
            f'<circle cx="{f(x + w * .72 + j(4))}" cy="{f(y + h * .3 + j(3))}" r="{f(w * .12 + j(2))}" fill="#ffd166"/>'
            f'<path d="M{x} {f(y + h * .75)} Q{f(x + w * .3)} {f(y + h * .45 + j(10))} {f(x + w * .6)} {f(y + h * .7)} '
            f'T{x + w} {f(y + h * .62 - j(8))} V{y + h} H{x} Z" fill="#52b788"/>')


def emulate():
    b = ['<rect y="340" width="400" height="60" fill="#e9d8c4"/>',
         # the painter's big easel
         '<g transform="translate(-22 0)"><path d="M240 350 L262 120 M330 350 L308 120 M285 350 V120" stroke="#7f5539" stroke-width="7" '
         'stroke-linecap="round"/>',
         '<rect x="222" y="104" width="126" height="104" fill="#fff"/>', canvas_art(230, 112, 110, 88),
         '<rect x="222" y="206" width="126" height="8" fill="#7f5539"/></g>',
         # the child's small easel
         '<path d="M70 350 L84 230 M140 350 L126 230 M105 350 V230" stroke="#7f5539" stroke-width="6" '
         'stroke-linecap="round"/>',
         '<rect x="58" y="214" width="94" height="78" fill="#fff"/>', canvas_art(64, 220, 82, 64, .6),
         '<rect x="58" y="290" width="94" height="7" fill="#7f5539"/>',
         shadow(344, 344, 26, 5), shadow(184, 344, 20, 5)]
    b.append(person(346, 342, .9, SKIN[1], "#457b9d", "#264653", "#5c4033", "side", mood="left",
                    larm=((-26, -10), (-48, -36)), rarm=((10, 40), (14, 74))))
    b.append(person(184, 342, .6, SKIN[2], "#e9c46a", "#457b9d", "#1b1b1b", "short", mood="left",
                    larm=((-30, -10), (-54, -40)), rarm=((10, 40), (14, 74))))
    # brushes, in the same stroke
    b += ['<line x1="303" y1="190" x2="278" y2="160" stroke="#e76f51" stroke-width="5" stroke-linecap="round"/>',
          '<circle cx="276" cy="158" r="5" fill="#2a9d8f"/>',
          '<line x1="160" y1="248" x2="140" y2="224" stroke="#e76f51" stroke-width="4" stroke-linecap="round"/>',
          '<circle cx="138" cy="222" r="4" fill="#2a9d8f"/>',
          carrow(220, 80, 160, 30, 110, 190, "#2a9d8f", 5, 14)]
    return svg(b, "#fdf6ec")



def sheep(x, y, flip=False, k=1.0):
    sgn = -1 if flip else 1
    wool = "".join(f'<circle cx="{dx}" cy="{dy}" r="{r}" fill="#fff"/>'
                   for dx, dy, r in ((-22, -40, 16), (0, -46, 18), (22, -40, 16), (-14, -26, 16), (12, -26, 16)))
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sgn * k)} {k})">'
            '<ellipse cx="0" cy="2" rx="30" ry="5" fill="#000" opacity=".12"/>'
            f'<path d="M-18 -14 V2 M-6 -14 V2 M8 -14 V2 M20 -14 V2" stroke="{INK}" stroke-width="5" '
            'stroke-linecap="round"/>' + wool +
            '<ellipse cx="34" cy="-48" rx="13" ry="16" fill="#495057"/>'
            '<ellipse cx="24" cy="-58" rx="8" ry="4" fill="#495057" transform="rotate(-30 24 -58)"/>'
            '<circle cx="38" cy="-52" r="4" fill="#fff"/><circle cx="40" cy="-52" r="2" fill="#1b1b1b"/></g>')


def oddity():
    b = ['<rect y="250" width="400" height="150" fill="#a7c957"/>',
         '<path d="M0 250 Q200 236 400 250" fill="#90be6d"/>',
         '<rect x="10" y="190" width="380" height="8" fill="#b08968"/>',
         '<path d="M30 190 V252 M120 190 V252 M210 190 V252 M300 190 V252 M380 190 V252" stroke="#9c6b3c" '
         'stroke-width="8"/>',
         '<circle cx="60" cy="60" r="28" fill="#ffd166"/>',
         sheep(50, 340), sheep(80, 262, k=.8), sheep(350, 340, True), sheep(320, 262, True, .8),
         # the platypus in the middle
         '<g transform="translate(200 340) scale(1.45) translate(-210 -340)">',
         '<ellipse cx="200" cy="356" rx="58" ry="7" fill="#000" opacity=".15"/>',
         '<ellipse cx="150" cy="330" rx="34" ry="12" fill="#5c4033" transform="rotate(10 150 330)"/>',
         '<ellipse cx="200" cy="320" rx="46" ry="28" fill="#8d6e63"/>',
         '<path d="M182 344 l-6 12 l12 0 Z M214 344 l-4 12 l12 0 Z" fill="#f4a261"/>',
         '<circle cx="238" cy="306" r="18" fill="#8d6e63"/>',
         '<path d="M250 302 Q284 296 286 310 Q284 322 250 316 Z" fill="#457b9d"/>',
         f'<circle cx="240" cy="300" r="3.5" fill="{INK}"/></g>']
    return svg(b, "#cfe8f3")


def collaborators():
    b = ['<rect y="340" width="400" height="60" fill="#ced4da"/>', shadow(190, 344, 60), shadow(70, 352, 30, 5),
         shadow(300, 352, 30, 5), shadow(356, 352, 26, 5),
         # the robot they are building together
         '<rect x="166" y="296" width="18" height="46" fill="#6c757d"/><rect x="198" y="296" width="18" height="46" '
         'fill="#6c757d"/>',
         '<rect x="158" y="334" width="30" height="12" rx="5" fill="#495057"/>'
         '<rect x="194" y="334" width="30" height="12" rx="5" fill="#495057"/>',
         '<rect x="140" y="186" width="100" height="116" rx="14" fill="#457b9d"/>',
         '<rect x="158" y="204" width="64" height="40" rx="6" fill="#a8dadc"/>',
         '<circle cx="170" cy="270" r="8" fill="#e63946"/><circle cx="192" cy="270" r="8" fill="#ffd166"/>'
         '<circle cx="214" cy="270" r="8" fill="#52b788"/>',
         '<rect x="182" y="174" width="16" height="14" fill="#6c757d"/>',
         '<rect x="152" y="120" width="76" height="58" rx="12" fill="#a8dadc"/>',
         '<circle cx="174" cy="148" r="10" fill="#fff"/><circle cx="206" cy="148" r="10" fill="#fff"/>',
         f'<circle cx="176" cy="149" r="5" fill="{INK}"/><circle cx="208" cy="149" r="5" fill="{INK}"/>',
         '<path d="M178 166 H202" stroke="#457b9d" stroke-width="4" stroke-linecap="round"/>',
         '<path d="M190 120 V100" stroke="#6c757d" stroke-width="4"/><circle cx="190" cy="96" r="7" fill="#e63946"/>',
         # its right arm, already fitted
         '<path d="M240 204 Q262 214 262 250" fill="none" stroke="#6c757d" stroke-width="14" stroke-linecap="round"/>',
         '<path d="M252 256 l10 12 l10 -12" fill="none" stroke="#495057" stroke-width="5" stroke-linecap="round"/>']
    # left: fitting the other arm
    b.append(person(70, 350, .9, SKIN[0], "#fff", "#457b9d", "#e9c46a", "bun",
                    larm=((-10, 40), (-12, 76)), rarm=((16, 14), (34, -6)), mood="smile"))
    b += ['<rect x="100" y="198" width="48" height="16" rx="8" fill="#6c757d"/>',
          f'<circle cx="120" cy="213" r="8" fill="{SKIN[0]}"/>']
    # middle right: tightening a bolt
    b.append(person(300, 350, .9, SKIN[3], "#fff", "#264653", "#1b1b1b", "short",
                    larm=((-14, 14), (-22, -8)), rarm=((10, 40), (12, 76)), mood="smile"))
    b += ['<g transform="rotate(-20 250 210)"><rect x="244" y="205" width="34" height="10" rx="4" fill="#adb5bd"/>'
          '<circle cx="244" cy="210" r="10" fill="#adb5bd"/><circle cx="242" cy="210" r="5" fill="#457b9d"/></g>',
          f'<circle cx="260" cy="211" r="8" fill="{SKIN[3]}"/>']
    # right: reading out the plan
    b.append(person(358, 350, .85, SKIN[1], "#fff", "#7f5539", "#5c4033", "side",
                    larm=((-14, 34), (-14, 64)), rarm=((12, 34), (14, 64)), mood="smile"))
    b += ['<rect x="322" y="242" width="72" height="54" rx="3" fill="#4895ef"/>',
          '<rect x="346" y="250" width="22" height="18" fill="none" stroke="#fff" stroke-width="2"/>',
          '<rect x="340" y="270" width="34" height="18" fill="none" stroke="#fff" stroke-width="2"/>',
          '<path d="M330 250 h10 M330 258 h10 M378 252 h10 M378 262 h10" stroke="#fff" stroke-width="2"/>',
          f'<circle cx="330" cy="292" r="7" fill="{SKIN[1]}"/><circle cx="386" cy="292" r="7" fill="{SKIN[1]}"/>',
          sparkle(120, 140, 10, "#ffd166"), sparkle(270, 120, 8, "#ffd166")]
    return svg(b, "#eef4ff")


def gear(cx, cy, R, teeth, rot, color):
    step = 360 / teeth
    r = R - R * .2
    pts = []
    for i in range(teeth):
        a = rot + i * step
        for frac, rad in ((0, r), (.12, R), (.38, R), (.5, r)):
            t = math.radians(a + frac * step)
            pts.append((cx + rad * math.cos(t), cy + rad * math.sin(t)))
    d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts) + " Z"
    return (f'<path d="{d}" fill="{color}"/>'
            f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * .35)}" fill="#fff"/>')


def secretive():
    diary = ('<g transform="rotate(-10 -10 -112)">'
             '<rect x="-36" y="-142" width="50" height="60" rx="4" fill="#2a9d8f"/>'
             '<rect x="-36" y="-142" width="8" height="60" fill="#264653" opacity=".35"/>'
             '<rect x="0" y="-118" width="18" height="10" fill="#7f5539"/>'
             '<path d="M-6 -118 V-123 Q-6 -131 1 -131 Q8 -131 8 -123 V-118" fill="none" stroke="#adb5bd" '
             'stroke-width="3.5"/>'
             '<rect x="-10" y="-119" width="22" height="17" rx="3" fill="#e9c46a"/>'
             f'<circle cx="1" cy="-113" r="2.5" fill="{INK}"/><rect x="0" y="-113" width="2" height="6" fill="{INK}"/></g>')
    arms = (limb(((-22, -146), (-42, -112), (-14, -88)), "#e76f51", 15) + f'<circle cx="-10" cy="-88" r="8.5" fill="{SKIN[1]}"/>'
            + limb(((22, -146), (30, -112), (-2, -100)), "#e76f51", 15) + f'<circle cx="-6" cy="-100" r="8.5" fill="{SKIN[1]}"/>')
    b = ['<rect y="350" width="400" height="50" fill="#cdb4db" opacity=".6"/>', shadow(140, 354, 50), shadow(296, 354, 40),
         # the curious friend, on tiptoe and craning to see
         person(296, 352, 1.15, SKIN[3], "#e9c46a", "#264653", "#1b1b1b", "short", mood="left", tiptoe=True,
                larm=((-24, 20), (-46, 10)), rarm=((12, 40), (14, 74)), lleg=((-2, 44), (0, 80)),
                rleg=((2, 44), (4, 80)), brows="M-20 -195 Q-14 -200 -8 -195 M0 -195 Q6 -200 12 -195"),
         # the diary's owner, holding it tight and turned away, eyeing the friend
         person(140, 352, 1.35, SKIN[1], "#e76f51", "#457b9d", "#7f5539", "side",
                larm=((-20, 34), (8, 58)), rarm=((8, 34), (-24, 46)), mood="sly", extra=diary + arms,
                brows="M-14 -190 L-2 -188 M2 -188 L14 -191"),
         f'<path d="M236 136 q-8 -8 -4 -16 M244 132 q0 -10 6 -14" fill="none" stroke="{INK}" stroke-width="3" '
         'stroke-linecap="round" opacity=".45"/>']
    return svg(b, "#f3effa")


def tenderly():
    bundle = ('<g transform="rotate(-12 0 -112)">'
              '<ellipse cx="4" cy="-112" rx="54" ry="26" fill="#a8dadc"/>'
              '<path d="M-24 -126 Q8 -104 46 -124" fill="none" stroke="#caf0f8" stroke-width="5"/>'
              '<circle cx="-36" cy="-122" r="25" fill="#a8dadc"/>'
              f'<circle cx="-36" cy="-120" r="18" fill="{SKIN[0]}"/>'
              f'<path d="M-46 -120 q4 4 8 0 M-34 -120 q4 4 8 0" fill="none" stroke="{INK}" stroke-width="2.5" '
              'stroke-linecap="round"/>'
              f'<path d="M-40 -111 q3 2 6 0" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/></g>')
    under = limb(((-22, -146), (-44, -106), (14, -88)), "#e76f51", 15) + f'<circle cx="18" cy="-88" r="8.5" fill="{SKIN[2]}"/>'
    over = limb(((22, -146), (44, -118), (24, -116)), "#e76f51", 15) + f'<circle cx="20" cy="-116" r="8.5" fill="{SKIN[2]}"/>'
    b = ['<circle cx="200" cy="190" r="150" fill="#fde2e4"/>', '<rect y="350" width="400" height="50" fill="#f8edeb"/>',
         shadow(200, 352, 60),
         person(200, 350, 1.35, SKIN[2], "#e76f51", "#457b9d", "#3e2723", "bun", larm=((0, 10),), rarm=((0, 10),),
                mood="closed", extra=under + bundle + over, skirt=True, long_hair=True),
         zzz(84, 170, 10), zzz(60, 140, 13, w=4), heart(80, 90, 16), heart(330, 120, 18),
         heart(330, 220, 12, "#f4a261")]
    return svg(b, "#fff8f6")


def decorations():
    rnd = random.Random(5)
    colors = ["#e63946", "#ffd166", "#2a9d8f", "#4895ef", "#f4a261"]
    b = ['<rect y="320" width="400" height="80" fill="#d4a373"/>',
         '<rect x="140" y="140" width="120" height="130" rx="6" fill="#fff" stroke="#e9c46a" stroke-width="8"/>',
         '<path d="M200 140 V270 M140 205 H260" stroke="#e9c46a" stroke-width="6"/>',
         '<rect x="140" y="140" width="120" height="130" fill="#bde0fe" opacity=".5"/>']
    # bunting
    for k, (y0, sag) in enumerate(((20, 60), (60, 50))):
        pts = [(x, y0 + sag * 4 * (x / 400) * (1 - x / 400)) for x in range(0, 401, 2)]
        b.append(f'<polyline points="{" ".join(f"{x},{f(y)}" for x, y in pts)}" fill="none" stroke="#7f5539" '
                 'stroke-width="2.5"/>')
        for j, x in enumerate(range(14 + k * 18, 400, 36)):
            y = y0 + sag * 4 * (x / 400) * (1 - x / 400)
            b.append(f'<polygon points="{x - 12},{f(y)} {x + 12},{f(y)} {x},{f(y + 26)}" fill="{colors[(j + k * 2) % 5]}"/>')
    # paper lanterns
    for x, y, c in ((70, 150, "#e63946"), (330, 150, "#f4a261"), (200, 104, "#ffd166")):
        b += [f'<line x1="{x}" y1="{y - 60}" x2="{x}" y2="{y - 30}" stroke="#7f5539" stroke-width="2"/>',
              f'<rect x="{x - 12}" y="{y - 34}" width="24" height="8" fill="#7f5539"/>',
              f'<ellipse cx="{x}" cy="{y}" rx="30" ry="30" fill="{c}"/>',
              f'<path d="M{x} {y - 30} Q{x - 18} {y} {x} {y + 30} M{x} {y - 30} Q{x + 18} {y} {x} {y + 30}" fill="none" '
              'stroke="#fff" stroke-width="2" opacity=".5"/>',
              f'<rect x="{x - 12}" y="{y + 26}" width="24" height="8" fill="#7f5539"/>',
              f'<path d="M{x - 6} {y + 34} v14 M{x} {y + 34} v18 M{x + 6} {y + 34} v14" stroke="{c}" stroke-width="2"/>']
    # balloons in both corners
    for x, y, c in ((40, 230, "#e63946"), (80, 210, "#4895ef"), (60, 260, "#ffd166"),
                    (320, 220, "#2a9d8f"), (360, 236, "#e76f51"), (340, 266, "#ffd166")):
        sx = 60 if x < 200 else 340
        b += [f'<path d="M{x} {y + 30} Q{(x + sx) / 2 + 8} {y + 70} {sx} 330" fill="none" stroke="#6c757d" stroke-width="2"/>',
              f'<ellipse cx="{x}" cy="{y}" rx="24" ry="29" fill="{c}"/>',
              f'<polygon points="{x - 4},{y + 32} {x + 4},{y + 32} {x},{y + 26}" fill="{c}"/>',
              f'<ellipse cx="{x - 8}" cy="{y - 10}" rx="5" ry="9" fill="#fff" opacity=".45"/>']
    for _ in range(26):
        x, y = rnd.uniform(110, 290), rnd.uniform(290, 390)
        b.append(f'<rect x="{f(x)}" y="{f(y)}" width="8" height="4" fill="{rnd.choice(colors)}" '
                 f'transform="rotate({rnd.randint(0, 180)} {f(x)} {f(y)})"/>')
    return svg(b, "#fdf0d5")


def figurine(x, y, k=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            '<rect x="-30" y="-14" width="60" height="14" rx="3" fill="#6c757d"/>'
            '<ellipse cx="0" cy="-46" rx="26" ry="30" fill="#2a9d8f"/>'
            '<circle cx="6" cy="-86" r="18" fill="#2a9d8f"/>'
            '<polygon points="22,-90 38,-84 22,-80" fill="#e9c46a"/>'
            f'<circle cx="10" cy="-90" r="3.5" fill="{INK}"/>'
            '<path d="M-20 -54 Q-6 -36 14 -50" fill="none" stroke="#52b788" stroke-width="6" stroke-linecap="round"/>'
            '<ellipse cx="-10" cy="-60" rx="7" ry="11" fill="#52b788" opacity=".6"/></g>')


def replicate():
    b = ['<rect y="300" width="400" height="100" fill="#e9d8c4"/>',
         # the original on its stand
         '<rect x="40" y="250" width="100" height="70" fill="#adb5bd"/>',
         '<rect x="32" y="242" width="116" height="12" fill="#ced4da"/>', figurine(90, 242),
         # the printer and the finished copy
         '<rect x="220" y="80" width="160" height="240" rx="10" fill="#343a40"/>',
         '<rect x="234" y="96" width="132" height="190" rx="4" fill="#e9ecef"/>',
         '<rect x="234" y="108" width="132" height="8" fill="#6c757d"/>',
         '<rect x="292" y="104" width="16" height="26" fill="#e76f51"/>',
         '<polygon points="294,130 306,130 300,140" fill="#495057"/>',
         '<rect x="248" y="262" width="104" height="10" fill="#6c757d"/>', figurine(300, 266, .95),
         '<rect x="248" y="296" width="30" height="10" rx="3" fill="#2a9d8f"/>',
         '<circle cx="356" cy="301" r="6" fill="#a7c957"/>',
         arrow(156, 190, 210, 190, INK, 6, 16)]
    return svg(b, "#eef4ff")


def abandon():
    b = ['<rect y="300" width="400" height="100" fill="#8a9a5b"/>',
         '<ellipse cx="80" cy="60" rx="80" ry="28" fill="#adb5bd"/><ellipse cx="300" cy="44" rx="90" ry="26" fill="#adb5bd"/>',
         # the house
         '<rect x="90" y="170" width="220" height="150" fill="#a5a58d"/>',
         '<polygon points="70,176 200,80 330,176" fill="#6b705c"/>',
         '<polygon points="230,120 260,138 248,150 226,142" fill="#3d405b"/>',
         '<rect x="176" y="232" width="48" height="88" fill="#3d405b"/>',
         '<path d="M170 250 L230 270 M170 286 L230 262" stroke="#7f5539" stroke-width="9" stroke-linecap="round"/>']
    for x in (112, 250):
        b += [f'<rect x="{x}" y="200" width="44" height="44" fill="#3d405b"/>',
              f'<polygon points="{x},200 {x + 30},200 {x + 14},214 {x + 20},226 {x},236" fill="#cfd8dc"/>',
              f'<rect x="{x - 4}" y="196" width="52" height="52" fill="none" stroke="#6b705c" stroke-width="6"/>']
    # vines and weeds
    b += ['<path d="M96 320 Q110 270 92 230 Q86 200 104 176 M300 320 Q286 280 304 240" fill="none" stroke="#386641" '
          'stroke-width="5" stroke-linecap="round"/>']
    for x, y in ((96, 290), (104, 250), (90, 214), (300, 290), (296, 260)):
        b.append(f'<ellipse cx="{x + 8}" cy="{y}" rx="8" ry="5" fill="#386641" transform="rotate(-30 {x + 8} {y})"/>')
    rnd = random.Random(17)
    for _ in range(70):
        x = rnd.uniform(0, 400)
        h = rnd.uniform(20, 60)
        b.append(f'<path d="M{f(x)} 400 Q{f(x + rnd.uniform(-10, 10))} {f(400 - h * .6)} {f(x + rnd.uniform(-14, 14))} '
                 f'{f(360 - h)}" fill="none" stroke="{rnd.choice(("#6a994e", "#a7c957", "#588157"))}" stroke-width="4" '
                 'stroke-linecap="round"/>')
    # rusty bicycle lying in the weeds
    b += ['<g transform="rotate(-8 300 360)">'
          '<circle cx="262" cy="362" r="26" fill="none" stroke="#9c6644" stroke-width="5"/>'
          '<circle cx="342" cy="362" r="26" fill="none" stroke="#9c6644" stroke-width="5"/>'
          '<path d="M262 362 L292 330 H328 L342 362 M292 330 L304 362 L328 330 M286 322 H300 M326 330 L322 316 H334" '
          'fill="none" stroke="#bc6c25" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/></g>']
    for _ in range(30):
        x = rnd.uniform(230, 380)
        b.append(f'<path d="M{f(x)} 400 Q{f(x + 4)} 380 {f(x + rnd.uniform(-10, 10))} {f(rnd.uniform(340, 370))}" '
                 'fill="none" stroke="#6a994e" stroke-width="4" stroke-linecap="round"/>')
    b.append('<path d="M30 320 V200 M30 240 L10 220 M30 260 L52 236 M30 220 L44 196" stroke="#5c4033" '
             'stroke-width="6" stroke-linecap="round" fill="none"/>')
    return svg(b, "#cfd8dc")


def ornamental():
    stone, dark = "#e9e4dc", "#c9bfb2"
    b = ['<rect y="300" width="400" height="100" fill="#a7c957"/>',
         bush(30, 290, 40), bush(370, 290, 40), bush(70, 300, 30), bush(330, 300, 30),
         shadow(200, 350, 140, 12),
         # bottom basin with carved flowers
         f'<path d="M60 290 H340 L320 350 H80 Z" fill="{stone}"/>',
         f'<rect x="52" y="280" width="296" height="16" rx="6" fill="{dark}"/>',
         '<path d="M70 284 Q200 272 330 284" fill="#4895ef"/>']
    for x in (110, 160, 240, 290):
        b.append(flower(x, 320, 8, "#d4a373", "#c08552", 5))
    b += [f'<path d="M200 316 m-14 0 q14 -18 28 0 q-14 18 -28 0" fill="#d4a373"/>',
          # pillar with scrolls
          f'<path d="M184 280 Q176 230 190 190 H210 Q224 230 216 280 Z" fill="{stone}"/>',
          f'<path d="M184 260 q-26 -6 -20 -26 q8 -12 18 0 M216 260 q26 -6 20 -26 q-8 -12 -18 0" fill="none" '
          f'stroke="{dark}" stroke-width="7" stroke-linecap="round"/>',
          # upper bowl
          f'<path d="M120 180 H280 Q270 210 200 214 Q130 210 120 180 Z" fill="{stone}"/>',
          f'<rect x="114" y="172" width="172" height="12" rx="5" fill="{dark}"/>',
          '<path d="M124 176 Q200 168 276 176" fill="#4895ef"/>',
          f'<path d="M150 194 q10 10 20 0 q10 10 20 0 q10 10 20 0 q10 10 20 0 q10 10 20 0" fill="none" '
          f'stroke="{dark}" stroke-width="4"/>',
          f'<path d="M192 172 Q186 130 200 110 Q214 130 208 172 Z" fill="{stone}"/>',
          f'<circle cx="200" cy="102" r="12" fill="{dark}"/>',
          # water
          '<path d="M200 96 Q170 60 140 170 M200 96 Q230 60 260 170" fill="none" stroke="#a8dadc" stroke-width="5" '
          'stroke-linecap="round"/>',
          '<path d="M124 186 Q100 210 90 282 M276 186 Q300 210 310 282" fill="none" stroke="#a8dadc" stroke-width="5" '
          'stroke-linecap="round"/>']
    return svg(b, "#e3f2fd")


def bee(x, y, rot=0, k=1.0):
    """A bee heading in direction rot (degrees), kept upright when it flies leftwards."""
    sx = k
    if abs(rot) > 90:
        rot, sx = rot - 180, -k
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(sx)} {k})">'
            '<ellipse cx="-2" cy="-12" rx="8" ry="11" fill="#fff" opacity=".85" transform="rotate(-20 -2 -12)"/>'
            '<ellipse cx="6" cy="-12" rx="8" ry="11" fill="#fff" opacity=".85" transform="rotate(20 6 -12)"/>'
            '<ellipse cx="0" cy="0" rx="16" ry="11" fill="#ffd166"/>'
            f'<path d="M-6 -10 V10 M3 -11 V11" stroke="{INK}" stroke-width="4"/>'
            f'<circle cx="14" cy="-2" r="7" fill="{INK}"/><circle cx="16" cy="-4" r="2" fill="#fff"/></g>')


def attract():
    b = ['<rect y="330" width="400" height="70" fill="#a7c957"/>',
         '<path d="M200 330 Q196 280 200 230" stroke="#40916c" stroke-width="10" fill="none"/>',
         '<path d="M200 300 Q170 270 150 286 Q172 310 200 300 Z" fill="#52b788"/>',
         '<path d="M200 280 Q232 252 252 268 Q230 292 200 280 Z" fill="#52b788"/>',
         flower(200, 200, 34, "#e63946", "#ffd166", 7)]
    for x, y, cx, cy, ex, ey in ((30, 40, 60, 150, 148, 168), (370, 50, 340, 140, 252, 164), (20, 300, 80, 250, 152, 228),
                                 (380, 290, 330, 250, 250, 230), (200, 20, 240, 60, 210, 140)):
        b.append(f'<path d="M{x} {y} Q{cx} {cy} {ex} {ey}" fill="none" stroke="#6c757d" stroke-width="3" '
                 'stroke-dasharray="8 7" stroke-linecap="round"/>')
        ang = math.degrees(math.atan2(ey - cy, ex - cx))
        b.append(bee(cx + (ex - cx) * .55, cy + (ey - cy) * .55, ang, 1.2))
    return svg(b, "#fff8e1")


def imitation():
    b = ['<rect y="330" width="400" height="70" fill="#b08968"/>',
         # the original, framed in gold
         '<rect x="22" y="80" width="170" height="200" fill="#c9a227"/>',
         '<rect x="30" y="88" width="154" height="184" fill="#e9c46a"/>',
         '<rect x="40" y="98" width="134" height="164" fill="#caf0f8"/>',
         '<circle cx="138" cy="138" r="18" fill="#f4a261"/>',
         '<polygon points="40,262 100,160 150,262" fill="#457b9d"/><polygon points="100,262 140,200 174,262 Z" '
         'fill="#2a9d8f"/>',
         '<polygon points="84,188 100,160 116,188 108,184 100,190 92,184" fill="#fff"/>',
         '<rect x="40" y="244" width="134" height="18" fill="#52b788"/>',
         sparkle(28, 72, 10, "#ffd166"), sparkle(196, 290, 8, "#ffd166"),
         # the clumsy copy, crooked on its nail
         '<circle cx="300" cy="96" r="4" fill="#5c4033"/>',
         '<path d="M300 96 L254 130 M300 96 L352 118" stroke="#5c4033" stroke-width="2"/>',
         '<g transform="rotate(9 300 210)">'
         '<rect x="228" y="120" width="146" height="176" fill="#8d6e63"/>',
         '<rect x="236" y="128" width="130" height="160" fill="#e9f5f8"/>',
         '<circle cx="320" cy="170" r="22" fill="#e63946"/>',
         '<path d="M238 288 L282 196 Q290 186 296 200 L340 288 Z" fill="#6c757d"/>',
         '<path d="M290 288 L322 224 L364 288 Z" fill="#6a994e"/>',
         '<path d="M236 272 Q270 262 300 276 T366 270 V288 H236 Z" fill="#a7c957"/></g>']
    return svg(b, "#f2e9e4")



def refusing():
    b = ['<rect x="60" y="300" width="240" height="120" rx="60" fill="#e9c46a"/>',
         f'<circle cx="170" cy="190" r="100" fill="{SKIN[0]}"/>',
         '<path d="M70 180 Q60 80 170 84 Q280 80 270 180 Q250 120 210 118 Q190 136 160 124 Q120 128 70 180 Z" '
         'fill="#7f5539"/>',
         f'<circle cx="64" cy="200" r="16" fill="{SKIN[0]}"/>',
         # eyes squeezed shut, lips pressed tight
         f'<path d="M108 182 L128 190 L108 198 M212 182 L192 190 L212 198" fill="none" stroke="{INK}" stroke-width="5" '
         'stroke-linecap="round" stroke-linejoin="round"/>',
         f'<path d="M104 166 L130 174 M216 166 L190 174" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>',
         f'<path d="M140 240 Q150 234 160 240 Q170 246 180 240" fill="none" stroke="{INK}" stroke-width="5" '
         'stroke-linecap="round"/>',
         '<circle cx="114" cy="226" r="14" fill="#e5989b" opacity=".6"/><circle cx="208" cy="226" r="14" fill="#e5989b" '
         'opacity=".6"/>',
         # the spoon of broccoli, pushed away
         '<line x1="400" y1="190" x2="318" y2="164" stroke="#adb5bd" stroke-width="10" stroke-linecap="round"/>',
         '<ellipse cx="300" cy="158" rx="26" ry="12" fill="#adb5bd" transform="rotate(18 300 158)"/>',
         '<path d="M296 150 V132" stroke="#6a994e" stroke-width="7" stroke-linecap="round"/>',
         '<circle cx="288" cy="124" r="11" fill="#2d6a4f"/><circle cx="304" cy="120" r="12" fill="#40916c"/>'
         '<circle cx="296" cy="110" r="10" fill="#2d6a4f"/>',
         # the hand pushing it
         '<path d="M250 400 Q260 320 290 250" fill="none" stroke="#e9c46a" stroke-width="34" stroke-linecap="round"/>',
         f'<g transform="rotate(24 292 230)" fill="{SKIN[0]}"><rect x="266" y="206" width="52" height="52" rx="16"/>'
         '<rect x="268" y="176" width="11" height="40" rx="5.5"/><rect x="281" y="170" width="11" height="44" rx="5.5"/>'
         '<rect x="294" y="172" width="11" height="42" rx="5.5"/><rect x="307" y="180" width="11" height="36" rx="5.5"/>'
         '<rect x="248" y="220" width="30" height="12" rx="6" transform="rotate(-30 262 226)"/></g>',
         '<path d="M340 214 l18 6 M336 234 l20 2 M344 196 l14 -4" stroke="#6c757d" stroke-width="4" '
         'stroke-linecap="round"/>']
    return svg(b, "#e8f5e9")


def reveal():
    b = ['<rect y="320" width="400" height="80" fill="#6d597a"/>',
         '<rect x="60" y="300" width="200" height="24" rx="4" fill="#355070"/>',
         '<rect x="80" y="324" width="16" height="60" fill="#355070"/><rect x="224" y="324" width="16" height="60" '
         'fill="#355070"/>',
         '<ellipse cx="160" cy="292" rx="80" ry="10" fill="#c9a227"/>',
         '<path d="M90 290 V200 Q90 130 160 128 Q230 130 230 200 V290" fill="#fff8e1" opacity=".35"/>']
    for x in range(90, 231, 20):
        top = 200 - math.sqrt(max(0, 70 ** 2 - (x - 160) ** 2)) * (72 / 70)
        b.append(f'<path d="M{x} 290 V200 Q{x} {f(top + 6)} {f(160 + (x - 160) * .1)} 128" fill="none" '
                 'stroke="#c9a227" stroke-width="4"/>' if x in (90, 230) else
                 f'<line x1="{x}" y1="290" x2="{x}" y2="{f(top)}" stroke="#c9a227" stroke-width="4"/>')
    b += ['<path d="M90 290 V200 Q90 130 160 128 Q230 130 230 200 V290" fill="none" stroke="#c9a227" stroke-width="6"/>',
          '<circle cx="160" cy="118" r="10" fill="#c9a227"/>',
          # the dove
          '<ellipse cx="160" cy="250" rx="36" ry="24" fill="#fff"/>',
          '<path d="M128 246 L104 230 L110 254 Z" fill="#fff"/>',
          '<circle cx="188" cy="226" r="16" fill="#fff"/>',
          '<polygon points="202,224 214,228 202,232" fill="#f4a261"/>',
          f'<circle cx="192" cy="222" r="3" fill="{INK}"/>',
          '<path d="M150 246 Q168 232 180 252" fill="none" stroke="#dee2e6" stroke-width="4"/>',
          '<path d="M150 274 v14 M168 274 v14" stroke="#f4a261" stroke-width="4"/>',
          # the cloth whisked off
          '<path d="M232 120 Q300 60 380 90 Q360 150 390 210 Q320 190 280 230 Q290 170 232 120 Z" fill="#e63946"/>',
          '<path d="M260 140 Q310 120 350 150" fill="none" stroke="#9d0208" stroke-width="5"/>',
          '<rect x="356" y="64" width="44" height="40" fill="#1b1b1b" transform="rotate(-30 378 84)"/>',
          f'<circle cx="370" cy="96" r="13" fill="{SKIN[1]}"/>',
          '<path d="M240 70 l-16 -16 M220 92 l-22 -4 M262 52 l-4 -20" stroke="#ffd166" stroke-width="4" '
          'stroke-linecap="round"/>',
          sparkle(70, 120, 14, "#ffd166"), sparkle(110, 70, 9, "#ffd166"), sparkle(250, 250, 10, "#ffd166"),
          sparkle(60, 230, 8, "#ffd166")]
    return svg(b, "#3d405b")


def wave_bubble(x, y, w, h, tail):
    pts = " ".join(f"{f(x + 18 + t * (w - 36) / 60)},{f(y + h / 2 - math.sin(t / 60 * 6 * math.pi) * h * .28 * (1 if t % 2 == 0 else 1) * (.6 + .4 * math.sin(t / 60 * math.pi)))}"
                   for t in range(61))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="#fff"/>'
            f'<polygon points="{tail}" fill="#fff"/>'
            f'<polyline points="{pts}" fill="none" stroke="#e76f51" stroke-width="5" stroke-linejoin="round" '
            'stroke-linecap="round"/>')


def mimicked():
    b = ['<rect y="320" width="400" height="80" fill="#e9d8c4"/>',
         wave_bubble(20, 60, 150, 80, "60,138 90,138 70,172"),
         wave_bubble(230, 60, 150, 80, "300,138 330,138 316,176"),
         # telephone on a small table
         '<rect x="30" y="268" width="130" height="12" rx="3" fill="#7f5539"/>',
         '<rect x="42" y="280" width="10" height="50" fill="#6f4518"/><rect x="138" y="280" width="10" height="50" '
         'fill="#6f4518"/>',
         '<path d="M52 268 L64 220 H126 L138 268 Z" fill="#e63946"/>',
         '<path d="M48 214 Q95 190 142 214 L136 226 Q95 210 54 226 Z" fill="#9d0208"/>',
         '<circle cx="95" cy="246" r="14" fill="#fff"/><circle cx="95" cy="246" r="5" fill="#9d0208"/>',
         '<path d="M38 200 l-10 -10 M152 200 l10 -10 M30 222 h-12 M160 222 h12" stroke="#6c757d" stroke-width="4" '
         'stroke-linecap="round"/>',
         # parrot on a perch
         '<line x1="260" y1="312" x2="390" y2="312" stroke="#7f5539" stroke-width="10" stroke-linecap="round"/>',
         '<line x1="370" y1="312" x2="370" y2="330" stroke="#7f5539" stroke-width="8"/>',
         '<path d="M318 300 L300 360 L330 360 Z" fill="#2a9d8f"/>',
         '<ellipse cx="320" cy="270" rx="28" ry="40" fill="#52b788"/>',
         '<ellipse cx="330" cy="276" rx="16" ry="30" fill="#2d6a4f"/>',
         '<circle cx="312" cy="222" r="24" fill="#52b788"/>',
         '<path d="M292 214 Q276 220 282 240 Q290 236 296 232 Z" fill="#ffd166"/>',
         '<circle cx="314" cy="216" r="7" fill="#fff"/>', f'<circle cx="312" cy="216" r="3.5" fill="{INK}"/>',
         '<path d="M306 310 v8 M322 310 v8" stroke="#6c757d" stroke-width="4" stroke-linecap="round"/>',
         '<ellipse cx="320" cy="200" rx="10" ry="5" fill="#e63946" transform="rotate(-20 320 200)"/>']
    return svg(b, "#e3f2fd")


def anomaly():
    rnd = random.Random(41)
    b = ['<path d="M0 250 Q200 230 400 250 V400 H0Z" fill="#fff"/>',
         '<path d="M0 300 Q120 284 220 300 T400 296 V400 H0Z" fill="#f1f5f9"/>']
    for x, h in ((50, 110), (120, 80), (300, 100), (360, 130)):
        b.append(f'<path d="M{x} 250 V{250 - h} M{x} {250 - h * .5} l-18 -18 M{x} {250 - h * .7} l16 -16 '
                 f'M{x} {250 - h * .35} l14 -10" stroke="#8d99ae" stroke-width="5" stroke-linecap="round" fill="none"/>')
    for _ in range(50):
        b.append(f'<circle cx="{f(rnd.uniform(5, 395))}" cy="{f(rnd.uniform(5, 390))}" r="{rnd.choice((2, 2.5, 3))}" '
                 'fill="#fff"/>')
    b += ['<g transform="translate(200 322) scale(1.7) translate(-200 -322)">', shadow(200, 322, 30, 5, .12),
          '<path d="M200 322 Q198 280 200 250" stroke="#2d6a4f" stroke-width="6" fill="none"/>',
          '<path d="M200 300 Q176 284 168 296 Q184 312 200 300 Z" fill="#40916c"/>',
          '<path d="M200 284 Q226 264 236 276 Q220 294 200 284 Z" fill="#40916c"/>',
          '<path d="M176 222 Q176 252 200 254 Q224 252 224 222 L212 232 L200 214 L188 232 Z" fill="#e63946"/></g>']
    return svg(b, "#dbe7f0")


def monkey(x, y, flip=False, k=1.0):
    sgn = -1 if flip else 1
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sgn * k)} {k})">'
            '<ellipse cx="0" cy="4" rx="40" ry="6" fill="#000" opacity=".12"/>'
            '<path d="M-24 -10 Q-70 -20 -60 -70 Q-56 -90 -40 -84" fill="none" stroke="#7f5539" stroke-width="8" '
            'stroke-linecap="round"/>'
            '<ellipse cx="0" cy="-40" rx="30" ry="40" fill="#8d6e63"/>'
            '<ellipse cx="4" cy="-32" rx="18" ry="26" fill="#d7b899"/>'
            '<path d="M-14 -6 v8 M14 -6 v8" stroke="#7f5539" stroke-width="12" stroke-linecap="round"/>'
            '<circle cx="-26" cy="-108" r="12" fill="#8d6e63"/><circle cx="26" cy="-108" r="12" fill="#8d6e63"/>'
            '<circle cx="-26" cy="-108" r="6" fill="#d7b899"/><circle cx="26" cy="-108" r="6" fill="#d7b899"/>'
            '<circle cx="0" cy="-104" r="30" fill="#8d6e63"/>'
            '<ellipse cx="6" cy="-98" rx="22" ry="20" fill="#d7b899"/>'
            f'<circle cx="0" cy="-104" r="3.5" fill="{INK}"/><circle cx="16" cy="-104" r="3.5" fill="{INK}"/>'
            f'<path d="M2 -88 Q9 -82 16 -88" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M18 -54 Q48 -60 62 -78" fill="none" stroke="#8d6e63" stroke-width="11" stroke-linecap="round"/>'
            '<circle cx="64" cy="-80" r="8" fill="#d7b899"/></g>')


def banana(x, y, rot):
    return (f'<g transform="rotate({rot} {x} {y})"><path d="M{x - 24} {y} Q{x} {y + 30} {x + 24} {y} '
            f'Q{x} {y + 12} {x - 24} {y} Z" fill="#ffd166" stroke="#e9c46a" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M{x - 22} {y} l-4 -3" stroke="#7f5539" stroke-width="4" stroke-linecap="round"/></g>')


def reciprocates():
    b = ['<rect y="320" width="400" height="80" fill="#a7c957"/>',
         bush(30, 300, 34), bush(370, 300, 34),
         monkey(110, 330), monkey(290, 330, True),
         banana(176, 232, -70),
         '<circle cx="230" cy="238" r="14" fill="#e63946"/><circle cx="225" cy="233" r="4" fill="#fff" opacity=".6"/>'
         '<path d="M230 224 l2 -7" stroke="#6b4226" stroke-width="3" stroke-linecap="round"/>',
         carrow(150, 150, 200, 90, 250, 150, "#e76f51", 6, 16),
         carrow(250, 300, 200, 360, 150, 300, "#2a9d8f", 6, 16)]
    return svg(b, "#e8f5e9")


def acclaim():
    rnd = random.Random(2)
    b = ['<polygon points="160,0 240,0 300,240 100,240" fill="#fff3b0" opacity=".3"/>',
         '<rect x="0" y="220" width="400" height="30" fill="#9c6b3c"/>',
         '<rect x="0" y="0" width="40" height="230" fill="#9d0208"/><rect x="360" y="0" width="40" height="230" '
         'fill="#9d0208"/>',
         '<path d="M0 0 H400 V26 Q300 46 200 26 Q100 46 0 26 Z" fill="#c1121f"/>',
         shadow(200, 224, 40),
         person(200, 222, .95, SKIN[0], "#e9c46a", "#264653", "#7f5539", "bun",
                larm=((-34, -20), (-70, -40)), rarm=((34, -20), (70, -40)), mood="grin")]
    for x, y, r in ((110, 140, 30), (300, 120, 50), (90, 60, -20), (320, 190, 60), (150, 190, 10)):
        b.append(f'<g transform="rotate({r} {x} {y})"><path d="M{x} {y} v26" stroke="#2d6a4f" stroke-width="4"/>'
                 f'<circle cx="{x}" cy="{y}" r="10" fill="#e63946"/><circle cx="{x - 3}" cy="{y - 3}" r="4" '
                 'fill="#ff8fab"/></g>')
    # the audience on its feet, clapping
    colors = ["#457b9d", "#2a9d8f", "#e76f51", "#6c757d", "#f4a261", "#264653"]
    for row, y in enumerate((300, 360)):
        for k in range(6):
            x = 34 + k * 66 + (row * 33) - (16 if row else 0)
            c = colors[(k + row * 3) % 6]
            sk = SKIN[(k + row) % 4]
            b += [f'<path d="M{x - 16} {y - 30} L{x - 26} {y - 72} M{x + 16} {y - 30} L{x + 26} {y - 72}" stroke="{c}" '
                  'stroke-width="10" stroke-linecap="round"/>',
                  f'<circle cx="{x - 26}" cy="{y - 76}" r="7" fill="{sk}"/><circle cx="{x + 26}" cy="{y - 76}" r="7" '
                  f'fill="{sk}"/>',
                  f'<rect x="{x - 26}" y="{y - 34}" width="52" height="80" rx="20" fill="{c}"/>',
                  f'<circle cx="{x}" cy="{y - 48}" r="20" fill="{sk}"/>',
                  f'<path d="M{x - 40} {y - 88} l-6 -8 M{x + 40} {y - 88} l6 -8" stroke="#ffd166" stroke-width="3" '
                  'stroke-linecap="round"/>']
    return svg(b, "#3d405b")


def recognize():
    rnd = random.Random(9)
    b = ['<rect y="300" width="400" height="100" fill="#dee2e6"/>',
         '<rect x="0" y="40" width="400" height="120" fill="#caf0f8"/>',
         '<path d="M0 160 H400 M100 40 V160 M200 40 V160 M300 40 V160" stroke="#adb5bd" stroke-width="6"/>']
    # the crowd, all in gray except the old friend
    for x, y, s in ((40, 300, .55), (90, 296, .58), (150, 302, .55), (270, 298, .56), (320, 302, .55),
                    (370, 296, .58), (220, 300, .56)):
        b.append(person(x, y, s, "#ced4da", "#adb5bd", "#8d99ae", "#8d99ae", "short", mood="flat"))
    b.append(person(250, 306, .62, SKIN[3], "#e76f51", "#264653", "#1b1b1b", "short", mood="grin",
                    rarm=((26, -26), (40, -60))))
    b += [shadow(120, 384, 30, 5),
          person(120, 384, .95, SKIN[0], "#2a9d8f", "#457b9d", "#e9c46a", "bun",
                 larm=((-14, 36), (-16, 74)), rarm=((30, -28), (40, -66)), mood="grin"),
          '<rect x="34" y="320" width="46" height="62" rx="8" fill="#f4a261"/>',
          '<path d="M46 320 V306 H68 V320" fill="none" stroke="#7f5539" stroke-width="5"/>',
          '<path d="M104 180 l-8 -14 M120 174 v-16 M136 180 l8 -14" stroke="#e76f51" stroke-width="4" '
          'stroke-linecap="round"/>',
          f'<path d="M160 200 Q210 160 232 200" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="6 6"/>']
    return svg(b, "#f1faee")


def stretching_toward():
    b = ['<rect x="230" y="30" width="160" height="230" fill="#caf0f8"/>',
         '<circle cx="320" cy="100" r="32" fill="#ffd166"/>',
         '<rect x="226" y="26" width="168" height="238" fill="none" stroke="#fff" stroke-width="10"/>',
         '<path d="M310 26 V264 M226 146 H394" stroke="#fff" stroke-width="8"/>',
         '<polygon points="230,60 230,260 40,330 20,240" fill="#fff3b0" opacity=".45"/>',
         '<rect x="0" y="300" width="400" height="16" fill="#d4a373"/>',
         '<rect x="0" y="316" width="400" height="84" fill="#f2e2d0"/>']
    for x, h, c in ((60, 1.0, "#52b788"), (150, .8, "#40916c"), (220, .6, "#52b788")):
        top = (x + 140 * h, 300 - 200 * h)
        b.append(f'<path d="M{x} 260 Q{x} {f(220 - 60 * h)} {f(top[0])} {f(top[1])}" fill="none" stroke="#2d6a4f" '
                 'stroke-width="6" stroke-linecap="round"/>')
        for t in (.35, .6, .85):
            px = x + (top[0] - x) * t * t
            py = 260 - (260 - top[1]) * t
            b.append(f'<ellipse cx="{f(px + 14)}" cy="{f(py)}" rx="16" ry="8" fill="{c}" transform="rotate(-20 {f(px + 14)} {f(py)})"/>')
        b.append(f'<ellipse cx="{f(top[0] + 8)}" cy="{f(top[1])}" rx="14" ry="9" fill="{c}"/>')
        b += [f'<path d="M{x - 30} 254 H{x + 30} L{x + 24} 300 H{x - 24} Z" fill="#e76f51"/>',
              f'<rect x="{x - 34}" y="250" width="68" height="12" rx="3" fill="#f4a261"/>']
    return svg(b, "#fdf6ec")


def partnership():
    b = ['<rect y="320" width="400" height="80" fill="#e9d8c4"/>',
         puzzle_piece(110, 36, 90, (0, 1, 0, 0), "#2a9d8f", "#fff", 0),
         puzzle_piece(200, 36, 90, (0, 0, 0, -1), "#e76f51", "#fff", 0),
         shadow(80, 324, 36), shadow(320, 324, 36),
         person(80, 322, 1.0, SKIN[1], "#457b9d", "#264653", "#5c4033", "short",
                rarm=((40, 20), (82, 26)), mood="grin"),
         person(320, 322, 1.0, SKIN[3], "#e9c46a", "#7f5539", "#1b1b1b", "bun",
                larm=((-40, 20), (-82, 26)), mood="grin"),
         '<rect x="186" y="186" width="30" height="24" rx="10" fill="#e0ac69"/>',
         '<rect x="184" y="196" width="32" height="20" rx="10" fill="#8d5524" opacity=".85"/>',
         '<path d="M180 176 l-10 -10 M200 170 v-14 M220 176 l10 -10" stroke="#e9c46a" stroke-width="4" '
         'stroke-linecap="round"/>']
    return svg(b, "#f1faee")


def cactus(x, y, h, c="#40916c", hi="#52b788", arms=True):
    w = h * .22
    out = [f'<rect x="{f(x - w / 2)}" y="{f(y - h)}" width="{f(w)}" height="{f(h)}" rx="{f(w / 2)}" fill="{c}"/>',
           f'<rect x="{f(x - w * .2)}" y="{f(y - h + w * .3)}" width="{f(w * .18)}" height="{f(h * .8)}" rx="2" fill="{hi}"/>']
    if arms:
        out += [f'<path d="M{f(x - w / 2)} {f(y - h * .45)} H{f(x - w * 1.3)} V{f(y - h * .8)}" fill="none" stroke="{c}" '
                f'stroke-width="{f(w * .7)}" stroke-linecap="round" stroke-linejoin="round"/>',
                f'<path d="M{f(x + w / 2)} {f(y - h * .6)} H{f(x + w * 1.3)} V{f(y - h * .9)}" fill="none" stroke="{c}" '
                f'stroke-width="{f(w * .7)}" stroke-linecap="round" stroke-linejoin="round"/>']
    return "".join(out)


def thrive():
    b = ['<circle cx="330" cy="70" r="40" fill="#ffd166"/>']
    for a in range(0, 360, 30):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(f'<line x1="{f(330 + 50 * ca)}" y1="{f(70 + 50 * sa)}" x2="{f(330 + 64 * ca)}" y2="{f(70 + 64 * sa)}" '
                 'stroke="#ffd166" stroke-width="6" stroke-linecap="round"/>')
    b += ['<path d="M0 300 Q200 280 400 300 V400 H0Z" fill="#f4d58d"/>',
          cactus(110, 320, 230), cactus(260, 330, 170, "#2d6a4f", "#40916c"),
          flower(110, 84, 10, "#ff8fab", "#ffd166", 6), flower(70, 126, 8, "#e63946", "#ffd166", 6),
          flower(150, 112, 8, "#ffd166", "#f4a261", 6), flower(260, 152, 9, "#e63946", "#ffd166", 6),
          flower(228, 196, 7, "#ff8fab", "#ffd166", 6), flower(296, 176, 7, "#ffd166", "#f4a261", 6)]
    for x, y, r, c in ((40, 340, 24, "#52b788"), (190, 350, 26, "#40916c"), (350, 346, 28, "#52b788"),
                       (320, 370, 18, "#40916c"), (70, 372, 18, "#40916c")):
        b += [f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{f(r * .85)}" fill="{c}"/>',
              f'<path d="M{x} {y - r * .85} V{y + r * .8} M{x - r * .5} {y - r * .7} Q{x - r * .7} {y} {x - r * .5} {y + r * .7} '
              f'M{x + r * .5} {y - r * .7} Q{x + r * .7} {y} {x + r * .5} {y + r * .7}" fill="none" stroke="#2d6a4f" '
              'stroke-width="2"/>',
              flower(x, y - r * .85, r * .3, "#ff8fab" if x % 2 else "#e63946", "#ffd166", 6)]
    return svg(b, "#fff1d6")



def rapid():
    b = ['<circle cx="340" cy="60" r="30" fill="#ffd166"/>',
         '<path d="M0 270 Q200 256 400 270 V400 H0Z" fill="#e9c46a"/>',
         '<path d="M362 268 L360 196 M360 220 L334 196 M360 210 L384 190" fill="none" stroke="#7f5539" '
         'stroke-width="7" stroke-linecap="round"/>',
         '<ellipse cx="358" cy="190" rx="52" ry="14" fill="#6a994e"/>',
         '<path d="M20 274 l4 -14 l4 14 M44 280 l4 -12 l4 12 M370 300 l4 -14 l4 14" fill="none" stroke="#6a994e" '
         'stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
         '<ellipse cx="210" cy="320" rx="110" ry="9" fill="#000" opacity=".12"/>']
    for y, x1, x2 in ((210, 10, 80), (240, 30, 90), (270, 0, 70), (180, 40, 96)):
        b.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#fff" stroke-width="6" stroke-linecap="round"/>')
    cat = "#f4a261"
    b += [f'<path d="M120 216 Q70 200 40 236" fill="none" stroke="{cat}" stroke-width="9" stroke-linecap="round"/>',
          f'<path d="M140 236 L96 270 L70 280 M150 240 L130 290 L110 306" fill="none" stroke="{cat}" stroke-width="13" '
          'stroke-linecap="round" stroke-linejoin="round"/>',
          f'<path d="M262 236 L300 270 L330 268 M250 240 L286 290 L314 296" fill="none" stroke="{cat}" stroke-width="13" '
          'stroke-linecap="round" stroke-linejoin="round"/>',
          f'<ellipse cx="196" cy="224" rx="84" ry="32" fill="{cat}"/>',
          '<ellipse cx="200" cy="238" rx="66" ry="14" fill="#fde2c8"/>',
          f'<path d="M262 214 Q286 196 300 204" fill="none" stroke="{cat}" stroke-width="24" stroke-linecap="round"/>',
          f'<circle cx="310" cy="200" r="22" fill="{cat}"/>',
          f'<circle cx="300" cy="180" r="7" fill="{cat}"/>',
          '<ellipse cx="324" cy="208" rx="10" ry="8" fill="#fde2c8"/>',
          f'<circle cx="314" cy="194" r="3.5" fill="{INK}"/><circle cx="332" cy="204" r="3" fill="{INK}"/>',
          f'<path d="M316 196 Q318 210 312 220" fill="none" stroke="{INK}" stroke-width="2.5"/>']
    rnd = random.Random(3)
    for _ in range(22):
        x, y = rnd.uniform(130, 270), rnd.uniform(200, 248)
        if ((x - 196) / 80) ** 2 + ((y - 224) / 30) ** 2 < 1 and y < 230:
            b.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="3.5" fill="#5c4033"/>')
    for x, y, r in ((60, 300, 12), (40, 290, 9), (84, 310, 8)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ddb892" opacity=".8"/>')
    return svg(b, "#fdf0d5")


def surpassed_by():
    b = ['<rect y="270" width="400" height="130" fill="#e76f51"/>',
         '<path d="M0 300 H400 M0 340 H400" stroke="#fff" stroke-width="3" opacity=".6"/>',
         '<rect x="40" y="130" width="10" height="190" fill="#adb5bd"/><rect x="350" y="130" width="10" height="190" '
         'fill="#adb5bd"/>',
         '<path d="M50 160 Q120 172 168 214 M350 160 Q300 168 276 230" fill="none" stroke="#fff" stroke-width="6" '
         'stroke-linecap="round"/>']
    # runner behind, overtaken
    b.append(person(120, 318, .8, SKIN[0], "#457b9d", "#264653", "#e9c46a", "short", mood="flat",
                    brows="M-14 -188 L-4 -192 M4 -192 L14 -188",
                    larm=((-20, 10), (-10, 40)), rarm=((24, 20), (34, -4)), lleg=((-10, 40), (-24, 70)),
                    rleg=((8, 30), (26, 50))))
    # winner, breaking the tape
    b.append(person(232, 330, 1.0, SKIN[3], "#2a9d8f", "#264653", "#1b1b1b", "short", mood="grin",
                    larm=((-28, -30), (-40, -66)), rarm=((28, -30), (40, -66)), lleg=((-12, 40), (-28, 74)),
                    rleg=((10, 30), (30, 48))))
    b.append(carrow(90, 120, 160, 40, 220, 100, INK, 5, 14))
    return svg(b, "#eaf4f4")


def duck(x, y, k=1.0, flip=False):
    sgn = -1 if flip else 1
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sgn * k)} {k})">'
            '<ellipse cx="0" cy="2" rx="18" ry="4" fill="#000" opacity=".12"/>'
            '<ellipse cx="0" cy="-14" rx="18" ry="13" fill="#ffd166"/>'
            '<circle cx="-12" cy="-30" r="10" fill="#ffd166"/>'
            '<polygon points="-20,-31 -30,-28 -20,-25" fill="#f4a261"/>'
            f'<circle cx="-14" cy="-32" r="2" fill="{INK}"/>'
            '<path d="M-4 -2 v4 M4 -2 v4" stroke="#f4a261" stroke-width="3"/></g>')


def abruptly():
    b = ['<rect y="230" width="400" height="170" fill="#6c757d"/>',
         '<path d="M0 384 H400" stroke="#fff" stroke-width="5" stroke-dasharray="30 20"/>',
         bush(40, 220, 24), bush(360, 222, 22), bush(250, 224, 18),
         # skid marks behind the tyres
         '<path d="M0 346 H232 M0 356 H232" stroke="#1b1b1b" stroke-width="6" stroke-linecap="round" opacity=".7"/>',
         '<circle cx="30" cy="318" r="16" fill="#dee2e6"/><circle cx="54" cy="306" r="12" fill="#dee2e6"/>'
         '<circle cx="14" cy="300" r="11" fill="#dee2e6"/>',
         # the car, nose dipped from the hard stop
         '<g transform="translate(-40 24) rotate(4 220 300)">'
         '<path d="M70 320 V276 Q72 258 96 256 L130 252 L160 210 H234 L264 252 H302 Q322 254 322 276 V320 Z" '
         'fill="#457b9d"/>'
         '<path d="M170 220 H228 L250 250 H170 Z M140 250 L162 220 H164 V250 Z" fill="#caf0f8"/>'
         '<rect x="306" y="268" width="16" height="10" rx="3" fill="#ffd166"/></g>',
         '<circle cx="86" cy="340" r="26" fill="#343a40"/><circle cx="86" cy="340" r="11" fill="#adb5bd"/>',
         '<circle cx="232" cy="350" r="26" fill="#343a40"/><circle cx="232" cy="350" r="11" fill="#adb5bd"/>',
         '<path d="M290 232 l12 -14 M300 254 l16 -6 M278 218 l2 -16" stroke="#e63946" stroke-width="5" '
         'stroke-linecap="round"/>',
         duck(322, 364, 1.2), duck(352, 366, .66), duck(376, 368, .58)]
    return svg(b, "#cfe8f3")


def accomplishment():
    b = ['<circle cx="70" cy="70" r="30" fill="#ffd166"/>',
         '<polygon points="0,400 0,300 120,200 190,140 230,170 310,250 400,320 400,400" fill="#6d597a"/>',
         '<polygon points="120,200 190,140 230,170 210,190 190,176 170,198 150,186" fill="#fff"/>',
         '<polygon points="0,400 0,340 90,290 160,330 250,280 400,350 400,400" fill="#9a8c98"/>',
         '<ellipse cx="80" cy="250" rx="70" ry="18" fill="#fff" opacity=".8"/>',
         '<ellipse cx="320" cy="230" rx="80" ry="20" fill="#fff" opacity=".8"/>',
         # the flag planted on top
         '<line x1="238" y1="166" x2="238" y2="40" stroke="#6c757d" stroke-width="5"/>',
         '<path d="M240 42 L300 58 L240 78 Z" fill="#e63946"/>',
         '<rect x="198" y="58" width="28" height="44" rx="8" fill="#2a9d8f"/>',
         person(190, 146, .62, SKIN[1], "#f4a261", "#264653", "#5c4033", "cap",
                larm=((-30, -30), (-44, -66)), rarm=((30, -30), (44, -66)), mood="grin"),
         sparkle(130, 70, 10, "#ffd166"), sparkle(270, 110, 8, "#ffd166")]
    return svg(b, "#cfe8f3")


def incomplete():
    rnd = random.Random(6)
    n, s0, ox, oy = 4, 70, 34, 30
    right = [[rnd.choice((1, -1)) for _ in range(n)] for _ in range(n)]
    down = [[rnd.choice((1, -1)) for _ in range(n)] for _ in range(n)]
    def edges(c, r):
        top = 0 if r == 0 else -down[r - 1][c]
        rt = 0 if c == n - 1 else right[r][c]
        bot = 0 if r == n - 1 else down[r][c]
        lf = 0 if c == 0 else -right[r][c - 1]
        return (top, rt, bot, lf)
    def color(c, r):
        if (c, r) in ((2, 0), (3, 0)):
            return "#ffd166" if (c, r) == (3, 0) else "#a8dadc"
        return ("#a8dadc", "#8ecae6", "#52b788", "#40916c")[r]
    missing = {(1, 1), (2, 1), (1, 2)}
    b = ['<rect x="18" y="14" width="312" height="312" rx="10" fill="#d4a373"/>',
         f'<rect x="{ox}" y="{oy}" width="{n * s0}" height="{n * s0}" fill="#bc8a5f"/>']
    for r in range(n):
        for c in range(n):
            if (c, r) not in missing:
                b.append(puzzle_piece(ox + c * s0, oy + r * s0, s0, edges(c, r), color(c, r), "#fff", 2.5))
    b += ['<circle cx="274" cy="64" r="18" fill="#f4a261"/>', shadow(334, 372, 44, 6),
          f'<g transform="rotate(-20 334 330)">{puzzle_piece(299, 295, s0, edges(2, 1), color(2, 1), "#fff", 2.5)}</g>']
    return svg(b, "#f1faee")


def trophy(x, y, k=1.0, c="#e9c46a", d="#c9a227"):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({k})">'
            f'<rect x="-22" y="-14" width="44" height="14" rx="2" fill="{d}"/>'
            f'<rect x="-6" y="-34" width="12" height="22" fill="{c}"/>'
            f'<path d="M-26 -92 H26 Q26 -40 0 -36 Q-26 -40 -26 -92 Z" fill="{c}"/>'
            f'<path d="M-24 -84 Q-44 -84 -40 -66 Q-36 -54 -20 -56 M24 -84 Q44 -84 40 -66 Q36 -54 20 -56" fill="none" '
            f'stroke="{c}" stroke-width="6"/>'
            '<path d="M-14 -84 Q-14 -56 -4 -48" fill="none" stroke="#fff" stroke-width="5" opacity=".5" '
            'stroke-linecap="round"/></g>')


def achievements():
    b = ['<rect x="20" y="170" width="360" height="14" fill="#7f5539"/>',
         '<rect x="20" y="330" width="360" height="14" fill="#7f5539"/>',
         '<rect x="20" y="184" width="360" height="6" fill="#5c4033" opacity=".5"/>',
         trophy(80, 170, 1.0), trophy(200, 170, 1.4), trophy(320, 170, .9, "#ced4da", "#adb5bd"),
         trophy(250, 330, .8, "#d4a373", "#b08968")]
    # medals hanging on ribbons
    for x, c, rc in ((70, "#e9c46a", "#e63946"), (120, "#ced4da", "#457b9d"), (170, "#d4a373", "#2a9d8f")):
        b += [f'<polygon points="{x - 12},214 {x + 12},214 {x + 6},268 {x - 6},268" fill="{rc}"/>',
              f'<circle cx="{x}" cy="284" r="20" fill="{c}"/>',
              star(x, 284, 10, "#fff", .45)]
    b += ['<rect x="56" y="206" width="128" height="10" rx="3" fill="#6c757d"/>']
    # a ribbon rosette
    b += [f'<polygon points="324,270 312,326 326,316 336,328 338,272" fill="#457b9d"/>',
          flower(334, 264, 18, "#4895ef", "#457b9d", 10), '<circle cx="334" cy="264" r="14" fill="#ffd166"/>']
    for x, y in ((140, 60), (300, 50), (36, 110)):
        b.append(sparkle(x, y, 10, "#ffd166"))
    return svg(b, "#fdf6ec")


def observant():
    b = ['<rect y="330" width="400" height="70" fill="#a7c957"/>', '<g transform="translate(-30 0)">',
         '<path d="M318 330 L326 160 H346 L354 330 Z" fill="#7f5539"/>',
         '<path d="M336 220 L290 170 M336 200 L380 150" stroke="#7f5539" stroke-width="10" stroke-linecap="round"/>']
    for x, y, r in ((290, 120, 60), (356, 116, 52), (326, 64, 50), (260, 180, 40), (380, 180, 36), (240, 80, 36)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#40916c"/>')
    rnd = random.Random(12)
    for _ in range(40):
        x, y = rnd.uniform(220, 400), rnd.uniform(30, 210)
        if not any(math.hypot(x - cx, y - cy) < r - 6 for cx, cy, r in ((290, 120, 60), (356, 116, 52), (326, 64, 50),
                                                                          (260, 180, 40), (380, 180, 36), (240, 80, 36))):
            continue
        b.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="10" ry="6" fill="#2d6a4f" transform="rotate({rnd.randint(0, 180)} '
                 f'{f(x)} {f(y)})"/>')
    # the tiny bird among the leaves
    b += ['<ellipse cx="294" cy="128" rx="11" ry="8" fill="#e76f51"/>', '<circle cx="303" cy="121" r="6" fill="#e76f51"/>',
          '<polygon points="308,120 314,122 308,124" fill="#ffd166"/>', f'<circle cx="304" cy="120" r="1.5" fill="{INK}"/>',
          '<ellipse cx="292" cy="114" rx="10" ry="5" fill="#2d6a4f" transform="rotate(-20 292 114)"/>',
          '<circle cx="296" cy="124" r="24" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="7 5"/></g>',
          '<path d="M128 156 L242 128 M128 172 L242 136" stroke="#fff" stroke-width="2.5" stroke-dasharray="6 6"/>',
          shadow(110, 334, 40)]
    bino = (f'<rect x="-22" y="-188" width="44" height="14" rx="5" fill="{INK}"/>'
            f'<circle cx="-11" cy="-180" r="11" fill="{INK}"/><circle cx="11" cy="-180" r="11" fill="{INK}"/>'
            '<circle cx="-11" cy="-180" r="6" fill="#8ecae6"/><circle cx="11" cy="-180" r="6" fill="#8ecae6"/>'
            f'<circle cx="-22" cy="-170" r="8.5" fill="{SKIN[2]}"/><circle cx="22" cy="-170" r="8.5" fill="{SKIN[2]}"/>')
    b.append(person(110, 332, 1.0, SKIN[2], "#6a994e", "#7f5539", "#1b1b1b", "cap",
                    larm=((-14, 12), (0, -24)), rarm=((14, 12), (0, -24)), mood="smile", extra=bino))
    return svg(b, "#e3f2fd")


def content():
    b = ['<rect x="60" y="30" width="280" height="210" fill="#bde0fe"/>',
         '<circle cx="270" cy="90" r="30" fill="#ffd166"/>',
         '<rect x="56" y="26" width="288" height="218" fill="none" stroke="#fff" stroke-width="12"/>',
         '<path d="M200 26 V244" stroke="#fff" stroke-width="10"/>',
         '<polygon points="60,244 340,244 400,360 0,360" fill="#fff3b0" opacity=".55"/>',
         '<rect x="20" y="244" width="360" height="20" fill="#e9d8c4"/>',
         '<rect x="0" y="264" width="400" height="136" fill="#d4a373"/>',
         '<ellipse cx="200" cy="262" rx="120" ry="20" fill="#e76f51"/>',
         # the cat, curled up asleep
         '<path d="M110 248 Q100 210 150 196 Q220 180 270 210 Q300 230 286 252 Z" fill="#f4a261"/>',
         '<path d="M150 214 Q180 206 210 214 M170 226 Q200 216 232 226" fill="none" stroke="#e76f51" stroke-width="6" '
         'stroke-linecap="round"/>',
         '<path d="M284 252 Q330 246 316 222 Q306 206 290 214" fill="none" stroke="#f4a261" stroke-width="16" '
         'stroke-linecap="round"/>',
         '<circle cx="132" cy="226" r="32" fill="#f4a261"/>',
         '<polygon points="106,210 108,180 128,198" fill="#f4a261"/><polygon points="140,196 160,176 162,206" fill="#f4a261"/>',
         '<polygon points="112,204 113,190 122,198" fill="#ffb4a2"/><polygon points="146,198 156,188 157,202" fill="#ffb4a2"/>',
         f'<path d="M112 228 Q119 234 126 228 M138 228 Q145 234 152 228" fill="none" stroke="{INK}" stroke-width="3" '
         'stroke-linecap="round"/>',
         f'<path d="M126 242 Q132 248 138 242" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>',
         '<circle cx="110" cy="240" r="5" fill="#e5989b" opacity=".7"/><circle cx="154" cy="240" r="5" fill="#e5989b" '
         'opacity=".7"/>',
         zzz(170, 160, 12), zzz(190, 130, 16, w=4.5)]
    return svg(b, "#fdf0d5")


PICTURES = {
    "skepticism toward": skepticism_toward,
    "careful": careful,
    "assistance": assistance,
    "scrutinize": scrutinize,
    "restricted": restricted,
    "cherished": cherished,
    "enthusiasm for": enthusiasm_for,
    "publicity": publicity,
    "overshadowed by": overshadowed_by,
    "surprise at": surprise_at,
    "vague": vague,
    "struggling": struggling,
    "disorganized": disorganized,
    "nurture": nurture,
    "advice": advice,
    "inspect": inspect,
    "lift": lift,
    "overlooked": overlooked,
    "evidence": evidence,
    "buttress": buttress,
    "profusion of": profusion_of,
    "emulate": emulate,
    "oddity": oddity,
    "collaborators": collaborators,
    "secretive": secretive,
    "tenderly": tenderly,
    "decorations": decorations,
    "replicate": replicate,
    "abandon": abandon,
    "ornamental": ornamental,
    "attract": attract,
    "imitation": imitation,
    "refusing": refusing,
    "reveal": reveal,
    "mimicked": mimicked,
    "anomaly": anomaly,
    "reciprocates": reciprocates,
    "acclaim": acclaim,
    "recognize": recognize,
    "stretching toward": stretching_toward,
    "partnership": partnership,
    "thrive": thrive,
    "rapid": rapid,
    "surpassed by": surpassed_by,
    "abruptly": abruptly,
    "accomplishment": accomplishment,
    "incomplete": incomplete,
    "achievements": achievements,
    "observant": observant,
    "content": content,
}
