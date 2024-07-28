import java.util.Scanner;

public class FibonacciSeries {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the nth number: ");
        int n = sc.nextInt();
        int a = 0;
        int b = 1;

        for(int i=1; i<=n; i++){
            int c = a+b;
            System.out.print(a);
            a=b;
            b=c;
            if(i!=n){
                System.out.print(", ");
            }

        }
    }
}
