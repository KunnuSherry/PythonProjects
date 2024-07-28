//Print the Largest Number out of the three given numbers.

import java.util.Scanner;

public class Largest_Number {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter The First Number");
        int a = input.nextInt();
        System.out.println("Enter The Second Number");
        int b = input.nextInt();
        System.out.println("Enter The Third Number");
        int c = input.nextInt();

        if (a > b && a > c) {
            System.out.println(a + " is the greatest");
        }
        else if(b>a && b>c){
            System.out.println(b+ " is the greatest");
        }
        else{
            System.out.println(c+ " is the greatest");
        }
    }
}
