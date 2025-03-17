sol = [[1,2,3],[4,5,6],[7,8,0]]
moves = [   [['r', 'd'],        ['r', 'd', 'l'],        ['d', 'l']],
            [['u', 'd', 'r'],   ['r', 'd', 'u', 'l'],   ['u', 'd', 'l']],
            [['r', 'u'],        ['r', 'u', 'l'],        ['u', 'l']]]

import heapq

class Board:
    def __init__(self, nums=[[1,2,3],[4,5,6],[7,8,0]]):
        self.nums = nums
    
    def solution(self):
        return self.nums==sol
    
    def printBoard(puzzle):
        for i in range(3):
            for j in range(3):
                print(puzzle[i][j], end=' ')
            print()
        print()

    def empty(self):
        for ir, r in enumerate(self.nums):
            for ic, c in enumerate(r):
                if c==0:
                    return ir, ic
    
    def available_moves(self):
        r, c = self.empty()
        return moves[r][c]
    
    def make_move(self, dir):
        r, c= self.empty()
        if dir == 'l':
            self.nums[r][c], self.nums[r][c-1] = self.nums[r][c-1], self.nums[r][c]
        elif dir == 'r':
            self.nums[r][c], self.nums[r][c+1] = self.nums[r][c+1], self.nums[r][c]
        elif dir == 'u':
            self.nums[r][c], self.nums[r-1][c] = self.nums[r-1][c], self.nums[r][c]
        elif dir == 'd':
            self.nums[r][c], self.nums[r+1][c] = self.nums[r+1][c], self.nums[r][c]

class Node:
    def __init__(self, board, movement, cost, heuristic, parent):
        self.board = board
        self.movement = movement
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent
    
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def heuristic(board):
    h = 0
    for i in range(3):
        for j in range(3):
            if board.nums[i][j] != sol[i][j]:
                goal_r, goal_c = [(r, c) for r in range(3) for c in range(3) if sol[r][c] == board.nums[i][j]][0]
                h += abs(i - goal_r) + abs(j - goal_c)
    return h

def solve_puzzle(board):
    visited = set()
    queue = []
    heapq.heappush(queue, Node(board, "", 0, heuristic(board), None))
    
    while queue:
        current = heapq.heappop(queue)
        if current.board.solution():
            path = []
            while current:
                path.append(current)
                current = current.parent
            path.reverse()
            for node in path:
                if node.movement:
                    print(f"Cero hacia : {node.movement}")
                Board.printBoard(node.board.nums)
            print(f"Movimientos: {len(path) - 1}")
            return
        
        visited.add(str(current.board.nums))
        for move in current.board.available_moves():
            new_board = Board([row[:] for row in current.board.nums])
            new_board.make_move(move)
            if str(new_board.nums) not in visited:
                heapq.heappush(queue, Node(new_board, move, current.cost + 1, heuristic(new_board), current))

initial_board = Board([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
print("Puzzle Inicial")
Board.printBoard(initial_board.nums)
print("Solucion")
Board.printBoard(sol)
print("----------")
solve_puzzle(initial_board)
