# Memory Usage Monitor with Alerts

This repository contains scripts for monitoring memory usage and sending alerts via email and SMS when memory usage exceeds a defined threshold.

## Features
- Monitors system memory usage in real-time.
- Logs memory usage details into a `.tsv` file.
- Sends email and SMS alerts when memory usage exceeds the specified threshold.
- Utilizes Python for alert functionality and Bash for monitoring.

---

## File Structure

```
.
├── monitor_memory.sh       # Bash script to monitor memory usage and trigger alerts
├── send_email.py           # Python script for sending email alerts
├── send_sms.py             # Python script for sending SMS alerts via Twilio
├── mem_report.tsv          # Memory usage logs (generated during execution)
└── README.md               # Documentation
```

---

## Prerequisites

### Tools and Libraries
1. **Python** (>=3.6): Ensure Python is installed.
2. **Twilio Library**: Install using `pip install twilio`.
3. **xclip** (Linux only): Install using the appropriate package manager for clipboard functionality.

### Accounts
- **Email SMTP Server**: Gmail is recommended. Enable "Less secure app access" or use an app password.
- **Twilio Account**: Create a Twilio account and obtain the `account_sid`, `auth_token`, and phone numbers.

### Environment Variables (Recommended for Security)
Set the following variables in your environment:
- `EMAIL_ADDRESS`  
- `EMAIL_PASSWORD`  
- `TWILIO_SID`  
- `TWILIO_AUTH_TOKEN`  
- `TWILIO_PHONE_NUMBER`  
- `RECIPIENT_PHONE_NUMBER`  
- `RECIPIENT_EMAIL`  

---

## Setup and Execution

### 1. Clone the Repository
```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

### 2. Configure Scripts
Ensure required environment variables are set or replace placeholders in `send_email.py` and `send_sms.py` with actual credentials.

### 3. Run the Monitor Script
```bash
bash monitor_memory.sh
```
This will continuously monitor memory usage and trigger alerts when usage exceeds 75%.

---

## Customization
- **Threshold**: Update the `threshold` variable in `monitor_memory.sh` to set a custom memory usage limit.
- **Log File**: Change the `output_file` variable in `monitor_memory.sh` to specify a different log file.

---

## Sample Output
### Log File (`mem_report.tsv`)
```
08:00:01 PM 12/31/24	Memory Used % = 72%
08:00:02 PM 12/31/24	Memory Used % = 75%
```

### Console Alert
```
Security Alarm for memory
Email sent successfully!
SMS sent successfully!
```

---

## Troubleshooting
- **Email Not Sent**: Check SMTP credentials and server configuration.
- **SMS Not Sent**: Verify Twilio credentials and sufficient balance.
- **Command Not Found**: Ensure required tools (e.g., `xclip`) are installed.

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests for enhancements or bug fixes.

---

## License
This project is licensed under the [MIT License](LICENSE).

