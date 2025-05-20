import argparse

parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--argument1", type=str, help="Argument 1")
parser.add_argument("--argument2", type=int, help="Argument 2")

args = parser.parse_args()

print("Received parameters:")
print(f"Arg1: {args.argument1}")
print(f"Arg2: {args.argument2}")
