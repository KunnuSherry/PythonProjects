import java.util.Scanner;

public class PrimeNumbersBetweenTwoNumbers {
    public static void main(String[] args) {
        System.out.println("Enter the numbers: ");
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        prime(num1, num2);

    }
    static void prime(int a, int b){
        System.out.println("The Prime Number Between " + a + " and " + b + " are: ");
        for(int i=a+1; i<b; i++){
            if(isPrime(i)){
                System.out.println(i);
            }
        }
    }
    static boolean isPrime(int num){
        boolean x = false;
        for(int i=2; i<num; i++){
            if(num==2){
                x = true ;
            }
            else if(num%i==0){
                x = false;
                break;
            }
            else{
                x = true;
            }
        }
        return x;
    }
}
