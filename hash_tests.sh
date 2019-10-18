#!/bin/bash

# ascii hash distribution with random input
python hash_functions.py rand_words.txt ascii | python scatter.py ascii_hash_rand.png "Hashed word" "Hashed value" "Ascii Hash Rand Words"

# ascii hash distribution with non random input
python hash_functions.py non_rand_words.txt ascii | python scatter.py ascii_hash_nonrand.png "Hashed word" "Hashed value" "Ascii Hash NonRand Words"

# rolling hash distribution with random input
python hash_functions.py rand_words.txt rolling | python scatter.py rolling_hash_rand.png "Hashed word" "Hashed value" "Rolling Hash Rand Words"

# rolling hash distribution with non random input
python hash_functions.py non_rand_words.txt rolling | python scatter.py rolling_hash_nonrand.png "Hashed word" "Hashed value" "Rolling Hash NonRand Words"

# rolling hash time linear add
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py 10000 rolling linear rand_words.txt $M >  rolling_linear_add.$M.txt
done

grep add rolling_linear_add.*.txt | cut -d " " -f2,3 | python scatter.py rolling_linear_add.png "Load factor" "Insert time" "Rolling Linear Add"

for M in $( seq  1000 1000 10000 ); do
    rm rolling_linear_add.$M.txt
done

# rolling hash time chain add
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py 10000 rolling chain rand_words.txt $M >  rolling_chain_add.$M.txt
done

grep add rolling_chain_add.*.txt | cut -d " " -f2,3 | python scatter.py rolling_chain_add.png "Load factor" "Insert time" "Rolling Chain Add"

for M in $( seq  1000 1000 10000 ); do
    rm rolling_chain_add.$M.txt
done

# rolling hash time linear search
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py 10000 rolling linear rand_words.txt $M >  rolling_linear_search.$M.txt
done

grep search rolling_linear_search.*.txt | cut -d " " -f2,3 | python scatter.py rolling_linear_search.png "Load factor" "Insert time" "Rolling Linear Search"

for M in $( seq  1000 1000 10000 ); do
    rm rolling_linear_search.$M.txt
done

# rolling hash time chain search
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py 10000 rolling chain rand_words.txt $M >  rolling_chain_search.$M.txt
done

grep search rolling_chain_search.*.txt | cut -d " " -f2,3 | python scatter.py rolling_chain_search.png "Load factor" "Insert time" "Rolling Chain Search"

for M in $( seq  1000 1000 10000 ); do
    rm rolling_chain_search.$M.txt
done
