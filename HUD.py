import constants


def draw_hud(screen, font, player, score, frame, seconds, debug_mode):
	# Money
	text = font.render("Gold: " + str(player.gold), True, (255, 255, 255))
	textrect = text.get_rect()
	textrect.top = 10
	textrect.left = 10
	screen.blit(text, textrect)

	# Health
	healthdisplay = font.render("Health: " + str(round(player.health)), True, (255, 255, 255))
	heathrect = text.get_rect()
	heathrect.top = constants.DISPLAY_HEIGHT - 30
	heathrect.left = 10
	screen.blit(healthdisplay, heathrect)

	# Score
	score_display = font.render("Score: " + str(score), True, (255, 255, 255))
	score_rect = score_display.get_rect()
	score_rect.top = 10
	score_rect.left = 1200
	screen.blit(score_display, score_rect)

	# Frame
	if debug_mode:
		frame_display = font.render("Frame: " + str(seconds) + "." + str(frame), True, (255, 255, 255))
		frame_rect = score_display.get_rect()
		frame_rect.top = constants.DISPLAY_HEIGHT - 30
		frame_rect.left = 1175
		screen.blit(frame_display, frame_rect)


def draw_wave_number(screen, font, height, width, wave_num):
	text = font.render("Wave: " + str(wave_num), True, (255,255,255))
	rect = text.get_rect()
	rect.top = 10
	rect.left = width/2
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