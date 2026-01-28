# CTFSaleh

This repository is a personal working archive that brings together several of my interests:
competitive programming, CTFs, coursework, machine learning experiments, and finance notes
(particularly CFA Level I preparation). It is not a single cohesive project, but rather a
collection of solutions, templates, experiments, and notes that I revisit and extend over time.

## Repository Structure

At a high level, the repository contains the following folders:

- **codeforces/**  
  Solutions to Codeforces problems, written primarily for contest practice and post-contest
  cleanup. Expect fast I/O patterns, standard CP tricks, and minimal commentary.

- **cp3/**  
  Competitive programming practice inspired by the *CS 41100* at Purdue,
  including drills, problem sets, and personal notes on problems im working through for the course.

- **leetcode/**  
  LeetCode solutions and algorithmic experiments, oftentimes overlapping with CP topics.

- **CTFs/**  
  Capture-the-Flag related material: scripts, exploits, challenge solutions, and notes.
  
- **kaggle/Titanic/**  
  Machine learning sandboxing using the classic Titanic dataset. Rough first approachs.

- **Obsidian_Vault/**  
  Personal notes maintained in Obsidian. This includes finance and economics material
  (notably CFA Level I prep), along with general technical notes.

- **scratch/**  
  Miscellaneous experiments, partial solutions, and quick tests that do not yet have a
  permanent home.

## Languages and Tools

- **Python** (primary)
- **C++ / C** (competitive programming and for when I'm in the mood)
- Occasional data science and scripting utilities

## Usage

This repository is not intended to be built or run as a single project.

### Competitive Programming
Most solutions are standalone files:

```bash
# Python
python3 solution.py < input.txt

# C++
g++ -std=c++17 -O2 solution.cpp -o solution
./solution < input.txt
```

### Notes (Obsidian)

To properly view the notes:
1. Install **Obsidian**
2. Open `Obsidian_Vault/` as a vault

## Philosophy

- **Practical over polished** — code and notes are written primarily for learning, iteration,
  and future reuse rather than presentation.
- **Template-driven** — common competitive programming patterns (fast I/O, bitmask DP,
  greedy scaffolding, graph routines) appear repeatedly.
- **Iterative and exploratory** — many files reflect intermediate thinking, where my head was at the time, rather than
  finalized solutions.

## Disclaimer

Some code was written under contest time constraints or as rapid experimentation.
Expect minimal comments, occasional rough edges, and problem-specific assumptions.
Review and adapt before reuse.
