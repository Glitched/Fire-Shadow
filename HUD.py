def draw_hud(screen, font, height, money, health, score, frame, debug_mode):
	# Money
	text = font.render("Gold: " + str(money), True, (255, 255, 255))
	textrect = text.get_rect()
	textrect.top = 10
	textrect.left = 10
	screen.blit(text, textrect)

	# Health
	healthdisplay = font.render("Health: " + str(round(health)), True, (255, 255, 255))
	heathrect = text.get_rect()
	heathrect.top = height - 30
	heathrect.left = 10
	screen.blit(healthdisplay, heathrect)

	# Score
	score_display = font.render("Score: " + str(score), True, (255,255,255))
	score_rect = score_display.get_rect()
	score_rect.top = 10
	score_rect.left = 1200
	screen.blit(score_display, score_rect)

	# Frame
	if debug_mode:
		frame_display = font.render("Frame: " + str(frame), True, (255,255,255))
		frame_rect = score_display.get_rect()
		frame_rect.top = height - 30
		frame_rect.left = 1200
		screen.blit(frame_display, frame_rect)
