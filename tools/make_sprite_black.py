"""Cut a character out of a black background and save a transparent PNG.

Made for glowing art (ice, magic): transparency follows brightness, so a soft
glow fades out smoothly instead of leaving a black fringe.

Usage:
    python3 tools/make_sprite_black.py <input.png> <output.png> [threshold] [scale]

threshold  brightness (0-255) above which a pixel is fully opaque, default 70
scale      resize factor, default 0.45 (use the same for all poses of one character)

The output is never overwritten: if the file exists, the script stops.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

if len(sys.argv) not in (3, 4, 5):
    sys.exit(__doc__)

src, dst = Path(sys.argv[1]).expanduser(), Path(sys.argv[2]).expanduser()
thr = float(sys.argv[3]) if len(sys.argv) > 3 else 70
scale = float(sys.argv[4]) if len(sys.argv) > 4 else .45
if dst.exists():
    sys.exit(f"File exists, not overwriting: {dst}")

rgb = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
bright = rgb.max(axis=2)

# near-black noise (JPEG-like dirt in the background) is cut off completely
floor = 12
alpha = np.clip((bright - floor) / (thr - floor), 0, 1)

# un-mix the black: a half-transparent pixel gets its full colour back,
# so the glow keeps its colour over any ground instead of turning grey
safe = np.maximum(alpha, 1e-3)[..., None]
col = np.clip(rgb / safe, 0, 255)
col = np.where(alpha[..., None] > 0, col, 0)

out = np.dstack([col, alpha * 255]).astype(np.uint8)
img = Image.fromarray(out, "RGBA")

bbox = img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
pad = 8
box = (max(bbox[0] - pad, 0), max(bbox[1] - pad, 0), min(bbox[2] + pad, img.width), min(bbox[3] + pad, img.height))
img = img.crop(box)
k = scale
if k != 1:
    img = img.resize((round(img.width * k), round(img.height * k)), Image.LANCZOS)
dst.parent.mkdir(parents=True, exist_ok=True)
img.save(dst, optimize=True)
print(f"Saved: {dst}  size {img.width}x{img.height}  scale {k}  crop {box}")
