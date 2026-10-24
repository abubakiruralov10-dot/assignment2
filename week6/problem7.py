def treasure_positions(grid):
    positions = []
    # Qatorlar bo'yicha indeks bilan yurish
    for r in range(len(grid)):
        # Ustunlar bo'yicha indeks bilan yurish
        for c in range(len(grid[r])):
            # Agar katakchada 1 bo'lsa
            if grid[r][c] == 1:
                # Koordinatani tuple ko'rinishida qo'shamiz[cite: 1]
                positions.append((r, c))
    return positions

grid = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 0]
]

positions = treasure_positions(grid)
print(f"Positions: {positions}")
print(f"Treasures: {len(positions)}")

# Tuple unpacking yordamida xazinalarni 0 ga o'zgartiramiz[cite: 1]
for r, c in positions:
    grid[r][c] = 0

print(f"Updated map: {grid}")