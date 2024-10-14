import time
import json
import pygame

# Load JSON data from the file
with open('fam_colors.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)

# Convert hex color (e.g., '#RRGGBB') to RGB tuple
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("JSON")

font = pygame.font.SysFont("Arial", 24)

text_color = (255, 255, 255)  # White color

running = True
# extra_squares = False
while running:
    # Fill the background with black
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     extra_squares = True
  
    
    # Iterate through the rows in the JSON data
    for row in fcc_data:
        screen.fill((0, 0, 0))

        name = row["name"]
        image = row['image']
        base_color_name = row["base_color_name"]
        base_color = hex_to_rgb(row["base_color"])  # Convert hex to RGB
        accent_color_name = row["accent_color_name"]
        accent_color = hex_to_rgb(row["accent_color"])  # Convert hex to RGB
        secondary_color_name = row["secondary_color_name"]
        secondary_color = hex_to_rgb(row["secondary_color"])  # Convert hex to RGB

        #text title: Color Scheme
        text = "Color Scheme: " + name		
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(400 // 2, 30))
        screen.blit(text_surface, text_rect)

        #image set up
        imp = pygame.image.load(image['image_url']).convert()
        imp = pygame.transform.scale(imp, (100, 100))
        screen.blit(imp, (200, 50))

        # Draw squares with the colors from JSON
        pygame.draw.rect(screen, accent_color, pygame.Rect(50, 50, 100, 100))  # A square with accent color
        pygame.draw.rect(screen, secondary_color, pygame.Rect(200, 50, 100, 100), 5)  # A square outline with secondary color
        pygame.draw.rect(screen, base_color, pygame.Rect(125, 200, 150, 150))  # A square with base color
        
        #first color label
        text = accent_color_name		
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center = (100, 170))
        screen.blit(text_surface, text_rect)

        #second color label
        text = secondary_color_name		
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center = (250, 170))
        screen.blit(text_surface, text_rect)

        #third color label
        text = base_color_name		
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center = (200, 370))
        screen.blit(text_surface, text_rect)

        # if extra_squares:
        # 	#draw sqaures
        # 	print("Test")

        pygame.display.flip()
        time.sleep(5)
    running = False


# Quit Pygame
pygame.quit()
