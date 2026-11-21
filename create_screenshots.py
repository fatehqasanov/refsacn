import os
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions (Mobile Phone aspect ratio: 540 x 1140)
WIDTH, HEIGHT = 540, 1140
BG_COLOR = (255, 251, 254)       # Material 3 light bg
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

font_title = get_font(32)
font_h2 = get_font(20)
font_subtitle = get_font(15)
font_label = get_font(13)
font_input = get_font(15)
font_btn = get_font(15)

def draw_status_bar(draw):
    draw.text((24, 16), "09:41", fill=DARK_TEXT, font=get_font(14))
    draw.ellipse([470, 18, 482, 30], fill=DARK_TEXT)
    draw.rectangle([490, 18, 516, 30], outline=DARK_TEXT, width=2)
    draw.rectangle([492, 20, 510, 28], fill=DARK_TEXT)

def draw_nav_bar(draw):
    draw.rectangle([210, HEIGHT - 18, 330, HEIGHT - 12], fill=DARK_TEXT)

def create_login_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_status_bar(draw)

    draw.text((WIDTH//2, 260), "RefScan", fill=PURPLE, font=font_title, anchor="mm")
    draw.text((WIDTH//2, 310), "Log in to your account", fill=MUTED_TEXT, font=font_subtitle, anchor="mm")

    y = 400
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=PURPLE, width=2)
    draw.text((56, y-10), " Email ", fill=PURPLE, font=get_font(12))
    draw.text((56, y+18), "fatehqasanov@gmail.com", fill=DARK_TEXT, font=font_input)

    y = 490
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((56, y-10), " Password ", fill=MUTED_TEXT, font=get_font(12))
    draw.text((56, y+18), "••••••••••••", fill=DARK_TEXT, font=font_input)

    y = 590
    draw.rounded_rectangle([40, y, WIDTH-40, y+50], radius=25, fill=PURPLE)
    draw.text((WIDTH//2, y+25), "Log in", fill=WHITE, font=font_btn, anchor="mm")

    y = 660
    draw.text((WIDTH//2, y), "No account? Register", fill=PURPLE, font=font_subtitle, anchor="mm")

    draw_nav_bar(draw)
    img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\login_screenshot.png")

def create_register_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_status_bar(draw)

    draw.text((WIDTH//2, 220), "RefScan", fill=PURPLE, font=font_title, anchor="mm")
    draw.text((WIDTH//2, 270), "Create a new account", fill=MUTED_TEXT, font=font_subtitle, anchor="mm")

    y = 350
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=PURPLE, width=2)
    draw.text((56, y-10), " Email ", fill=PURPLE, font=get_font(12))
    draw.text((56, y+18), "fatehqasanov@gmail.com", fill=DARK_TEXT, font=font_input)

    y = 430
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((56, y-10), " Password ", fill=MUTED_TEXT, font=get_font(12))
    draw.text((56, y+18), "••••••••••••", fill=DARK_TEXT, font=font_input)

    y = 510
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((56, y-10), " Confirm Password ", fill=MUTED_TEXT, font=get_font(12))
    draw.text((56, y+18), "••••••••••••", fill=DARK_TEXT, font=font_input)

    y = 610
    draw.rounded_rectangle([40, y, WIDTH-40, y+50], radius=25, fill=PURPLE)
    draw.text((WIDTH//2, y+25), "Create account", fill=WHITE, font=font_btn, anchor="mm")

    y = 680
    draw.text((WIDTH//2, y), "Already have an account? Log in", fill=PURPLE, font=font_subtitle, anchor="mm")

    draw_nav_bar(draw)
    img.save(r"C:\Users\fateh\AndroidStudioProjects/RefScan/register_screenshot.png")

def create_reference_list_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_status_bar(draw)

    # Top Bar
    draw.rectangle([0, 50, WIDTH, 110], fill=PURPLE_CONTAINER)
    draw.text((20, 70), "RefScan Material References", fill=DARK_TEXT, font=font_h2)
    # Logout Icon
    draw.rectangle([480, 70, 510, 95], outline=PURPLE, width=2)

    # E1: Search Bar
    y = 130
    draw.rounded_rectangle([20, y, WIDTH-20, y+48], radius=24, outline=OUTLINE_COLOR, width=1)
    draw.text((36, y+14), "🔍  Search by note or level...", fill=MUTED_TEXT, font=font_input)

    # E7: Statistics Header Card
    y = 195
    draw.rounded_rectangle([20, y, WIDTH-20, y+70], radius=12, fill=PURPLE_CONTAINER)
    draw.text((36, y+14), "Logged in: fatehqasanov@gmail.com", fill=MUTED_TEXT, font=get_font(12))
    draw.text((36, y+36), "Total References: 3", fill=DARK_TEXT, font=font_label)
    draw.text((WIDTH-36, y+36), "2 active · 1 archived", fill=PURPLE, font=font_label, anchor="ra")

    # E5: Status Filter Chips
    y = 280
    draw.rounded_rectangle([20, y, 100, y+32], radius=16, fill=PURPLE)
    draw.text((60, y+16), "All (3)", fill=WHITE, font=get_font(12), anchor="mm")

    draw.rounded_rectangle([110, y, 200, y+32], radius=16, outline=OUTLINE_COLOR)
    draw.text((155, y+16), "Active (2)", fill=DARK_TEXT, font=get_font(12), anchor="mm")

    draw.rounded_rectangle([210, y, 320, y+32], radius=16, outline=OUTLINE_COLOR)
    draw.text((265, y+16), "Archived (1)", fill=DARK_TEXT, font=get_font(12), anchor="mm")

    # Reference Item 1
    y = 330
    draw.rounded_rectangle([20, y, WIDTH-20, y+110], radius=12, fill=WHITE, outline=OUTLINE_COLOR, width=1)
    draw.ellipse([36, y+20, 76, y+60], fill=(26, 43, 60)) # #1A2B3C
    draw.text((90, y+16), "Cyberpunk Alley Level", fill=DARK_TEXT, font=font_label)
    draw.text((90, y+38), "Wet asphalt roughness & puddle reflection", fill=MUTED_TEXT, font=get_font(12))
    draw.text((90, y+62), "★★★★★", fill=GOLD, font=get_font(14))
    draw.rounded_rectangle([170, y+60, 230, y+80], radius=4, fill=GREEN_BADGE)
    draw.text((200, y+70), "ACTIVE", fill=GREEN_TEXT, font=get_font(10), anchor="mm")
    draw.text((WIDTH-40, y+45), "🗑", fill=(186, 26, 26), font=font_h2)

    # Reference Item 2
    y = 455
    draw.rounded_rectangle([20, y, WIDTH-20, y+110], radius=12, fill=WHITE, outline=OUTLINE_COLOR, width=1)
    draw.ellipse([36, y+20, 76, y+60], fill=(42, 123, 60)) # #2A7B3C
    draw.text((90, y+16), "Overgrown Ruin Environment", fill=DARK_TEXT, font=font_label)
    draw.text((90, y+38), "Mossy stone brick normal map notes", fill=MUTED_TEXT, font=get_font(12))
    draw.text((90, y+62), "★★★★☆", fill=GOLD, font=get_font(14))
    draw.rounded_rectangle([170, y+60, 240, y+80], radius=4, fill=(244, 244, 244))
    draw.text((205, y+70), "ARCHIVED", fill=MUTED_TEXT, font=get_font(10), anchor="mm")
    draw.text((WIDTH-40, y+45), "🗑", fill=(186, 26, 26), font=font_h2)

    # Reference Item 3
    y = 580
    draw.rounded_rectangle([20, y, WIDTH-20, y+110], radius=12, fill=WHITE, outline=OUTLINE_COLOR, width=1)
    draw.ellipse([36, y+20, 76, y+60], fill=(180, 100, 40))
    draw.text((90, y+16), "Medieval Castle Interior", fill=DARK_TEXT, font=font_label)
    draw.text((90, y+38), "Aged oak wood grain & iron hinge specular", fill=MUTED_TEXT, font=get_font(12))
    draw.text((90, y+62), "★★★★★", fill=GOLD, font=get_font(14))
    draw.rounded_rectangle([170, y+60, 230, y+80], radius=4, fill=GREEN_BADGE)
    draw.text((200, y+70), "ACTIVE", fill=GREEN_TEXT, font=get_font(10), anchor="mm")
    draw.text((WIDTH-40, y+45), "🗑", fill=(186, 26, 26), font=font_h2)

    # FAB (+)
    draw.ellipse([WIDTH-90, HEIGHT-100, WIDTH-30, HEIGHT-40], fill=PURPLE)
    draw.text((WIDTH-60, HEIGHT-70), "+", fill=WHITE, font=get_font(32), anchor="mm")

    draw_nav_bar(draw)
    img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\reference_list_screenshot.png")

def create_reference_edit_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_status_bar(draw)

    # Top Bar
    draw.rectangle([0, 50, WIDTH, 110], fill=PURPLE_CONTAINER)
    draw.text((20, 75), "←  Create Material Reference", fill=DARK_TEXT, font=font_h2)

    # Project Selector Field (Reference Collection)
    y = 140
    draw.text((20, y), "Target Game Project", fill=DARK_TEXT, font=font_label)
    y += 24
    draw.rounded_rectangle([20, y, WIDTH-20, y+50], radius=8, outline=PURPLE, width=2)
    draw.text((36, y+15), "Cyberpunk Alley Level (Unreal Engine 5)  ▼", fill=DARK_TEXT, font=font_input)

    # Material Note Field
    y += 70
    draw.text((20, y), "Material Reference Note", fill=DARK_TEXT, font=font_label)
    y += 24
    draw.rounded_rectangle([20, y, WIDTH-20, y+100], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((36, y+18), "Wet asphalt roughness & puddle reflection", fill=DARK_TEXT, font=font_input)

    # Color Hex Field
    y += 120
    draw.text((20, y), "Surface Color Hex Code (#RRGGBB)", fill=DARK_TEXT, font=font_label)
    y += 24
    draw.rounded_rectangle([20, y, WIDTH-20, y+50], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((36, y+15), "#1A2B3C", fill=DARK_TEXT, font=font_input)
    draw.ellipse([WIDTH-60, y+10, WIDTH-30, y+40], fill=(26, 43, 60))

    # Rating Stars Picker
    y += 70
    draw.text((20, y), "Texture Importance Rating", fill=DARK_TEXT, font=font_label)
    y += 24
    draw.text((20, y), "★ ★ ★ ★ ★", fill=GOLD, font=get_font(28))

    # Status Picker
    y += 50
    draw.text((20, y), "Reference Status", fill=DARK_TEXT, font=font_label)
    y += 24
    draw.rounded_rectangle([20, y, 100, y+32], radius=16, fill=PURPLE)
    draw.text((60, y+16), "Active", fill=WHITE, font=get_font(12), anchor="mm")

    draw.rounded_rectangle([110, y, 200, y+32], radius=16, outline=OUTLINE_COLOR)
    draw.text((155, y+16), "Archived", fill=DARK_TEXT, font=get_font(12), anchor="mm")

    # Save Button
    y += 70
    draw.rounded_rectangle([20, y, WIDTH-20, y+50], radius=25, fill=PURPLE)
    draw.text((WIDTH//2, y+25), "Create Reference", fill=WHITE, font=font_btn, anchor="mm")

    draw_nav_bar(draw)
    img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\reference_edit_screenshot.png")

create_login_screen()
create_register_screen()
create_reference_list_screen()
create_reference_edit_screen()
print("All 4 Lab 2 screenshot PNG files generated successfully!")
