# Membuat papan catur kosong 4x4
board = [[0 for _ in range(4)] for _ in range(4)]

# Tampilkan papan catur
def print_board(board):
    for row in board:
        for x in row:
            if x == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
print_board(board)

# Fungsi untuk memeriksa apakah posisi aman
def is_safe(board, row, col):
    # Periksa kolom
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Periksa diagonal kiri atas
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Periksa diagonal kanan atas
    for i, j in zip(range(row, -1, -1), range(col, 4)):
        if board[i][j] == 1:
            return False
    return True

# Solusi masalah 4 queen
def solve_n_queens(board, row):
    if row == 4:
        return True
    for col in range(4):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0
    return False

# Proses input posisi ratu
for i in range(4):
    while True:
        print(f"Masukkan posisi untuk ratu ke-{i+1}:")
        row = int(input(f"Baris (0-3): "))
        col = int(input(f"Kolom (0-3): "))
        
        # Memastikan input berada dalam rentang yang valid
        if 0 <= row < 4 and 0 <= col < 4 and board[row][col] == 0:
            board[row][col] = 1  # Tempatkan ratu meskipun tidak aman
            print(f"Papan setelah ratu ke-{i+1} ditempatkan:")
            print_board(board)
            break
        else:
            print("Input tidak valid atau posisi sudah ditempati, coba lagi.")


# Solusi yang benar (sebagai referensi)
solution_1 = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]

solution_2 = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

# Memeriksa validitas akhir papan
valid = True

# Membandingkan papan dengan solusi yang benar
if board == solution_1 or board == solution_2:
    valid = True
else:
    valid = False

if valid:
    print("Selamat! Anda berhasil menempatkan semua ratu dengan benar.")
else:
    print("Maaf, Anda kalah. Solusi yang benar adalah:")

    # Temukan solusi 
    solution_board_1 = [[0 for _ in range(4)] for _ in range(4)]
    solve_n_queens(solution_board_1, 0)
    print("Solusi 1:")
    print_board(solution_1)

    solution_board_2 = [[0 for _ in range(4)] for _ in range(4)]
    solve_n_queens(solution_board_2, 0)
    print("Solusi 2:")
    print_board(solution_2)
