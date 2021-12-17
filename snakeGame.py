import pygame
import time
import random



#variables
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 400
SCREEN_AREA = SCREEN_WIDTH * SCREEN_HEIGHT # 400 * 600 = 240000
BLOCK_LENGHT = 20
BLOCK_SIZE = BLOCK_LENGHT * BLOCK_LENGHT
TIME_CHANGE = 10
OBSTACLES_NUMBER = random.randint(1, 100);
BLOCKS_NUMBER = (SCREEN_AREA) // BLOCK_SIZE


#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
	

foodX = SCREEN_WIDTH//2
foodY = SCREEN_HEIGHT//2



obstacles = [(random.randint(0, SCREEN_WIDTH // BLOCK_LENGHT - 1) * BLOCK_LENGHT, random.randint(0, SCREEN_HEIGHT // BLOCK_LENGHT - 1) * BLOCK_LENGHT) for _ in range(OBSTACLES_NUMBER)] 


def newFood():
	# should use global keyword to modify position variables
	global foodX, foodY
	foodX = random.randint(0, SCREEN_WIDTH // BLOCK_LENGHT - 1) * BLOCK_LENGHT
	foodY = random.randint(0, SCREEN_HEIGHT // BLOCK_LENGHT - 1) * BLOCK_LENGHT
	print(f"({foodX}, {foodY})")


class Snake(object):
	"""docstring for Snake"""
	x = [0] * BLOCKS_NUMBER
	y = [0] * BLOCKS_NUMBER
	def __init__(self, disp, x0, y0, length, direction, activateBorder):
		super(Snake, self).__init__()
		self.disp = disp
		self.x[0] = x0
		self.y[0] = y0
		self.length = length
		self.direction = direction
		self.activateBorder = activateBorder

	def move(self):
		for i in range(self.length-1, 0, -1):
			self.x[i] = self.x[i-1]
			self.y[i] = self.y[i-1]

		if self.direction == 'U':
			self.y[0] -= BLOCK_LENGHT
		elif self.direction == 'D':
			self.y[0] += BLOCK_LENGHT
		elif self.direction == 'L':
			self.x[0] -= BLOCK_LENGHT
		elif self.direction == 'R':
			self.x[0] += BLOCK_LENGHT

		if self.activateBorder:
			self.x[0] = (self.x[0] + SCREEN_WIDTH) % SCREEN_WIDTH
			self.y[0] = (self.y[0] + SCREEN_HEIGHT) % SCREEN_HEIGHT
		

	def draw(self):
		for i in range(self.length):
			pygame.draw.rect(self.disp, black, [self.x[i], self.y[i], BLOCK_LENGHT, BLOCK_LENGHT])
		
		# draw obstacles
		for ob in obstacles:
			pygame.draw.rect(self.disp, blue, [ob[0], ob[1], BLOCK_LENGHT, BLOCK_LENGHT])

		# draw food
		# print(f"--{foodX}, {foodY}--")
		pygame.draw.rect(self.disp, red, [foodX, foodY, BLOCK_LENGHT, BLOCK_LENGHT])

	def eat(self):
		if foodX == self.x[0] and foodY == self.y[0]:
			# self.x.append(0)
			# self.y.append(0)
			self.length += 1
			#new food position
			newFood()
			print("Yummy!")


	def checkCollisions(self):
		# out of borders
		if not self.activateBorder:
			if self.x[0] >= SCREEN_WIDTH or self.x[0] < 0 or self.y[0] >= SCREEN_HEIGHT or self.y[0] < 0:
				return True

		# obstacles
		for ob in obstacles:
			if ob[0] == self.x[0] and ob[1] == self.y[0]:
				return True

		# head and body collision
		for i in range(1, self.length):
			if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
				return True
		return False




if __name__ == '__main__':
 
	pygame.init()
	disp = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.update()
	pygame.display.set_caption("Snake Game")

	clock = pygame.time.Clock()


	running = True

	snake = Snake(disp, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 1, 'R', True)

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN and snake.direction != 'U':
					snake.direction = 'D'
				elif event.key == pygame.K_UP and snake.direction != 'D':
					snake.direction = 'U'
				elif event.key == pygame.K_RIGHT and snake.direction != 'L':
					snake.direction = 'R'
				elif event.key == pygame.K_LEFT and snake.direction != 'R':
					snake.direction = 'L'
				# hack the game (make the snake longer)
				elif event.key == pygame.K_SPACE:
					foodX = snake.x[0]
					foodY = snake.y[0]
					snake.eat()
				break
				# wihout break the game can be hacked by pressing 2 arrow keys at the same time to switch direction from up <-> down or left <-> right

		disp.fill(white)
		snake.move()
		snake.draw()
		if snake.checkCollisions():
			print(f"Collision at <{snake.x[0], snake.y[0]}>")
			snake.length = 1
		snake.eat()
		pygame.display.update()

		clock.tick(TIME_CHANGE)

	

	pygame.quit()
	quit()