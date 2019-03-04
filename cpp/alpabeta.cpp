#include<bits/stdc++.h>
using namespace std;
map<char,int>mp;
map<int,char>revmp;
int score[100];
vector<int>adj[100];
int alpha_beta_multiple_edge(int source, bool isMax,int alpha,int beta)
{
    if(score[source]!=-1)
    {
        return score[source];
    }
	if (isMax)
	{
        int maxval=-1000;
        for(int i=0;i<adj[source].size();i++)
        {
            int val=alpha_beta_multiple_edge(adj[source][i],false,alpha,beta);
            maxval=max(maxval,val);
            alpha=max(maxval,alpha);
            if(beta<=alpha)
                break;
        }

        return maxval;
	}
	else
    {
        int minval=1000000;
        for(int i=0;i<adj[source].size();i++)
        {
            int val=alpha_beta_multiple_edge(adj[source][i],true,alpha,beta);
            minval=min(minval,val);
            beta=min(beta,minval);
            if(beta<=alpha)
                break;
        }
        return minval;
    }
}
int temp=1;
int chartoint(char c)
{
    if(mp.find(c) == mp.end())
    {
        ///not found
        mp[c]=temp;
        revmp[temp]=c;
        temp++;
    }
    return mp[c];
}
char inttochar(int n)
{
    return revmp[n];
}
int main()
{
    int index,val,root,i,number_child,child_index,number_of_nodes;
    char nodechar,child_index_char;
    freopen("alphabeta.txt","r",stdin);
    for(i=0;i<100;i++)
    {
        score[i]=-1;
    }
    cin>>number_of_nodes;
    while(cin>>nodechar)
    {
       index=chartoint(nodechar);
       cin>>number_child;
       if(number_child==0)
       {
           cin>>val;
            score[index]=val;
       }
       for(i=0;i<number_child;i++)
       {
            cin>>child_index_char;
            child_index=chartoint(child_index_char);
            adj[index].push_back(child_index);
       }
    }
    int ans=alpha_beta_multiple_edge(1,true,-1000,1000);
    cout<<ans<<endl;

}
