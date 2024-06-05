#include <iostream>
#include <ctime>

#define FOR(a, b, c) for(int a = b; a < c; a++)

int main(){
    clock_t time_req = clock();
    int N, ans;
    std::cin >> N;

    std::cout << ans << std::endl;
    std::cout << ((double)(clock() - time_req))/1000 << "seconds" << std::endl;
    return 0;
}