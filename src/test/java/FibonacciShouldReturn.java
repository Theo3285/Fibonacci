import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class FibonacciShouldReturn {

    private Fibonacci fibonacci;

    @Before public void setUp() {
        fibonacci = new Fibonacci();
    }

    @Test public void zeroForFirstNumber() {
        assertEquals(0, getNumberAtIndex(0));
    }

    @Test public void oneForSecondNumber() {
        assertEquals(1, getNumberAtIndex(1));
    }

    @Test public void oneForThirdNumber() {
        assertEquals(1, getNumberAtIndex(2));
    }

    @Test public void twoForTheFourthNumber() {
        assertEquals(2, getNumberAtIndex(3));
    }

    @Test public void fiveForTheFifthNumber() {
        assertEquals(5, getNumberAtIndex(5));
    }

    @Test public void hugeValueForFiftiethNumber() {
        assertTrue(getNumberAtIndex(49) > 1000000000);
    }

    private long getNumberAtIndex(int index) {
        return fibonacci.generate(index + 1)[index];
    }
}
