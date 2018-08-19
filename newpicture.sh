#!/bin/bash
inotifywait -mrq -e create --format %w%f /home/pi/Pictures/woauchimmer/ | while read FILE
do
    echo "Die Datei $FILE wurde gerade erstellt."
    python send.py $FILE
done
