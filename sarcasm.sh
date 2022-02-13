#!/usr/bin/env bash

USAGE="Usage: $(basename $0) [ -d -l -u -h ] <str>\n
	-d:	Print debugging output.\n
	-l:	Start with lowercase character.\n
	-u:	Start with uppercase character.\n
	-h:	Displays help message.\n
	<str>:	String to be formatted.\n
"

# Read options:
while getopts "dluh" flag
do
        case "$flag" in
                d)
                        DEBUG=1
                        ;;
                l)
                        UPPERCASE=false
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
echo "${OUT}"
