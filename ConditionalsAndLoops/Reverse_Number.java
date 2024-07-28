import java.util.Scanner;

public class Reverse_Number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        long num = sc.nextLong();
        int length = Long.toString(num).length();
        long num1 = num;
        long numRev = 0;
        while (num1 != 0) {
            long rem = num1 % 10;
            numRev = numRev * 10 + rem;
            num1 /= 10;
        }
        System.out.println("The reversed number is: "+ numRev);

    }
}
