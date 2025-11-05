# Warden's Sanctum

A short text-adventure about escape, discovery, and a mysterious sanctum.

Overview
--------
Warden's Sanctum is a compact Python text adventure in which you awaken in a grimy cell, discover a mysterious wand, and are swept into the sanctum of a powerful and suspicious figure. The game focuses on exploration, simple inventory flags, atmosphere created by a typed-text effect, and branching choices that change the outcome.

This repository contains the game code (Python) and the story/prose currently embedded in the code.

Quick facts
-----------
- Project name: Warden's Sanctum
- Language: Python (single-file prototype: TextAdventure.py)
- Status: Prototype / early demo
- Intended distribution: Free to play and edit; non-commercial restriction on assets and prose

Requirements
------------
- Python 3.8+ (standard library only)
- No external packages required

How to play
-----------
1. Clone this repository:
   git clone https://github.com/TheEmbersOfTwilight/Text-Adventure1.git
2. Change into the repository directory:
   cd Text-Adventure1
3. Run the game:
   python TextAdventure.py

Controls
--------
- When you are presented with options, type the number of your choice and press Enter.
- The game displays text with a typing effect; if you want a no-delay run, consider adding a --fast or --no-delay flag and a small change in the code to skip time.sleep delays.

Project structure
-----------------
- TextAdventure.py — main Python game file (prototype)
- (future) assets/ — images, audio, or other resources (if/when added)
- README.md — this file
- LICENSE-AGPLv3.txt — (add) AGPLv3 text for code
- LICENSE-CC-BY-NC-SA-4.0.txt — (add) CC BY-NC-SA 4.0 text for assets/prose
- LICENSES.md — (add) mapping file explaining which parts of the repo are under which license

Contributing
------------
- Contributions welcome! If you plan a small change (bugfix, typo, small refactor), open a pull request.
- For larger changes (new chapters, design changes), please open an issue first to discuss scope and compatibility.
- By contributing code you agree to license your contributions under AGPL-3.0 for code and CC BY-NC-SA 4.0 for creative content included in your contributions (this should be formalized in CONTRIBUTING.md).

Support / Contact
-----------------
Author / maintainer: TheEmbersOfTwilight  
Repo: https://github.com/TheEmbersOfTwilight/Text-Adventure1

Acknowledgements
----------------
- This project started as a small Python prototype with an emphasis on atmosphere and branching choices.

Changelog / Roadmap
-------------------
- v0.1 — Prototype: single-file Python demo (TextAdventure.py) with simple item flags and branching.
- Planned:
  - Add save/load
  - Add accessibility flags (skip typing effect)
