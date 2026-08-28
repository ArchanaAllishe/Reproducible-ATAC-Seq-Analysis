# Step 3 — BAM Filtering and Cleanup

## Objective

Aligned BAM files were filtered to retain high-quality, properly paired nuclear reads and remove unwanted alignments before downstream ATAC-seq analysis.

This cleanup step reduced technical noise and produced BAM files suitable for peak calling and chromatin-accessibility analysis.

## BAM Filtering

SAMtools was used to retain reads that were:

* properly paired
* mapped with a mapping quality of at least 30
* not unmapped
* not paired with an unmapped mate
* not secondary alignments
* not supplementary alignments

The filtering command used was:

```bash
samtools view \
  -b \
  -q 30 \
  -f 2 \
  -F 2316 \
  -o SAMPLE_filtered.bam \
  SAMPLE_sorted.bam
```

The main options were:

| Option    | Purpose                                                                  |
| --------- | ------------------------------------------------------------------------ |
| `-b`      | Write BAM output                                                         |
| `-q 30`   | Retain alignments with MAPQ ≥ 30                                         |
| `-f 2`    | Retain properly paired reads                                             |
| `-F 2316` | Exclude unmapped, mate-unmapped, secondary, and supplementary alignments |

The exclusion flag `2316` corresponds to:

```text
4      unmapped read
8      mate unmapped
256    secondary alignment
2048   supplementary alignment
```

## Mitochondrial Read Removal

Reads aligned to the mitochondrial chromosome (`chrM`) were removed from the filtered BAM files.

This step focused the downstream analysis on nuclear chromatin accessibility and reduced the contribution of mitochondrial reads, which can represent a substantial fraction of ATAC-seq libraries.

## Mate Information and Sorting

After filtering, BAM files were prepared for duplicate removal using SAMtools.

The processing sequence included:

1. name-sorting the BAM file;
2. adding mate information with `samtools fixmate -m`;
3. coordinate-sorting the resulting BAM file.

This preparation allows duplicate marking to use paired-end fragment information correctly.

## PCR Duplicate Removal

PCR duplicates were removed using:

```bash
samtools markdup -r
```

The `-r` option removes reads identified as duplicates rather than only marking them.

The resulting BAM files therefore represented high-quality, properly paired, non-mitochondrial alignments with duplicate reads removed.

## BAM Indexing and QC

Final cleaned BAM files were indexed with SAMtools:

```bash
samtools index SAMPLE_clean.bam
```

Additional BAM-level checks were performed using tools such as:

```bash
samtools flagstat
samtools idxstats
```

These summaries were used to review read retention after filtering and cleanup.

## Read Retention

Read counts decreased progressively during filtering and duplicate removal, as expected.

Examples from the completed analysis are shown below.

| Sample     | Aligned reads | After filtering | After chrM removal | Final clean reads |
| ---------- | ------------: | --------------: | -----------------: | ----------------: |
| 28P_1_L1   |    79,114,352 |      65,452,920 |         54,853,439 |        34,711,208 |
| 28P_1_L2   |    78,214,964 |      64,678,254 |         54,173,456 |        34,413,830 |
| 39P_2_L1   |    73,099,113 |      60,768,260 |         58,422,604 |        44,899,322 |
| 39P_2_L2   |    73,799,160 |      61,313,962 |         58,917,986 |        45,141,556 |
| ORG15_1_L1 |   108,031,999 |      86,537,042 |         83,567,859 |        45,320,678 |
| ORG15_1_L2 |   110,225,873 |      88,161,707 |         85,056,471 |        45,715,775 |
| ORG34_5_L1 |   109,365,905 |      34,412,272 |         24,697,224 |        17,710,780 |
| ORG34_5_L2 |   111,221,970 |      34,820,928 |         24,928,295 |        17,856,370 |
| ORG39_6_L1 |    93,017,628 |      75,229,461 |         64,300,272 |        39,268,183 |
| ORG39_6_L2 |    94,500,331 |      76,395,291 |         65,153,866 |        39,615,232 |
| ORG40_8_L1 |   130,248,720 |      98,279,637 |         92,868,594 |        72,912,995 |
| ORG40_8_L2 |   134,516,210 |     101,143,981 |         95,603,413 |        74,451,470 |
| ORG44_7_L1 |    98,756,458 |      68,715,982 |         64,518,994 |        47,243,601 |
| ORG44_7_L2 |   101,617,131 |      70,276,513 |         65,909,237 |        47,904,859 |
| PK4_9_L1   |   103,774,272 |      82,744,921 |         48,052,340 |        36,711,776 |
| PK4_9_L2   |   106,447,741 |      84,665,019 |         48,975,798 |        37,420,196 |

The largest reductions were observed in libraries with lower alignment quality or higher proportions of reads removed during mitochondrial filtering and duplicate cleanup.

## Workflow

```text
Sorted BAM
    │
    ▼
MAPQ ≥ 30
Properly paired reads
    │
    ▼
Remove unwanted alignment flags
    │
    ▼
Remove chrM reads
    │
    ▼
Name sort
    │
    ▼
SAMtools fixmate
    │
    ▼
Coordinate sort
    │
    ▼
SAMtools markdup -r
    │
    ▼
Index final BAM
    │
    ▼
Clean BAM for downstream analysis
```

## Output

The final output of this step was a cleaned BAM file for each retained ATAC-seq library.

These files were used as the input for downstream ATAC-seq processing and peak calling.

## Next Step

**Step 4 — ATAC-seq Quality Control and Peak Calling**

The cleaned BAM files were used to evaluate ATAC-seq-specific library quality and identify accessible chromatin regions.

