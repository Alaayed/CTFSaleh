#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define MAXN 2 * 10'000 + 5
typedef struct edge
{
    int u, v, w;
} edge_t;
istream &operator>>(istream &in, edge_t &e)
{
    return in >> e.u >> e.v >> e.w;
}

edge_t allEdges[MAXN];
edge_t curEdges[MAXN];
unsigned char visited[(MAXN >> 3) + 1];
int N, M, T;
void mark_node(int);
bool is_connected(int);
void mark_node(int node)
{
    visited[node >> 3] |= (1 << (node & 7));
}
bool is_connected(int edgesNum)
{
    // Mark all visited nodes
    memset(visited, 0, sizeof(visited));
    rep(i, 0, edgesNum)
    {
        mark_node(curEdges[i].u);
        mark_node(curEdges[i].v);
    }
    // Check if all nodes are visited
    rep(i, 0, N >> 3)
    {
        if (visited[i] != 0xFF)
        {
            return false;
        }
    }
    unsigned lastByte = visited[N >> 3];
    bool lastByteFull = lastByte == 0xFF ? true : __builtin_popcount(lastByte + 1) == 1;
    return lastByteFull;
}
int greedy_mst()
{
    int bestWeight = 1 << 30;
    bestWeight--;
    rep (i , 0 , 30) 
    {
        // Turn off the the top ith bit
        int topbit = 1 << (29-i);
        int curWeight = bestWeight ^ topbit;
        // Copy edges with that only include bits in curWeight
        int edgesUsed = 0 ;
        rep (j , 0 , M) 
        {
            if ((allEdges[j].w | curWeight) == curWeight) 
            {
                curEdges[edgesUsed++] = allEdges[j];
            }
        }
        // Check if connected
        if (is_connected(edgesUsed))
            bestWeight = curWeight;
        
    }
    return bestWeight;
}
int main()
{
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    cin >> T;
    rep(l, 0, T)
    {
        // Read in test case
        cin >> N >> M;
        rep(i, 0, M)
        {
            cin >> allEdges[i];
        }
        // Solve test case
        int ans = greedy_mst();
        cout << ans << "\n";
    }
}