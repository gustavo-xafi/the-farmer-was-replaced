# Mapeamento manual já que não temos .items()
# Direção: (dx, dy, oposta)
DIRECTIONS = {
	North: (0, 1, South),
	South: (0, -1, North),
	East:  (1, 0, West),
	West:  (-1, 0, East)
}

visited = set()

def maze_hunter():
	# 1. Pegar posição atual e marcar como visitada
	x, y = get_pos_x(), get_pos_y()
	visited.add((x, y))
	
	# 2. Verificar se chegamos ao objetivo
	# Nota: measure() geralmente retorna o alvo, compare com sua pos atual
	alvo = measure()
	if (x, y) == alvo:
		if get_entity_type() == Entities.Treasure:
			harvest()
		# Se for um desafio de "labirintos infinitos", limpamos o set aqui
		if get_entity_type() == Entities.Bush:
			visited.clear() 
			create_maze()
		return True

	# 3. Tentar cada direção
	# Em Python, iterar num dicionário retorna as CHAVES (North, South, etc)
	for direction in DIRECTIONS:
		stats = DIRECTIONS[direction]
		dx = stats[0]
		dy = stats[1]
		opposite = stats[2]
		
		next_x, next_y = x + dx, y + dy
		
		# Só tenta se estiver dentro do grid positivo e não visitado
		if next_x >= 0 and next_y >= 0 and (next_x, next_y) not in visited:
			if move(direction):
				if maze_hunter(): # Recursão
					return True
				
				# --- BACKTRACKING FÍSICO ---
				# Se a recursão voltou False, movemos o drone de volta
				move(opposite)
			else:
				# Se bateu na parede, marca como visitado para não tentar mais
				visited.add((next_x, next_y))
				
	return False