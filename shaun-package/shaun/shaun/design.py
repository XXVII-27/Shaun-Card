from .data import ASCII

def render_design_showcase() -> str:
    poster = ASCII["poster_box"]
    caption = "Minimal design sample (terminal-safe). For full visuals, visit portfolio site or GitHub README."
    return f"{poster}\n{caption}"
