#!/bin/bash
# This script runs testssl.sh for each provided IP address.

# Navigate to the results directory
cd /opt/testssl.sh/results || exit

# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
    echo "You must provide at least one IP address."
    exit 1
fi

for ip in "$@"
do
    echo "Running testssl.sh for IP: $ip"
    # ../testssl.sh -p --jsonfile "results_${ip}.json" --csvfile "results_${ip}.csv" --overwrite "$ip"
    ../testssl.sh -p -P -f -S --jsonfile "results_${ip}.json" --csvfile "results_${ip}.csv" --overwrite "$ip"
done

echo "All scans completed. Results stored in /opt/testssl.sh/results"
