#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
# define MAXN 2*10'000 + 5
int arr[MAXN];
int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int t, n;
	cin>>t;
	rep (l , 0 , t) {
		cin >> n;
		rep (i , 0 , n) {
			cin >> arr[i];
		}
		
	}
}