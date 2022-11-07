import pygame

window = pygame.display.set_mode( (800,800) )
clock = pygame.time.Clock()
cube_points = [n for n in range(8)]

projecrion_matrix = [[1,0,0],
                     [0,1,0],
                     [0,0,1]]

cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]
cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[0] = [[1], [1], [-1]]
cube_points[0] = [[-1], [1], [-1]]


# Main loop
while True:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  pygame.display.update()
