#!/bin/sh

if [ -f /usr/share/java-utils/java-functions ] ; then
  . /usr/share/java-utils/java-functions
else
  echo "Can't find functions library, aborting"
  exit 1
fi

MAIN_CLASS="net.sf.freecol.FreeCol"
BASE_JARS="freecol commons-cli higlayout miglayout-swing cortado-fc"
BASE_FLAGS="-Xmx256M"

set_jvm
set_classpath $BASE_JARS
set_flags $BASE_FLAGS
set_options $BASE_OPTIONS

run --freecol-data /usr/share/freecol "$@"
