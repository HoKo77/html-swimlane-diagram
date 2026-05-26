#!/usr/bin/env python3
"""Lint SVG connector paths for diagonal, crossing, or overlapping segments."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


PATH_RE = re.compile(r'<path\b(?=[^>]*\bclass="[^"]*\blink\b[^"]*")[^>]*\bd="([^"]+)"', re.I)
TOKEN_RE = re.compile(r"[MmLlHhVvZz]|-?\d+(?:\.\d+)?")
EPSILON = 0.001


def numbers(tokens: list[str], index: int, count: int) -> tuple[list[float], int]:
    values = []
    for _ in range(count):
        if index >= len(tokens) or re.match(r"^[A-Za-z]$", tokens[index]):
            raise ValueError("path command is missing coordinates")
        values.append(float(tokens[index]))
        index += 1
    return values, index


Segment = tuple[float, float, float, float]


def is_endpoint(x: float, y: float, segment: Segment) -> bool:
    return (
        abs(x - segment[0]) <= EPSILON and abs(y - segment[1]) <= EPSILON
    ) or (
        abs(x - segment[2]) <= EPSILON and abs(y - segment[3]) <= EPSILON
    )


def segment_orientation(segment: Segment) -> str:
    x1, y1, x2, y2 = segment
    if abs(y1 - y2) <= EPSILON:
        return "h"
    if abs(x1 - x2) <= EPSILON:
        return "v"
    return "d"


def between(value: float, a: float, b: float) -> bool:
    return min(a, b) + EPSILON < value < max(a, b) - EPSILON


def parse_path(d: str) -> tuple[list[str], list[Segment]]:
    tokens = TOKEN_RE.findall(d.replace(",", " "))
    errors: list[str] = []
    segments: list[Segment] = []
    index = 0
    command = None
    x = y = start_x = start_y = None

    def check_segment(next_x: float, next_y: float, token_index: int) -> None:
        nonlocal x, y
        if x is None or y is None:
            return
        dx = abs(next_x - x)
        dy = abs(next_y - y)
        if dx > EPSILON and dy > EPSILON:
            errors.append(f"diagonal segment near token {token_index}: ({x:g}, {y:g}) -> ({next_x:g}, {next_y:g})")
        elif dx > EPSILON or dy > EPSILON:
            segments.append((x, y, next_x, next_y))

    while index < len(tokens):
        token = tokens[index]
        if re.match(r"^[A-Za-z]$", token):
            command = token
            index += 1
        if command is None:
            errors.append("path starts without a command")
            break

        cmd = command
        absolute = cmd.isupper()
        op = cmd.upper()

        if op == "M":
            vals, index = numbers(tokens, index, 2)
            next_x, next_y = vals
            if not absolute and x is not None and y is not None:
                next_x += x
                next_y += y
            x = start_x = next_x
            y = start_y = next_y
            command = "L" if absolute else "l"
        elif op == "L":
            vals, old_index = numbers(tokens, index, 2)
            index = old_index
            next_x, next_y = vals
            if not absolute:
                next_x = (x or 0) + next_x
                next_y = (y or 0) + next_y
            check_segment(next_x, next_y, old_index)
            x, y = next_x, next_y
        elif op == "H":
            vals, old_index = numbers(tokens, index, 1)
            index = old_index
            next_x = vals[0] if absolute else (x or 0) + vals[0]
            check_segment(next_x, y or 0, old_index)
            x = next_x
        elif op == "V":
            vals, old_index = numbers(tokens, index, 1)
            index = old_index
            next_y = vals[0] if absolute else (y or 0) + vals[0]
            check_segment(x or 0, next_y, old_index)
            y = next_y
        elif op == "Z":
            if start_x is not None and start_y is not None:
                check_segment(start_x, start_y, index)
                x, y = start_x, start_y
        else:
            errors.append(f"unsupported path command {cmd!r}; use M/L/H/V for connectors")
            break

        if index < len(tokens) and re.match(r"^[A-Za-z]$", tokens[index]):
            continue
        if op in {"Z"}:
            command = None

    return errors, segments


def lint_crossings(all_segments: list[tuple[int, Segment]]) -> list[str]:
    errors: list[str] = []
    for i, (link_a, a) in enumerate(all_segments):
        ax1, ay1, ax2, ay2 = a
        a_orientation = segment_orientation(a)
        for link_b, b in all_segments[i + 1 :]:
            if link_a == link_b:
                continue
            bx1, by1, bx2, by2 = b
            b_orientation = segment_orientation(b)

            if {a_orientation, b_orientation} == {"h", "v"}:
                h = a if a_orientation == "h" else b
                v = a if a_orientation == "v" else b
                h_link = link_a if a_orientation == "h" else link_b
                v_link = link_a if a_orientation == "v" else link_b
                hx1, hy, hx2, _ = h
                vx, vy1, _, vy2 = v
                if between(vx, hx1, hx2) and between(hy, vy1, vy2):
                    errors.append(
                        f"link #{h_link} crosses link #{v_link} at ({vx:g}, {hy:g})"
                    )
                continue

            if a_orientation == b_orientation == "h" and abs(ay1 - by1) <= EPSILON:
                overlap_start = max(min(ax1, ax2), min(bx1, bx2))
                overlap_end = min(max(ax1, ax2), max(bx1, bx2))
                if overlap_end - overlap_start > EPSILON:
                    if not (
                        is_endpoint(overlap_start, ay1, a)
                        and is_endpoint(overlap_start, ay1, b)
                        and abs(overlap_end - overlap_start) <= EPSILON
                    ):
                        errors.append(
                            f"link #{link_a} overlaps link #{link_b} on y={ay1:g}, x={overlap_start:g}..{overlap_end:g}"
                        )
                continue

            if a_orientation == b_orientation == "v" and abs(ax1 - bx1) <= EPSILON:
                overlap_start = max(min(ay1, ay2), min(by1, by2))
                overlap_end = min(max(ay1, ay2), max(by1, by2))
                if overlap_end - overlap_start > EPSILON:
                    errors.append(
                        f"link #{link_a} overlaps link #{link_b} on x={ax1:g}, y={overlap_start:g}..{overlap_end:g}"
                    )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=pathlib.Path, help="HTML file containing SVG .link paths")
    ns = parser.parse_args()

    content = ns.html.read_text(encoding="utf-8")
    failures = []
    all_segments: list[tuple[int, Segment]] = []
    for idx, d in enumerate(PATH_RE.findall(content), start=1):
        errors, segments = parse_path(d)
        all_segments.extend((idx, segment) for segment in segments)
        for error in errors:
            failures.append(f"link #{idx}: {error}; d={d}")
    failures.extend(lint_crossings(all_segments))

    if failures:
        print(f"{ns.html}: found {len(failures)} connector issue(s)")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"{ns.html}: all .link paths are orthogonal and non-crossing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
