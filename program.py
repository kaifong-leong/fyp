import json

POSSIBLE_TLS_VERSIONS = ("SSL 2.0", "SSL 3.0", "TLS 1.0", "TLS 1.1", "TLS 1.2", "TLS 1.3")
POSSIBLE_CERTIFICATE_TYPES = ("ecdsa", "dsa", "rsa", "ecdh", "dh")
word_mapping = {
    "shall": "MANDATORY",
    "should": "RECOMMENDED",
    "should_not": "CAUTIONARY",
    "shall_not": "PROHIBITED"
}

def main():
    name_of_policy = input("Enter Name of Policy: ")
    description_of_policy = input("Enter Description of Policy: ")

    sr_list = []
    srv_list = []
    pr_sr_list = []
    pr_sr_list_2 = []

    next_index = 1 # Global index for SR and SRV codes
    
    # Rule 1: TLS VERSION FOR CONNECTION
    define_rule_1 = input("Would you like to define Rule 1 (TLS VERSION FOR CONNECTION)? (yes/no): ").strip().lower()
    if define_rule_1 == "yes":
        rule_1_sr_list, rule_1_srv_list, rule_1_pr_sr_list, next_index = handle_rule(
            rule_name="TLS VERSION FOR CONNECTION",
            rule_code="R01",
            description="Checking the TLS Version Used for the Connection",
            connection_type = "TLS_CONNECTION",
            connection_field="TLS_CONNECTION_VERSION",
            possible_values=POSSIBLE_TLS_VERSIONS,
            word_mapping=word_mapping,
            starting_index=next_index
        )
        sr_list.extend(rule_1_sr_list)
        srv_list.extend(rule_1_srv_list)
        pr_sr_list.extend(rule_1_pr_sr_list)
    
    # Rule 2: CERTIFICATE TYPES
    define_rule_2 = input("Would you like to define Rule 2 (CERTIFICATE TYPES)? (yes/no): ").strip().lower()
    if define_rule_2 == "yes":
        rule_2_sr_list, rule_2_srv_list, rule_2_pr_sr_list, next_index = handle_rule(
            rule_name="CERTIFICATE TYPES",
            rule_code="R02",
            description="Checking the Certificate Types Used for the Connection",
            connection_type="TLS_CONNECTION",
            connection_field="CERTIFICATE_TYPES",
            possible_values=POSSIBLE_CERTIFICATE_TYPES,
            word_mapping=word_mapping,
            starting_index=next_index
        )
        sr_list.extend(rule_2_sr_list)
        srv_list.extend(rule_2_srv_list)
        pr_sr_list_2.extend(rule_2_pr_sr_list)

    output = {
        "name": name_of_policy,
        "description": description_of_policy,
        "rules": [
            {
                "name": "TLS VERSION FOR CONNECTION",
                "code": "R01",
                "description": "Checking the TLS Version Used for the Connection",
                "connection_type": "TLS_CONNECTION",
                "connection_field": "TLS_CONNECTION_VERSION"
            } if define_rule_1 == "yes" else None,
            {
                "name": "CERTIFICATE TYPES",
                "code": "R02",
                "description": "Checking the Certificate Types Used for the Connection",
                "connection_type": "TLS_CONNECTION",
                "connection_field": "CERTIFICATE_TYPES"
            } if define_rule_2 == "yes" else None
        ],
        "policy_rules": [
            {
                "code": "PR01",
                "rule": "R01",
                "sub_rules": pr_sr_list,
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
            } if define_rule_1 == "yes" else None,
            {
                "code": "PR02",
                "rule": "R02",
                "sub_rules": pr_sr_list_2,
                "violation_data": {
                    "HIGH": {
                        "title": "-",
                        "description": "-"
                    },
                    "MEDIUM": {
                        "title": "-",
                        "description": "-"
                    },
                    "LOW": {
                        "title": "-",
                        "description": "-"
                    }
                },
                "consequence": "-",
                "explanation": "-",
                "remediation": "-"
            } if define_rule_2 == "yes" else None
        ],
        "sub_rules": sr_list,
        "sub_rule_values": srv_list
    }
    
    # Remove None entries in lists
    output["rules"] = [rule for rule in output["rules"] if rule is not None]
    output["policy_rules"] = [policy_rule for policy_rule in output["policy_rules"] if policy_rule is not None]

    with open("output.json", "w") as json_file:
        json.dump(output, json_file, indent=4)


def handle_rule(rule_name, rule_code, description, connection_type, connection_field, possible_values, word_mapping, starting_index):
    """
    Handles a single rule definition process.

    Parameters:
    - rule_name: Name of the rule.
    - rule_code: Code for the rule.
    - description: Description of the rule.
    - connection_type: Type of connection for the rule.
    - connection_field: Field to check for the rule.
    - possible_values: Tuple of possible values for this rule.
    - word_mapping: Dictionary mapping shall/should/shall_not/should_not to human-readable labels.
    - starting_index: The index to start numbering for SR and SRV codes.

    Returns:
    - sr_list: List of sub-rules for this rule.
    - srv_list: List of sub-rule values for this rule.
    - pr_sr_list: List of sub-rules for this policy rule?
    - next_index: The next available index after processing this rule.
    """
    print(f"""
    Defining Rule
    -------------
    Name: {rule_name}
    Description: {description}
    Connection Type: {connection_type}
    Connection Field: {connection_field}
    -------------------------------------------------------------
    """)
    possible_values_list = list(possible_values)
    category_values = {
        "shall": [],
        "should": [],
        "should_not": [],
        "shall_not": []
    }

    print(f"Here are the values to be assigned for this rule: {', '.join(possible_values_list)}\n"
          f"Please copy and paste the values in each of the categories you desire, separated by commas."
          f"The 4 categories are mandatory, recommended, cautionary, and prohibited. Enter 'NA' if the category is not to be used.")
    for key, value in category_values.items():
        user_key = word_mapping.get(key, "UNKNOWN")  # Get user-friendly key
        user_input = input(f"{user_key}:")  # Get user input
        if not user_input or user_input.lower() == "na":  # Check if the input is "NA"
            continue  # Skip processing this category if "NA" is entered
        new_elements = [item.strip() for item in user_input.split(",") if item.strip()]  # Clean input
        category_values[key].extend(new_elements)  # Add valid input to the dictionary

    sr_list = []
    srv_list = []
    pr_sr_list = []

    index = starting_index
    for key, value in category_values.items(): #TODO start=1
        if not value:  # Skip categories with empty values
            continue
        sr_code = f"SR{index:02}"
        label = key.upper()
        sub_rule_values = [f"SRV{index:02}"]
        srv_code = f"SRV{index:02}"
        srv = value
        sr_list.append({"code": sr_code, "label": label, "sub_rule_values": sub_rule_values, "rule": rule_code})
        srv_list.append({"code": srv_code, "connection_field": connection_field, "value": srv})
        pr_sr_list.append(f"SR{index:02}")
        index += 1 

    return sr_list, srv_list, pr_sr_list, index

if __name__ == "__main__":
    main()