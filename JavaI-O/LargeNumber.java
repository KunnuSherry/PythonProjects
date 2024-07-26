import java.util.Scanner;

public class LargeNumber {
    public static void main(String[] args) {
        Scanner input  = new Scanner(System.in);
        System.out.println("The First Number: ");
        float a = input.nextFloat();
        System.out.println("The Second Number: ");
        float b = input.nextFloat();
        if(a>b){
            System.out.println(a+ " is greater than "+b);
        }
        else{
            System.out.println(b+ " is greater than "+a);
        }
    }
}
