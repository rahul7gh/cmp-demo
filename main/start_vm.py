import argparse
import json
parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--ipaddress", type=str, help="ipaddress")
parser.add_argument("--comments", type=str, help="comments")
parser.add_argument("--instance_spec_vars", type=str, help="instance_spec_vars")

loaded_data=json.loads(args.instance_spec_vars)

args = parser.parse_args()
output={"ipaddress":args.ipaddress,"status":"ON","comments":args.comments,"instance_spec_vars":loaded_data}
print(json.dumps({"output":output}))


#python3 test.py --ipaddress=10.25.10.20 --machine_name=YOSH
