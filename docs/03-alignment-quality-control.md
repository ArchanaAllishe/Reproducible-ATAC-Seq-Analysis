# Step 3 — Alignment Quality Control

## Objective

The sorted BAM files generated after BWA-MEM alignment were evaluated to assess mapping performance before downstream BAM filtering.

**SAMtools flagstat** was used to summarize alignment statistics for each sample/lane.

## Alignment Metrics

The main metrics reviewed were:

* total aligned reads
* mapped reads
* mapping rate
* properly paired reads
* properly paired rate
* secondary alignments
* supplementary alignments

## Alignment Summary

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

Most libraries showed high mapping rates. **ORG34_5** showed substantially lower mapping than the other libraries, while **ORG44_7** also showed moderately reduced mapping. These statistics were reviewed before proceeding with downstream filtering.

## Workflow

```text
Sorted BAM files
      │
      ▼
SAMtools flagstat
      │
      ▼
Alignment statistics
      │
      ▼
Review mapping and pairing
      │
      ▼
BAM filtering and cleanup
```

## Alignment QC Script

The Python script used to summarize `samtools flagstat` results across the BAM files is documented here:

**[View Alignment QC Script](../scripts/03_alignment_qc.py)**

## Next Step

**Step 4 — BAM Filtering and Cleanup**

Aligned reads were filtered to retain high-quality, properly paired nuclear reads and remove unwanted alignments before peak calling.

