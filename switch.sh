#!/bin/sh
curl -X POST http://localhost:5001/lights/1/$1 &
curl -X POST http://localhost:5001/lights/2/$1 &
curl -X POST http://localhost:5001/lights/3/$1 &
wait
