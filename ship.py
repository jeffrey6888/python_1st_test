import pygame

class Ship():
	
	def __init__(self, screen):
		"""init ship and set initial location"""
		self.screen = screen
		self.ai_settings =ai_settings
		
		
		#load ship picture and get its rectange
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#place new  ship at center of screen bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#save decimals in property center of ship
		self.center = float(self.rect.centerx)
		
		#moving flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		#change ship position along to moving flag
		if self.moving_right and self.rect.right <\
			self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor		

		#upadate rect accord to self.center
		self.rect.centerx = self. center

	def blitme(self):
		"""paint ship at the location"""
		self.screen.blit(self.image, self.rect)
