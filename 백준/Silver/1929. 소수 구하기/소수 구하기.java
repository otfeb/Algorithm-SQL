import java.util.Scanner;

public class Main {
	
	static boolean[] prime;
	
	static void isprime() {
		// true = 소수X / false = 소수
		prime[0] = true;
		prime[1] = true;
		
		for(int i=2;i<=Math.sqrt(prime.length);i++) {
			if(prime[i])
				continue;
			for(int j=i*i;j<prime.length;j+=i) {
				prime[j] = true;
			}
		}
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = sc.nextInt();
		
		prime = new boolean[n+1];
		isprime();
		
		for(int i=m;i<=n;i++) {
			if(!prime[i]) {
				System.out.println(i);
			}
		}
	}

}
