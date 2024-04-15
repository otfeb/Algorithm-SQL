import java.util.Scanner;

// 1로 만들기
public class Main {
	
	public static int[] ary;
	public static int dp(int n) {
		
		if(n == 1) {
			return 0;
		}
		if(ary[n] > 0) {
			return ary[n];
		}
		ary[n] = dp(n-1) + 1;
		if(n%2 == 0) {
			int min = dp(n/2) + 1;
			if(ary[n] > min) {
				ary[n] = min;
			}
		}
		if(n%3 == 0) {
			int min = ary[n/3] + 1;
			if(ary[n] > min) {
				ary[n] = min;
			}
		}
		return ary[n];
		
		
	}
	public static void main(String[] args) {

		int n;
		Scanner scanner = new Scanner(System.in);
		n = scanner.nextInt();
		ary = new int[n+1];
		System.out.println(dp(n));

	}

}
