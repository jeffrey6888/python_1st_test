# -*- coding: GBK -*-

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""create a bullet speed manager class"""
	
	def __init__(self, ai_settings, screen, ship):
		"""create a bullet object at ship position"""
		super(Bullet, self).__init__()
		self.screen = screen
		
		#at(0,0) create a bullet rectange and correct position 
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet.height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#store bullet position indicated by decimal
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""move up bullet"""
		# update decimal of bullet
		self.y -= self.speed_factor
		# update rect position of bullet
		self.rect.y = self.y
		
	def draw_bullet(self):
		""" draw bullet on screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
		
		
		
		
	
	 
