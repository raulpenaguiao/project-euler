#include <iostream>
#include <vector>
#include <string>
#include "CL_Rational.h"

#define FOR(a, b) for(int a = 0; a < b; a++)


long long int binom[100][100];

std::vector<std::pair<int, Rational>> probs(std::vector<std::vector<std::vector<std::vector<std::vector<std::vector<long long int>>>>>> counts){
	std::vector<std::pair<int, Rational>> ans;
	std::pair<int, Rational> pr(0, Rational());
	FOR(i, 60) ans.push_back(pr);
	FOR(a, 13) FOR(b, 13) FOR(c, 13) FOR(d, 13) FOR(e, 13) for(int i = 1; i <= 4 ; i++){
		int cards = 4*a+3*b+2*c+d;
		if(cards < 53){
			ans[cards].first += counts[a][b][c][d][e][i];
		}
	}
	std::cout << "first" << std::endl;
	int LIM = 5;
	FOR(a, LIM) FOR(b, LIM) FOR(c, LIM) FOR(d, LIM) FOR(e, LIM) for(int i = 1; i <= 4 ; i++){
		int cards = 4*a+3*b+2*c+d;
		if(cards < 53){
			ans[cards].second = Rational::plus(ans[cards].second, Rational::times(Rational(counts[a][b][c][d][e][i]), Rational(4-i, 52-cards)));
		}
	}
	std::cout << "scnd" << std::endl;
	pr.second = Rational(1, 1);
	pr.first = 1;
	ans[0] = pr;
	return ans;
}

long long int t(int a, int b, int c, int d, int e){
	long long int ans = 1;
	FOR(k, a) ans *= binom[4*(a-k) + 3 * b + 2 * c + d][4];
	FOR(k, b) ans *= binom[3 * (b - k) + 2 * c + d][3];
	FOR(k, c) ans *= binom[2 * (c - k) + d][2];
	FOR(k, a + b + c + d) ans *= 13 - k;
	return ans;
}

long long int f(int a, int b, int c, int d, int e, int i){
	if (i == 1) return (e+1) * t(a, b, c, d-1, e+1);
	if (i == 2) return (d+1) * t(a, b, c-1, d+1, e);
	if (i == 3) return (c+1) * t(a, b-1, c+1, d, e);
	if (i == 4) return (b+1) * t(a-1, b+1, c, d, e);
	return 0;
}



int main() {
	binom[0][0] = 1;
	for(int i = 1; i <95; i++) for(int j = 0; j <= i; j++) {
		binom[i][j] = binom[i-1][j] + binom[i-1][j-1];
	}
	std::vector<long long int> vec0;
	FOR(i, 5) vec0.push_back(0);
	std::vector<std::vector<long long int>> vec1;
	FOR(i, 15) vec1.push_back(vec0);
	std::vector<std::vector<std::vector<long long int>>> vec2;
	FOR(i, 15) vec2.push_back(vec1);
	std::vector<std::vector<std::vector<std::vector<long long int>>>> vec3;
	FOR(i, 15) vec3.push_back(vec2);
	std::vector<std::vector<std::vector<std::vector<std::vector<long long int>>>>> vec4;
	FOR(i, 15) vec4.push_back(vec3);
	std::vector<std::vector<std::vector<std::vector<std::vector<std::vector<long long int>>>>>> vec5;
	FOR(i, 15) vec5.push_back(vec4);
	vec5[0][0][0][1][12][1] = 1;

	FOR(a, 14) FOR(b, 14) FOR(c, 14) FOR(d, 14) {
		int e = 13 - a - b - c - d;
		if(e >= 0){
			if(d > 0) vec5[a][b][c][d][e][1] += e*(vec5[a][b][c][d-1][e+1][1] + (e+1)*vec5[a][b][c][d-1][e+1][2] + (e+1)*vec5[a][b][c][d-1][e+1][3] + (e+1)*vec5[a][b][c][d-1][e+1][4]);
			if(c > 0) vec5[a][b][c][d][e][2] = (d+1)*(vec5[a][b][c-1][d+1][e][1] + d*vec5[a][b][c-1][d+1][e][2] + (d+1)*vec5[a][b][c-1][d+1][e][3] + (d+1)*vec5[a][b][c-1][d+1][e][4]);
			if(b > 0) vec5[a][b][c][d][e][3] = (c+1)*(vec5[a][b-1][c+1][d][e][1] + (c+1)*vec5[a][b-1][c+1][d][e][2] + c*vec5[a][b-1][c+1][d][e][3] + (c+1)*vec5[a][b-1][c+1][d][e][4]);
			if(a > 0) vec5[a][b][c][d][e][4] = (b+1)*(vec5[a-1][b+1][c][d][e][1] + (b+1)*vec5[a-1][b+1][c][d][e][2] + (b+1)*vec5[a-1][b+1][c][d][e][3] + b*vec5[a-1][b+1][c][d][e][4]);
		}
	}
	long long int max = 0;
	FOR(a, 14) FOR(b, 14) FOR(c, 14) FOR(d, 14) FOR(e, 14) for(int i = 1; i<= 4 ; i++){
		if (vec5[a][b][c][d][e][i] > max) max = vec5[a][b][c][d][e][i];
		if (vec5[a][b][c][d][e][i] < 0) std::cout << vec5[a][b][c][d][e][i] << std:: endl;
	}
	std::cout << max << std:: endl;


	
	FOR(a, 6) FOR(b, 6) FOR(c, 6) FOR(d, 6) FOR(e, 6) for(int i = 1; i<= 4 ; i++) if (vec5[a][b][c][d][e][i] != f(a, b, c, d, e, i)) {
		 std::cout << a << " - " << b << " - " << c << " - " << d << " - " << e << " - " << i << " - " << vec5[a][b][c][d][e][i] << " - " << f(a, b, c, d, e, i) << std:: endl;
	}
	std::cout << max << std:: endl;

	std::vector<std::pair<int, Rational>>parsed_cards = probs(vec5);

	double ans = 0;
	FOR(i, 52){
		std::cout << "Phase " << i << std::endl;
		ans += (double)parsed_cards[i].second * i / parsed_cards[i].first;
		std::cout << ans << " - "  <<  (double)parsed_cards[i].second << std::endl;
		std::cout << " - " << parsed_cards[i].second.Numerator() << " - " << parsed_cards[i].second.Denominator()   << std::endl;
		std::cout << " - " << parsed_cards[i].first << std::endl;
	}
	std::cout << ans << std::endl;
	return 0;
}