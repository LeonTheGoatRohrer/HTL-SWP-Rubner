package YouTubeChannel;

public class User implements Subscriber {
    private final String name;

    public User(String name) {
        this.name = name;
    }

    @Override
    public void notify(String videoTitle) {
        System.out.println(name + " erhielt Benachrichtigung: " + videoTitle);
    }

    @Override
    public String toString() {
        return name;
    }
}
