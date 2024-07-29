import java.util.Scanner;

//To Find HCF of two numbers
public class HCFofTwoNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number1: ");
        int num1 = sc.nextInt();
        System.out.print("Enter the number2: ");
        int num2 = sc.nextInt();
        int rem;
        int y;
        int HCF;
        if(num1>num2){
            do{
                y = num1/num2;
                rem = num1%num2;
                num1 = num2;
                num2 = rem;
            }while(rem!=0);
            System.out.println(num1+ " is the HCF");
        }
        else{
            do{
                y = num2/num1;
                rem = num2%num1;
                num2 = num1;
                num1 = rem;
            } while(rem!= 0);
            System.out.println(num2 + " is the HCF");
        }
    }
}

/* To find the hcf keep on dividing the two numbers and find the remainder everytime and the assign the remainder to the
smaller number. do this until the remainder is not zero and the answer would be the last num2*/
