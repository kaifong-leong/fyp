# Define possible values for each rule
POSSIBLE_TLS_VERSIONS = ("SSL 2.0", "SSL 3.0", "TLS 1.0", "TLS 1.1", "TLS 1.2", "TLS 1.3")
POSSIBLE_CERTIFICATE_TYPES = ("ecdsa", "dsa", "rsa", "ecdh", "dh")

# Categories for each rule
CATEGORIES = ["shall", "should", "should_not", "shall_not"]

# Mapping for subrule categories to human-readable labels
WORD_MAPPING = {
    "shall": "MANDATORY",
    "should": "RECOMMENDED",
    "should_not": "CAUTIONARY",
    "shall_not": "PROHIBITED"
}

# Rules for policy definitions
RULES = [
    # Rule 1 for checking TLS versions
    {
        "rule_name": "TLS VERSION FOR CONNECTION",
        "rule_code": "R01",
        "description": "Checking the TLS Version Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "TLS_CONNECTION_VERSION",
        "possible_values": POSSIBLE_TLS_VERSIONS,
        "violation_data": {
            "HIGH": {
                "title": "Outdated and Insecure Protocols",
                "description": "SSL v2 and SSL v3 are deprecated and considered highly insecure due to numerous vulnerabilities, including lack of proper encryption and susceptibility to attacks like POODLE. Connections using these protocols risk exposing sensitive data and enabling unauthorized access."
            },
            "MEDIUM": {
                "title": "Legacy Protocols with Weak Security",
                "description": "TLS v1.0 and TLS v1.1 are outdated and no longer considered secure by modern standards. These protocols lack support for strong encryption algorithms and are vulnerable to attacks such as BEAST and downgrade attacks. Migration to TLS v1.2 or higher is strongly recommended."
            },
            "LOW": {
                "title": "Improved but Aging Protocol",
                "description": "While TLS v1.2 is widely used and more secure than older protocols, it lacks the advanced security features of TLS v1.3, such as faster handshakes and stronger default cipher suites. For enhanced security, upgrading to TLS v1.3 is recommended where possible."
            }
        },
        "consequence": "Non-compliance with secure TLS version requirements exposes connections to potential interception, data breaches, and unauthorized access due to known vulnerabilities in outdated protocols.",
        "explanation": "Older TLS versions (SSL v2/v3, TLS 1.0/1.1) lack adequate security measures and are vulnerable to attacks such as POODLE, BEAST, and downgrade attacks, putting encrypted communications at significant risk.",
        "remediation": "Upgrade all systems to support TLS v1.2 or higher, with a preference for TLS v1.3, and disable all outdated protocols to ensure secure and compliant communication."
    },
    # Rule 2 for checking certificate types
    {
        "rule_name": "CERTIFICATE TYPES",
        "rule_code": "R02",
        "description": "Checking the Certificate Types Used for the Connection",
        "connection_type": "TLS_CONNECTION",
        "connection_field": "CERTIFICATE_TYPES",
        "possible_values": POSSIBLE_CERTIFICATE_TYPES,
        "violation_data": {
            "HIGH": {
                "title": "Placeholder for certificate types violation data HIGH title",
                "description": "Placeholder for certificate types violation data HIGH description"
            },
            "MEDIUM": {
                "title": "Placeholder for certificate types violation data MEDIUM title",
                "description": "Placeholder for certificate types violation data MEDIUM description"
            },
            "LOW": {
                "title": "Placeholder for certificate types violation data LOW title",
                "description": "Placeholder for certificate types violation data LOW description"
            }
        },
        "consequence": "Placeholder for certificate types consequence",
        "explanation": "Placeholder for certificate types explanation",
        "remediation": "Placeholder for certificate types remediation"
    }
]