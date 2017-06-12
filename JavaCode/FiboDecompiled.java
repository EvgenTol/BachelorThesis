class Fibo {

   private static int fib(int var0) {
      return var0 > 1?fib(var0 - 1) + fib(var0 - 2):var0;
   }

   public static void main(String[] var0) throws Exception {
      int var1 = 0;

      try {
         var1 = Integer.parseInt(var0[0]);
      } catch (Exception var4) {
         System.out.println("Input error ");
         System.exit(1);
      }

      int var2 = fib(var1);
      System.out.println("fibonacci(" + var1 + ") = " + var2);
   }
}
