import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace images
html_content = html_content.replace('images/ekta-chibi-hero.png', 'images/avatar_hello.png')
html_content = html_content.replace('images/ekta-brickwall.jpg', 'images/avatar_about.png')

# Update hardcoded SVG gradient colors
# #3B5BDB -> #E61C8C (Vibrant Pink/Magenta)
# #D46BDD -> #FF1A75 (Hot Pink)
# #C060D8 -> #D946EF (Fuchsia)
html_content = html_content.replace('#3B5BDB', '#E61C8C')
html_content = html_content.replace('#D46BDD', '#FF1A75')
html_content = html_content.replace('#C060D8', '#D946EF')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated index.html successfully.")

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace CSS variables
css_content = css_content.replace('--blue:         #3B5BDB;', '--blue:         #E61C8C;')
css_content = css_content.replace('--blue-mid:     #5C4EC9;', '--blue-mid:     #A855F7;')
css_content = css_content.replace('--lavender:     #C060D8;', '--lavender:     #D946EF;')
css_content = css_content.replace('--pink:         #D46BDD;', '--pink:         #FF1A75;')
css_content = css_content.replace('--teal:         #2E9E8A;', '--teal:         #059669;')
css_content = css_content.replace('--mint:         #5CC8C8;', '--mint:         #22C55E;')
css_content = css_content.replace('--bg-light:     #F4F2FF;', '--bg-light:     #FFF5F9;')
css_content = css_content.replace('--bg-section:   #EDE9FF;', '--bg-section:   #FCE7F3;')
css_content = css_content.replace('--bg-dark:      #0F0B1F;', '--bg-dark:      #160824;')
css_content = css_content.replace('--bg-dark2:     #1A1440;', '--bg-dark2:     #240E3B;')
css_content = css_content.replace('--text-dark:    #1A1440;', '--text-dark:    #240E3B;')
css_content = css_content.replace('--text-mid:     #3D2F6B;', '--text-mid:     #581C87;')
css_content = css_content.replace('--text-muted:   #7B6BA8;', '--text-muted:   #8B5CF6;')

# Replace RGBA colors
# Royal blue rgb(59,91,219) -> pink rgb(230,28,140)
# Lavender rgb(212,107,221) -> pink rgb(255,26,117)
# Note: check for variants with spaces
css_content = css_content.replace('59,91,219', '230,28,140')
css_content = css_content.replace('59, 91, 219', '230, 28, 140')
css_content = css_content.replace('212,107,221', '255,26,117')
css_content = css_content.replace('212, 107, 221', '255, 26, 117')

# Remove clip-path from .chibi-img-about
css_content = css_content.replace('clip-path: inset(5% 0);', '/* clip-path removed */')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated style.css successfully.")
