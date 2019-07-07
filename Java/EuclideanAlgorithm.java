import com.sun.imageio.plugins.common.InputStreamAdapter;

class EuclideanAlgorithm {
    public static long getGCD(long... arg) {
        if (arg.length < 2) {
            throw new RuntimeException();
        } else if (arg.length == 2) {
            if (arg[0] < arg[1]) {
                long t = arg[0];
                arg[0] = arg[1];
                arg[1] = t;
            }
            if (arg[0] % arg[1] == 0) {
                return arg[1];
            }
             else {
                return getGCD(arg[1], arg[0] % arg[1]);
            }
        } else {
            long[] arg1 = new long[arg.length - 1];
            arg1[0] = getGCD(arg[0], arg[1]);
            for (int i = 1; i < arg1.length; i++) {
                arg1[i] = arg[i + 1];
            }
            return getGCD(arg1);
        }

    }
}

class Test{
    public static void main(String[]args){
        System.out.println("sdf");
        
    }
}