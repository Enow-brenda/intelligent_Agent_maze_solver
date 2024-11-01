import pygame

from Text import *
from agent import *
from agentBFS import *
import random

def draw_background():
    screen.fill((blue))
    screen.blit(statistics_box, ((WIDTH - 240, 0)))
    screen.blit(txtSurf, (120, 10), )
    screen.blit(Points, (WIDTH-200, 50), )
    screen.blit(GRASS, (0, 40))
    screen.blit(HOUSE, (WIDTH - 220, HEIGHT-130))
    # screen.blit(bg,(0,60))

    pygame.draw.rect(screen, button_color, button_rect)

    # Render button text

    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

pygame.init()
WIDTH = 1200
HEIGHT= 600

last_execution_time = pygame.time.get_ticks()  # Get the initial time
function_running = False

start = (0,40)
end = (WIDTH-240,HEIGHT)


GRASS = pygame.image.load("images/grass.jfif")
GRASS = pygame.transform.scale(GRASS, (WIDTH-240,HEIGHT-40))

HOUSE = pygame.image.load("images/house.png")
HOUSE = pygame.transform.scale(HOUSE,(200,120))

target =  pygame.image.load("images/home.png")
target = pygame.transform.scale(target,(35,35))

stone =  pygame.image.load("images/stone1.png")
stone = pygame.transform.scale(stone,(35,35))

tree =  pygame.image.load("images/tree.png")
tree = pygame.transform.scale(tree,(35,35))

obstacles = [stone,tree]

jimmy =  pygame.image.load("images/bot.png")
jimmy= pygame.transform.scale(jimmy,(40,40))

bot =  pygame.image.load("images/bot2.png")
bot= pygame.transform.scale(bot,(40,40))

agent = Agent(jimmy, 0, 40)
agentbfs = AgentBFS(bot, 0, 40)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Jimmy Goes Home")
clock = pygame.time.Clock()

#defining the grid:0 for free,1 for obstacles and 2 for target

cell_size = 40
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 182, 193)
blue = (0, 128, 200)

#grid that wil show how the things will be distributed
grid = [[3, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,1, 1, 1, 1, 0,1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0,1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1,1],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0,0],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0,0],
    [0, 0, 1, 0, 1, 1, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,1],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0,1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1,1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0,1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0,0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1,0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0,1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,0]
]


font = pygame.font.SysFont("Poppins",36)
story_font= pygame.font.SysFont("Poppins",23)
heading_font=pygame.font.SysFont("Poppins",55)
txtSurf = font.render("Watch as Jimmy tries to find his way home ",True ,white)
Points = font.render(f"Points :  {agent.point}",True ,white)
story = "One sunny afternoon, Jimmy wandered too far into the woods and got lost. Now he has to use the Depth-First Search (DFS) technique he learned in school by marking his starting point and exploring different paths, leaving pebbles to remember where he has been"
button_text = font.render("Find Home",True ,white)



statistics_box=pygame.Surface((WIDTH-260,HEIGHT))
statistics_box.fill((pink))

button_color = blue
button_rect = pygame.Rect(WIDTH-200, HEIGHT/4, 150, 50)
story_rect = pygame.Rect(WIDTH-230,HEIGHT-200, 200,200)


draw_background()
target_pos = []
running = True
agent.draw(screen)
agentbfs.bfs(grid)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    draw_background()

    # Draw vertical grid lines
    for x in range(0, WIDTH-200, cell_size):
      pygame.draw.line(screen, black, (x, 40), (x, HEIGHT))

    # Draw horizontal grid lines
    for y in range(40, HEIGHT, cell_size):
      pygame.draw.line(screen, black, ( 0,y), (WIDTH-240, y))

    #i is the x axis while j is the y axis
    for i in range (0,24):
        for j in range(0,14):
            x = i * cell_size
            y = j * cell_size
            if grid[j][i]==2:
                screen.blit(target,(x,y+35))
                target_pos = [j, i]
            if grid[j][i]==0:
                if i%2 == 0:
                    screen.blit(stone,(x,y+35))
                else:
                    screen.blit(tree, (x, y + 35))


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    print(mouse_pos)
                    if button_rect.collidepoint(mouse_pos):
                        function_running =  True



    agent.draw(screen)
    agentbfs.draw(screen)

    write_text(story, screen, (WIDTH-230, 225), (WIDTH-10, HEIGHT-150))
    # Get the current time
    current_time = pygame.time.get_ticks()

    # If the function is supposed to run, check the time interval
    if function_running and current_time - last_execution_time >= 1000 and not agent.foundTarget and not agent.noPath:
        agent.move(grid)  # Call the function
        agentbfs.move()
        Points = font.render(f"Points :  {agent.point}", True, white)
        last_execution_time = current_time


    if(agent.foundTarget):
        text = f"Yay ! Jimmy found his way home .Number of steps : {agent.steps} ."
        write_text(text, screen, (WIDTH - 230, 90), (WIDTH - 10,130))
    if(agent.noPath):
        text = "Nooooo ! Jimmy Says he can't find a path"
        write_text(text, screen, (WIDTH - 230, 90), (WIDTH - 10,130))

    # Update the display
    pygame.display.flip()


pygame.quit()
