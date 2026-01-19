#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
bool is_valid_run(const vi a, const vi b, int si, int sj, int n)
{
	rep(i, 0, n)
	{
		if (not(a[(si + i) % n] < b[(sj + i) % n]))
			return false;
	}
	return true;
}
int main()
{
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int t, n;
	cin >> t;
	rep(l, 0, t)
	{
		cin >> n;
		vi a(n), b(n), c(n);
		ll valid_tuples = 0;
		rep(i, 0, n) cin >> a[i];
		rep(i, 0, n) cin >> b[i];
		rep(i, 0, n) cin >> c[i];
		ll ijp = 0, jkp = 0;
		rep(i, 0, n)
			ijp += is_valid_run(a, b, i, 0, n) ? 1 : 0;
		rep(k, 0, n)
			jkp += is_valid_run(b, c, 0, k, n) ? 1 : 0;
		valid_tuples = ijp * jkp* n;
		cout << valid_tuples << '\n';

		// (2 , 2) \equiv (1, 1)
	}
}