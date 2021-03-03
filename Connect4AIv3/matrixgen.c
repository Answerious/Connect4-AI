#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    int random[5][5];
    int i, o;
    srand(time(NULL));
    for(o = 0; o<3; o++)
        for(i = 0; i<3; i++)
            random[o][i] = rand();
    return rand()/25612864;
};
int main2(){
    int random1[7][7];
    int j, k;
    srand(time(NULL));
    for(k = 0; k<3; k++)
        for(j = 0; j<3; j++)
            random1[k][j] = rand();
    return random1[k][j]/25612864;
};
int main3(){
    int random2[3][3];
    int q, w;
    srand(time(NULL));
    for(w = 0; w<3; w++)
        for(q = 0; q<3; q++)
            random2[w][q] = rand();
    return random2[w][q]/25612864;
}