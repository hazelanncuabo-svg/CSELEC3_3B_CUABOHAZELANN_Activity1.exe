from PIL import Image, ImageDraw, ImageFont

canvas_w, canvas_h = 600, 800
img = Image.new("RGB", (canvas_w, canvas_h), (250, 230, 250))  # light pink background
draw = ImageDraw.Draw(img)

trophy_color = (230, 180, 100)   # gold-like color
outline_color = (100, 70, 50)   # darker brown for outline
text_color = (0, 0, 0)

oval_bbox = (180, 80, 420, 460)  # left, top, right, bottom
draw.ellipse(oval_bbox, fill=trophy_color, outline=outline_color, width=5)

base_top = 450
draw.ellipse((150, base_top+50, 450, base_top+110), fill=trophy_color, outline=outline_color, width=4)

base_height = 80
base_bbox = (180, base_top, 420, base_top + base_height)
draw.rectangle(base_bbox, fill=trophy_color, outline=outline_color, width=4)

title_font = ImageFont.truetype("timesbd.ttf", 54)
subtitle_font = ImageFont.truetype("timesbd.ttf", 32)
small_font = ImageFont.truetype("arialbd.ttf", 24)

text = "CCIS"
bbox = draw.textbbox((15, 15), text, font=title_font)
w = bbox[2] - bbox[0]
draw.text(((canvas_w - w) // 2, 140), text, font=title_font, fill=text_color)

text2 = "PHANTOMS"
bbox2 = draw.textbbox((0, 0), text2, font=subtitle_font)
w2 = bbox2[2] - bbox2[0]
draw.text(((canvas_w - w2) // 2, 190), text2, font=subtitle_font, fill=text_color)

text3 = "2nd PLACER"
bbox3 = draw.textbbox((0, 0), text3, font=subtitle_font)
w3 = bbox3[2] - bbox3[0]
draw.text(((canvas_w - w3) // 2, base_top+15), text3, font=subtitle_font, fill=text_color)

text4 = "INTRAMURALS 2025"
bbox4 = draw.textbbox((0, 0), text4, font=small_font)
w4 = bbox4[2] - bbox4[0]
draw.text(((canvas_w - w4) // 2, base_top+45), text4, font=small_font, fill=text_color)

img.save("trophy_award.png")
img.show()