#!/bin/bash

while :
do
    # Capture memory usage and calculate percentage
    memUsed=$(free -m | awk 'NR==2 {print $3}')
    totalMem=$(free -m | awk 'NR==2 {print $2}')
    memUsedPer=$(expr $memUsed \* 100 / $totalMem)

    # Append memory usage details to a TSV file
    echo -e "$(date +"%r %D")\tMemory Used % = $memUsedPer%" >> mem_report.tsv

    # Check if memory usage exceeds threshold
    if [[ $memUsedPer -ge 75 ]]; then
        echo "Security Alarm for memory"

        # Trigger the Python script to send email
        subject="High Memory Usage Alert"
        message="Memory usage has exceeded the threshold. Current usage: ${memUsedPer}%."
        python3 send_email.py "$subject" "$message"
	python3 send_sms.py "$message"

        # Exit after sending the alert
        exit
    fi

    # Wait for 1 second before the next check
    sleep 1
done

