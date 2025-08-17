from typing import Dict, List, Tuple
from .data import ABOUT

BAR_CHAR = "█"
BAR_WIDTH = 10

def title(t: str) -> str:
    line = "─" * len(t)
    return f"{t}\n{line}"

def pad(s: str, n: int) -> str:
    return s + " " * max(0, n - len(s))

def bar(value: int, width: int = BAR_WIDTH) -> str:
    value = max(0, min(width, int(value)))
    return BAR_CHAR * value + " " * (width - value)

def render_about() -> str:
    return (
        f"{ABOUT['name']} — {ABOUT['tagline']}\n"
        f"{ABOUT['note']}\n"
        f"Location: {ABOUT.get('location', '—')}"
    )

def render_skills(skills: Dict[str, int]) -> str:
    lines = [title("Skills (0-10)")]
    longest = max(len(k) for k in skills.keys())
    for k, v in skills.items():
        lines.append(f"{pad(k, longest)}  {bar(v)} ({v})")
    return "\n".join(lines)

def render_list(items: List[str]) -> str:
    return "\n".join(f"- {x}" for x in items)

def render_projects(projects: List[Dict[str, str]]) -> str:
    lines = [title("Projects")]
    for p in projects:
        tags = ", ".join(p.get("tags", []))
        lines.append(f"• {p['name']} [{p.get('year','')}]")
        lines.append(f"  {p['desc']}")
        if tags:
            lines.append(f"  tags: {tags}")
        link = p.get("link")
        if link:
            lines.append(f"  link: {link}")
    return "\n".join(lines)

def render_timeline(timeline: List[Tuple[str, str]]) -> str:
    lines = [title("Timeline")]
    for year, event in timeline:
        lines.append(f"{year} ── {event}")
    return "\n".join(lines)

def boxed(text: str) -> str:
    lines = text.splitlines()
    width = max(len(line) for line in lines) if lines else 0
    top = "+" + "-" * (width + 2) + "+"
    body = [f"| {line}{' ' * (width - len(line))} |" for line in lines]
    return "\n".join([top, *body, top])
