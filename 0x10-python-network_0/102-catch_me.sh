#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that
curl -sX PUT -L -d "user_id=98" 0:5000/catch_me -H "Origin: You got me!"
