#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int t,n;
	cin >> t;
	rep(k , 0 , t) {
		cin >> n;
		vector<int>	arr;
		rep (i, 0, n+1) {
			arr.push_back(  (1 << (n-i)) - 1);
			// 000
			// 111
			// 101
			// Condition implies: j can be represented using i bits
			for (int j = 2; j < ((1 << i) - 1); j+=2 ) {
				// set the lowest n-i bits, then set all possible permutations of the top i most bits (excluding 1 repeating)
				arr.push_back( (1<< n-i) - 1 | (j << n-i));
			}
		}
		for (int a : arr) {
			cout << a << ' ';
		}
		cout << '\n';
	}
}