# Step 2 — BWA-MEM Alignment

## Objective

Paired-end ATAC-seq FASTQ files retained after raw-data QC and sample selection were aligned to the **hg38 human reference genome**.

Alignment assigns the sequencing reads to their genomic locations, providing the basis for identifying regions enriched in ATAC-seq fragments and, subsequently, regions of accessible chromatin.

## Alignment with BWA-MEM

**BWA-MEM** was used to align the paired-end reads to hg38. It is well suited for paired-end genomic DNA sequencing and generates SAM/BAM-compatible alignments that can be processed with downstream tools such as **SAMtools** and **MACS3**.

The retained FASTQ files were processed as matching R1 and R2 pairs. For example:

```text
ORG39_6_L1_R1.fastq.gz
ORG39_6_L1_R2.fastq.gz
```

A Python script automated the alignment workflow across the FASTQ pairs. For each pair, the script:

1. identified the corresponding R1 and R2 files;
2. aligned the reads to **hg38 using BWA-MEM**;
3. generated a SAM alignment file;
4. coordinate-sorted the alignment using **SAMtools**; and
5. indexed the resulting sorted BAM file.

BWA-MEM alignment used **10 threads**, and SAMtools sorting used **8 threads**.

**[View BWA-MEM Alignment Script](../scripts/02_bwa_alignment.py)**

## Workflow

```text
Paired-end FASTQ files
        │
        ▼
BWA-MEM alignment to hg38
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
  BAM + BAM index
```

## Output

For each aligned sample/lane, the workflow generated:

```text
SAMPLE_Aligned.sam
SAMPLE_sorted.bam
SAMPLE_sorted.bam.bai
```

These aligned BAM files provide the genomic positions of the ATAC-seq fragments and were carried forward for **alignment quality assessment and subsequent BAM filtering**.

## Next Step

**Step 3 — Alignment Quality Control**

Alignment statistics were evaluated before downstream filtering and cleanup.

