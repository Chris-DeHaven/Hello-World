import pathlib
import json

#Functions
def make_File(in_file):
    out_file = open("amz.json", "w")

    #json.dump(in_file.split("~"), out_file, indent = 6)

    lines = in_file.split("~")
    for line in lines:
         json.dump(line.split("*"), out_file)

    #lines = in_file.split("~")
    #for line in lines:
    #     segments = line.split("*")
    #     for segment in segments:
    #         json.dump(segment, out_file, indent = 4)
    out_file.close()

#Start of Code
my_filepath = pathlib.Path(__file__).parent / "amz.edi"

with my_filepath.open("r") as fp:
     in_file = fp.read()



make_File(in_file)