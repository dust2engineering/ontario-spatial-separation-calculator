#!/usr/bin/env python3
"""Ontario spatial separation quick check (OBC 3.2.3.1). See README.md for scope."""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "spatial-separation-data.json")))

def pct(face, band, ld):
    row = D["table_3.2.3.1B_not_sprinklered_groups_A_C_D_F3_percent"].get("%g" % face, {}).get(band)
    if row is None: return None
    cols = D["limiting_distance_columns_m"]
    idx = max(i for i, c in enumerate(cols) if c <= ld)
    return row[idx] if idx < len(row) else 100

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--face-area", type=float, required=True, help="exposing building face area, m2 (10, 15 or 20)")
    p.add_argument("--length", type=float, required=True)
    p.add_argument("--height", type=float, required=True)
    p.add_argument("--limiting-distance", type=float, required=True)
    a = p.parse_args()
    ratio = max(a.length / a.height, a.height / a.length)
    band = "lt3" if ratio < 3 else ("3to10" if ratio <= 10 else "gt10")
    v = pct(a.face_area, band, a.limiting_distance)
    if v is None:
        print("Outside the verified rows of this quick tool (face areas 10/15/20 m2; the 15 and 20 m2 rows cover L/H up to 10:1). Consult full Table 3.2.3.1.B.")
        return
    print(f"Exposing face {a.face_area:g} m2, L/H ratio {ratio:.1f}:1 (band {band}), limiting distance {a.limiting_distance:g} m")
    print(f"Maximum aggregate unprotected openings: {v}% of the face = {v * a.face_area / 100:.2f} m2")
    if a.limiting_distance <= 2 and a.limiting_distance >= 1.2:
        print(f"Each individual opening (not sprinklered, LD <= 2 m): max {0.24 * (2 * a.limiting_distance - 1.2) ** 2:.2f} m2 (Table 3.2.3.1.A formula)")
    print("Preliminary only - verify against the OBC in force.")

if __name__ == "__main__":
    main()
