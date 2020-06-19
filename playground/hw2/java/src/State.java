public class State {

    public final String name;
    public final City[] cities;

    public State(String name, City[] cities) {
        this.name = name;
        this.cities = cities;
    }

    @Override
    public String toString() {
        String str = this.name;

        for (City city : this.cities) {
            str = str + "\n" + city.name + "(" + city.zipcode + ") " + city.latitude + ", " + city.longitude;
        }

        return str;
    }
}
