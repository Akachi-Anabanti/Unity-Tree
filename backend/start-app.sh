#!/usr/bin/env bash

# STARTS THE FLASK APPLICATION WITH GUNICORN
#
# TERMINAL COLORS
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

ENV=$FLASK_ENV

# Start the virtual Environment

if [ "$ENV"  == "production" ]; then
	echo -e "${GREEN}Starting App in Production Mode..${NC}"
	gunicorn -w4 run:app
else
	echo -e "${GREEN}Starting App in Development Mode.. ${NC}"
	flask run --debug -p 8000
fi
