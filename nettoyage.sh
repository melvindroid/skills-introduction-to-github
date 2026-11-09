#!/bin/bash


DOSSIER="$HOME/Desktop/Dossier_test"

echo "début du rangement"

for fichier in "$DOSSIER"/*
do
    extension="${fichier##*.}"

    if [ "$extension" = "png" ]; then

        destination="$DOSSIER/png"

        mkdir -p "$destination"

        mv -n "$fichier" "$destination/"
		
	elif [ "$extension" = "pdf" ]
		
		sleep 5

	then
        destination="$DOSSIER/pdf"

        mkdir -p "$destination"

        mv -n "$fichier" "$destination/"
		
	elif [ "$extension" = "csv" ]
	then
        destination="$DOSSIER/csv"

        mkdir -p "$destination"

        mv -n "$fichier" "$destination/"
		
		echo "fin du rangement"

    fi
done
