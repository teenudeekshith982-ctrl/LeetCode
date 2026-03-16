class Solution {
public:
    void dfs(int node , vector<vector<int>>&adj , vector<int>&vis ){
        vis[node]=1;

        for(auto it: adj[node]){
            if(!vis[it]){
                dfs(it,adj,vis);
            }
        }
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int v = isConnected.size();
        vector<vector<int>>adj(v+1);
        for(int i=0;i<v;i++){
            for(int j=0;j<v;j++){
                if(isConnected[i][j]==1 && i!=j){
                    adj[i+1].push_back(j+1);
                    adj[j+1].push_back(i+1);
                }
            }
        }

        vector<int>vis(v+1,0);
        int cnt=0;
        for(int i=1;i<=v;i++){
            if(!vis[i]){
                cnt+=1;
                dfs(i,adj,vis);
            }
        }
        return cnt;
    }
    
};