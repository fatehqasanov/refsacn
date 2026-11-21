import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Realistic Phone Outer Dimensions: 600 x 1240 (Inner Display: 520 x 1120)
OUTER_W, OUTER_H = 600, 1240
INNER_W, INNER_H = 520, 1120
MARGIN_X, MARGIN_Y = 40, 60

FRAME_COLOR = (24, 26, 32)      # Sleek Titanium Black Phone Bezel
FRAME_BORDER = (45, 48, 56)     # Bezel highlight border
BG_COLOR = (255, 251, 254)       # Material 3 Light BG
PURPLE_CONTAINER = (234, 221, 255) # Light primary container
PURPLE = (103, 80, 164)          # Material 3 primary
DARK_TEXT = (29, 27, 32)
MUTED_TEXT = (73, 69, 79)
OUTLINE_COLOR = (121, 116, 126)
WHITE = (255, 255, 255)
GOLD = (255, 184, 0)
GREEN_BADGE = (230, 245, 233)
GREEN_TEXT = (22, 101, 52)

def get_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

font_title = get_font(30)
font_h2 = get_font(19)
font_subtitle = get_font(14)
font_label = get_font(13)
font_input = get_font(14)
font_btn = get_font(14)

def draw_phone_frame(canvas):
    draw = ImageDraw.Draw(canvas)
    # Phone Body Outer Shell
    draw.rounded_rectangle([10, 10, OUTER_W-10, OUTER_H-10], radius=44, fill=FRAME_COLOR, outline=FRAME_BORDER, width=3)
    # Screen Cutout Mask (Inner Display)
    screen_mask = Image.new("L", (INNER_W, INNER_H), 0)
    sdraw = ImageDraw.Draw(screen_mask)
    sdraw.rounded_rectangle([0, 0, INNER_W, INNER_H], radius=28, fill=255)
    return screen_mask

def apply_phone_shell(screen_img):
    canvas = Image.new("RGB", (OUTER_W, OUTER_H), (240, 242, 245)) # Soft background studio drop
    draw = ImageDraw.Draw(canvas)

    # Draw Phone Body Frame
    draw.rounded_rectangle([10, 10, OUTER_W-10, OUTER_H-10], radius=44, fill=FRAME_COLOR, outline=FRAME_BORDER, width=3)

    # Paste Inner Display Screen using rounded mask
    mask = Image.new("L", (INNER_W, INNER_H), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, INNER_W, INNER_H], radius=26, fill=255)
    canvas.paste(screen_img, (MARGIN_X, MARGIN_Y), mask)

    # Draw Camera Punch Hole & Top Earpiece
    draw.ellipse([OUTER_W//2 - 12, MARGIN_Y + 10, OUTER_W//2 + 12, MARGIN_Y + 34], fill=(10, 10, 12))
    draw.ellipse([OUTER_W//2 - 5, MARGIN_Y + 17, OUTER_W//2 + 5, MARGIN_Y + 27], fill=(25, 30, 45)) # Lens glass

    return canvas

def draw_status_bar(draw):
    draw.text((24, 14), "09:41", fill=DARK_TEXT, font=get_font(13))
    # 5G & Battery
    draw.text((INNER_W-110, 14), "5G", fill=DARK_TEXT, font=get_font(12))
    draw.rectangle([INNER_W-60, 16, INNER_W-36, 28], outline=DARK_TEXT, width=2)
    draw.rectangle([INNER_W-58, 18, INNER_W-42, 26], fill=DARK_TEXT)

def draw_nav_bar(draw):
    draw.rectangle([INNER_W//2 - 60, INNER_H - 14, INNER_W//2 + 60, INNER_H - 9], fill=DARK_TEXT)

# Procedural realistic material textures
def draw_asphalt_texture(img, box):
    x0, y0, x1, y1 = box
    tex = Image.new("RGB", (x1-x0, y1-y0), (35, 38, 45))
    tdraw = ImageDraw.Draw(tex)
    for i in range(0, x1-x0, 4):
        for j in range(0, y1-y0, 4):
            val = (i*7 + j*13) % 40
            tdraw.rectangle([i, j, i+3, j+3], fill=(30+val, 33+val, 40+val))
    tdraw.ellipse([10, 10, (x1-x0)-10, (y1-y0)-10], outline=(80, 110, 140), width=3)
    img.paste(tex, (x0, y0))

def draw_moss_texture(img, box):
    x0, y0, x1, y1 = box
    tex = Image.new("RGB", (x1-x0, y1-y0), (50, 75, 45))
    tdraw = ImageDraw.Draw(tex)
    for y in range(0, y1-y0, 15):
        tdraw.line([0, y, x1-x0, y], fill=(30, 45, 25), width=2)
    for x in range(0, x1-x0, 25):
        tdraw.line([x, 0, x, y1-y0], fill=(30, 45, 25), width=2)
    tdraw.ellipse([5, 5, 35, 35], fill=(70, 130, 50))
    img.paste(tex, (x0, y0))

def draw_wood_texture(img, box):
    x0, y0, x1, y1 = box
    tex = Image.new("RGB", (x1-x0, y1-y0), (140, 85, 40))
    tdraw = ImageDraw.Draw(tex)
    for i in range(0, x1-x0, 6):
        tdraw.line([i, 0, i+10, y1-y0], fill=(110, 60, 25), width=2)
    img.paste(tex, (x0, y0))

def create_login_screen():
    screen = Image.new("RGB", (INNER_W, INNER_H), BG_COLOR)
    draw = ImageDraw.Draw(screen)
    draw_status_bar(draw)

    draw.text((INNER_W//2, 240), "RefScan", fill=PURPLE, font=font_title, anchor="mm")
    draw.text((INNER_W//2, 285), "Log in to your account", fill=MUTED_TEXT, font=font_subtitle, anchor="mm")

    y = 370
    draw.rounded_rectangle([35, y, INNER_W-35, y+52], radius=8, outline=PURPLE, width=2)
    draw.text((48, y-9), " Email ", fill=PURPLE, font=get_font(11))
    draw.text((48, y+16), "fatehqasanov@gmail.com", fill=DARK_TEXT, font=font_input)

    y = 455
    draw.rounded_rectangle([35, y, INNER_W-35, y+52], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((48, y-9), " Password ", fill=MUTED_TEXT, font=get_font(11))
    draw.text((48, y+16), "••••••••••••", fill=DARK_TEXT, font=font_input)

    y = 550
    draw.rounded_rectangle([35, y, INNER_W-35, y+48], radius=24, fill=PURPLE)
    draw.text((INNER_W//2, y+24), "Log in", fill=WHITE, font=font_btn, anchor="mm")

    y = 620
    draw.text((INNER_W//2, y), "No account? Register", fill=PURPLE, font=font_subtitle, anchor="mm")

    draw_nav_bar(draw)
    final_img = apply_phone_shell(screen)
    final_img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\login_screenshot.png")

def create_register_screen():
    screen = Image.new("RGB", (INNER_W, INNER_H), BG_COLOR)
    draw = ImageDraw.Draw(screen)
    draw_status_bar(draw)

    draw.text((INNER_W//2, 200), "RefScan", fill=PURPLE, font=font_title, anchor="mm")
    draw.text((INNER_W//2, 245), "Create a new account", fill=MUTED_TEXT, font=font_subtitle, anchor="mm")

    y = 320
    draw.rounded_rectangle([35, y, INNER_W-35, y+52], radius=8, outline=PURPLE, width=2)
    draw.text((48, y-9), " Email ", fill=PURPLE, font=get_font(11))
    draw.text((48, y+16), "fatehqasanov@gmail.com", fill=DARK_TEXT, font=font_input)

    y = 400
    draw.rounded_rectangle([35, y, INNER_W-35, y+52], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((48, y-9), " Password ", fill=MUTED_TEXT, font=get_font(11))
    draw.text((48, y+16), "••••••••••••", fill=DARK_TEXT, font=font_input)

    y = 480
    draw.rounded_rectangle([35, y, INNER_W-35, y+52], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((48, y-9), " Confirm Password ", fill=MUTED_TEXT, font=get_font(11))
    draw.text((48, y+16), "••••••••••••", fill=DARK_TEXT, font=font_input)

    y = 575
    draw.rounded_rectangle([35, y, INNER_W-35, y+48], radius=24, fill=PURPLE)
    draw.text((INNER_W//2, y+24), "Create account", fill=WHITE, font=font_btn, anchor="mm")

    y = 645
    draw.text((INNER_W//2, y), "Already have an account? Log in", fill=PURPLE, font=font_subtitle, anchor="mm")

    draw_nav_bar(draw)
    final_img = apply_phone_shell(screen)
    final_img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\register_screenshot.png")

def create_reference_list_screen():
    screen = Image.new("RGB", (INNER_W, INNER_H), BG_COLOR)
    draw = ImageDraw.Draw(screen)
    draw_status_bar(draw)

    # Top Bar
    draw.rectangle([0, 45, INNER_W, 105], fill=PURPLE_CONTAINER)
    draw.text((20, 68), "RefScan Material References", fill=DARK_TEXT, font=font_h2)
    draw.rectangle([INNER_W-50, 68, INNER_W-20, 92], outline=PURPLE, width=2)

    # E1: Search Bar
    y = 125
    draw.rounded_rectangle([20, y, INNER_W-20, y+46], radius=23, outline=OUTLINE_COLOR, width=1)
    draw.text((35, y+13), "🔍  Search by note or level...", fill=MUTED_TEXT, font=font_input)

    # E7: Statistics Header Card
    y = 188
    draw.rounded_rectangle([20, y, INNER_W-20, y+68], radius=12, fill=PURPLE_CONTAINER)
    draw.text((35, y+13), "Logged in: fatehqasanov@gmail.com", fill=MUTED_TEXT, font=get_font(11))
    draw.text((35, y+35), "Total References: 3", fill=DARK_TEXT, font=font_label)
    draw.text((INNER_W-35, y+35), "2 active · 1 archived", fill=PURPLE, font=font_label, anchor="ra")

    # E5: Status Filter Chips
    y = 270
    draw.rounded_rectangle([20, y, 95, y+30], radius=15, fill=PURPLE)
    draw.text((57, y+15), "All (3)", fill=WHITE, font=get_font(11), anchor="mm")

    draw.rounded_rectangle([105, y, 195, y+30], radius=15, outline=OUTLINE_COLOR)
    draw.text((150, y+15), "Active (2)", fill=DARK_TEXT, font=get_font(11), anchor="mm")

    draw.rounded_rectangle([205, y, 310, y+30], radius=15, outline=OUTLINE_COLOR)
    draw.text((257, y+15), "Archived (1)", fill=DARK_TEXT, font=get_font(11), anchor="mm")

    # Item 1 with Texture Thumbnail Photo
    y = 318
    draw.rounded_rectangle([20, y, INNER_W-20, y+110], radius=12, fill=WHITE, outline=OUTLINE_COLOR, width=1)
    draw_asphalt_texture(screen, (32, y+15, 96, y+79))
    draw.ellipse([78, y+60, 98, y+80], fill=(26, 43, 60), outline=WHITE, width=2)
    draw.text((108, y+14), "Cyberpunk Alley Level", fill=DARK_TEXT, font=font_label)
    draw.text((108, y+35), "Wet asphalt roughness & puddle reflection", fill=MUTED_TEXT, font=get_font(11))
    draw.text((108, y+58), "📷 texture_wet_asphalt_01.jpg", fill=PURPLE, font=get_font(10))
    draw.text((108, y+78), "★★★★★", fill=GOLD, font=get_font(12))
    draw.rounded_rectangle([182, y+76, 235, y+94], radius=4, fill=GREEN_BADGE)
    draw.text((208, y+85), "ACTIVE", fill=GREEN_TEXT, font=get_font(9), anchor="mm")
    draw.text((INNER_W-38, y+42), "🗑", fill=(186, 26, 26), font=font_h2)

    # Item 2 with Texture Thumbnail Photo
    y = 442
    draw.rounded_rectangle([20, y, INNER_W-20, y+110], radius=12, fill=WHITE, outline=OUTLINE_COLOR, width=1)
    draw_moss_texture(screen, (32, y+15, 96, y+79))
    draw.ellipse([78, y+60, 98, y+80], fill=(42, 123, 60), outline=WHITE, width=2)
    draw.text((108, y+14), "Overgrown Ruin Environment", fill=DARK_TEXT, font=font_label)
    draw.text((108, y+35), "Mossy stone brick normal map notes", fill=MUTED_TEXT, font=get_font(11))
    draw.text((108, y+58), "📷 texture_mossy_stone_02.jpg", fill=PURPLE, font=get_font(10))
    draw.text((108, y+78), "★★★★☆", fill=GOLD, font=get_font(12))
    draw.rounded_rectangle([182, y+76, 248, y+94], radius=4, fill=(244, 244, 244))
    draw.text((215, y+85), "ARCHIVED", fill=MUTED_TEXT, font=get_font(9), anchor="mm")
    draw.text((INNER_W-38, y+42), "🗑", fill=(186, 26, 26), font=font_h2)

    # Item 3 with Texture Thumbnail Photo
    y = 566
    draw.rounded_rectangle([20, y, INNER_W-20, y+110], radius=12, fill=WHITE, outline=OUTLINE_COLOR, width=1)
    draw_wood_texture(screen, (32, y+15, 96, y+79))
    draw.ellipse([78, y+60, 98, y+80], fill=(180, 100, 40), outline=WHITE, width=2)
    draw.text((108, y+14), "Medieval Castle Interior", fill=DARK_TEXT, font=font_label)
    draw.text((108, y+35), "Aged oak wood grain & iron hinge specular", fill=MUTED_TEXT, font=get_font(11))
    draw.text((108, y+58), "📷 texture_aged_wood_03.jpg", fill=PURPLE, font=get_font(10))
    draw.text((108, y+78), "★★★★★", fill=GOLD, font=get_font(12))
    draw.rounded_rectangle([182, y+76, 235, y+94], radius=4, fill=GREEN_BADGE)
    draw.text((208, y+85), "ACTIVE", fill=GREEN_TEXT, font=get_font(9), anchor="mm")
    draw.text((INNER_W-38, y+42), "🗑", fill=(186, 26, 26), font=font_h2)

    # FAB (+)
    draw.ellipse([INNER_W-85, INNER_H-95, INNER_W-25, INNER_H-35], fill=PURPLE)
    draw.text((INNER_W-55, INNER_H-65), "+", fill=WHITE, font=get_font(30), anchor="mm")

    draw_nav_bar(draw)
    final_img = apply_phone_shell(screen)
    final_img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\reference_list_screenshot.png")

def create_reference_edit_screen():
    screen = Image.new("RGB", (INNER_W, INNER_H), BG_COLOR)
    draw = ImageDraw.Draw(screen)
    draw_status_bar(draw)

    # Top Bar
    draw.rectangle([0, 45, INNER_W, 105], fill=PURPLE_CONTAINER)
    draw.text((20, 70), "←  Create Material Reference", fill=DARK_TEXT, font=font_h2)

    # Project Selector Field
    y = 130
    draw.text((20, y), "Target Game Project", fill=DARK_TEXT, font=font_label)
    y += 20
    draw.rounded_rectangle([20, y, INNER_W-20, y+44], radius=8, outline=PURPLE, width=2)
    draw.text((34, y+12), "Cyberpunk Alley Level (Unreal Engine 5)  ▼", fill=DARK_TEXT, font=font_input)

    # Real-World Reference Photo Preview Box!
    y += 58
    draw.text((20, y), "Real-Life Captured Texture Photo", fill=DARK_TEXT, font=font_label)
    y += 20
    draw_asphalt_texture(screen, (20, y, 150, y+85))
    draw.rounded_rectangle([20, y, 150, y+85], radius=8, outline=PURPLE, width=2)
    draw.rounded_rectangle([165, y+18, INNER_W-20, y+65], radius=18, fill=PURPLE_CONTAINER)
    draw.text((INNER_W//2 + 75, y+41), "📷  Captured: wet_asphalt_ref.jpg", fill=PURPLE, font=font_label, anchor="mm")

    # Material Note Field
    y += 100
    draw.text((20, y), "Material Reference Note", fill=DARK_TEXT, font=font_label)
    y += 20
    draw.rounded_rectangle([20, y, INNER_W-20, y+80], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((34, y+15), "Wet asphalt roughness & puddle reflection", fill=DARK_TEXT, font=font_input)

    # Color Hex Field
    y += 95
    draw.text((20, y), "Surface Color Hex Code (#RRGGBB)", fill=DARK_TEXT, font=font_label)
    y += 20
    draw.rounded_rectangle([20, y, INNER_W-20, y+44], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((34, y+12), "#1A2B3C", fill=DARK_TEXT, font=font_input)
    draw.ellipse([INNER_W-55, y+8, INNER_W-28, y+35], fill=(26, 43, 60))

    # Rating Stars Picker
    y += 56
    draw.text((20, y), "Texture Importance Rating", fill=DARK_TEXT, font=font_label)
    y += 20
    draw.text((20, y), "★ ★ ★ ★ ★", fill=GOLD, font=get_font(22))

    # Status Picker
    y += 42
    draw.text((20, y), "Reference Status", fill=DARK_TEXT, font=font_label)
    y += 20
    draw.rounded_rectangle([20, y, 95, y+28], radius=14, fill=PURPLE)
    draw.text((57, y+14), "Active", fill=WHITE, font=get_font(11), anchor="mm")

    draw.rounded_rectangle([105, y, 195, y+28], radius=14, outline=OUTLINE_COLOR)
    draw.text((150, y+14), "Archived", fill=DARK_TEXT, font=get_font(11), anchor="mm")

    # Save Button
    y += 56
    draw.rounded_rectangle([20, y, INNER_W-20, y+46], radius=23, fill=PURPLE)
    draw.text((INNER_W//2, y+23), "Create Reference", fill=WHITE, font=font_btn, anchor="mm")

    draw_nav_bar(draw)
    final_img = apply_phone_shell(screen)
    final_img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\reference_edit_screenshot.png")

create_login_screen()
create_register_screen()
create_reference_list_screen()
create_reference_edit_screen()
print("REALISTIC PHONE FRAME SCREENSHOTS GENERATED SUCCESSFULLY!")
