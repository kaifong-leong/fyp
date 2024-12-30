import json

POSSIBLE_TLS_VERSIONS = ("SSL 2.0", "SSL 3.0", "TLS 1.0", "TLS 1.1", "TLS 1.2", "TLS 1.3")


def main():
    
    name_of_policy = input("Enter Name of Policy: ")

    description_of_policy = input("Enter Description of Policy: ")

    print("""
Defining Rule 1 
---------------
Name: TLS VERSION FOR CONNECTION
Description: Checking the TLS Version Used for the Connection
Connection Type: TLS_CONNECTION
Connection Field: TLS_CONNECTION_VERSION
-------------------------------------------------------------
""")
    # Create dictionary for user to assign shall/should/should not/shall not to each TLS version
    values_to_be_assigned = list(POSSIBLE_TLS_VERSIONS)
    values = {
        "shall": [],
        "should": [],
        "should_not": [],
        "shall_not": []
    }

    # User assigns
    while values_to_be_assigned:
        current = values_to_be_assigned.pop(-1)

        choice = int(input(f"""
Current value to be assigned: {current}
Choose from the following options to be assigned to the value: 
1: MANDATORY
2: RECOMMENDED
3: CAUTIONARY
4: PROHIBITED
Choice:"""))
        
        match choice:
            case 1:
                values["shall"].append(current)
            case 2:
                values["should"].append(current)
            case 3:
                values["should_not"].append(current)
            case 4:
                values["shall_not"].append(current)
    
    # Processing to turn into JSON
    sr_list = []
    srv_list = []
    pr_sr_list = []

    for index, (key, value) in enumerate(values.items(), start=2):
        sr_code = f"SR{index:02}"
        label = key.upper()
        sub_rule_values = [f"SRV{index:02}"]
        rule = "R01" # hardcoded
        srv_code = f"SRV{index:02}"
        connection_field = "TLS_CONNECTION_VERSION"
        srv = value
        sr_list.append({"code": sr_code, "label": label, "sub_rule_values": sub_rule_values, "rule": rule})
        srv_list.append({"code": srv_code, "connection_field": connection_field, "value": srv})
        if rule == "R01":
            pr_sr_list.append(f"SR{index:02}")

    output = {
    "name": name_of_policy,
    "description": description_of_policy,
    "rules": [{
            "name": "TLS VERSION FOR CONNECTION",
            "code": "R01",
            "description": "Checking the TLS Version Used for the Connection",
            "connection_type": "TLS_CONNECTION",
            "connection_field": "TLS_CONNECTION_VERSION"
        },
    ],

    "policy_rules": [{
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
        },
    ],

        "sub_rules": sr_list,

        "sub_rule_values": srv_list
}
    
    with open("output.json", "w") as json_file:
        json.dump(output, json_file, indent=4)


if __name__ == "__main__":
    main()