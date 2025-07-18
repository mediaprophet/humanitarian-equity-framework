import json
import uuid
from datetime import datetime

# Define the index as a list of contributions (in-memory; could load from file if needed)
contributions_index = []

# Function to add a contribution (defaults to 'pending' status)
def add_contribution(contributor_name, contributor_email, description, value, jurisdiction=None):
    claim_id = str(uuid.uuid4())
    date = datetime.now().isoformat()
    entry = {
        "claim_id": claim_id,
        "contributor": {
            "name": contributor_name,
            "email": contributor_email,
            "jurisdiction": jurisdiction
        },
        "description": description,
        "value": value,
        "date": date,
        "status": "pending"  # Default status before approval
    }
    contributions_index.append(entry)
    return entry

# Function to approve a contribution (changes status to 'approved')
def approve_contribution(claim_id):
    for entry in contributions_index:
        if entry["claim_id"] == claim_id:
            entry["status"] = "approved"
            return entry
    raise ValueError(f"Claim ID {claim_id} not found")

# Function to generate and save JSON
def generate_json(filename='contributions.json'):
    with open(filename, 'w') as f:
        json.dump(contributions_index, f, indent=4)
    return f"JSON saved to {filename}"

# Function to generate and save RDF Turtle
def generate_rdf(filename='contributions.ttl'):
    rdf_prefixes = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix schema: <http://schema.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix hef: <http://mediaprophet.github.io/humanitarian-equity-framework/ontology/contributors#> .
    """
    
    rdf_instances = ""
    for idx, entry in enumerate(contributions_index):
        contrib_id = f":Contribution{idx+1}"
        contrib_person_id = f":Contributor{idx+1}"
        jurisdiction_str = entry['contributor']['jurisdiction'] if entry['contributor']['jurisdiction'] else ""
        
        rdf_instances += f"""
{contrib_person_id} rdf:type hef:Contributor ;
    foaf:name "{entry['contributor']['name']}" ;
    foaf:mbox "{entry['contributor']['email']}" ;
    hef:jurisdiction "{jurisdiction_str}" ;
    hef:hasContribution {contrib_id} .

{contrib_id} rdf:type hef:Contribution ;
    prov:generatedAtTime "{entry['date']}" ;
    schema:description "{entry['description']}" ;
    schema:value {entry['value']} ;
    hef:status "{entry['status']}" .
"""
    
    rdf_content = rdf_prefixes + rdf_instances
    with open(filename, 'w') as f:
        f.write(rdf_content)
    return f"RDF Turtle saved to {filename}"

# Example Usage
pending_claim = add_contribution("Timothy Holborn", "timothy.holborn@gmail.com", "Initial framework definition", 1000.0, "Australia")
add_contribution("Example Contributor", "example@example.com", "RDF ontology development", 500.0)

# Approve the first claim
approve_contribution(pending_claim["claim_id"])

# Generate files
generate_json()
generate_rdf()