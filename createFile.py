from pathlib import Path
import json

p = Path('.')
l= [x for x in p.iterdir() if x.is_dir()]

# l = []
# for x in p.iterdir():
#     if x.is_dir():
#         l.append(x)

# Functions
def make_File(in_file):
    with open("amz.json", "w") as out_file:
        # edi_lines = [l.split("*") for l in in_file.split("~")]
        edi_lines = []
        lines = in_file.split("~")

        for line in lines:
            segment = line.split("*")
            edi_lines.append(segment)

        json.dump(edi_lines, out_file, indent=2)


# Start of Code
my_filepath = Path(__file__).parent / "amz.edi"

with my_filepath.open("r") as fp:
    in_file = fp.read()


make_File(in_file)
