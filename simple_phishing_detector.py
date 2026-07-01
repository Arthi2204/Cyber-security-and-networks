"""
simple_phishing_detector.py
-----------------------------
A BEGINNER-FRIENDLY phishing URL detector.

No machine learning, no extra libraries needed — just plain Python.
It works by checking a URL against a list of common "red flags" that
phishing links usually have, and gives it a risk score.

HOW TO RUN THIS FILE:
1. Make sure Python is installed (type "python --version" in your terminal
   to check).
2. Save this file as simple_phishing_detector.py
3. Open a terminal in the same folder and run:
      python simple_phishing_detector.py
4. It will ask you to type a URL, then tell you if it looks safe or risky.
"""

# ---------------------------------------------------------
# STEP 1: List of suspicious keywords often found in phishing URLs
# ---------------------------------------------------------
SUSPICIOUS_WORDS = ["login", "verify", "update", "secure", "account",
                     "banking", "confirm", "signin", "password"]

# A few known link-shortening services (phishers use these to hide the real link)
SHORTENERS = ["bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly"]


def check_url(url):
    """
    Takes a URL (as text) and checks it for common phishing red flags.
    Returns a score (higher = more suspicious) and a list of reasons.
    """
    score = 0
    reasons = []

    # Make a lowercase copy so our checks aren't case-sensitive
    url_lower = url.lower()

    # --- Check 1: Is the URL very long? ---
    # Phishing URLs are often long to hide the real destination
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    # --- Check 2: Does it use HTTPS? ---
    # Legitimate sites almost always use https, not http
    if not url_lower.startswith("https://"):
        score += 1
        reasons.append("Does not use HTTPS (secure connection)")

    # --- Check 3: Does it contain an "@" symbol? ---
    # Browsers ignore everything before "@", so phishers hide the real
    # domain after it, e.g. http://paypal.com@fakepage.com
    if "@" in url:
        score += 2
        reasons.append("Contains '@' symbol (used to hide real domain)")

    # --- Check 4: Too many dots? ---
    # Lots of dots can mean lots of fake subdomains,
    # e.g. paypal.login.verify.fakesite.com
    if url.count(".") > 4:
        score += 1
        reasons.append("Too many dots/subdomains")

    # --- Check 5: Contains a suspicious keyword? ---
    for word in SUSPICIOUS_WORDS:
        if word in url_lower:
            score += 1
            reasons.append(f"Contains suspicious keyword: '{word}'")
            break  # only count this once, even if multiple keywords match

    # --- Check 6: Uses a link shortener? ---
    for short in SHORTENERS:
        if short in url_lower:
            score += 1
            reasons.append(f"Uses a link shortener ({short})")
            break

    # --- Check 7: Has a hyphen in the domain? ---
    # e.g. paypal-secure-login.com instead of paypal.com
    if "-" in url_lower.split("/")[2] if "//" in url_lower else "-" in url_lower:
        score += 1
        reasons.append("Domain contains a hyphen (common in fake domains)")

    return score, reasons


def get_verdict(score):
    """Turns the numeric score into a simple, human-readable verdict."""
    if score == 0:
        return "SAFE"
    elif score <= 2:
        return "LOW RISK"
    elif score <= 4:
        return "SUSPICIOUS"
    else:
        return "HIGH RISK - LIKELY PHISHING"


def main():
    print("=== Simple Phishing URL Detector ===")
    print("Type a URL to check it, or type 'quit' to exit.\n")

    while True:
        url = input("Enter a URL: ").strip()

        if url.lower() == "quit":
            print("Goodbye!")
            break

        if url == "":
            print("Please enter a URL.\n")
            continue

        score, reasons = check_url(url)
        verdict = get_verdict(score)

        print(f"\nURL: {url}")
        print(f"Risk Score: {score}")
        print(f"Verdict: {verdict}")

        if reasons:
            print("Reasons:")
            for r in reasons:
                print(f"  - {r}")
        else:
            print("No red flags found.")

        print("-" * 50)


# This line means: "only run main() if this file is run directly"
# (this is standard practice in every Python program)
if __name__ == "__main__":
    main()
