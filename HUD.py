def draw_hud(screen, font, height, money, health, score):
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

	#Score
	score_display = font.render("Score: " + str(score), True, (255,255,255))
	score_rect = score_display.get_rect()
	score_rect.top = 10
	score_rect.left = 1200
	screen.blit(score_display,score_rect)
