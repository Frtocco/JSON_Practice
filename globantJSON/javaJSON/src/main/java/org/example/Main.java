import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.HashMap;
import java.util.Map;

public static Map<String, Object> concatenateMap(Map<String, Object> parentMap, String parentKey) {
    // newMap is going to be the new concatenated map
    Map<String, Object> newMap = new HashMap<>();

    // Iterate through the map
    for (Map.Entry<String,Object> entry : parentMap.entrySet()) {
        // Get key and value
        String key = entry.getKey();
        Object value = entry.getValue();
        // If the value is an instance, we call the function recursively with the value as the new Parent
        if (value instanceof Map) {
            // Asign the parentKey
            newMap.putAll(concatenateMap((Map<String, Object>) value,  (key + ".")));
        } else {
            newMap.put(parentKey + key, value);
        }
    }
    return newMap;
}


public static void main(String[] args) throws JsonProcessingException{
    String json = "{ \"a\": true, \"b\": { \"b1\": \"hello\", \"b2\": 3.5 }, \"c\": 3 }";

    // Maper to get the JSON string as Map
    ObjectMapper mapper = new ObjectMapper();

    Map<String, Object> map = mapper.readValue(json, new TypeReference<>() {});
    System.out.println("map = " + map);

    // New map with concatenated values
    Map<String,Object> newMap = concatenateMap(map, "");
    // Print map
    for(Map.Entry<String, Object> entry : newMap.entrySet()){
        System.out.println(entry.getKey() +  " " + entry.getValue());
    }
}
