//Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.

import java.util.Scanner;

public class SimpleInterest {
    public static void main(String[] args) {
        Scanner input  = new Scanner(System.in);
        System.out.print("Enter the Principle: ");
        float principle = input.nextFloat();
        System.out.print("Enter the Time(in years): ");
        int time = input.nextInt();
        System.out.print("Enter the Rate: ");
        float rate = input.nextInt();

        System.out.println("The SI is : "+ principle*time*rate/100);
    }

}
