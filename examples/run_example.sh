#!/bin/bash

PYTHONPATH=. FLASK_APP=$1.app FLASK_ENV=development flask run