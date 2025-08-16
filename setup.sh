#!/bin/bash
pip install -r requirements.txt
gunicorn -w 4 -b 0.0.0.0:7860 app:app