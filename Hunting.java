import java.util.Scanner;

public class Hunting {
    public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
            int  n =  input.nextInt();
            int m =  input.nextInt();
            int[][] Data = new int[n][m];

            int [][]dp = new  int[n+1][m+1];

            int total = 0 ;
            for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Data[i][j] = input.nextInt();
            }
        }
        for (int i = 1; i <n+1 ; i++) {
            for (int j = 1; j <=m ; j++) {
                if(Data[i-1][j-1] == 0) continue;
                dp[i][j] = Math.min(Math.min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1]) + 1 ;
                total += dp[i][j];
            }
        }
        System.out.println(total);
    }
}
