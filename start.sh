#!/bin/bash

mongod --dbpath data_chatbot/db/
./rpyc_server.sh

