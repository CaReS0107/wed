from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
img = Image.new('RGB', (W, H), '#f5f0e8')
draw = ImageDraw.Draw(img)

# Background gradient effect with subtle dots
for x in range(0, W, 30):
    for y in range(0, H, 30):
        draw.ellipse([x+14, y+14, x+16, y+16], fill='#e8e3db')

# Border
gold = '#9a8c5e'
gold_light = '#c9a84c'
draw.rounded_rectangle([30, 30, W-30, H-30], radius=6, outline=gold, width=2)
draw.rounded_rectangle([42, 42, W-42, H-42], radius=4, outline=gold_light, width=1)

# Wedding rings
cx1, cy1 = 560, 220  # Left ring center
cx2, cy2 = 640, 220  # Right ring center
r = 65  # Ring radius

# Draw rings with thickness
for offset in range(-4, 5):
    draw.ellipse([cx1-r+offset//2, cy1-r+offset//3, cx1+r+offset//2, cy1+r+offset//3], outline=gold, width=3)
    draw.ellipse([cx2-r+offset//2, cy2-r+offset//3, cx2+r+offset//2, cy2+r+offset//3], outline=gold, width=3)

# Clean rings
draw.ellipse([cx1-r, cy1-r, cx1+r, cy1+r], outline=gold, width=7)
draw.ellipse([cx2-r, cy2-r, cx2+r, cy2+r], outline=gold, width=7)

# Inner ring shine lines
draw.ellipse([cx1-r+10, cy1-r+10, cx1+r-10, cy1+r-10], outline=gold_light, width=1)
draw.ellipse([cx2-r+10, cy2-r+10, cx2+r-10, cy2+r-10], outline=gold_light, width=1)

# Diamond on right ring
diamond_top = (cx2, cy2 - r - 20)
diamond_left = (cx2 - 15, cy2 - r)
diamond_right = (cx2 + 15, cy2 - r)
draw.polygon([diamond_top, diamond_left, diamond_right], outline=gold, width=3)
draw.line([diamond_left, diamond_right], fill=gold, width=2)

# Sparkles around diamond
sparkle_color = '#c9a84c'
# Top
draw.line([(cx2, cy2-r-30), (cx2, cy2-r-24)], fill=sparkle_color, width=2)
# Left
draw.line([(cx2-18, cy2-r-15), (cx2-12, cy2-r-10)], fill=sparkle_color, width=2)
# Right
draw.line([(cx2+18, cy2-r-15), (cx2+12, cy2-r-10)], fill=sparkle_color, width=2)

# Try to load a nice font, fall back to default
try:
    font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Italic.ttf", 68)
    font_amp = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Italic.ttf", 52)
    font_date = ImageFont.truetype("/System/Library/Fonts/Supplemental/Helvetica Neue.ttc", 24)
except:
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Georgia.ttf", 68)
        font_amp = ImageFont.truetype("/System/Library/Fonts/Georgia.ttf", 52)
        font_date = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    except:
        font_large = ImageFont.load_default().font_variant(size=68)
        font_amp = ImageFont.load_default().font_variant(size=52)
        font_date = ImageFont.load_default().font_variant(size=24)

# Names
text_color = '#333333'
y_names = 340

# Measure text
vasile_bbox = draw.textbbox((0, 0), "Vasile", font=font_large)
amp_bbox = draw.textbbox((0, 0), " & ", font=font_amp)
victoria_bbox = draw.textbbox((0, 0), "Victoria", font=font_large)

vasile_w = vasile_bbox[2] - vasile_bbox[0]
amp_w = amp_bbox[2] - amp_bbox[0]
victoria_w = victoria_bbox[2] - victoria_bbox[0]

total_w = vasile_w + amp_w + victoria_w
start_x = (W - total_w) // 2

draw.text((start_x, y_names), "Vasile", fill=text_color, font=font_large)
draw.text((start_x + vasile_w, y_names + 10), " & ", fill=gold, font=font_amp)
draw.text((start_x + vasile_w + amp_w, y_names), "Victoria", fill=text_color, font=font_large)

# Decorative line
line_y = y_names + 85
draw.line([(420, line_y), (780, line_y)], fill=gold_light, width=1)

# Date
date_text = "11 SEPTEMBRIE 2026"
date_bbox = draw.textbbox((0, 0), date_text, font=font_date)
date_w = date_bbox[2] - date_bbox[0]
draw.text(((W - date_w) // 2, line_y + 15), date_text, fill=gold, font=font_date)

# Small heart
hx, hy = W // 2, line_y + 60
heart_points = []
for t in range(0, 360):
    rad = math.radians(t)
    x = 8 * (16 * math.sin(rad)**3)
    y = -8 * (13 * math.cos(rad) - 5 * math.cos(2*rad) - 2 * math.cos(3*rad) - math.cos(4*rad))
    heart_points.append((hx + x/12, hy + y/12))
draw.line(heart_points, fill=gold, width=1)

# Save
img.save('/Users/vasilepapuc/Business/Wedding/og-image.jpg', 'JPEG', quality=90)
print("Done! og-image.jpg created")

