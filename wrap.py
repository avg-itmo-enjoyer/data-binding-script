import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--predicates", action="store_true")
    parser.add_argument("--fromIris",  action="store_true")
    parser.add_argument("--toIris", action="store_true")

    args = parser.parse_args()
    dirnames = {
        "predicates" : args.predicates,
        "fromIris" : args.fromIris,
        "toIris" : args.toIris,
    }

    for key, val in dirnames.items():
        if val:
            with open(f"{key}/raw.txt", "r") as raw, open(f"{key}/wrapped.txt", "w") as wrapped:
                predicates = [s.strip() for s in raw.read().strip().split(",")]
                for n, predicate in enumerate(predicates):
                    if n != len(predicates) - 1:
                        wrapped.write(f"'{predicate}',\n")
                    else:
                        wrapped.write(f"'{predicate}'")

if __name__ == "__main__":
    main()