public class City extends Place {

    public String name;
    public int zipcode;

    public City(String name, int zipcode, double latitude, double longitude) {
        super(latitude, longitude);
        this.name = name;
        this.zipcode = zipcode;
    }

    @Override
    public String toString() {
        return this.name + "(" + this.zipcode + ") " + this.latitude + ", " + this.longitude;
    }
}
