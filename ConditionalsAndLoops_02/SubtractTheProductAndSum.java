//Subtract the Product and Sum of Digits of an Integer

import java.util.Scanner;

public class SubtractTheProductAndSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter The Number: ");
        long num = sc.nextLong();
        int length = Long.toString(num).length();
        long product = 1;
        long num1 = num;
        long sum = 0;
        for(int i=1; i<=length; i++){
            long rem = num1%10;
            product*=rem;
            sum+=rem;
            num1/=10;
        }
        System.out.println("The Prodcut is: "+ product);
        System.out.println("The Sum is: "+ sum);
    }
}
