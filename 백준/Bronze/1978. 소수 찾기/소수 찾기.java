import java.util.Iterator;
import java.util.Scanner;

// 소수 찾기
public class Main {

	public static boolean prime(int n) {
		int i;
		
		if(n < 2) {
			return false;
		}
		for(i=2; i<=n-1; i++) {
			if(n % i == 0) {
				return false;
			}
		}
		return true;
	}
	
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int ans = 0;
		int i;
		
		for(i=0; i<n; i++) {
			if(prime(scanner.nextInt())) {
				ans += 1;
			}
		}
		System.out.println(ans);
	}

}
