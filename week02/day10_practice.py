"""Day 10 — File I/O"""
import csv
from pathlib import Path

# Update write_lines and write_csv to accept either a str or a Path as filepath,
# and auto-create any missing parent directories before writing.
# Hint: one line with Path and mkdir handles it.

# write_lines(filepath, lines) — writes a list of strings to a file, one per line
def write_lines(filepath, lines):
    path = Path(filepath) if isinstance(filepath, str) else filepath
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.writelines([line + "\n" for line in lines])


# read_lines(filepath) — reads the file back, returns a list of strings stripped of \n
def read_lines(filepath):
    with open(filepath, "r") as f:
        return [line.rstrip("\n") for line in f.readlines()]

# write_csv(filepath, rows) — takes a list of dicts and writes them to a CSV
# (infer headers from the first dict's keys)
def write_csv(filepath, rows):
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        csv_writer.writeheader()
        for row in rows:
            csv_writer.writerow(row)


# read_csv(filepath) — reads the CSV back and returns a list of dicts
def read_csv(filepath):
    with open(filepath, "r") as f:
        return list(csv.DictReader(f))

