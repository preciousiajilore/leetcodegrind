from typing import List

def wordSearch(board: List[List[str]], word:str) -> bool:
    rows = len(board)
    cols = len(board[0])
    
    def dfs(row: int, col:int, index:int) -> bool: 

        if row >= rows or col >= cols or col < 0 or row < 0:
            #out of bounds
            return False
        
        
        if board[row][col] != word[index]:
            #cell doesn't the letter we are looking for
            return False
        
        if index == len(word)-1:
            return True
        
        temp = board[row][col]
        board[row][col] = "#"

        found = (
            #up
            dfs(row-1,col,index + 1) or
            #down
            dfs(row+1,col,index + 1) or
            #left
            dfs(row,col-1,index + 1) or 
            #right
            dfs(row,col+1,index + 1)
        )

        board[row][col] = temp
        return found

    #moving through the board
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if dfs(r, c, 0):
                    return True
                
    return False



def main():
   board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
    ]
   word = "ABCCED"
   print(wordSearch(board,word))

if __name__ == "__main__":
    main()