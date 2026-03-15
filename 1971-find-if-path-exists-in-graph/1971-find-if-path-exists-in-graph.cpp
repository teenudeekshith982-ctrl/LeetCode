class Solution {
public:
    bool dfs(int src,vector<vector<int>>&adj,vector<int>&vis,int des){
        if(src==des){
            return true;
        }
        vis[src]=1;
        for(auto it:adj[src]){
            if(!vis[it]){
                if(dfs(it,adj,vis,des)==true)
                    return true;
            }
        }
        return false;

    }



    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>>adj(n);
        for(auto it:edges){
            int u = it[0];
            int v = it[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<int>vis(n,0);
        if(dfs(source,adj,vis,destination)==true)
            return true;
        return false;
        
    }
};