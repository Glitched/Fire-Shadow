import constants


def draw(screen, instance, player):
	draw_tower_items(screen)
	draw_player_upgrades(screen, player)


def new_list_item(value, screen, left, y):
	text = constants.FONT_ITEM.render(value, True, (255, 188, 144))
	rect = text.get_rect()
	rect.left = left
	rect.top = y
	screen.blit(text, rect)
	return 10 + rect.bottom


def draw_tower_items(screen):
	tower_header = constants.FONT_HEADER.render("Build:", True, (255, 188, 144))
	tower_rect = tower_header.get_rect()
	tower_rect.top = 100
	tower_rect.left = 100
	screen.blit(tower_header, tower_rect)
	y = 150
	items = [
		"[T] Trap: $" + str(constants.PRICE["trap"]),
		"[G] Campfire: $" + str(constants.PRICE["campfire"]),
		"[F] Freeze: $" + str(constants.PRICE["freeze"]),
		"[R] Turret: $" + str(constants.PRICE["turret"]),
	]
	for item in items:
		y = new_list_item(item, screen, 120, y)


def draw_player_upgrades(screen, player):
	tower_header = constants.FONT_HEADER.render("Upgrades:", True, (255, 188, 144))
	tower_rect = tower_header.get_rect()
	tower_rect.top = 310
	tower_rect.left = 100
	screen.blit(tower_header, tower_rect)
	y = 360
	speed_multiplier = str(round(1 + (0.2 / (player.speed_upgrades + 1)), 2))
	items = [
		"[D] Damage x 1.5: $" + str(constants.PRICE["attack"]),
		"[C] Speed x" + speed_multiplier + ": $" + str(constants.PRICE["speed"]),
		"[X] Intelligence: $" + str(constants.PRICE["intelligence"]),
	]
	for item in items:
		y = new_list_item(item, screen, 120, y)

