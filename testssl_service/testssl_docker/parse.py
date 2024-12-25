import json

# Function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to categorize the findings based on TLS version and generate the HTML report
def generate_html_report(data):
    tls_versions = {
        "TLS 1.0": [],
        "TLS 1.1": [],
        "TLS 1.2": [],
        "TLS 1.3": []
    }
    
    for item in data:
        finding = item.get('finding', '')
        if 'TLSv1.3' in finding:
            tls_versions["TLS 1.3"].append(finding)
        elif 'TLSv1.2' in finding:
            tls_versions["TLS 1.2"].append(finding)
        elif 'TLSv1.1' in finding:
            tls_versions["TLS 1.1"].append(finding)
        elif 'TLSv1' in finding:
            tls_versions["TLS 1.0"].append(finding)

    # Generate HTML report
    html_content = "<html><head><title>Cipher Report</title></head><body>"
    html_content += "<h1>Report on Ciphers</h1>"
    
    for version, ciphers in tls_versions.items():
        html_content += f"<h2>{version}</h2><ul>"
        if ciphers:
            for cipher in ciphers:
                html_content += f"<li>{cipher}</li>"
        else:
            html_content += "<li>No ciphers found</li>"
        html_content += "</ul>"

    html_content += "</body></html>"
    
    return html_content

# Load the JSON file
data = load_json('ciphers.json')

# Generate the HTML report
html_report = generate_html_report(data)

# Save the HTML report to a file
with open("cipher_report.html", "w") as file:
    file.write(html_report)

print("Report generated as 'cipher_report.html'")

