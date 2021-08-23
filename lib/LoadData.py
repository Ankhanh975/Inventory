import yaml
import traceback
import sys
import json

def LoadYaml(filename):
    stream = open(filename, 'r')
    try:
        dictionary = yaml.load(stream, Loader=yaml.FullLoader)
        return dictionary
    except yaml.parser.ParserError:  # , yaml.scanner.ScannerError, yaml.YAMLError:
        try:
            exc_info = sys.exc_info()
        finally:
            traceback.print_exception(*exc_info)
            del exc_info
        print("Your input filename is in wrong format")
        return None


def JsonToTxt(data):
    return json.dumps(data, indent=4, sort_keys=True)

def lower_dict(data):
    # Lower all string in tag name for easier use
    if isinstance(data, dict):
        for key in list(data.keys()):
            if key.islower():
                lower_dict(data[key])
            else:
                key_lower = key.lower()
                data[key_lower] = data[key]
                del data[key]
                lower_dict(data[key_lower])

    elif isinstance(data, list):
        for item in data:
            lower_dict(item)


if __name__ == '__main__':
    data = LoadFile()
    lower_dict(data)
    print(KeyboardInUse(data, False))
