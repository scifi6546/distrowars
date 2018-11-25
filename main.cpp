#include <iostream>
#include "window.h"
#include <unistd.h>
int main(){
    init();
    usleep(1000000);
    quit();
    return 0;
}