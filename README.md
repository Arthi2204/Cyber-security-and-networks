# Phishing URL Detector 🔍

A simple Python tool that checks whether a URL looks like a phishing link, based on common red flags used in real phishing attacks. Built as a final year project for Computer Science (Cybersecurity).

## About

This tool doesn't use machine learning — it uses **rule-based detection**, checking each URL against known phishing patterns such as:

- Missing HTTPS (unsecured connection)
- Presence of `@` symbol (used to hide the real domain)
- Excessive URL length
- Too many subdomains/dots
- Suspicious keywords (`login`, `verify`, `secure`, `account`, etc.)
- Use of link shorteners (bit.ly, tinyurl, etc.)
- Hyphens in the domain name (common in fake lookalike domains)

Each red flag adds to a **risk score**, which is then translated into a verdict: `SAFE`, `LOW RISK`, `SUSPICIOUS`, or `HIGH RISK`.

## How It Works

1. User enters a URL
2. The program scans it against a set of rules
3. Each matched rule increases the risk score and is logged as a reason
4. A final verdict is displayed along with the reasons

## Tech Stack

- **Language:** Python 3
- **Libraries:** None (uses only Python's built-in features)

## Installation

1. Install [Python 3](https://www.python.org/downloads/) (make sure to check "Add Python to PATH" during setup)
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/phishing-url-detector.git
   cd phishing-url-detector
   ```

## Usage

Run the script:
```bash
python simple_phishing_detector.py
```

Enter any URL when prompted:
```
Enter a URL: http://paypal-verify-login-secure.tk/account

URL: http://paypal-verify-login-secure.tk/account
Risk Score: 4
Verdict: SUSPICIOUS
Reasons:
  - Does not use HTTPS (secure connection)
  - Contains suspicious keyword: 'login'
  - Domain contains a hyphen (common in fake domains)
```

Type `quit` to exit the program.

## Example Test URLs

| URL | Expected Result |
|---|---|
| `https://www.google.com` | SAFE |
| `http://paypal-verify-login.tk/secure` | HIGH RISK |
| `http://bit.ly/free-prize-claim-now` | SUSPICIOUS |

## Future Scope

- Add machine learning-based classification for higher accuracy
- Check domain age and WHOIS information
- Verify SSL certificate validity
- Build a web interface using Flask
- Integrate with a browser extension for real-time protection

## Author

Your Name
Final Year Project — Computer Science Engineering

## License

This project is open source and available for educational use.
