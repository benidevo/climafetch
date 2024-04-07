#!/bin/bash

set -e

if [ ! -f .env ]; then
    cp .env.example .env
fi

source .env

docker compose up -d
docker compose logs

if [ ! -d "venv" ]; then
    python -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r dev-requirements.txt
fi

source venv/bin/activate

export LOG_LEVEL=info

python main.py
