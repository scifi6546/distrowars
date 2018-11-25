#include <string>
#ifndef WINDOW_H
#define WINDOW_H
int init();
int quit(); 
enum SPLIT_TYPE{VERTICAL,HORIZONTAL};
extern int NUM_ROOT;
class Split{
    public:
        Split(Split* parent,int x_top,int x_bottom,int y_top,int y_bottom);
        /*
        Top ----------*
        |             |
        |             |
        |             |
        |             |
        *-----------Bottom

        */
        //percent: int from 0-100;
        Split* splitPane(int percent,SPLIT_TYPE);
        //percent: int from 0-100;
        Split();
        //to only be used by root split
        void fill(char to_fill);
        void update();
    private:
        //number of root objects
        int topX;
        int topY;
        int bottomX;
        int bottomY;

        
};
class Window{
    public:
        Window();
};
#endif