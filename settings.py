class Settings():
	"""store AI all settings"""
	
	def __init__(self):
		"""initial  game settings"""
		
		#set screen
		self.screen_width = 1200
		self.screen_heigh = 800
		self.bg_color = (230, 230, 230)
		
		#ship speed
		self.ship_speed_factor = 1.5
		
		#bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
