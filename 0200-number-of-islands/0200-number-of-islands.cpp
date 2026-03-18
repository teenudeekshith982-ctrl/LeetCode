class Solution {
public:
    bool isvalid(int row,int col,int n,int m){
        if(row>=0 && row<n && col>=0 && col<m){
            return true;
        }
        return false;
    }

    void dfs(int row, int col, vector<vector<int>>&vis ,vector<vector<char>>& grid,int n,int m){
        vis[row][col]=1;

        int dr[4] = {0,-1,0,1};
        int dc[4] = {-1,0,1,0};

        for(int i=0;i<4;i++){
            int nr = row + dr[i];
            int nc = col + dc[i];
            if(isvalid(nr,nc,n,m) && !vis[nr][nc] && grid[nr][nc]=='1'){
                dfs(nr,nc,vis,grid,n,m);
            }
        }
                
    }




    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();

        vector<vector<int>>vis(n,vector<int>(m,0));
        int cnt=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(!vis[i][j] && grid[i][j]=='1'){
                    cnt+=1;
                    dfs(i,j,vis,grid,n,m);
                }
            }
        }

        return cnt;
    }
};