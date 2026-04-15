class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            fila = set()
            columna = set()
            for j in range(9):

                # checamos si el num es unico en fila
                if board[i][j] in fila:
                    print(f"Encontre {i}{j} en fila, {board[i][j]}")
                    return False
                if board[i][j]!='.':
                    fila.add(board[i][j])
                
                # checamos si el num es unico en columna
                if board[j][i] in columna:
                    print(f"Encontre {j}{i} en columna")
                    return False
                if board[j][i]!='.':
                    columna.add(board[j][i])         
                
        for block in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    num = board[i+3*(block%3)][j+3*(block//3)]
                    if num in seen:
                        print(f"Encontre {i}{j} en bloque, {board[i][j]}")
                        return False
                    if num!='.':
                        seen.add(num)
                    
        return True