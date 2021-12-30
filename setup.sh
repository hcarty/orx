#!/bin/sh

OS=`uname -s`
ARCH=`uname -m`

if [ "${OS}" = "Darwin" ]; then
    REBOL=code/build/rebol/r3-mac
else
    if [ "${ARCH}" = "x86_64" ]; then
        echo "I am 64 bit"
        REBOL=code/build/rebol/r3-linux
    else
        echo "I am 32 bit"
        REBOL=code/build/rebol/r3-linux
    fi
fi

${REBOL} -qs code/build/rebol/setup.r "$@"
