# shaun — Terminal Portfolio

An interactive **business card in your terminal**. After installing, run `shaun` to browse skills, projects, a timeline, a humble investment snapshot, design samples, and fun easter eggs.

> Friendly face, undeniable receipts.

## Install (local dev)
```bash
git clone https://github.com/YOURUSERNAME/shaun.git
cd shaun
python -m pip install --upgrade build
pip install -e .
```

Run:
```bash
shaun
# or jump to a section
shaun skills
shaun projects
shaun timeline
shaun design
shaun hobbies
shaun investments --show    # hidden by default unless --show
shaun fun
```

Module mode also works:
```bash
python -m shaun
```

## Publish to PyPI
```bash
# inside repo root
python -m pip install --upgrade build twine
python -m build
twine upload dist/*
```

## Philosophy
Minimal, subtle, **data & dev first**. Design showcased tastefully. No external deps.

## License
MIT
