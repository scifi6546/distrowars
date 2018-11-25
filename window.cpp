#include "window.h"
#include "error.h"
#include <iostream>
#include <ncurses.h>
int NUM_ROOT=0;
int Rows;
int Cols;
int init(){
    initscr();
    noecho();
    clear();
    refresh();
    getmaxyx(stdscr,Rows,Cols);
    Split root;
    root.fill('*');
    return 0;
}
int quit(){
    endwin();
    std::cout<<"Cols: "<<Cols<<" Rows: "<<Rows<<"\n";
    return 0;
}
Split::Split(){
    if(NUM_ROOT!=0){
        char* error = (char*) malloc(sizeof(char)*1000);
        error =(char*) sprintf(error,"ERROR ON %S ON LINE %i NUM ROOT NOT ZERO",__FILE__,__LINE__);
        printError("NUM_ROOT NOT ZERO");
    }else{
        NUM_ROOT++;
        this->topX=0;
        this->topY=0;
        this->bottomX=Cols;
        this->bottomY=Rows;
    }
}
void Split::fill(char to_fill){
    for(int i =topX;i<=bottomX;i++){
        for(int j=topY;j<=bottomY;j++){
            mvaddch(j,i,to_fill);
        }
    }
    refresh();
}

Split* Split::splitPane(int percent,SPLIT_TYPE){

}