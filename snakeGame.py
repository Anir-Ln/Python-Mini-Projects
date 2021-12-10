import pygame
import time
import random



#variables
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 400
BLOCK_LENGHT = 10
BLOCK_SIZE = BLOCK_LENGHT * BLOCK_LENGHT


#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)


foodX = SCREEN_WIDTH//2
foodY = SCREEN_HEIGHT//2



def newFood():
	# should use global keyword to modify position variables
	global foodX, foodY
	foodX = random.randint(0, SCREEN_WIDTH // BLOCK_LENGHT) * BLOCK_LENGHT
	foodY = random.randint(0, SCREEN_HEIGHT // BLOCK_LENGHT) * BLOCK_LENGHT
	print(f"({foodX}, {foodY})")


class Snake(object):
	"""docstring for Snake"""
	def __init__(self, disp, x, y, length, direction):
		super(Snake, self).__init__()
		self.disp = disp
		self.x = x
		self.y = y
		self.length = length
		self.direction = direction

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

	def draw(self):
		for i in range(self.length):
			pygame.draw.rect(self.disp, black, [self.x[i], self.y[i], BLOCK_LENGHT, BLOCK_LENGHT])
		# draw food
		# print(f"--{foodX}, {foodY}--")
		pygame.draw.rect(self.disp, red, [foodX, foodY, BLOCK_LENGHT, BLOCK_LENGHT])

	def eat(self):
		if foodX == self.x[0] and foodY == self.y[0]:
			self.x.append(0)
			self.y.append(0)
			self.length += 1
			#new food position
			newFood()
			print("Yummy!")


	def checkCollisions(self):
		if self.x[0] > SCREEN_WIDTH or self.x[0] < 0 or self.y[0] > SCREEN_HEIGHT or self.y[0] < 0:
			return True
		return False




if __name__ == '__main__':
 
	pygame.init()
	disp = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.update()
	pygame.display.set_caption("Snake Game")

	clock = pygame.time.Clock()


	running = True

	snake = Snake(disp, [SCREEN_WIDTH//2], [SCREEN_HEIGHT//2], 1, 'R')

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

		disp.fill(white)
		snake.move()
		snake.draw()
		snake.checkCollisions()
		snake.eat()
		pygame.display.update()

		clock.tick(BLOCK_LENGHT)

	

	pygame.quit()
	quit()