#include <iostream>
using namespace std;

char board[3][3];

void initBoard() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            board[i][j] = ' ';
}

void printBoard() {
    cout << "\n";
    for (int i = 0; i < 3; i++) {
        cout << " ";
        for (int j = 0; j < 3; j++) {
            cout << board[i][j];
            if (j < 2) cout << " | ";
        }
        cout << "\n";
        if (i < 2) cout << "---+---+---\n";
    }
}

bool checkWin(char p) {
    for (int i = 0; i < 3; i++)
        if ((board[i][0]==p && board[i][1]==p && board[i][2]==p) ||
            (board[0][i]==p && board[1][i]==p && board[2][i]==p))
            return true;

    return (board[0][0]==p && board[1][1]==p && board[2][2]==p) ||
           (board[0][2]==p && board[1][1]==p && board[2][0]==p);
}

bool isDraw() {
    for (auto &row : board)
        for (char c : row)
            if (c == ' ') return false;
    return true;
}

int main() {
    initBoard();
    char player = 'X';

    while (true) {
        printBoard();
        cout << "\nPlayer " << player << " (row col) or -1 to quit: ";

        int r;
        if (!(cin >> r)) {
            cin.clear();
            cin.ignore(1000, '\n');
            cout << "Invalid input.\n";
            continue;
        }
        if (r == -1) break;

        int c;
        cin >> c;

        if (r < 1 || r > 3 || c < 1 || c > 3) {
            cout << "Out of range!\n";
            continue;
        }

        r--; c--;

        if (board[r][c] != ' ') {
            cout << "Cell already taken!\n";
            continue;
        }

        board[r][c] = player;

        if (checkWin(player)) {
            printBoard();
            cout << "\nPlayer " << player << " wins!\n";
            break;
        }

        if (isDraw()) {
            printBoard();
            cout << "\nIt's a draw!\n";
            break;
        }

        player = (player == 'X') ? 'O' : 'X';
    }
    return 0;
}
