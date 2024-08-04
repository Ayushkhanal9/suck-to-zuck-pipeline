package com.mycompany.app;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.*;
import java.util.Map;
import java.util.Set;

public class App {
    public static void main(String[] args) {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            Map<String, Stats> dataMap = objectMapper.readValue(
                    new File("C:\\Users\\ITAXK03\\Documents\\my-app\\src\\main\\java\\com\\mycompany\\app\\babalPicks.json"),
                    new TypeReference<Map<String, Stats>>() {
                    }
            );

            FileWriter fileWriter = new FileWriter("C:\\Users\\ITAXK03\\Documents\\my-app\\src\\main\\java\\com\\mycompany\\app\\bballpicks.csv");
            CSVPrinter csvPrinter = new CSVPrinter(fileWriter, CSVFormat.DEFAULT.withHeader("Name", "Siera", "FB%", "xFIP", "k/9", "GB%", "HR/FB"));


            for (Map.Entry<String, Stats> entry : dataMap.entrySet()) {
                String name = entry.getKey();
                Stats data = entry.getValue();

                csvPrinter.printRecord(
                        name,
                        data.getSiera(),
                        data.getFb(),
                        data.getxFip(),
                        data.getK9(),
                        data.getGb(),
                        data.getHrFB()
                );
            }
                csvPrinter.close();
                fileWriter.close();

//                System.out.println("Name: " + name);
//                System.out.println("Siera: " + data.getSiera());
//                System.out.println("FB%: " + data.getFb());
//                System.out.println("xFIP: " + data.getxFip());
//                System.out.println("K/9: " + data.getK9());
//                System.out.println("GB%: " + data.getGb());
//                System.out.println("HR/FB: " + data.getHrFB());
//                System.out.println();


        } catch (Exception e) {
            e.printStackTrace();
        }
    }


}


//        try {
//            JSONObject jsonObject = (JSONObject) parser.parse(new FileReader("C:\\Users\\ITAXK03\\Documents\\my-app\\src\\main\\java\\com\\mycompany\\app\\babalPicks.json"));
//
//            Set<String> keys = jsonObject.keySet();
//            for (String key : keys) {
//                System.out.println("Name: " + key);
//
//
//                JSONObject stats = (JSONObject) jsonObject.get(key);
//
//                for (Object statKey : stats.keySet()) {
//                    System.out.println(statKey + ": " + stats.get(statKey));
//                }
//
//                System.out.println();
//            }
//        } catch (IOException e) {
//            e.printStackTrace();
//        } catch (ParseException e) {
//            e.printStackTrace();
//        }
//    }
//}
