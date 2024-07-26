import java.util.Scanner;

//Write a program to print whether a number is even or odd, also take input from the user.
public class OddOrEven {
    public static void main(String[] args) {
        System.out.print("Enter The Number To Be Checked: ");
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        if(number%2==0){
            System.out.println(number + " is an even number");
        }
        else{
            System.out.println(number+ " is an odd number");
        }

    }
}
