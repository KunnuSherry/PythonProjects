import java.util.Scanner;

//Take integer inputs till the user enters 0 and print the sum of all numbers (HINT: while loop)
public class SumTill0 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter The Number: ");
        int num = sc.nextInt();
        int sum = 0;
        if (num != 0) {
            do{
                sum+=num;
                System.out.println("Current Sum: "+ sum);
                System.out.print("Enter The Number: ");
                num = sc.nextInt();

            }while(num!=0);
            System.out.println("Loop Exited!");
            System.out.println("Sum: "+ sum);
        }
        else{
            System.out.print("Loops Exited!");
            System.out.println("Sum: "+ sum);
        }
    }
}
