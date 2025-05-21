import argparse
import json
parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--ipaddress", type=str, help="ipaddress")
parser.add_argument("--machine_name", type=int, help="machine_name")

args = parser.parse_args()
output={"ipaddress":parser.ipaddress,"machine_name":parser.machine_name,"cpu":"2GB","memory":"16384MB","disk":"131072MB"}
print(json.dumps({"output":output}))
