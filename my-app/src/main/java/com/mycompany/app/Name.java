package com.mycompany.app;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Name {
    @JsonProperty("name")
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
