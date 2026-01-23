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
	int t;
	cin >> t;
	rep(l , 0 , t) {
		int k,x;
		cin >> k >> x;
		int sol = k*x + 1;
		cout  << k*x + 1 << '\n';
	}
	// Why?
	// let x be 3, k 1
	// aaab
	// We can repeat the same letter x times. Repeat k times. we fail when we add one more.
}