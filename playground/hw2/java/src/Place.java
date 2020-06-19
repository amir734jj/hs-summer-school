public class Place {

    public double latitude;
    public double longitude;

    public Place(double latitude, double longitude) {
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public double distance(Place other) {
        // TODO
        return this.latitude - other.latitude;
    }

    @Override
    public String toString() {
        return this.latitude + ", " + this.longitude;
    }
}
