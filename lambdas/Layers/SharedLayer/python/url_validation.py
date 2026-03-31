"""
URL and domain validation utilities for SSRF prevention.

Provides allowlist-based validation for meeting URLs and email domains
to prevent Server-Side Request Forgery attacks.
"""

import ipaddress
import re
import socket
from urllib.parse import urlparse

# Allowed meeting platform domains (exact match on root domain)
ALLOWED_MEETING_DOMAINS = {
    "meet.google.com",
    "zoom.us",
    "us02web.zoom.us",
    "us04web.zoom.us",
    "us05web.zoom.us",
    "us06web.zoom.us",
    "teams.microsoft.com",
    "teams.live.com",
    "webex.com",
    "meetingsamer.webex.com",
    "meetingsemea.webex.com",
    "meetingsapac.webex.com",
    "chime.aws",
    "app.chime.aws",
    "gotomeeting.com",
    "global.gotomeeting.com",
    "whereby.com",
    "app.livestorm.co",
}

# Patterns for zoom subdomains (org-specific vanity URLs)
ALLOWED_DOMAIN_PATTERNS = [
    re.compile(r"^[a-zA-Z0-9-]+\.zoom\.us$"),
    re.compile(r"^[a-zA-Z0-9-]+\.webex\.com$"),
    re.compile(r"^[a-zA-Z0-9-]+\.chime\.aws$"),
]


def _is_private_ip(hostname: str) -> bool:
    """Check if a hostname resolves to a private/reserved IP address."""
    try:
        addr_infos = socket.getaddrinfo(hostname, None)
        for family, _, _, _, sockaddr in addr_infos:
            ip = ipaddress.ip_address(sockaddr[0])
            if (
                ip.is_private
                or ip.is_loopback
                or ip.is_link_local
                or ip.is_reserved
                or ip.is_multicast
            ):
                return True
    except (socket.gaierror, ValueError, OSError):
        # DNS resolution failure — treat as unsafe
        return True
    return False


def validate_meeting_link(url: str) -> str | None:
    """
    Validate a meeting link against the allowlist of known platforms.

    Args:
        url: The meeting URL to validate.

    Returns:
        None if valid, or an error message string if invalid.
    """
    if not url or not isinstance(url, str):
        return "Meeting link is required"

    url = url.strip()

    parsed = urlparse(url)

    # Must be HTTPS
    if parsed.scheme != "https":
        return "Meeting link must use HTTPS"

    hostname = parsed.hostname
    if not hostname:
        return "Invalid meeting link URL"

    hostname = hostname.lower()

    # Check exact domain match
    if hostname in ALLOWED_MEETING_DOMAINS:
        return None

    # Check pattern match (vanity subdomains)
    for pattern in ALLOWED_DOMAIN_PATTERNS:
        if pattern.match(hostname):
            return None

    return (
        "Unsupported meeting platform. "
        "Supported: Google Meet, Zoom, Microsoft Teams, Webex, Amazon Chime, "
        "GoToMeeting, Whereby, Livestorm"
    )


def validate_email_domain(email: str) -> str | None:
    """
    Validate that an email domain is not targeting internal/private resources.

    Checks that the domain portion of the email does not resolve to
    private, loopback, link-local, or reserved IP addresses.

    Args:
        email: The email address to validate.

    Returns:
        None if safe, or an error message string if the domain is unsafe.
    """
    if not email or "@" not in email:
        return "Invalid email address"

    domain = email.split("@")[-1].lower().strip()

    if not domain or "." not in domain:
        return "Invalid email domain"

    # Block obviously dangerous domains
    if domain in ("localhost", "localhost.localdomain"):
        return "Invalid email domain"

    # Reject IP-address domains (user@[127.0.0.1] or user@169.254.169.254)
    ip_match = re.match(r"^\[?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]?$", domain)
    if ip_match:
        return "IP address domains are not allowed"

    # Resolve domain and check for private IPs
    if _is_private_ip(domain):
        return f"Email domain '{domain}' resolves to a private or reserved address"

    return None
