#!/usr/bin/env bash

USAGE="Usage: $(basename $0) [ -d -l -n -u -h ] <str>\n
	-d:	Print debugging output.\n
	-l:	Start with lowercase character.\n
	-n:	Do not write output to clipboard (wl-clipboard and xclip).\n
	-u:	Start with uppercase character.\n
	-h:	Displays help message.\n
	<str>:	String to be formatted.\n
"

# Read options:
while getopts "dlnuh" flag
do
        case "$flag" in
                d)
                        DEBUG=1
                        ;;
                l)
                        UPPERCASE=false
                        ;;
                n)
                        NO_CLIPBOARD=1
                        ;;
                u)
                        UPPERCASE=true
                        ;;
                h)
                        echo -e "$USAGE"
                        exit 0
                        ;;
                \?)
                        echo "Invalid option: -$OPTARG" >&2
                        exit 1
                        ;;
        esac
done

# Select remaining inputs, this avoids the need to enclose the input string in quotation marks.
IN=${@:$OPTIND}
OUT=""
FORCE_UPPER="
	Ll
	Tt
"
FORCE_LOWER="
	iI
	jJ
"

for i in $(seq 1 ${#IN}); do
	LETTER="${IN:i-1:1}"
	if [ "$DEBUG" ]; then
		echo "Letter $i: ${LETTER}"
	fi
	if [[ $FORCE_UPPER == *"${LETTER}"* ]]; then
		LETTER="${LETTER^^}"
		UPPERCASE=false
	elif [[ $FORCE_LOWER == *"${LETTER}"* ]]; then
		LETTER="${LETTER,,}"
		UPPERCASE=true
	elif [[ "$UPPERCASE" == true ]]; then
		LETTER="${LETTER^^}"
		UPPERCASE=false
	else
		LETTER="${LETTER,,}"
		UPPERCASE=true
	fi
	if [ "$DEBUG" ]; then
		echo "Letter $i (processed): ${LETTER}"
	fi
	OUT="${OUT}${LETTER}"
done

if [ -z "$NO_CLIPBOARD" ]; then
	wl-copy "${OUT}"
	echo "${OUT}" | xclip
	echo "\"${OUT}\" written to clipboard."
else
	echo "${OUT}"
fi
