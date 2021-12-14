package dev.dankom.ceh.rest;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletResponse;

@RestController
public class AuthRest {
    @PostMapping
    public void auth(String id, HttpServletResponse response) {
        
    }
}
