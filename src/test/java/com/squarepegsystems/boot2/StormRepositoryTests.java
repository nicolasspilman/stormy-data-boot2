package com.squarepegsystems.boot2;

import com.squarepegsystems.boot2.entity.State;
import com.squarepegsystems.boot2.entity.Storm;
import com.squarepegsystems.boot2.entity.StormType;
import junit.framework.TestCase;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.test.context.junit4.SpringRunner;

import java.net.URI;
import java.time.LocalDateTime;
import java.util.Map;

@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class StormRepositoryTests {

    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    public void getsStateSuccess() throws Exception {
        State state = new State();
        state.setId(1l);
        state.setName("Minnesota");

        StormType stormType = new StormType();
        stormType.setId(1l);
        stormType.setName("Name");

        Storm storm = new Storm();
        storm.setId(1l);
        storm.setBeginTime(LocalDateTime.now());
        storm.setEndTime(LocalDateTime.now());
        storm.setState(state);
        storm.setStormType(stormType);

        URI location = restTemplate.postForLocation(new URI("/api/storms"), storm);

        Map page = restTemplate.getForObject("/api/storms", Map.class);

        // Not sure what assertions are valid here.
        TestCase.assertEquals(Integer.valueOf((String) page.get("status")).intValue(), 200);
    }
}
