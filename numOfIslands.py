from typing import List

def numIslands(grid: List[List[str]]) -> int:
    islandCount = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col):
       if row >= rows or row < 0 or col >= cols or col < 0:
          return False
       
       if grid[row][col] == "0":
          return 
       
       #mark it as visited
       grid[row][col] = "0"

       dfs(row -1, col) #up
       dfs(row +1, col) #down
       dfs(row, col +1) #right
       dfs(row, col-1) #left


    for r in range(rows):
       for c in range(cols):
          if grid[r][c] == "1":
             islandCount += 1
             dfs(r,c)

    return islandCount
def main():
 grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
    ]
 print(numIslands(grid))

if __name__ == "__main__":
   main()