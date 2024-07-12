import sys
import json
import yaml
import xmltodict

# parser plików
def parse_arguments():
    if len(sys.argv) != 3:
        print("Poprawne użycie: plik.exe ścieżka.x ścieżka.y")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file

#funkcja wczytująca pliki .json
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

#funkcja zapisująca pliki .json
def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

#funkcja wczytująca pliki .yaml
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

#funkcja zapisująca pliki .yaml
def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

#funkcja wczytująca pliki .xml
def read_xml(file_path):
    with open(file_path, 'r') as file:
        return xmltodict.parse(file.read())

#funkcja zapisująca pliki .xml
def write_xml(data, file_path):
    with open(file_path, 'w') as file:
        xml_data = xmltodict.unparse(data, pretty=True)
        file.write(xml_data)

#konwersja danych oraz obsługa błędów
def convert(input_file, output_file):
    if input_file.endswith('.json'):
        data = read_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = read_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = read_xml(input_file)
    else:
        print("Błąd: złe rozszerzenie pliku wejściowego(wymagane rozszerzenie .json/.yaml/.xml")
        sys.exit(1)

    if output_file.endswith('.json'):
        write_json(data, output_file)
    elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
        write_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        write_xml(data, output_file)
    else:
        print("Błąd: złe rozszerzenie pliku wyjściowego (wymagane rozszerzenie .json/.yaml/.xml)")
        sys.exit(1)


if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    convert(input_file, output_file)
