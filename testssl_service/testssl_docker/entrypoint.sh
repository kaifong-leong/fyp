#!/bin/bash
# This script runs testssl.sh for each provided IP address.

# Navigate to the results directory
cd /home/testssl/results || exit

# Loop over all the IPs passed as arguments
if [ "$#" -lt 1 ]; then
    echo "You must provide at least one IP address."
    exit 1
fi

for ip in "$@"
do
    echo "Running testssl.sh for IP: $ip"
    # ../testssl.sh --std --fs --protocols --server-defaults --server-preference --htmlfile results.html --jsonfile results.json --csvfile results.csv --overwrite "$ip"
    ../testssl.sh --protocols --htmlfile results.html --jsonfile results.json --csvfile results.csv --overwrite "$ip"
done

