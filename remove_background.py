import os
from PIL import Image

def process_image(img_path, output_path, padding=20, thresh=30):
    if not os.path.exists(img_path):
        print(f"Error: {img_path} does not exist.")
        return False
        
    img = Image.open(img_path).convert("RGB")
    width, height = img.size
    
    # 1. Identify background color (average of 4 corners)
    corners = [img.getpixel((0,0)), img.getpixel((width-1, 0)), 
               img.getpixel((0, height-1)), img.getpixel((width-1, height-1))]
    bg_r = sum(c[0] for c in corners) // 4
    bg_g = sum(c[1] for c in corners) // 4
    bg_b = sum(c[2] for c in corners) // 4
    bg_color = (bg_r, bg_g, bg_b)
    print(f"Processing {img_path}")
    print(f"Detected background color: {bg_color}")
    
    # 2. Find bounding box of non-background content
    left = width
    right = 0
    top = height
    bottom = 0
    
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            dist = ((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)**0.5
            if dist > thresh:
                if x < left: left = x
                if x > right: right = x
                if y < top: top = y
                if y > bottom: bottom = y
                
    print(f"Found content bounding box: left={left}, top={top}, right={right}, bottom={bottom}")
    
    # Crop with padding
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(width, right + padding)
    bottom = min(height, bottom + padding)
    
    cropped = img.crop((left, top, right, bottom))
    c_width, c_height = cropped.size
    print(f"Cropped size: {c_width}x{c_height}")
    
    # 3. Flood fill background starting from all borders of the cropped image
    rgba_img = cropped.convert("RGBA")
    visited = set()
    queue = []
    
    # Initialize queue with all border pixels
    for x in range(c_width):
        queue.append((x, 0))
        queue.append((x, c_height - 1))
    for y in range(1, c_height - 1):
        queue.append((0, y))
        queue.append((c_width - 1, y))
        
    border_bg = []
    for x, y in queue:
        r, g, b, a = rgba_img.getpixel((x, y))
        dist = ((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)**0.5
        if dist <= thresh + 15:
            border_bg.append((x, y))
            visited.add((x, y))
            
    # BFS to find all connected background pixels
    bg_pixels = set(border_bg)
    queue = border_bg
    
    while queue:
        cx, cy = queue.pop(0)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < c_width and 0 <= ny < c_height:
                if (nx, ny) not in visited:
                    r, g, b, a = rgba_img.getpixel((nx, ny))
                    dist = ((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)**0.5
                    if dist <= thresh + 20: # flood fill threshold
                        visited.add((nx, ny))
                        bg_pixels.add((nx, ny))
                        queue.append((nx, ny))
                        
    # 4. Save with transparent background
    data = rgba_img.getdata()
    new_data = []
    for idx, item in enumerate(data):
        x = idx % c_width
        y = idx // c_width
        if (x, y) in bg_pixels:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)
            
    rgba_img.putdata(new_data)
    rgba_img.save(output_path)
    print(f"Saved processed image to {output_path}\n")
    return True

if __name__ == "__main__":
    # Correct paths from the brain directory
    img1_path = "C:/Users/ektaa/.gemini/antigravity-ide/brain/266913ca-2849-48fb-a8f0-558ef05b105a/media__1781079842790.jpg"
    img2_path = "C:/Users/ektaa/.gemini/antigravity-ide/brain/266913ca-2849-48fb-a8f0-558ef05b105a/media__1781079877962.jpg"
    
    process_image(img1_path, "images/avatar_hello.png")
    process_image(img2_path, "images/avatar_about.png")
