#include <string>
#ifndef ERROR_H
#define ERROR_H
int init();
int quit(); 
void printError(char* error){
    printf("%s\n",error);
}
#endif