import constants
import tower


def draw(screen, instance, player):
	if instance.current_tower is None:
		draw_tower_items(screen)
	else:
		draw_tower_upgrades(screen, instance)
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


def draw_tower_upgrades(screen, instance):
	tower_header = constants.FONT_HEADER.render("Current Tower Upgrades:", True, (255, 188, 144))
	tower_rect = tower_header.get_rect()
	tower_rect.top = 100
	tower_rect.left = 100
	screen.blit(tower_header, tower_rect)
	y = 150

	upgrade_1 = ""
	upgrade_2 = ""
	if isinstance(instance.current_tower, tower.Trap1):
		upgrade_1 = "[V] $" + str(constants.PRICE["trap2"])
		upgrade_2 = "Upgrading will half the cooldown time"
	elif isinstance(instance.current_tower, tower.Freeze1):
		upgrade_1 = "[V] $" + str(constants.PRICE["freeze2"])
		upgrade_2 = "Upgrading will increase range"
	elif isinstance(instance.current_tower, tower.Freeze2):
		upgrade_1 = "[V] $" + str(constants.PRICE["freeze3"])
		upgrade_2 = "Upgrading will increase range"
	elif isinstance(instance.current_tower, tower.Turret1):
		upgrade_1 = "[V] $" + str(constants.PRICE["turret2"])
		upgrade_2 = "Upgrading will increase rate of fire and range"
	elif isinstance(instance.current_tower, tower.Turret2):
		upgrade_1 = "[V] $" + str(constants.PRICE["turret3"])
		upgrade_2 = "Upgrading will increase rate of fire and range"
	else:
		upgrade_1 = "No upgrades available"

	items = [instance.current_tower.name, upgrade_1, upgrade_2]
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
		"[D] Damage x1.5: $" + str(constants.PRICE["attack"]),
		"[C] Speed x" + speed_multiplier + ": $" + str(constants.PRICE["speed"]),
		"[X] Intelligence: $" + str(constants.PRICE["intelligence"]),
	]
	for item in items:
		y = new_list_item(item, screen, 120, y)

