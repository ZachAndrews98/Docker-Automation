#!/bin/bash

success=0
NUMTESTS=5

if python3 pythonTest.py | grep -q 'Hello, World!'; then
  ((success=success+1))
fi

if node jsTest.js | grep -q 'Hello, World!'; then
  ((success=success+1))
fi

gcc cTest.c -o cTest
if ./cTest | grep -q 'Hello, World!'; then
  ((success=success+1))
fi
rm cTest

javac javaTest.java
if java javaTest | grep -q 'Hello, World!'; then
  ((success=success+1))
fi
rm javaTest.class

go build goTest.go
if ./goTest | grep -q 'Hello, World!'; then
  ((success=success+1))
fi
rm goTest

if [[ $success == $NUMTESTS ]]; then
  echo "All Tests Passed"
  exit 0
else
  echo "Tests Failed"
  exit 1
fi
# echo $success
