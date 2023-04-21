#include <stdio.h>
#include <stdlib.h>

int main(){
    int ano;
    int check = 0; //false

    scanf("%d", &ano);

    if(ano % 4 == 0 && ano % 100 != 0) check = 1;
    else if(ano % 400 == 0) check = 1;
    else check = 0;

    if(check == 1) printf("%d e bissexto\n", ano);
    else printf("%d nao e bissexto\n", ano);
    return 0;
}