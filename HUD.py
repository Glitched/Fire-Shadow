import constants
import images as i

def draw_hud(screen, font, player, instance):
	# Money
	text = font.render("Gold: " + str(player.gold), True, (255, 226, 96))
	textrect = text.get_rect()
	textrect.top = 10
	textrect.left = 10
	screen.blit(text, textrect)

	# Health
	if player.getHealth() < 0:
		player.setHealth(0)

	#Process hearts
	heart_image = health_logic(player.getHealth()) #IS AN IMAGE

	heathrect = heart_image.get_rect()
	heathrect.top = constants.DISPLAY_HEIGHT - 30
	heathrect.left = 10
	screen.blit(heart_image, heathrect)

	# Score
	score_display = font.render("Score: " + str(instance.score), True, (255, 255, 255))
	score_rect = score_display.get_rect()
	score_rect.top = 10
	score_rect.left = 1200
	screen.blit(score_display, score_rect)

	# Frame
	if instance.debug_mode:
		frame_display = font.render("Frame: " + str(instance.seconds) + "." + str(instance.frame), True, (255, 255, 255))
		frame_rect = score_display.get_rect()
		frame_rect.top = constants.DISPLAY_HEIGHT - 30
		frame_rect.left = 1175
		screen.blit(frame_display, frame_rect)


def draw_wave_number(screen, font, wave_num):
	text = font.render("Wave: " + str(wave_num), True, (255,255,255))
	rect = text.get_rect()
	rect.top = 10
	rect.left = constants.DISPLAY_WIDTH/2
	screen.blit(text, rect)


def draw_incoming_wave(screen, font, wave_num):
	text = font.render("Wave " + str(wave_num) + " over. Prepare for wave " + str(wave_num + 1) + ".", True, (255, 0, 0))
	rect = text.get_rect()
	rect.top = 45
	rect.left = constants.DISPLAY_WIDTH/2 - 90
	screen.blit(text, rect)


def draw_build_hud(screen, font, tower):
	score_display = font.render("Current Tower: ", True, (255, 255, 255))
	score_rect = score_display.get_rect()
	score_rect.top = 510
	score_rect.left = 600
	screen.blit(score_display, score_rect)

def health_logic(h):
	"""
	This function will decide which heart image to process depending on the health (h) that is passed in. 
	Returns an IMAGE.

	"""
	if h >= 95:
		return i.one_hundred
	elif h < 95 and h >= 90:
		return i.ninety_five
	elif h < 90 and h >= 85:
		return i.ninety
	elif h < 85 and h >= 80:
		return i.eighty_five
	elif h < 80 and h >= 75:
		return i.eighty
	elif h < 75 and h >= 70:
		return i.seventy_five
	elif h < 70 and h >= 65:
		return i.seventy 
	elif h < 65 and h >= 60:
		return i.sixty_five
	elif h < 60 and h >= 55:
		return i.sixty 
	elif h < 55 and h >= 50:
		return i.fifty_five
	elif h < 50 and h >= 45:
		return i.fifty 
	elif h < 45 and h >= 40:
		return i.fourty_five
	elif h < 40 and h >= 35:
		return i.fourty 
	elif h < 35 and h >= 30:
		return i.thirty_five
	elif h < 30 and h >= 25:
		return i.thirty 
	elif h < 25 and h >= 20:
		return i.twenty_five
	elif h < 20 and h >= 15:
		return i.twenty
	elif h < 15 and h >= 10:
		return i.fifteen
	elif h < 10 and h >= 5:
		return i.ten
	elif h < 5 and h > 0:
		return i.five 
	else:
		return i.zero 
