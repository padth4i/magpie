#!/bin/sh

#filename of wordlist
LIST=$1
#language to translate from
LANGF=$2
#language to translate to
LANGT=$3

for LWORD in `cat $LIST`; do
        TEXT=`wget -q http://$LANGF.wikipedia.org/wiki/$LWORD -O - | grep 'interwiki-'$LANGT`; 
        if [ $? -eq '0' ]; then
                RWORD=`echo $TEXT |
                cut -f4 -d'"' | cut -f5 -d'/' |
                python -c 'import urllib, sys; print urllib.unquote(sys.stdin.read());' |
                sed 's/(\w*)//g'`;
                echo '<e><p><l>'$LWORD'<s n="n"/></l><r>'$RWORD'<s n="n"/></r></p></e>';
        fi;
        sleep 8;
done
