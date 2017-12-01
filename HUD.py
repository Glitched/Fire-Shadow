def draw_hud(screen, font, height, money, health):
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
