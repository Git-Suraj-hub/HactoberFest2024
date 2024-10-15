import java.util.Scanner;

public class ReverseTheNumber {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("enter a number : ");
        int a = sc.nextInt();
        int b = a;
        int c = 0;
        while (a > 0) {
            int d = a%10;
            c = c*10 + d;
            a/=10;
        }
        System.out.println("the real value of A is :  " + b);
        System.out.println("the value of A after the reverse is : " +c);
    }
}
