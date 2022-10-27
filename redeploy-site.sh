#!/bin/bash
cd portfolio
# make sure git repo in VPS has the latest changes from the main branch on GH
git fetch && git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
