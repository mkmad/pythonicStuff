#!/bin/bash

# Function to execute clingo command and handle output
run_clingo() {
    local n=$1
    clingo warehouse.lp "i$n.lp" > "output$n.txt" 2>&1 &  
    #  ^ redirects errors to the same file   ^ starts in the background
}

# Loop to execute clingo commands in parallel
for n in {1..5}; do
    run_clingo $n
done

# Wait for all background processes to finish
echo "Clingo processes started. Waiting for completion..."
wait

# Check for errors and report
for n in {1..5}; do
    if [ $? -ne 0 ]; then
        echo "ERROR: clingo encountered an issue for i$n.lp. Check output$n.txt"
    else
        echo "SUCCESS: Output for I$n.lp is in output$n.txt"
    fi
done