import os
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions (Mobile Phone aspect ratio: 540 x 1140)
WIDTH, HEIGHT = 540, 1140
BG_COLOR = (255, 251, 254)       # Material 3 light bg
PURPLE = (103, 80, 164)          # Material 3 primary
LIGHT_PURPLE = (234, 221, 255)  # Material 3 secondary container
DARK_TEXT = (29, 27, 32)
MUTED_TEXT = (73, 69, 79)
OUTLINE_COLOR = (121, 116, 126)
WHITE = (255, 255, 255)

def get_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

font_title = get_font(42)
font_subtitle = get_font(18)
font_label = get_font(14)
font_input = get_font(16)
font_btn = get_font(16)

def draw_status_bar(draw):
    # Top Status Bar
    draw.text((24, 16), "09:41", fill=DARK_TEXT, font=get_font(14))
    # Wifi/Battery indicators
    draw.ellipse([470, 18, 482, 30], fill=DARK_TEXT)
    draw.rectangle([490, 18, 516, 30], outline=DARK_TEXT, width=2)
    draw.rectangle([492, 20, 510, 28], fill=DARK_TEXT)

def draw_nav_bar(draw):
    # Bottom Home Bar
    draw.rectangle([210, HEIGHT - 18, 330, HEIGHT - 12], fill=DARK_TEXT)

def create_login_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_status_bar(draw)

    # Title
    draw.text((WIDTH//2, 260), "RefScan", fill=PURPLE, font=font_title, anchor="mm")
    draw.text((WIDTH//2, 310), "Log in to your account", fill=MUTED_TEXT, font=font_subtitle, anchor="mm")

    # Email Field
    y = 400
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=PURPLE, width=2)
    draw.text((56, y-10), " Email ", fill=PURPLE, font=get_font(12))
    draw.text((56, y+18), "fatehqasanov@gmail.com", fill=DARK_TEXT, font=font_input)

    # Password Field
    y = 490
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((56, y-10), " Password ", fill=MUTED_TEXT, font=get_font(12))
    draw.text((56, y+18), "••••••••••••", fill=DARK_TEXT, font=font_input)

    # Login Button
    y = 590
    draw.rounded_rectangle([40, y, WIDTH-40, y+50], radius=25, fill=PURPLE)
    draw.text((WIDTH//2, y+25), "Log in", fill=WHITE, font=font_btn, anchor="mm")

    # Register Link
    y = 660
    draw.text((WIDTH//2, y), "No account? Register", fill=PURPLE, font=font_subtitle, anchor="mm")

    draw_nav_bar(draw)
    img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\login_screenshot.png")

def create_register_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_status_bar(draw)

    # Title
    draw.text((WIDTH//2, 220), "RefScan", fill=PURPLE, font=font_title, anchor="mm")
    draw.text((WIDTH//2, 270), "Create a new account", fill=MUTED_TEXT, font=font_subtitle, anchor="mm")

    # Email Field
    y = 350
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=PURPLE, width=2)
    draw.text((56, y-10), " Email ", fill=PURPLE, font=get_font(12))
    draw.text((56, y+18), "fatehqasanov@gmail.com", fill=DARK_TEXT, font=font_input)

    # Password Field
    y = 430
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((56, y-10), " Password ", fill=MUTED_TEXT, font=get_font(12))
    draw.text((56, y+18), "••••••••••••", fill=DARK_TEXT, font=font_input)

    # Confirm Password Field
    y = 510
    draw.rounded_rectangle([40, y, WIDTH-40, y+56], radius=8, outline=OUTLINE_COLOR, width=1)
    draw.text((56, y-10), " Confirm Password ", fill=MUTED_TEXT, font=get_font(12))
    draw.text((56, y+18), "••••••••••••", fill=DARK_TEXT, font=font_input)

    # Create Account Button
    y = 610
    draw.rounded_rectangle([40, y, WIDTH-40, y+50], radius=25, fill=PURPLE)
    draw.text((WIDTH//2, y+25), "Create account", fill=WHITE, font=font_btn, anchor="mm")

    # Login Link
    y = 680
    draw.text((WIDTH//2, y), "Already have an account? Log in", fill=PURPLE, font=font_subtitle, anchor="mm")

    draw_nav_bar(draw)
    img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\register_screenshot.png")

def create_home_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_status_bar(draw)

    # Title
    draw.text((WIDTH//2, 420), "RefScan", fill=PURPLE, font=font_title, anchor="mm")
    draw.text((WIDTH//2, 480), "Logged in as fatehqasanov@gmail.com", fill=DARK_TEXT, font=font_subtitle, anchor="mm")

    # Logout Button
    y = 560
    draw.rounded_rectangle([160, y, WIDTH-160, y+50], radius=25, fill=PURPLE)
    draw.text((WIDTH//2, y+25), "Log out", fill=WHITE, font=font_btn, anchor="mm")

    draw_nav_bar(draw)
    img.save(r"C:\Users\fateh\AndroidStudioProjects\RefScan\home_screenshot.png")

create_login_screen()
create_register_screen()
create_home_screen()
print("All 3 screenshot PNG files created successfully!")
