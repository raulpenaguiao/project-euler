#ifndef CL_Primes
#define CL_Primes

#include "CL_Arithmetics.h"
#include <vector>


bool MRTest(long long int n, int r) {
	long long int d = n - 1, e = 0;
	while (d % 2 == 0) {
		d /= 2;
		e += 1;
	}
	long long int a = PowerMod(r, d, n);
	//std::cout << d << ", " << e << ", " << a << ", " << r << ", " << n << std::endl;
	if (a == 1) return true;
	long long int b = ProdMod(a, a, n);
	while (b != 1 && e > 0) {
		a = b;
		b = ProdMod(a, a, n);
		e -= 1;
	}
	//std::cout << e << ", " << a << std::endl;
	return ( e > 0 ) && (a + 1 == n);
}

static std::vector<int> Divisors(int n){
	if (n%2 == 0){
		std::pair<int, int> sD = SuperDivides(n, 2);
		std::vector<int> listD1 = Divisors(sD.first);
		int LIM = listD1.size(), pow2 = 1;
		for(int j = 1; j<=sD.second; j++){
			pow2 *= 2;
			for(int i = 0; i < LIM; i++){
				listD1.push_back(listD1[i]*pow2);
			}
		}
		return listD1;
	}
	for(int p = 3; p * p <= n; p+=2){
		if(n%p == 0){
			std::pair<int, int> sD = SuperDivides(n, p);
			std::vector<int> listD1 = Divisors(sD.first);
			int LIM = listD1.size(), powp = 1;
			for(int j = 1; j<=sD.second; j++){
				powp *= p;
				for(int i = 0; i < LIM; i++){
					listD1.push_back(listD1[i]*powp);
				}
			}
			return listD1;
		}
	}
	std::vector<int> divisors = std::vector<int>();
	divisors.push_back(1);
	if(n == 1) return divisors;
	divisors.push_back(n);
	return divisors;
}

static bool MillerRabin(long long int n) {
	if (n == 0 || n == 1 ) return false;
	if (n < 0 ) return MillerRabin(-n);
	if (n % 2 == 0) return n == 2;
	if (n % 3 == 0) return n == 3;
	if (n % 5 == 0) return n == 5;
	if (n % 7 == 0) return n == 7;
	if (n % 11 == 0) return n == 11;
	if (n % 13 == 0) return n == 13;
	//std::cout << n << " :: test " << 2 << " > ";
	if (!MRTest(n, 2)) return false;
	if (n < 2047) return true;

	//std::cout << n << " :: test " << 3 << " > ";
	if (!MRTest(n, 3)) return false;
	if (n < 13733653) return true;

	//std::cout << n << " :: test " << 5 << " > ";
	if (!MRTest(n, 5)) return false;
	if (n < 25326001) return true;

	//std::cout << n << " :: test " << 7 << " > ";
	if (!MRTest(n, 7)) return false;
	if (n < 3215031751) return true;

	//std::cout << n << " :: test " << 11 << " > ";
	if (!MRTest(n, 11)) return false;
	if (n < 2152302898747) return true;

	//std::cout << n << " :: test " << 13 << " > ";
	if (!MRTest(n, 13)) return false;
	if (n < 3474749660383) return true;

	//std::cout << n << " :: test " << 17 << " > ";
	if (!MRTest(n, 17)) return false;
	if (n < 341550071728321) return true;

	//std::cout << n << " :: test " << 23 << " > ";
	if (!MRTest(n, 19) && !MRTest(n, 23)) return false;
	if (n < 3825123056546413051) return true;

	//std::cout << n << " :: test " << 29 << " to " << 37 << " > ";
	if (!MRTest(n, 29) && !MRTest(n, 31) && !MRTest(n, 37)) return false;
	return true;
}


#endif