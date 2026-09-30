#!/bin/bash
# Load-balancing test: expect A, B, A, B
MAC2="2409:40d6:1019:a702:1c96:d0e2:bf6a:ae25"
for i in 1 2 3 4; do
  curl -s -D - -o /dev/null --resolve "app.team1.test:80:[$MAC2]" "http://app.team1.test/api/status" | grep -i x-backend
done
