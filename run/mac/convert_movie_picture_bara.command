#!/bin/sh
cd `dirname $0`
cd ../../drawing
python convert_movie_picture_bara.py
open ./picture