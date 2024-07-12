import sys
import json

# parser plików 
def parse_arguments():
    if len(sys.argv) != 3:
        print("Poprawne użycie: plik.exe ścieżka.x ścieżka.y")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file

# wczytuje .json ze ścieżki + obsługa błędów z tym związana
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("Poprawnie wczytano plik")
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd: nie można odczytać pliku {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Błąd: nie znaleziono ścieżki {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        sys.exit(1)


def write_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Dane pomyślnie zapisane w {file_path}")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania pliku: {e}")
        sys.exit(1)


if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = read_json(input_file)
        print(data)
    else:
        print("Błąd: złe rozszerzenie pliku wejściowego(wymagane rozszerzenie .json)")
        sys.exit(1)

    if output_file.endswith('.json'):
        write_json(data, output_file)
    else:
        print("Błąd: złe rozszerzenie pliku wyjściowego(wymagane rozszerzenie .json)")
        sys.exit(1)