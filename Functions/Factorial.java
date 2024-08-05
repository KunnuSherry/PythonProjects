import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        System.out.println("Enter the number: ");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        factorial(num);


    }
    static void factorial(int num){
        int fac = 1;
        for(int i=num; i>0; i--){
            fac*=i;
        }
        System.out.println(num+ "! = "+ fac);
    }
}
