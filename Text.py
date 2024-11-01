import pygame

# Initialize pygame
pygame.init()

# Create the font object
font = pygame.font.SysFont("Lucida Console", 14)


def write_text(text, sur, start_point, end_point):
    # Split the text into words
    words = text.split()
    x = start_point[0]
    y = start_point[1]

    # Get the width of a space
    space_width = font.render(" ", True, (255, 255, 255)).get_width()

    # Loop through each word and render it
    for word in words:
        # Render the word into a surface
        word_surface = font.render(word, True, (74, 74, 74))
        word_width = word_surface.get_width()

        # Check if the word fits in the current line, else move to the next line
        if x + word_width >= end_point[0]:
            x = start_point[0]  # Reset x to the start of the new line
            y += word_surface.get_height() + space_width  # Move y down by the height of the text + space width

        # Blit the word onto the surface at the current position
        sur.blit(word_surface, (x, y))

        # Move x to the right by the word width + space width
        x += word_width + space_width
