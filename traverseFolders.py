from pathlib import Path
import json

#make_json Function

def make_json(in_file, output_file_path):
    with open(output_file_path, "w") as out_file:
        #json.dump("Hello World", out_file)
        
        edi_lines = []
        lines = in_file.split("~")

        for line in lines:
            segment = line.split("*")
            edi_lines.append(segment)

        json.dump(edi_lines, out_file, indent=2)

#Start of Code
input_folder = Path(__file__).parent / "In"
output_folder = Path(__file__).parent / "Out"

for input_file_path in input_folder.iterdir():
    #print(input_file_path.stem)
    output_file_path = output_folder / (input_file_path.stem + ".json")


    with input_file_path.open("r") as fp:
        in_file = fp.read()
    make_json(in_file, output_file_path)
