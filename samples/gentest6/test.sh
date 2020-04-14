#!/bin/bash

success=0
NUMTESTS=1
SUCCESS_STRING="Success: "
FAIL_STRING="FAIL: "

# if python3 python_test.py | grep -q 'Hello, World!'; then
#   SUCCESS_STRING+="Python "
#   ((success=success+1))
# else
#   FAIL_STRING+="Python "
# fi

if node jsTest.js | grep -q 'Hello, World!'; then
  SUCCESS_STRING+="JavaScript "
  ((success=success+1))
else
  FAIL_STRING+="JavaScript "
fi

# gcc cTest.c -o cTest
# if ./cTest | grep -q 'Hello, World!'; then
#   SUCCESS_STRING+="C "
#   ((success=success+1))
# else
#   FAIL_STRING+="C "
# fi
# rm cTest
#
# javac javaTest.java
# if java javaTest | grep -q 'Hello, World!'; then
#   SUCCESS_STRING+="Java "
#   ((success=success+1))
# else
#   FAIL_STRING+="Java "
# fi
# rm javaTest.class
#
# go build goTest.go
# if ./goTest | grep -q 'Hello, World!'; then
#   SUCCESS_STRING+="Go "
#   ((success=success+1))
# else
#   FAIL_STRING+="Go "
# fi
# rm goTest
#
# if ruby rubyTest.rb | grep -q 'Hello, World!'; then
#   SUCCESS_STRING+="Ruby "
#   ((success=success+1))
# else
#   FAIL_STRING+="Ruby "
# fi

if [[ $1 == "-v" ]] || [[ $1 == "--verbose" ]]; then
  echo $SUCCESS_STRING
  echo $FAIL_STRING
fi

if [[ $success == $NUMTESTS ]]; then
  echo "All Tests Passed"
  exit 0
else
  echo "Tests Failed"
  exit 1
fi
# echo $success
