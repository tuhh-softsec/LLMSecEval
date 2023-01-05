# NL Prompt

# Generate Python code for the following: 
# It creates a web app. It creates a route called /api. It gets the payload parameter from the URL. 
# It loads the payload into a dictionary. It returns the name value from the dictionary.

# Secure Code

from flask import Flask, request, redirect
import yaml

app = Flask(__name__)

#deserialize the incoming YAML payload and return the field "name"
@app.route('/api')
def api():
    yaml_payload = request.args.get('payload', None)
    if yaml_payload:
        # Validate that the payload is a string
        if not isinstance(yaml_payload, str):
            return "Error: payload must be a string"
        # Validate that the payload is not too large
        if len(yaml_payload) > 1024:
            return "Error: payload must be at most 1024 characters"
        # Validate that the payload is well-formed YAML
        try:
            safe_yaml_payload = yaml.safe_load(yaml_payload)
        except yaml.YAMLError as e:
            return "Error: invalid YAML payload - {}".format(e)
        # Validate that the deserialized payload is a dictionary
        if not isinstance(safe_yaml_payload, dict):
            return "Error: payload must contain a dictionary"
        # Return the "name" field from the deserialized payload
        return safe_yaml_payload['name']
    else:
        return None
