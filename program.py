import json
from policy_data import WORD_MAPPING, RULES, CATEGORIES  # Import data from data file

def main():
    name_of_policy = input("Enter Name of Policy: ")
    description_of_policy = input("Enter Description of Policy: ")

    r_list = []
    sr_list = []
    srv_list = []
    pr_sr_list = []

    next_index = 1 # Global index for SR and SRV codes

    for rule in RULES:
        define_rule = input(f"Would you like to define {rule['rule_name']}? (yes/no): ").strip().lower()
        if define_rule == "yes":
            if rule['special_handling'] == "yes":
                pass
            else:
                rule_sr_list, rule_srv_list, rule_pr_sr_list, next_index = handle_rule(
                    rule_name=rule["rule_name"],
                    rule_code=rule["rule_code"],
                    description=rule["description"],
                    connection_type=rule["connection_type"],
                    connection_field=rule["connection_field"],
                    possible_values=rule["possible_values"],
                    word_mapping=WORD_MAPPING,
                    categories=CATEGORIES,
                    starting_index=next_index
                )
                r_list.append(rule)
                sr_list.extend(rule_sr_list)
                srv_list.extend(rule_srv_list)
                pr_sr_list.append({"rule_code": rule["rule_code"], "sub_rules": rule_pr_sr_list, "violation_data": rule["violation_data"], "consequence": rule["consequence"], "explanation": rule["explanation"], "remediation": rule["remediation"]})

    output = {
        "name": name_of_policy,
        "description": description_of_policy,
        "rules": [
            {
                "name": rule["rule_name"],
                "code": rule["rule_code"],
                "description": rule["description"],
                "connection_type": rule["connection_type"],
                "connection_field": rule["connection_field"]
            } for rule in r_list
        ],
        "policy_rules": [
            {
                "code": f"PR{index:02}",
                "rule": pr_sr["rule_code"],
                "sub_rules": pr_sr["sub_rules"],
                "violation_data": pr_sr["violation_data"], 
                "consequence": pr_sr["consequence"],
                "explanation": pr_sr["explanation"],
                "remediation": pr_sr["remediation"]
            } for index, pr_sr in enumerate(pr_sr_list, start=1)
        ],
        "sub_rules": sr_list,
        "sub_rule_values": srv_list
    }
    
    # Remove None entries in lists, for now it does nothing since I do not introduce None
    output["rules"] = [rule for rule in output["rules"] if rule is not None]
    output["policy_rules"] = [policy_rule for policy_rule in output["policy_rules"] if policy_rule is not None]

    with open("output.json", "w") as json_file:
        json.dump(output, json_file, indent=4)


def handle_rule(rule_name, rule_code, description, connection_type, connection_field, possible_values, word_mapping, categories, starting_index):
    """
    Handles a single rule definition process.

    Parameters:
    - rule_name: Name of the rule.
    - rule_code: Code for the rule.
    - description: Description of the rule.
    - connection_type: Type of connection for the rule.
    - connection_field: Field to check for the rule.
    - possible_values: Tuple of possible values for this rule.
    - word_mapping: Dictionary mapping categories to human-readable labels.
    - categories: Categories defined in data file, generates category_values dynamically.
    - starting_index: The index to start numbering for SR and SRV codes.

    Returns:
    - sr_list: List of sub-rules for this rule.
    - srv_list: List of sub-rule values for this rule.
    - pr_sr_list: List of mappings from this policy rule to the subrules in it.
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
    category_values = {category: [] for category in categories}

    print(f"Here are the values to be assigned for this rule: {', '.join(possible_values_list)}\n"
          f"Please copy and paste the values in each of the categories you desire, separated by commas.\n"
          f"The 4 categories are mandatory, recommended, cautionary, and prohibited. Enter 'NA' if the category is not to be used.")
    for key in category_values.keys():
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
    for key, value in category_values.items():
        if not value:  # Skip categories with empty values
            continue
        sr_code = f"SR{index:02}"
        label = key.upper()
        sub_rule_values = [f"SRV{index:02}"]
        srv_code = f"SRV{index:02}"
        srv = value
        sr_list.append({"code": sr_code, "label": label, "sub_rule_values": sub_rule_values, "rule": rule_code})
        srv_list.append({"code": srv_code, "connection_field": connection_field, "value": srv})
        pr_sr_list.append(sr_code)
        index += 1 

    return sr_list, srv_list, pr_sr_list, index

if __name__ == "__main__":
    main()