//Display days name in we enter 1 to 7


import java.util.Scanner;

public class Swtich1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter 1 to 7 to display days name respectively: ");
        int num = sc.nextInt();
        switch (num){
            case 1 -> System.out.println("Monday");
            case 2 -> System.out.println("Tuesday");
            case 3 -> System.out.println("Wednesday");
            case 4 -> System.out.println("Thursday");
            case 5 -> System.out.println("Friday");
            case 6 -> System.out.println("Saturday");
            case 7 -> System.out.println("Sunday");
            default -> System.out.println("Please enter a valid number from 1-7");
        }

    }
}
