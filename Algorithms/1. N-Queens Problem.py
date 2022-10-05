#-------------------------------------------------------------------------------------------------
# N-Queens Problem
# ----------------
# Finished Solve Date : 06/04/2022
# Description :
# -------------
# You have a chess board [8*8] and you should put one Queen in all Rows and all Coulmns but you can't
# put 2 or more in the same coulmn or in the same row or in the same diagonal
#
# Soultion 1
# ----------
# class Solution:
#     def solveNQueens(self, n):
#         res = set()		# تخزين إحداثيات موضع الملكة في كل صف
#         # العودية
#         def find_pos(row_index, queen, n):
#             for j in range(n):
#                 if pos_available(queen, (row_index, j)):
#                     queen[row_index] = j
#                     if row_index == n-1:    # بالفعل السطر الأخير ووجد مكانا لوضعه
#                         res.add(tuple(queen))
#                         return
#                     else:   # لا إلى السطر الأخير
#                         find_pos(row_index+1, queen, n)
# 		# تحقق مما إذا كان الموقع الحالي متاحًا
#         def pos_available(queen, pos):
#             # ضع الخط i-th للحكم وفقًا لخط 0 ~ i-1
#             for i in range(pos[0]):
#                 if queen[i] == pos[1]:  # العمود نفسه
#                     return False
#                 elif abs(i-pos[0]) == abs(queen[i]-pos[1]): # قطري ابتدائي وثانوي
#                     return False
#             return True
# 		# اطبع النموذج الإحداثي كنموذج Q ...
#         def plot_queen(queen, n):
#             out = []
#             for i in range(n):
#                 s = '.' * queen[i] + 'Q' * 1 + '.' * (n-queen[i]-1)
#
#                 out.append(s)
#             return out
#         # موقع الملكة الأولي -1 ليس له أي تأثير في الواقع
#         queen = [-1 for _ in range(n)]  # الوضعية الأولية
#         # العودية تبدأ من السطر 0
#         find_pos(0, queen, n)
#         out = []
#         for t in res:
#           out.append(plot_queen(t, n))
#         return out
#
# # كود الاختبار
#test = Solution()
#print(test.solveNQueens(4))
#-------------------------------------------------------------------------------------------------
#
# Soultion 2
# ----------
# # Python3 program to solve N Queen
# # Problem using backtracking
# global N
# N = 4
#
#
# def printSolution(board):
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j], end=" ")
#         print()
#
#
# # A utility function to check if a queen can
# # be placed on board[row][col]. Note that this
# # function is called when "col" queens are
# # already placed in columns from 0 to col -1.
# # So we need to check only left side for
# # attacking queens
# def isSafe(board, row, col):
#     # Check this row on left side
#     for i in range(col):
#         if board[row][i] == 1:
#             return False
#
#     # Check upper diagonal on left side
#     for i, j in zip(range(row, -1, -1),
#                     range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False
#
#     # Check lower diagonal on left side
#     for i, j in zip(range(row, N, 1),
#                     range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False
#
#     return True
#
#
# def solveNQUtil(board, col):
#     # base case: If all queens are placed
#     # then return true
#     if col >= N:
#         return True
#
#     # Consider this column and try placing
#     # this queen in all rows one by one
#     for i in range(N):
#
#         if isSafe(board, i, col):
#
#             # Place this queen in board[i][col]
#             board[i][col] = 1
#
#             # recur to place rest of the queens
#             if solveNQUtil(board, col + 1) == True:
#                 return True
#
#             # If placing queen in board[i][col
#             # doesn't lead to a solution, then
#             # queen from board[i][col]
#             board[i][col] = 0
#
#     # if the queen can not be placed in any row in
#     # this column col then return false
#     return False
#
#
# # This function solves the N Queen problem using
# # Backtracking. It mainly uses solveNQUtil() to
# # solve the problem. It returns false if queens
# # cannot be placed, otherwise return true and
# # placement of queens in the form of 1s.
# # note that there may be more than one
# # solutions, this function prints one of the
# # feasible solutions.
# def solveNQ():
#     board = [[0, 0, 0, 0],
#              [0, 0, 0, 0],
#              [0, 0, 0, 0],
#              [0, 0, 0, 0]]
#
#     if solveNQUtil(board, 0) == False:
#         print("Solution does not exist")
#         return False
#
#     printSolution(board)
#     return True
#
#
# # Driver Code
# solveNQ()
#
# # This code is contributed by Divyanshu Mehta
#-------------------------------------------------------------------------------------------------
