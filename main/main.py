import argparse

parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--argument1", type=str, help="Argument 1")
parser.add_argument("--argument2", type=int, help="Argument 2")

args = parser.parse_args()

print("Received parameters:")
print(f"Argument 1: {args.argument1}")
print(f"Argument 2: {args.argument2}")
