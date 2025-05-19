import argparse

parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--arg1", type=str, help="Argument 1")
parser.add_argument("--arg2", type=int, help="Argument 2")

args = parser.parse_args()

print("Received parameters:")
print(f"Arg1: {args.arg1}")
print(f"Arg2: {args.arg2}")