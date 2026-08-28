# Step 1 — Raw FASTQ Quality Control

## Objective

Raw paired-end ATAC-seq FASTQ files were assessed with **FastQC** and **MultiQC** to evaluate sequencing quality and read depth before alignment.

## Input FASTQ Files

The dataset contained **47 FASTQ files** representing 12 samples sequenced across two lanes (L1 and L2), with paired-end reads (R1 and R2).

| Sample  | Lane 1  | Lane 2 |
| ------- | ------- | ------ |
| 28P_1   | R1, R2  | R1, R2 |
| 39P_2   | R1, R2  | R1, R2 |
| ORG15_1 | R1, R2  | R1, R2 |
| ORG28_4 | R1 only | R1, R2 |
| ORG34_5 | R1, R2  | R1, R2 |
| ORG39_6 | R1, R2  | R1, R2 |
| ORG40_8 | R1, R2  | R1, R2 |
| ORG44_7 | R1, R2  | R1, R2 |
| PK4_2   | R1, R2  | R1, R2 |
| PK4_9   | R1, R2  | R1, R2 |
| PK5_3   | R1, R2  | R1, R2 |
| PK5_10  | R1, R2  | R1, R2 |

> **Note:** `ORG28_4_L1_R2` was not present in the available FASTQ file list.

## Raw Data Quality Control

**FastQC** was run on the raw FASTQ files, and the individual reports were aggregated with **MultiQC** for cross-sample review.

The main metrics reviewed included:

* total read count
* per-base sequence quality
* GC content
* sequence duplication
* adapter content
* overrepresented sequences
* read length

### Commands

The commands were run from the sample working directory containing the raw FASTQ files.

```bash
# Run FastQC
fastqc *.fastq.gz -o fastqc_results/

# Aggregate FastQC results
multiqc fastqc_results/ -o multiqc_results/
```

## MultiQC Review and Sample Selection

The MultiQC report was reviewed to compare sequencing quality and read depth across the FASTQ files.

**[View the interactive MultiQC report](../results/qc/multiqc_report.html)**

Samples with **fewer than 30 million reads were excluded from further analysis** to maintain sufficient sequencing depth for downstream ATAC-seq processing.

For context, open-chromatin profiling commonly uses **≥50 million paired-end reads per sample/replicate**, while some older or minimal recommendations use approximately **20–25 million unique or mapped reads**. Higher starting depth helps account for reads lost during processing, particularly mitochondrial reads and PCR duplicates.

The **30-million-read threshold was used as the project-specific minimum cutoff**, rather than as a universal ATAC-seq standard.

```text
Raw FASTQ files
      │
      ▼
FastQC + MultiQC
      │
      ▼
Review quality and read depth
      │
   ┌──┴───┐
   │      │
 <30M    ≥30M
 reads   reads
   │      │
   ▼      ▼
Exclude  Retain
          │
          ▼
      Alignment
```

## Output

The primary output was the MultiQC report used for raw-data QC and sample selection:

```text
results/qc/
└── multiqc_report.html
```

Samples meeting the **≥30 million read cutoff** were carried forward to **Step 2 — BWA-MEM alignment**.

