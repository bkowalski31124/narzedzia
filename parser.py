import sys

def parse_arguments():
    if len(sys.argv) != 3:
        print("Poprawne użycie: plik.exe ścieżka.x ścieżka.y")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    print(f"Plik wejściowy: {input_file}")
    print(f"Plik wyjściowy: {output_file}")