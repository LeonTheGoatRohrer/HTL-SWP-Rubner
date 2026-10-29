package YouTubeChannel;

import java.util.ArrayList;
import java.util.List;

public class YouTubeChannel {
    private final String name;
    private final List<Subscriber> subscribers = new ArrayList<>();

    public YouTubeChannel(String name) {
        this.name = name;
    }

    public void subscribe(Subscriber user) {
        if (user != null && !subscribers.contains(user)) {
            subscribers.add(user);
            System.out.println(user + " abonnierte " + name);
        }
    }

    public void unsubscribe(Subscriber user) {
        subscribers.remove(user);
        System.out.println(user + " hat " + name + " verlassen");
    }

    public void uploadVideo(String title) {
        System.out.println(name + " ladt neues Video hoch: " + title);
        notifyAll(title);
    }

    private void notifyAll(String videoTitle) {
        for (Subscriber sub : subscribers) {
            sub.notify(videoTitle);
        }
    }
}
