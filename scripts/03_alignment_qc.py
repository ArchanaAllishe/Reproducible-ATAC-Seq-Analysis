"""
Purpose:
    Document the alignment QC workflow used in the completed ATAC-seq analysis.

What this script does:
    1. Finds coordinate-sorted BAM files.
    2. Runs SAMtools flagstat for each BAM file.
    3. Extracts key alignment statistics.
    4. Writes a summary table for cross-sample review.

Note:
    The original machine-specific path was replaced with a placeholder
    for the public GitHub repository.
"""

import glob
import subprocess


BAM_DIR = "/path/to/ATAC_Seq/"


for bam in glob.glob(BAM_DIR + "*_sorted.bam"):

    result = subprocess.run(
        ["samtools", "flagstat", bam],
        capture_output=True,
        text=True,
        check=True,
    )

    print(f"\n{bam}")
    print(result.stdout)
