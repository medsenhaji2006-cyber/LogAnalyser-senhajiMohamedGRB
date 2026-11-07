import re

PATTERN = re.compile(r'(\w{3})\s+(\d{1,2})\s+(\d{2}:\d{2}:\d{2}).+?:\s(.+)')
IP_PATTERN = re.compile(r'\b(\d{1,3}(?:\.\d{1,3}){3})\b')

# L'tartib mohim: l'pattern l'akhass dima 9bel l'3am
EVENT_PATTERNS = [
    ('failed_invalid_user', re.compile(r'Failed \w+ for invalid user (\S+) from (\S+)')),
    ('failed_password',     re.compile(r'Failed \w+ for (\S+) from (\S+)')),
    ('accepted',            re.compile(r'Accepted \w+ for (\S+) from (\S+)')),
    ('invalid_user',        re.compile(r'Invalid user (\S+) from (\S+)')),
]


def classify(message):
    for event_type, pattern in EVENT_PATTERNS:
        m = pattern.match(message)
        if m:
            return event_type, m.group(1), m.group(2)
    return 'other', None, None


def extract_from_row(row):
    match = PATTERN.search(row)
    if not match:
        return None

    message = match.group(4)
    event_type, user, ip = classify(message)

    if ip is None:
        ip_match = IP_PATTERN.search(message)
        ip = ip_match.group(1) if ip_match else None

    return {
        'month': match.group(1),
        'day': int(match.group(2)),
        'time': match.group(3),
        'message': message,
        'ip': ip,
        'user': user,
        'event_type': event_type,
    }