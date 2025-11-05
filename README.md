# Warden's Sanctum

Short tagline: A short text-adventure about escape, discovery, and a mysterious sanctum.

Overview
--------
Warden's Sanctum is a compact Python text adventure in which you awaken in a grimy cell, discover a mysterious wand-like stick, and are swept into the sanctum of a powerful and suspicious figure. The game focuses on exploration, simple inventory flags, atmosphere created by a typed-text effect, and branching choices that change the outcome.

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

License (what I recommend)
--------------------------
You asked for AGPL 3.0 for code and CC BY‑NC‑SA 4.0 for assets and prose. This README documents that choice and what to add to the repository.

- Code (source files, scripts): GNU Affero General Public License v3 (AGPL-3.0).
  - Strong copyleft for software; requires that modifications and network-available derivatives provide source under AGPL-3.0.
- Assets and prose (story text, art, images, audio, dialogue): Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY‑NC‑SA 4.0).
  - Prevents commercial use of the creative contents while allowing modifications shared under the same non-commercial terms.

Why this mapping
----------------
- AGPL-3.0 is a widely used software license that ensures derivative code and network-served changes remain free and open.
- CC BY‑NC‑SA 4.0 is appropriate for narrative, art, and other creative assets when you want to forbid commercial use while allowing remix and sharing under the same terms.
- Using AGPL for code and CC BY‑NC‑SA for creative assets is a common, pragmatic compromise when you want to protect the story/art from commercial re-use while keeping software licensing standard.

What to add to the repository (recommended)
-------------------------------------------
1. LICENSE-AGPLv3.txt — the full text of the GNU AGPL v3 license (place in repo root).
2. LICENSE-CC-BY-NC-SA-4.0.txt — the full text or canonical link to CC BY‑NC-SA 4.0 (place in repo root).
3. LICENSES.md — a short file mapping paths to licenses. Example contents:
   - / (root) — README.md (informational)
   - /TextAdventure.py — AGPL-3.0
   - /assets/ — CC BY-NC-SA 4.0
   - /docs/ — CC BY-NC-SA 4.0
4. Add a short license header to each source file (example below).
5. Add a CONTRIBUTING.md (optional) and CODE_OF_CONDUCT.md (recommended) if you expect external contributors.

Suggested license header (put near the top of TextAdventure.py)
----------------------------------------------------------------
# Copyright (c) 2025 TheEmbersOfTwilight
# Licensed under the GNU Affero General Public License v3.0 (AGPL-3.0) for code.
# Creative assets and prose in this repository are licensed under CC BY-NC-SA 4.0 unless otherwise noted.
# See LICENSE-AGPLv3.txt and LICENSE-CC-BY-NC-SA-4.0.txt in the repository root for full license texts.

Notes and caveats
-----------------
- CC BY‑NC‑SA 4.0 forbids commercial use of CC-licensed content; however, there is a practical reality that someone could reuse your code (under AGPL) with different assets. The CC license prevents them from using your assets commercially without permission.
- Combining AGPL code with CC BY‑NC‑SA assets is legally reasonable and often used, but if you plan to accept contributions, make sure contributors agree to license their contributions under the same licenses (see CONTRIBUTING.md for a contributors license statement).
- I’m not a lawyer. For legal certainty or commercial enforcement plans, consult a lawyer.

Development notes & suggestions
------------------------------
- Improve input validation and provide a help screen (e.g., allow 'q' to quit gracefully).
- Add a save/load system (simple JSON storing inventory flags and player location).
- Make scenes data-driven: move text and choices into JSON or YAML to let writers contribute without changing code.
- Add unit tests for parsing and game-flow logic to make safe refactors easier.
- Consider extracting the typed-text effect into a small utility function with an option to disable delays for accessibility.

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
  - Move narrative to external scene files (JSON/YAML)
  - Add save/load
  - Add accessibility flags (skip typing effect)
  - Add test suite and CI

License reminder
----------------
This README is informational and not a license file. Add LICENSE-AGPLv3.txt and LICENSE-CC-BY-NC-SA-4.0.txt to the repository root to make licensing explicit and machine-readable.
