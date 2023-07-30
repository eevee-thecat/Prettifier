import argparse
import sys
import json
import yaml
from yaml import Loader, Dumper
from pprint import pprint


def main():
    parser = argparse.ArgumentParser(
        prog="Prettifier",
        description="Pretty-prints JSON or YAML. Pipe file into stdin.",
    )

    parser.add_argument(
        "-j", "--json", action="store_true"
    )  # option that takes a value
    parser.add_argument(
        "-y", "--yaml", action="store_true"
    )  # option that takes a value
    args = parser.parse_args()

    if args.json and args.yaml:
        print("JSON and YAML flags are mutually exclusive!")
        exit(1)

    if args.json:
        input_str = sys.stdin.read()
        j = json.loads(input_str)
        pprint(j, compact=True)
    if args.yaml:
        y = yaml.load(sys.stdin, Loader=Loader)
        print(yaml.dump(y, Dumper=Dumper))


if __name__ == "__main__":
    main()
