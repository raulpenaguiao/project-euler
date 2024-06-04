#include <iostream>
#include <vector>
#include <string>
#include <fstream>

#define FOR(a, b, c) for(int a = b; a < c; a++)

int main(){
    double f[252][252];
    std::ofstream myfile;
    myfile.open ("cenas.csv");
    int k[252][252];
    int bigLIM = 252;
    FOR(i, 0, bigLIM) FOR(j, 0, bigLIM) f[i][j] = 0;
    FOR(i, 0, bigLIM) FOR(j, 0, bigLIM) k[i][j] = 0;
    int LIM = 250;
    FOR(j, 1, bigLIM) {
        f[1][j] = 1; 
        k[1][j] = 1;
    }
    FOR(s, 3, 2*LIM) FOR(i, 2, LIM) if(i < LIM && s - i < LIM && s - i > 0){
        int j = s - i;
        double max = 1.0/(double)i + (double)((1 - f[j][i-1])*(i-1))/(double)i;
        //std::cout << "______ i = " << i << ", j = " << j  << ", a = " << 1  << "::: newguess > " << max << std::endl;
        int t = 1;
        FOR(a, 2, i/2+1){
            double newguess = ((1 - (double)f[j][a])*(double)a + (1 - (double)f[j][i-a])*((double)i-(double)a))/(double)i;
            //std::cout << "______ i = " << i << ", j = " << j  << ", a = " << a  << "::: newguess > " << newguess  << std::endl;
            if(newguess > max){
                max = newguess; 
                t = a;
            }
        } 
        f[i][j] = max;
        k[i][j] = t;
        //std::cout << " i = " << i << ", j = " << j  << "::: > " << f[i][j] << " / " << t << std::endl;
    }
    /*std::cout << f[3][1] << std::endl;
    FOR(i, 1, LIM){
        std::cout << f[i][1];
        FOR(j, 2, LIM) std::cout << ", " << f[i][j];
        std::cout << std::endl;
    }*/

    
    FOR(i, 1, LIM){
        myfile << k[i][1];
        FOR(j, 2, LIM) myfile << ", " << k[i][j];
        myfile << std::endl;
    }
    std::cout << f[7][5] << std::endl;
    myfile.close();
    return 0;
}