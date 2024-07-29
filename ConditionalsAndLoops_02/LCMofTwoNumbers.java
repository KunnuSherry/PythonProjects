import java.util.Scanner;

//LCM of two numbers
public class LCMofTwoNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number1: ");
        int num1 = sc.nextInt();
        int numa = num1;
        System.out.print("Enter the number2: ");
        int num2 = sc.nextInt();
        int numb = num2;
        // as we know LCM X HCF = num1 X num2
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
            HCF = num1;
        }
        else{
            do{
                y = num2/num1;
                rem = num2%num1;
                num2 = num1;
                num1 = rem;
            } while(rem!= 0);
            System.out.println(num2 + " is the HCF");
            HCF = num2;
        }

        int LCM  = (numa*numb)/HCF;
        System.out.println(LCM+ " is the LCM");
    }
}
