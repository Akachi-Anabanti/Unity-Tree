#!/usr/bin/python3

from app import create_app
from app.config import Settings


app = create_app(Settings)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
