import java.util.Scanner;

public class Prime {
    public static void main(String[] args) {
        System.out.println("Enter the number: ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        prime(a);

    }
    static void prime(int num){
        for(int i=2; i<num; i++){
            if(num==2){
                System.out.println("Prime Number");
            }
            else if(num%i==0){
                System.out.println("Composite number");
                break;
            }
            else{
                System.out.println("Prime Number");
            }
        }
    }
}
