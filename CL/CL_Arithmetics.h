#ifndef CL_Arithmetics
#define CL_Arithmetics

#include<utility>



static long long int ProdMod(long long int a, long long int b, long long int p){
	if (a < 0) return (p-ProdMod((-a)%p, b, p))%p;
	if (a == 0) return 0;
	if (a == 1) return b%p;
	long long int ans = ProdMod(a >> 1, b, p);
	ans = ans<<1;
	if (a%2 == 1) ans += b;
	return ans%p;
}

static long long int PowerMod(long long int a, long long int d, long long int p) {
	if (d == 0) return 1;
	if (d == 1) return a % p;
	long long int ans = PowerMod(ProdMod(a, a, p), d / 2, p);
	if (d % 2 == 1) ans = ProdMod(ans, a, p);
	return ans;
}


static std::pair<int, int> SuperDivides(int n, int p){
	int s = n, e = 0;
	while(s%p == 0){
		s /= p;
		e += 1;
	}
	std::pair<int, int> pair1;
	pair1.first = s;
	pair1.second = e;
	return pair1;
}


static long long int __GCD(long long int a, long long int b){
	//std::cout << a << " gcd " << b << std::endl;
	if ( a == 0 ) return b;
	return __GCD(b%a, a); 
}

static long long int GCD(long long int a, long long int b){
	//std::cout << a << " gcd " << b << std::endl;
	if ( a < 0 ) return GCD(-a, b);
	if ( a > b ) return GCD(b, a);
	return __GCD(a, b); 
}


#endif