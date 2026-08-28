"""
Purpose:
    Document the BWA-MEM alignment workflow used for the completed
    paired-end ATAC-seq analysis.

What this script does:
    1. Finds paired-end R1 FASTQ files.
    2. Identifies the corresponding R2 FASTQ file.
    3. Aligns reads to the hg38 reference genome using BWA-MEM.
    4. Sorts the alignments using SAMtools.
    5. Indexes the sorted BAM files.

Note:
    Original machine-specific paths were replaced with placeholders
    for the public GitHub repository.
"""

import glob
import subprocess


# Input paths
fastq_path = "/path/to/ATAC_Seq/"
genome_fasta = "/path/to/reference/hg38.fa"
bwa = "/path/to/bwa"


# Process each paired-end FASTQ pair
for r1 in glob.glob(fastq_path + "*_R1.fastq.gz"):

    r2 = r1.replace("_R1.fastq.gz", "_R2.fastq.gz")
    sample = r1.replace("_R1.fastq.gz", "")

    # Align paired-end reads to hg38
    subprocess.run(
        [
            bwa,
            "mem",
            "-t",
            "10",
            genome_fasta,
            r1,
            r2,
            "-o",
            sample + "_Aligned.sam",
        ],
        check=True,
    )

    # Coordinate-sort the alignment
    subprocess.run(
        [
            "samtools",
            "sort",
            "-@",
            "8",
            "-o",
            sample + "_sorted.bam",
            sample + "_Aligned.sam",
        ],
        check=True,
    )

    # Index the sorted BAM
    subprocess.run(
        ["samtools", "index", sample + "_sorted.bam"],
        check=True,
    )
