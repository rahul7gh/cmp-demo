import argparse
import json
parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--ipaddress", type=str, help="ipaddress")

args = parser.parse_args()
output={"ipaddress":args.ipaddress,"status":"OFF"}
print(json.dumps({"output":output}))


#python3 test.py --ipaddress=10.25.10.20 --machine_name=YOSH
