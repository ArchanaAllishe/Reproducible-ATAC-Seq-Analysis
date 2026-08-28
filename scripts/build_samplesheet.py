"""
Purpose:
    Build a sample sheet for the ATAC-seq analysis workflow from paired-end
    FASTQ files.

What this script does:
    1. Searches the raw-data directory for FASTQ files.
    2. Extracts the sample ID, sequencing lane, and read direction (R1/R2)
       from each filename.
    3. Matches R1 and R2 files belonging to the same sample and lane.
    4. Checks for incomplete FASTQ pairs and prints a warning if one is found.
    5. Writes the organized sample information to config/samplesheet.csv.

The original FASTQ files are not renamed or modified.
"""

from pathlib import Path
import csv
import re


# --------------------------------------------------
# Input and output
# --------------------------------------------------

FASTQ_DIR = Path("data/raw")
OUTPUT = Path("config/samplesheet.csv")


# --------------------------------------------------
# FASTQ filename pattern
# --------------------------------------------------

# Extract sample ID, sequencing lane, and read direction
# from the original FASTQ filenames.

pattern = re.compile(
    r"^AT-(?P<sample>.+?)\.[^_]+_(?P<lane>L\d+)_(?P<read>R[12])(?:_[^.]+)?\.fastq\.gz$"
)


# --------------------------------------------------
# Discover and organize FASTQ files
# --------------------------------------------------

records = {}

for fastq in sorted(FASTQ_DIR.glob("*.fastq.gz")):

    match = pattern.match(fastq.name)

    if not match:
        print(f"Skipping unrecognized filename: {fastq.name}")
        continue

    # Extract sample information from the filename.
    sample_id = match.group("sample").replace("-", "_")
    lane = match.group("lane")
    read = match.group("read")

    # Each sample/lane combination should contain
    # one R1 file and one R2 file.
    key = (sample_id, lane)

    if key not in records:
        records[key] = {
            "sample_id": sample_id,
            "condition": "",
            "lane": lane,
            "fastq_1": "",
            "fastq_2": "",
        }

    if read == "R1":
        records[key]["fastq_1"] = str(fastq)
    else:
        records[key]["fastq_2"] = str(fastq)


# --------------------------------------------------
# Write sample sheet
# --------------------------------------------------

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT.open("w", newline="") as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=[
            "sample_id",
            "condition",
            "lane",
            "fastq_1",
            "fastq_2",
        ],
    )

    writer.writeheader()

    for key in sorted(records):

        row = records[key]

        # Warn if a sample/lane is missing either R1 or R2.
        if not row["fastq_1"] or not row["fastq_2"]:
            print(
                f"WARNING: incomplete FASTQ pair for "
                f"{row['sample_id']} {row['lane']}"
            )

        writer.writerow(row)


print(f"Samplesheet written to: {OUTPUT}")
