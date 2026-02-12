from collections import deque

def water_jug_bfs(capA, capB, target):
    visited = set()
    queue = deque()

    queue.append((0, 0))
    visited.add((0, 0))

    parent = {}

    while queue:
        a, b = queue.popleft()

        
        if a == target or b == target:
            path = []
            while (a, b) != (0, 0):
                path.append((a, b))
                a, b = parent[(a, b)]
            path.append((0, 0))
            return path[::-1]

        
        moves = [
            (capA, b),  
            (a, capB),  
            (0, b),     
            (a, 0),    
            (min(capA, a + b), max(0, a + b - capA)),  
            (max(0, a + b - capB), min(capB, a + b))   
        ]

        for move in moves:
            if move not in visited:
                visited.add(move)
                parent[move] = (a, b)
                queue.append(move)

    return None



capA = 4
capB = 3
target = 2

solution = water_jug_bfs(capA, capB, target)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found")
