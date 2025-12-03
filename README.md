# Luxeillum Catalogue Build

This repository contains a templated catalogue (the source) and the rendered output (the file you ship). The build step hydrates `catalogue.template.html` with values from `variables.json` to produce the finalized `catalogue.html` that should be checked in and shared.

## Prerequisites
- Python 3.11+ (any recent Python 3 works)

## Render the catalogue
1. Update `variables.json` with any new values (copy URLs for images, change pricing, etc.).
2. Run the renderer:
   ```bash
   python render_catalogue.py
   ```
   This reads `catalogue.template.html` and writes the fully rendered `catalogue.html` with all placeholders filled.
3. Commit the updated `catalogue.html` along with any template or variable changes so the repository always carries the processed output.

## Exporting to PDF (optional)
Open the rendered `catalogue.html` in a browser and use **Print → Save as PDF**. Ensure background graphics are enabled for accurate colors.
