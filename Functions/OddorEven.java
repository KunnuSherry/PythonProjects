import java.util.Scanner;

public class OddorEven {
    public static void main(String[] args) {
        System.out.println("Enter the number: ");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        evenodd(num);

    }
    static void evenodd(int num){
        if(num%2==0){
            System.out.println("Even Number.");
        }
        else{
            System.out.println("Odd Number.");
        }
    }
}
