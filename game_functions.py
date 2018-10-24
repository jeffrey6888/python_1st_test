import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""response to key pressed down"""
	if event.key == pygame.K_RIGHT:
		#move ship right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		#create a bullet and add it into bullets group
		fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
	"""fire a bullet when not exceed limited"""
	#create a new bullet adn add it into bullets group		
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)

def check_keyup_event(event, ship):
	"""response to key release"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = Flase
	if event.key == pygame.K_LEFT:
		ship.moving_left = Flase	

def check_events(ai_settings, screen, ship, bullets):
	""" response to key and mouse events"""
	for event.type == pygame.QUIT():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship,
			 bullets)
			
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)	


			
def update_screen(ai_settings, screen, ship, bullets):
	"""change paint on screen to new paint"""
	#repaint at every circle
	screen.fill(ai_settings.bg_color)
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	
	#let new paint show on screen
	pygame.dispay.flip()

def update_bullets(bullets)
	"""update bullet location, and delete dispeared bullets"""
	#update bullet location
	bullets.update()
	
	#delete dispeared bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullet.remove(bullet)
	print(len(bullets))
