from utils.parser import parse_icd_file
from generator import generate_derived_parameters
from utils.constants import INPUT_CSV, OUTPUT_TXT


def main():
    rows = parse_icd_file(INPUT_CSV)
    derived_lines = generate_derived_parameters(rows)

    with open(OUTPUT_TXT, 'w') as outfile:
        outfile.writelines(derived_lines)


if __name__ == "__main__":
    main()
