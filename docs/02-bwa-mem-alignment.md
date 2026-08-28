# Step 2 — Read Alignment and Alignment Quality Control

## Objective

Paired-end ATAC-seq FASTQ files retained after raw-data QC were aligned to the **hg38 human reference genome**, followed by assessment of alignment quality before downstream BAM filtering.

Alignment assigns sequencing reads to their genomic locations, providing the basis for identifying regions enriched in ATAC-seq fragments and, subsequently, regions of accessible chromatin.

## BWA-MEM Alignment

**BWA-MEM** was used to align the paired-end reads to hg38. It is well suited for paired-end genomic DNA sequencing and produces SAM/BAM-compatible alignments that can be processed with downstream tools such as **SAMtools** and **MACS3**.

FASTQ files were processed as matching R1 and R2 pairs. For example:

```text
ORG39_6_L1_R1.fastq.gz
ORG39_6_L1_R2.fastq.gz
```

A Python script automated the alignment workflow. For each FASTQ pair, the script:

1. identified the corresponding R1 and R2 files;
2. aligned the reads to hg38 using BWA-MEM;
3. generated a SAM alignment file;
4. coordinate-sorted the alignment using SAMtools; and
5. indexed the resulting BAM file.

BWA-MEM alignment used **10 threads**, and SAMtools sorting used **8 threads**.

**[View BWA-MEM Alignment Script](../scripts/02_bwa_alignment.py)**

## Alignment Quality Control

The coordinate-sorted BAM files were evaluated using **SAMtools flagstat** before downstream filtering.

The main alignment metrics reviewed included:

* total reads
* mapped reads
* mapping rate
* properly paired reads
* properly paired rate
* secondary alignments
* supplementary alignments

### Alignment Summary

| Sample     | Total reads | Mapped reads | Mapping rate | Properly paired |
| ---------- | ----------: | -----------: | -----------: | --------------: |
| 28P_1_L1   |  79,114,352 |   78,297,957 |       98.97% |          98.03% |
| 28P_1_L2   |  78,214,964 |   77,420,472 |       98.99% |          98.06% |
| 39P_2_L1   |  73,099,113 |   72,229,834 |       98.81% |          98.00% |
| 39P_2_L2   |  73,799,160 |   72,956,711 |       98.86% |          98.04% |
| ORG15_1_L1 | 108,031,999 |  104,375,124 |       96.62% |          95.99% |
| ORG15_1_L2 | 110,225,873 |  106,484,111 |       96.61% |          96.00% |
| ORG34_5_L1 | 109,365,905 |   65,509,760 |       59.90% |          57.83% |
| ORG34_5_L2 | 111,221,970 |   66,085,794 |       59.42% |          57.35% |
| ORG39_6_L1 |  93,017,628 |   89,426,689 |       96.14% |          95.30% |
| ORG39_6_L2 |  94,500,331 |   90,878,415 |       96.17% |          95.37% |
| ORG40_8_L1 | 130,248,720 |  127,383,152 |       97.80% |          89.82% |
| ORG40_8_L2 | 134,516,210 |  131,673,014 |       97.89% |          89.66% |
| ORG44_7_L1 |  98,756,458 |   84,700,433 |       85.77% |          83.97% |
| ORG44_7_L2 | 101,617,131 |   87,191,877 |       85.81% |          83.61% |
| PK4_9_L1   | 103,774,272 |  101,809,715 |       98.11% |          96.46% |
| PK4_9_L2   | 106,447,741 |  104,426,014 |       98.10% |          96.37% |

Most libraries showed high mapping rates to hg38. **ORG34_5** showed substantially lower mapping rates (~59–60%), while **ORG44_7** showed moderately lower mapping rates (~86%). These results were reviewed before downstream BAM filtering.

> **Note:** SAMtools flagstat reports reads/alignment records rather than paired-end fragment counts.

**[View Alignment QC Script](../scripts/03_alignment_qc.py)**

## Workflow

```text
Paired-end FASTQ files
        │
        ▼
 BWA-MEM → hg38
        │
        ▼
    Aligned SAM
        │
        ▼
   SAMtools sort
        │
        ▼
    Sorted BAM
        │
        ▼
   SAMtools index
        │
        ▼
 SAMtools flagstat
        │
        ▼
 Review alignment QC
        │
        ▼
BAM filtering and cleanup
```

## Output

The alignment workflow generated:

```text
SAMPLE_Aligned.sam
SAMPLE_sorted.bam
SAMPLE_sorted.bam.bai
```

The sorted BAM files and their alignment statistics were used to evaluate mapping performance before downstream filtering.

## Next Step

**Step 3 — BAM Filtering and Cleanup**

Aligned reads were filtered to retain high-quality, properly paired nuclear alignments and remove unwanted reads before downstream ATAC-seq analysis.
