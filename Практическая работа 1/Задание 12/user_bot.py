def script(check, x, y):
	if check('gold', x, y):
		return 'take'
	if check('level', x, y) == 1: #Уровень 1
		if check('wall', x + 2, y) == 0:
			return 'right'
		return 'down'
	if check('level', x, y) == 2: #Уровень 2
		if check('gold', x + 1, y) or check('gold', x + 2, y):
			return 'right'
		if check('gold', x - 1, y):
			return 'down'
		if check('gold', x, y - 1):
			return 'up'
		if check('gold', x, y + 1):
			return 'down'
		return 'up'
	if check('level', x, y) == 3 or check('level', x, y) == 4: #Уровень 3, 4
		if check('level', x, y) == 4:
			print (x, y)
			if x == 4 and y == 14 and check('gold', 8, 16):
				return 'right'
			if x == 4 and y == 10:
				return 'right'
		if check('wall', x, y + 1) and check('wall', x - 1, y):
			return 'up'
		if check('wall', x, y - 1) and check('wall', x - 1, y):
			return 'right'
		if check('wall', x, y + 1) and check('wall', x + 1, y):
			return 'left'
		if check('wall', x, y - 1) and check('wall', x + 1, y):
			return 'down'
		if check('wall', x - 1, y):
			return 'up'
		if check('wall', x + 1, y):
			return 'down'
		if check('wall', x, y + 1):
			return 'left'
		if check('wall', x, y - 1):
			return 'right'
		if check('wall', x - 1, y - 1):
			return 'up'
		if check('wall', x + 1, y - 1):
			return 'right'
		if check('wall', x - 1, y + 1):
			return 'left'
		if check('wall', x + 1, y + 1):
			return 'down'
