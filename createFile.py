import pathlib
import json

#Functions
def make_File(in_file):
    out_file = open("amz.json", "w")

    #json.dump(in_file.split("~"), out_file, indent = 6)
    edi_lines = []
    lines = in_file.split("~")
    
    for line in lines:
        segment = line.split("*")
        edi_lines.append(segment)
    
    json.dump(edi_lines, out_file, indent = 2)

    out_file.close()

#Start of Code
my_filepath = pathlib.Path(__file__).parent / "amz.edi"

with my_filepath.open("r") as fp:
     in_file = fp.read()



make_File(in_file)