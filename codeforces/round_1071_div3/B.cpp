#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define MAXN 2*10'000 + 5
int arr[MAXN];
int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int t,n;
	cin >> t;
	rep (l , 0, t) {
		cin >> n;
		rep (k ,0 ,n) 
			cin >> arr[k];
		// Is minimized if
		// only meaningfull choice is deleting 0 or n-1.
		int value = min ( { arr[0] - arr[n-1] , arr[1] - arr[n-1] , arr[0] - arr[n-2]});
		cout << value << '\n';
	}
}