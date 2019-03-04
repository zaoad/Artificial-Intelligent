#include<bits/stdc++.h>
using namespace std;
map<char,int>mp;
map<int,char>revmp;

int temp=1;

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
    int nodeindex;
    int cost;
    node(int n,int c)
    {
        nodeindex=n;
        cost=c;
    }
};
bool operator<(node A,node B)
{
    if(A.cost>B.cost)
        return true;
    else
        return false;
}
vector<edge>adj[100];
priority_queue<node>PQ;
int dist[100], parent[100];
int n;

void ucs(int source)
{
    ///////////////////////////
    for(int i=0;i<100;i++)
    {
        dist[i]=100000;
    }
    /////////////////////////////
    node s=node(source,0);
    dist[source]=0;
    PQ.push(s);
    parent[source]=0;
    while(!PQ.empty())
    {
        node a=PQ.top();
        int u=a.nodeindex;
        PQ.pop();
        for(int i=0;i<adj[u].size();i++)
        {
            edge e=adj[u][i];
            if(dist[e.v]>dist[u]+e.w)
            {
                dist[e.v]=dist[u]+e.w;
                parent[e.v]=u;
                node b=node(e.v,dist[e.v]);
                PQ.push(b);
            }
        }
    }
}
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

void pathprint(int node)
{
    vector<int>path;
    while(!node==0)
    {
        path.push_back(node);
        node= parent[node];
    }
    reverse(path.begin(),path.end());
    for(int i=0; i<path.size(); i++)
    {
        cout<<inttochar(path[i])<<" ";
    }
    cout<<endl;
}

int main()
{
    char parent_char, child_char,source_char, destination_char;
    int n,number_edge,cost,i,j,u,v,w,huris, path_num, par, child,source,destination;

    if(freopen("ucs.txt", "r", stdin))
        cout<<"Input A* file found."<<endl;
    else
        cout<<"File not found.";
    cin>>n>>source_char>>destination_char;
    while(cin>>parent_char)
    {
        u= chartoint(parent_char);
        //u=parent_char;
        cin>>number_edge;
        for(i=0;i<number_edge;i++)
        {
            cin>>child_char;
            v=chartoint(child_char) ;
            //v=child_char
            cin>>w;
            adj[u].push_back(edge(v,w));
        }

    }
    ucs(chartoint(source_char));
    pathprint(chartoint(destination_char));
    for(i=0;i<6;i++)
    {
        cout<<i<<" "<<parent[i]<<endl;
    }
    cout<<"cost "<<dist[chartoint(destination_char)];
    /* for(i=1;i<=node;i++)
    {
       cin>>huris;
       huristic[i]=huris;
    }
    for(i=0;i<number_edge;i++)
    {
       cin>>u>>v>>w;
       adj[u].push_back(edge(v,w));
    }
    ucs(1);
    for(i=1;i<=node;i++)
    {
       cout<<i<<" "<<dist[i]<<endl;
    }
    for(i=1;i<=node;i++)
    {
       pathprint(i);*/
    // pathprint(source);
    return 0;

}

//cin>>node>>source>>destination;
/*for(i=1;i<=node;i++)
{
    cin>>huris;
    huristic[i]=huris;
}
for(i=0;i<number_edge;i++)
{
    cin>>u>>v>>w;
    adj[u].push_back(edge(v,w));
}
ucs(1);
for(i=1;i<=node;i++)
{
    cout<<i<<" "<<dist[i]<<endl;
}
for(i=1;i<=node;i++)
{
    pathprint(i);
}*/

