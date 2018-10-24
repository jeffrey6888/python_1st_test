import sys

import pygame

from  pygame.sprite import Group

from settings import Settings
from ship import Ship

def run_game():
#initial
	pygame.init()
	ai_settings = Settings()
	# screen = pygame.display.set_mode((1200,800))
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien_Invasion")
	
	#creat one ship
	ship == Ship(ai_settings, screen)
	bullets = Group()
	
	
	#define gray color for backgroud
	bg_color = (230, 230, 230)
	
	"""begin game main circle"""
	while true:
		"""watch keypad and mouse"""
		gf.check.events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)

		
		"""paint screen """
		#screen is part of surface,used to display game item
		#repaint screen for every circle
		gf.update_screen(ai_settings, screen, ship, bullets)
		
run_game()
