# Luxeillum Catalogue

This repository contains the Luxeillum catalogue HTML alongside the data used to render it.

## Regenerating the catalogue

1. Update `variables.json` with any new text, links, or imagery.
2. Run the renderer to merge the template with the variables:
   ```bash
   python render_catalogue.py
   ```
   This writes the rendered output to `catalogue.html` using `catalogue.template.html` as the template.

Commit both the template and rendered HTML whenever content changes so the published catalogue matches the data source.
