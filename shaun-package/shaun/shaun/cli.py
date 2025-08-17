import argparse
import sys
from . import __version__
from .data import ABOUT, SKILLS, TOOLS, PROJECTS, TIMELINE, INVESTMENTS, HOBBIES, ASCII
from .display import render_about, render_skills, render_projects, render_timeline, boxed, title
from .design import render_design_showcase
from .jokes import random_joke, random_quote

MENU = """\
Welcome to Shaun's Terminal Portfolio 👋
Select a section:
  [1] About & Skills
  [2] Projects
  [3] Timeline
  [4] Design
  [5] Hobbies
  [6] Investments (humble)
  [7] Fun / Easter eggs
  [0] Exit
"""

def show_about_skills():
    print(title("About"))
    print(render_about(), end="\n\n")
    print(render_skills(SKILLS), end="\n\n")
    print(title("Tools"))
    print("\n".join(f"- {t}" for t in TOOLS))

def show_projects():
    print(render_projects(PROJECTS))

def show_timeline():
    print(render_timeline(TIMELINE))

def show_design():
    print(title("Design"))
    print(render_design_showcase())

def show_hobbies():
    print(title("Hobbies"))
    music = "\n".join(f"- {m}" for m in HOBBIES.get("music_albums", []))
    movies = "\n".join(f"- {m}" for m in HOBBIES.get("movies", []))
    sports = ", ".join(HOBBIES.get("sports", []))
    extras = ", ".join(HOBBIES.get("cars_bikes", []))
    print(f"Sports: {sports}")
    print(f"Gaming: {'Yes' if HOBBIES.get('gaming') else 'No'}")
    print("\nMusic (albums):\n" + (music or "—"))
    print("\nMovies:\n" + (movies or "—"))
    print("\nCars/Bikes:\n" + (extras or "—"))

def show_investments(show: bool):
    print(title("Investments (humble snapshot)"))
    if not show:
        print("Hidden by default. Re-run with: shaun investments --show")
        return
    inv = INVESTMENTS
    print(f"Summary: {inv['summary']}")
    print(f"Dividend stocks: {inv['dividend_stocks']}")
    print(f"Index SIPs: {inv['index_sips']}")
    print(f"Penny stocks: {inv['penny_stocks']}")
    print(f"Realized status: {inv['realized_status']}")
    print(f"\nDisclaimer: {inv['disclaimer']}")

def show_fun(mafia: bool=False):
    print(title("Fun"))
    print("Joke: " + random_joke())
    print("Quote: " + random_quote())
    if mafia:
        print("\nMafia Mode:\n" + ASCII["mafia"])

def interactive_menu():
    while True:
        print(MENU)
        choice = input("Enter choice: ").strip()
        if choice == "1":
            show_about_skills()
        elif choice == "2":
            show_projects()
        elif choice == "3":
            show_timeline()
        elif choice == "4":
            show_design()
        elif choice == "5":
            show_hobbies()
        elif choice == "6":
            show_investments(show=False)
        elif choice == "7":
            show_fun(mafia=True)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")
        input("\n(press Enter to continue)")

def build_parser():
    p = argparse.ArgumentParser(prog="shaun", description="Terminal portfolio: Shaun's interactive business card")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("skills")
    sub.add_parser("projects")
    sub.add_parser("timeline")
    sub.add_parser("design")
    sub.add_parser("hobbies")

    inv = sub.add_parser("investments")
    inv.add_argument("--show", action="store_true", help="display humble snapshot")

    fun = sub.add_parser("fun")
    fun.add_argument("--mafia", action="store_true", help="show mafia ascii")

    p.add_argument("-v", "--version", action="store_true", help="print version")
    return p

def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    if not args.cmd:
        interactive_menu()
        return 0

    if args.cmd == "skills":
        show_about_skills()
    elif args.cmd == "projects":
        show_projects()
    elif args.cmd == "timeline":
        show_timeline()
    elif args.cmd == "design":
        show_design()
    elif args.cmd == "hobbies":
        show_hobbies()
    elif args.cmd == "investments":
        show_investments(show=args.show)
    elif args.cmd == "fun":
        show_fun(mafia=getattr(args, "mafia", False))
    else:
        parser.print_help()
        return 1

    return 0