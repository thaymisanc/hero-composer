#!/usr/bin/env python3
"""
rename_logos.py
---------------
1. Strips "Property 1=" from all filenames in this folder and subfolders
2. Generates manifest.json for the Fubo Hero Composer

USAGE
-----
Place this script in your logos root folder (the one containing MLB, NBA, Soccer etc.)

    your-logos-folder/
      rename_logos.py   ← this script goes here
      MLB/
      NBA/
      NFL/
      NHL/
      UFL/
      NCAA/
        Conferences/
        Teams/
      Soccer/
        Leagues/
        Teams/
          England/
          Spain/  etc.
      Tennis/

Then in Terminal:
    cd ~/Desktop/your-logos-folder
    python3 rename_logos.py

Afterwards, rename the folder to "logos" and place it
next to fubo_composer.html. The Composer auto-loads logos/manifest.json.
"""

import os
import re
import json
from pathlib import Path

PREFIX = "Property 1="

# Maps folder path patterns → (sport, sub-category label)
SUB_MAP = {
    "Soccer/Teams/England":     ("Soccer", "EPL"),
    "Soccer/Teams/Spain":       ("Soccer", "La Liga"),
    "Soccer/Teams/Italy":       ("Soccer", "Serie A"),
    "Soccer/Teams/Germany":     ("Soccer", "Bundesliga"),
    "Soccer/Teams/France":      ("Soccer", "Ligue 1"),
    "Soccer/Teams/Portugal":    ("Soccer", "Primeira Liga"),
    "Soccer/Teams/Netherlands": ("Soccer", "Eredivisie"),
    "Soccer/Teams/Turkey":      ("Soccer", "Süper Lig"),
    "Soccer/Teams/Brazil":      ("Soccer", "Brasileirão"),
    "Soccer/Teams/Argentina":   ("Soccer", "Liga Profesional"),
    "Soccer/Teams/Scotland":    ("Soccer", "Scottish Premiership"),
    "Soccer/Teams/Mexico":      ("Soccer", "Liga MX"),
    "Soccer/Teams/MLS":         ("Soccer", "MLS"),
    "Soccer/Teams/Canada":      ("Soccer", "CPL"),
    "Soccer/Leagues":           ("Soccer", "Leagues"),
    "NCAA/Teams":               ("NCAA",   "Teams"),
    "NCAA/Conferences":         ("NCAA",   "Conferences"),
}

UPPER_WORDS = {'FC','SC','CF','AFC','BC','BSC','HSV','VFL','SD','UD','RC','RB','AC','SS','AS','FK','MLS','CPL','NFL','NBA','NHL','MLB','UFL','NCAA'}

def clean_stem(raw_filename):
    s = raw_filename
    if s.startswith(PREFIX):
        s = s[len(PREFIX):]
    stem = Path(s).stem
    stem = re.sub(r'_logo\s*\d*\s*\d*$', '', stem, flags=re.IGNORECASE)
    stem = re.sub(r'\s+logo\s*\d*$',      '', stem, flags=re.IGNORECASE)
    stem = re.sub(r'_20\d{2}\s*\d*$',     '', stem)
    stem = re.sub(r'\s+\d+$',             '', stem)
    stem = re.sub(r'\d+$',                '', stem).strip()
    stem = stem.replace('_', ' ').strip()
    stem = re.sub(r'\s+', ' ', stem)
    words = [w.upper() if w.upper() in UPPER_WORDS else w.capitalize() for w in stem.split()]
    return ' '.join(words)

def infer_sport_sub(rel_folder_str):
    best_key, best_val = '', None
    for key, val in SUB_MAP.items():
        norm = rel_folder_str.replace('\\','/')
        if norm.startswith(key) and len(key) > len(best_key):
            best_key, best_val = key, val
    if best_val:
        return best_val
    parts = rel_folder_str.replace('\\','/').split('/')
    sport = parts[0] if parts and parts[0] else 'Other'
    sub   = parts[1] if len(parts) > 1 else ''
    return (sport, sub)

def make_id(sport, sub, name):
    def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    parts = [slug(sport)]
    if sub:  parts.append(slug(sub))
    parts.append(slug(name))
    return '-'.join(parts)

def main():
    root     = Path(__file__).parent
    manifest = []
    renamed  = 0
    skipped  = 0
    errors   = []

    for filepath in sorted(root.rglob('*.png')):
        # Skip the script itself (shouldn't happen but safety check)
        if filepath.suffix.lower() != '.png':
            continue

        original_name = filepath.name

        # ── Step 1: Rename ──
        if original_name.startswith(PREFIX):
            new_stem = clean_stem(original_name)
            new_path = filepath.parent / (new_stem + '.png')
            counter  = 1
            while new_path.exists() and new_path != filepath:
                new_path = filepath.parent / (f"{new_stem} {counter}.png")
                counter += 1
            try:
                filepath.rename(new_path)
                filepath = new_path
                renamed += 1
                print(f"  ✅ {original_name}  →  {new_path.name}")
            except Exception as e:
                errors.append(f"Could not rename {original_name}: {e}")
                continue
        else:
            skipped += 1

        # ── Step 2: Add to manifest ──
        rel_folder = str(filepath.parent.relative_to(root))
        sport, sub = infer_sport_sub(rel_folder)
        name       = filepath.stem
        logo_id    = make_id(sport, sub, name)
        # File path as it will appear relative to composer HTML
        # e.g. logos/NFL/Arizona Cardinals.png
        file_rel   = 'logos/' + '/'.join(filepath.relative_to(root).parts)

        manifest.append({
            'id':    logo_id,
            'name':  name,
            'sport': sport,
            'sub':   sub,
            'file':  file_rel,
        })

    # Sort
    manifest.sort(key=lambda x: (x['sport'], x['sub'], x['name']))

    # Write manifest.json in the same folder as the script
    out = root / 'manifest.json'
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*50}")
    print(f"  ✅ {renamed} files renamed")
    print(f"  ✓  {skipped} already clean (no prefix)")
    print(f"  📋 {len(manifest)} logos in manifest.json")
    if errors:
        print(f"\n  ⚠️  {len(errors)} errors:")
        for e in errors: print(f"     {e}")
    print(f"\n  Next steps:")
    print(f"  1. Rename this folder to 'logos'")
    print(f"  2. Place 'logos/' next to fubo_composer.html")
    print(f"  3. Open fubo_composer.html — logos load automatically")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
