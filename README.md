# Ontario Spatial Separation Calculator

A quick spatial-separation check: given the limiting distance, the area of an exposing building face and its length-to-height ratio, it returns the maximum aggregate area of unprotected openings from Ontario Building Code Table 3.2.3.1.B (building not sprinklered throughout, Groups A, C, D and F Division 3), plus the Table 3.2.3.1.A cap on each individual opening close to the line.

**Live web tool:** https://dust2engineering.github.io/ontario-spatial-separation-calculator/web/

## How it works

- Pick the table column at or below the actual limiting distance (the Code table is read in steps, not interpolated).
- Pick the next larger face-area row when the face falls between listed areas.
- Individual opening cap for limiting distances of 2 m or less: 0.24 x (2 x LD - 1.2)^2 m2.

## Data in this repository

- spatial-separation-data.json — the table rows and the opening-cap formula, machine-readable.

## Command line

```bash
python3 spatial_separation.py --face-area 20 --length 8 --height 3.2 --limiting-distance 2.5
```

## Worked examples

- [storefront-wall-20m2.md](examples/storefront-wall-20m2.md)
- [side-wall-10m2.md](examples/side-wall-10m2.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Fire and life safety. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
