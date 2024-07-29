//Take integer inputs till the user enters 0 and print the largest number from all.
import java.util.Scanner;

public class LargestNumberTill0 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter The Number: ");
        int num = sc.nextInt();
        int num1;
        int num2;
        if(num!=0){
            do{
                num1 = num;
                System.out.print("Enter The Number: ");
                num = sc.nextInt();
                if(num>num1){
                    num2 = num;
                }
                else{
                    num2 = num1;
                }
            }while(num!=0);
            System.out.println(num2+ " is the greatest Number!");
        }
        else{
            System.out.println("Greatest Number is 0");
        }
    }
}
