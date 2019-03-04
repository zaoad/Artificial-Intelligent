#include<bits/stdc++.h>
using namespace std;

struct edge
{
    int v;
    int w;
    edge(int _v, int _w)
    {
        v= _v;
        w= _w;
    }
};
struct node{
    int index,score;
    node(int _index, int _score)
    {
        index=_index;
        score=_score;
    }
};
vector<node>adj[100];
int minimax_multiple_edge(node source, bool isMax)
{
    if(source.score!=0)
    {
        return source.score;
    }
	if (isMax)
	{
        int maxval=0;
        for(int i=0;i<adj[source.index].size();i++)
        {
            maxval=max(maxval,minimax_multiple_edge(adj[source.index][i],false));
        }
        return maxval;
	}
	else
    {
        int minval=1000000;
        for(int i=0;i<adj[source.index].size();i++)
        {
            minval=min(minval,minimax_multiple_edge(adj[source.index][i],true));
        }
        return minval;
    }
}
int main()
{
    int index,val,root,i,number_child,child_index;
    freopen("minimax.txt","r",stdin);
    cin>>root;
    while(cin>>index)
    {
       cin>>number_child;
       for(i=0;i<number_child;i++)
       {
            cin>>child_index>>val;
            node c=node(child_index,val);
            adj[index].push_back(c);
       }
    }
    int ans=minimax_multiple_edge(node(root,0),true);
    cout<<ans<<endl;

}
