#!/usr/bin/env bash
# Regenerates docs/assets/social-preview.png (1280x640, under 1 MB) with ImageMagick.
# GitHub: Settings > Social preview > upload this file.
set -euo pipefail
cd "$(dirname "$0")/.."
BOLD=/usr/share/fonts/truetype/lato/Lato-Bold.ttf
REG=/usr/share/fonts/truetype/lato/Lato-Regular.ttf
MONO=/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf
COUNT=$(python3 -c "import json;print(len(json.load(open('skills.json'))['skills']))")
convert -size 1280x640 xc:'#ffffff' \
  -fill '#2563eb' -draw 'rectangle 0,0 1280,14' \
  \( docs/assets/syncgrowth-mark.png -resize x300 \) -gravity northeast -geometry +90+110 -composite \
  -gravity northwest -font "$BOLD" -fill '#0a0a0a' -pointsize 84 -annotate +80+96 'Marketing skills' \
  -fill '#2563eb' -annotate +80+192 'for AI agents' \
  -font "$REG" -fill '#4b5563' -pointsize 31 -annotate +80+322 "${COUNT} skills for conversion, copy, SEO, ads, analytics," \
  -annotate +80+366 'lifecycle and outbound. Open Agent Skills format.' \
  -fill '#eff6ff' -draw 'roundrectangle 80,440 862,516 14,14' \
  -font "$MONO" -fill '#1d4ed8' -pointsize 28 -annotate +106+462 'npx skills add SyncGrowth/marketing-skills' \
  -font "$REG" -fill '#4b5563' -pointsize 24 -annotate +80+566 'Maintained by SyncGrowth  |  MIT  |  Adapted from coreyhaines31/marketingskills' \
  -strip -colors 128 PNG8:docs/assets/social-preview.png
ls -l docs/assets/social-preview.png
