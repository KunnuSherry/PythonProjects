import java.util.Scanner;

public class MaxAndMin {
    public static void main(String[] args) {
        System.out.println("enter the three numbers: ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        Max(a, b, c);
        Min(a, b, c);

    }


static void Max(int a, int b, int c){
    if(a>b && a>c ){
        System.out.println(a + " is the maximum number.");

    } else if (b>a && b>c) {
        System.out.println(b + " is the maximum number.");

    } else{
        System.out.println(c + " is the maximum number.");
    }

}
    static void Min(int a, int b, int c){
        if(a<b && a<c ){
            System.out.println(a + " is the minimum number.");

        } else if (b<a && b<c) {
            System.out.println(b + " is the minimum number.");

        } else{
            System.out.println(c + " is the minimum number.");
        }

    }
}
