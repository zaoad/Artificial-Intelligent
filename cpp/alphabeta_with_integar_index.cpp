#include<bits/stdc++.h>
using namespace std;

int score[100];
vector<int>adj[100];

int alpha_beta_multiple_edge(int source, bool isMax, int alpha, int beta)
{
    if(score[source]!=-1)
    {
        return score[source];
    }
    if(isMax)
    {
        int maxval= -10000;
        for(int i=0; i<adj[source].size(); i++)
        {
            int val= alpha_beta_multiple_edge(adj[source][i], false, alpha, beta);
            maxval= max(maxval, val);
            alpha= max(maxval, alpha);
            if(beta<= alpha)
                break;
        }
        return maxval;
    }
    else
    {
        int minval= 10000;
        for(int i=0; i<adj[source].size(); i++)
        {
            int val= alpha_beta_multiple_edge(adj[source][i], true, alpha, beta);
            minval= min(minval,val);
            beta= min(minval, beta);
            if(beta<= alpha)
                break;
        }
        return minval;
    }
}

int main()
{
    int node_number, node_index, edge_number, value, child_index;
    freopen("alphabeta_with_integar_index.txt", "r", stdin);
    for(int i=0; i<100; i++)
    {
        score[i]= -1;
    }
    cin>>node_number;
    while(cin>>node_index)
    {
        cin>>edge_number;
        if(edge_number== 0)
        {
            cin>>value;
            score[node_index]= value;
        }
        for(int i=0; i<edge_number; i++)
        {
            cin>>child_index;
            adj[node_index].push_back(child_index);
        }
    }
    int ans;
    ans= alpha_beta_multiple_edge(1, true, -1000, 1000);
    cout<<"The ans is: "<<ans<<endl;
    return 0;
}
