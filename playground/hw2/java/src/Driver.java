public class Driver {

    public static void main(String[] args) {

        System.out.println(factorial(3));
        System.out.println(fahrenheitToCelsius(32));

        Place franklin = new Place(10, 20);
        Place shorewood = new Place(20, 10);

        System.out.println(franklin);
        System.out.println(shorewood);

        System.out.println(franklin.distance(shorewood));

        City milwaukee = new City("Milwaukee", 12345, 10, 20);
        City chicago = new City("Chicago", 54321, 20, 10);

        System.out.println(milwaukee);
        System.out.println(chicago);

        State wisconsin = new State("Wisconsin", new City[]{milwaukee, chicago});
        System.out.println(wisconsin);
    }

    static int factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    static double fahrenheitToCelsius(double f) {
        return (f - 32) / 180;
    }

}