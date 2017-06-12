/*
 * Decompiled with CFR 0_118.
 */
import java.io.PrintStream;

class Fibo {
    Fibo() {
    }

    private static int fib(int n) {
        if (n > 1) {
            return Fibo.fib(n - 1) + Fibo.fib(n - 2);
        }
        return n;
    }

    public static void main(String[] arrstring) throws Exception {
        int n = 0;
        try {
            n = Integer.parseInt(arrstring[0]);
        }
        catch (Exception var3_2) {
            System.out.println("Input error ");
            System.exit(1);
        }
        int n2 = Fibo.fib(n);
        System.out.println("fibonacci(" + n + ") = " + n2);
    }
}
