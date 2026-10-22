"""Shared pieces for the vocabulary drawings: the SVG frame and small reusable shapes.

Every drawing is a 400x400 SVG (rendered to an 800x800 PNG by make.py). Coordinates are in
that 400x400 space. INK is the dark outline/detail color used across all drawings.
"""

import math

INK = "#264653"


def svg(body, bg, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">'
            f'<defs>{defs}</defs><rect width="400" height="400" fill="{bg}"/>{"".join(body)}</svg>')


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def zzz(x, y, s, color=INK, w=4):
    return (f'<path d="M{f(x)} {f(y)} h{f(s)} l{f(-s)} {f(s)} h{f(s)}" fill="none" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def head(x2, y2, ang, color, size):
    bx, by = x2 - size * math.cos(ang), y2 - size * math.sin(ang)
    px, py = math.cos(ang + math.pi / 2) * size * 0.6, math.sin(ang + math.pi / 2) * size * 0.6
    return (f'<polygon points="{f(x2)},{f(y2)} {f(bx + px)},{f(by + py)} {f(bx - px)},{f(by - py)}" '
            f'fill="{color}" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>'), (bx, by)


def arrow(x1, y1, x2, y2, color=INK, w=6, size=16):
    tip, (bx, by) = head(x2, y2, math.atan2(y2 - y1, x2 - x1), color, size)
    return (f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(bx)}" y2="{f(by)}" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round"/>' + tip)


def carrow(x1, y1, cx, cy, x2, y2, color=INK, w=6, size=16):
    tip, (bx, by) = head(x2, y2, math.atan2(y2 - cy, x2 - cx), color, size)
    return (f'<path d="M{f(x1)} {f(y1)} Q{f(cx)} {f(cy)} {f(bx)} {f(by)}" fill="none" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="round"/>' + tip)


def arc_arrow(cx, cy, r, a1, a2, color=INK, w=6, size=14):
    """Arrow along a circle from angle a1 to a2 (degrees; increasing = clockwise on screen)."""
    p = lambda a: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
    (x1, y1), (x2, y2) = p(a1), p(a2)
    cw = a2 > a1
    tang = math.radians(a2) + (math.pi / 2 if cw else -math.pi / 2)
    tip, _ = head(x2, y2, tang, color, size)
    back = a2 - (1 if cw else -1) * math.degrees(size * 0.8 / r)
    bx, by = p(back)
    large = 1 if abs(back - a1) > 180 else 0
    return (f'<path d="M{f(x1)} {f(y1)} A{r} {r} 0 {large} {1 if cw else 0} {f(bx)} {f(by)}" fill="none" '
            f'stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>' + tip)


def bush(x, y, r, c="#2d6a4f", hi="#40916c"):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{c}"/>'
            f'<circle cx="{f(x - r * .3)}" cy="{f(y - r * .3)}" r="{f(r * .45)}" fill="{hi}"/>')


def pine(x, y, h, c="#386641"):
    w = h * 0.38
    return (f'<rect x="{f(x - h * .05)}" y="{f(y - h * .15)}" width="{f(h * .1)}" height="{f(h * .15)}" fill="#6d4c41"/>'
            f'<path d="M{f(x - w)} {f(y - h * .12)} L{f(x)} {f(y - h)} L{f(x + w)} {f(y - h * .12)} Z" fill="{c}"/>')
