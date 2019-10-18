#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# test if scatter produces a figure
test ! -f ascii_hash_function.png

python hash_functions.py rand_words.txt ascii | python scatter.py ascii_hash_function.png "Hashed word" "Hashed value" "plot title"

test -f ascii_hash_function.png

rm ascii_hash_function.png

run hash_ftn_test python hash_functions.py rand_words.txt ascii
assert_no_stderr

run hash_table_test python hash_tables.py 1000 ascii linear rand_words.txt 1
assert_no_stderr
