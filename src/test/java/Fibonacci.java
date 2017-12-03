public class Fibonacci {

    public long[] generate(int length) {
        long[] sequence = new long[length];
        for (int i = 0; i < length; i++) {
            if (i < 2) {
                sequence[i] = i;
            } else {
                sequence[i] = sequence[i - 1] + sequence[i - 2];
            }
        }
        return sequence;
    }
}
