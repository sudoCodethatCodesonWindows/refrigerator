#include <stdio.h>

char board[3][3];

void init() {
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            board[i][j]=' ';
}

void print() {
    for(int i=0;i<3;i++) {
        printf(" %c | %c | %c\n", board[i][0], board[i][1], board[i][2]);
        if(i<2) printf("---+---+---\n");
    }
}

int win(char p) {
    for(int i=0;i<3;i++)
        if((board[i][0]==p && board[i][1]==p && board[i][2]==p) ||
           (board[0][i]==p && board[1][i]==p && board[2][i]==p))
           return 1;

    return (board[0][0]==p && board[1][1]==p && board[2][2]==p) ||
           (board[0][2]==p && board[1][1]==p && board[2][0]==p);
}

int draw() {
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            if(board[i][j]==' ') return 0;
    return 1;
}

int main() {
    init();
    char p='X';
    int r,c;

    while(1) {
        print();
        printf("\nPlayer %c (row col, -1 quit): ", p);
        if(scanf("%d",&r)!=1) break;
        if(r==-1) break;
        scanf("%d",&c);
        if(r<1||r>3||c<1||c>3) continue;
        r--;c--;
        if(board[r][c]!=' ') continue;
        board[r][c]=p;
        if(win(p)){ print(); printf("\nPlayer %c wins!\n",p); break; }
        if(draw()){ print(); printf("\nDraw!\n"); break; }
        p = (p=='X')?'O':'X';
    }
    return 0;
}
