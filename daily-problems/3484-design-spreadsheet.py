# everything given in question, not that special
class Spreadsheet:
    def __init__(self, rows: int):
        self.matrix = [[0]*26 for _ in range(rows)]

    def getCell(self, cell: str):
        if len(cell) == 1 or cell[0].isalpha() == False:
            return (-1, -1)
        
        c = ord(cell[0]) - ord('A')
        r = int(cell[1:]) - 1
        return (r, c)

    def setCell(self, cell: str, value: int) -> None:
        r, c = self.getCell(cell)
        self.matrix[r][c] = value 
        

    def resetCell(self, cell: str) -> None:
        r, c = self.getCell(cell)
        self.matrix[r][c] = 0
        
    def getValue(self, formula: str) -> int:
        first, second = formula[1:].split('+')
        s = 0
        r1, c1 = self.getCell(first)
        r2, c2 = self.getCell(second)

        if r1 == -1:
            s += int(first)
        else:
            s += self.matrix[r1][c1]

        if r2 == -1:
            s += int(second)
        else: 
            s += self.matrix[r2][c2]
        return s



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)