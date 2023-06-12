from pathlib import Path
import json

#make_JSON Function

def make_JSON(in_file, outputFilePath):
    with open(outputFilePath / "amz2.json", "w") as out_file:
        #json.dump("Hello World", out_file)
        
        edi_lines = []
        lines = in_file.split("~")

        for line in lines:
            segment = line.split("*")
            edi_lines.append(segment)

        json.dump(edi_lines, out_file, indent=2)

#Start of Code
p = Path('.')
l= [x for x in p.iterdir() if x.is_dir()]

inputFolder = l[1]
outputFolder = l[2]

inputFilePath = Path(__file__).parent / inputFolder / "amz.edi"
outputFilePath = Path(__file__).parent / outputFolder

with inputFilePath.open("r") as fp:
    in_file = fp.read()


make_JSON(in_file, outputFilePath)





# print("Input folder is: ")
# print(inputFolder)

# print("Output folder is: ")
# print(outputFolder)

# print("Input File Path is: ")
# print(inputFilePath)

# print("Output File Path is: ")
# print(outputFilePath)
