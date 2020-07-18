## this is a fake SDK for providing demo 
## of notebook testing examples

import sys
import json
import jsonschema
from jsonschema import validate

class NotebookTestDemo(object):
    def __init__(self):
        pass
        
    def slow_perf_endpoint(self):        
        total = 0
        for i in range(1000):
            for j in range(1000):
                total += i * (-1) ** j

    def email_search(self, name):
        emails = {
                  "paul karayan": "paul@irregular.com"
        }

        return emails.get(name, 'No Email Found')

    def validate_json_schema(self, schema, test_json_data):
        print("Validating the input data using jsonschema:")
        for idx, item in enumerate(test_json_data):
            try:
                validate(item, schema)
                sys.stdout.write("Record #{}: OK\n".format(idx))
            except jsonschema.exceptions.ValidationError as ve:
                sys.stderr.write("Record #{}: ERROR\n".format(idx))
                sys.stderr.write(str(ve) + "\n")
