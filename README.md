# Hero Composer

**Internal tool — Fubo employees only. Do not share externally.**

A browser-based tool for composing hero images for fubo.tv. Upload a background image, select logos, configure overlays, preview across all breakpoints, and export production-ready files — no design software needed.

---

## What it does

You bring in an AI-generated image, add team or league logos in white circles, configure the overlay, preview how it looks at every breakpoint, and export flat PNGs at the correct dimensions — ready to hand off directly to engineering.

---

## Workflow

### Step 1 — Upload background image
Upload any image from Google Flow. Drag and drop supported. Once uploaded, drag the image to reposition it within the frame — each breakpoint remembers its own position independently.

### Step 2 — Select logos
Browse logos by sport using the tabs at the top of the Logo Selection panel. Use the search bar to find any team or league across all sports. Click a logo to select it — selected logos appear as chips below the grid. Click again to deselect.

**Available sports:** NFL · NBA · NHL · MLB · UFL · NCAA · Soccer · Tennis · Networks

**Soccer sub-categories:** MLS · EPL · La Liga · Serie A · Bundesliga · Ligue 1 · Primeira Liga · Eredivisie · Süper Lig · Brasileirão · Liga Profesional · Scottish Premiership · Liga MX · CPL · Leagues

### Step 3 — Logo placement
Choose a layout, position, circle size, and spacing. The grid auto-expands rows to always show every selected logo — no logos are ever hidden.

| Layout | Description |
|---|---|
| Single | One logo |
| 2 × 2 | 2 columns, auto rows |
| 3 × 4 | 4 columns, auto rows |
| Row | All logos in a single row |
| Custom Grid | Set your own columns and rows |

### Step 4 — Overlay
Choose an overlay style, color, opacity, and reach. **Right Fade** is the default — matches the current fubo.tv hero treatment.

| Style | Description |
|---|---|
| Right Fade | Fades from right (default) |
| Left Fade | Fades from left |
| Full Dark Tint | Uniform dark overlay |
| Bottom Fade | Fades from bottom up |
| Vignette | Dark edges, bright center |
| None | No overlay |

### Step 5 — Export
Select one or more formats and click **Export Selected Formats**. Each format downloads as a flat PNG, ready for engineering.

---

## Export formats & safe zones

| Format | Dimensions | Safe zone (text & CTAs) |
|---|---|---|
| CTV · Landscape | 3840 × 2160 px | Left 40% — x 0–1536 |
| Mobile · Landscape | 1600 × 720 px | Left 40% — x 0–640 |
| Mobile · Portrait | 720 × 1600 px | Bottom 50% — y 800–1600 |
| Tablet · Landscape | 1024 × 768 px | Left 40% — x 0–410 |
| Tablet · Portrait | 768 × 1024 px | Bottom 45% — y 563–1024 |

Toggle **Show safe zone overlay** to see a preview of where the fubo UI elements (logo, headline, CTAs) will appear on the landscape formats. This preview is never included in exported files.

---

## Repositioning per breakpoint

Each breakpoint has its own independent image position. Switch the preview dropdown in the toolbar to a different format, then drag the image to reposition it for that specific breakpoint. CTV might show the full player while Mobile Portrait focuses on the torso — each exports with its own position baked in.

Click **↺ Reset Pan** in the toolbar to recenter the image for the current breakpoint.

---


## Questions or feedback

Reach out to the Thaymisan Cavalcante on Slack or open an issue in this repo.
