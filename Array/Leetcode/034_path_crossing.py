# Problem: Path Crossing (LeetCode 1496)
# Idea: Track visited coordinates to detect revisit
# Pattern: "Track visited states" → use set/hashmap
# Moves: 'N', 'S', 'E', 'W' → update (x, y)
# Edge Cases: 
#   - immediate revisit at start
#   - long loops
#   - empty path
# Time: O(n)
# Space: O(n)
# 🔁 Optimization Hint: 
#   - For bounded grid → 2D array possible
#   - For diagonals → extend directions dict
# 🔁 Interview Tips: 
#   - Think step by step: position → check → add → repeat
#   - Ask: Can I reduce repeated work? Can I reduce space?


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # visited = {(0,0)}
        # x, y = 0,0 

        # for i in path:
        #     if i == 'N':
        #         y += 1
        #     elif i == 'S':
        #         y -= 1
        #     elif i == 'E':
        #         x += 1
        #     else:
        #         x -= 1

        #     if (x,y) in visited:
        #         return True
        #     visited.add((x,y))
        # return False 

        direction = {
            'N' : (0,1),
            'S' : (0,-1),
            'E' :(1,0),
            'W' : (-1,0)
        }

        visited = {(0,0)}
        x,y =0,0

        for c in path:
            dx, dy = direction[c]
            x += dx
            y += dy
            if (x,y) in visited:
                return True
            visited.add((x,y))
        return False