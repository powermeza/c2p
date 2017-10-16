import csv, sys, getopt

input_file =  "."
output_file = "."
errors = 0
lines_converted = 0
opts = []
args = []

print ("")
print ("|-----------------[ c2p converter by Juan Meza ]-----------------|")
print ("|                                                                |")

if len(sys.argv) > 5 or len(sys.argv) < 1 or len(sys.argv) < 4 or len(sys.argv) < 3 or len(sys.argv) < 2 :
    print ("|     Error: arguments needed, use:                              |")
    print ("|             c2p.py -i <inputfile> -o <outputfile>              |")
    print ("|                                                                |")
    print ("|----------------------------------------------------------------|")
    sys.exit(2)

try:
    opts, args = getopt.getopt(sys.argv[1:],"h:i:o:")
except getopt.GetoptError:
    print ("|     Use arguments                                              |")
    print ("|             c2p.py -i <inputfile> -o <outputfile>              |")
    print ("|                                                                |")
    print ("|----------------------------------------------------------------|")
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print ("|     Use arguments                                              |")
        print ("|             c2p.py -i <inputfile> -o <outputfile>              |")
        print ("|                                                                |")
        print ("|----------------------------------------------------------------|")
        sys.exit()
    elif opt == "-i":
        input_file = arg
    elif opt == "-o":
        output_file = arg

if input_file == "." or output_file == ".":
    print ("|     Use arguments                                              |")
    print ("|             c2p.py -i <inputfile> -o <outputfile>              |")
    print ("|                                                                |")
    print ("|----------------------------------------------------------------|")
    sys.exit()

print ("|    Input file:      ", input_file)
print ("|    Output file:     ", output_file)

from time import gmtime, strftime
print ("|    Start:           ", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

#input file
f_input = open(input_file)
reader = csv.DictReader(f_input, delimiter=',')

#Output file
f_out = open(output_file,'w')
writer = csv.DictWriter(f_out, delimiter='|',fieldnames=reader.fieldnames)
writer.writeheader()

for line in reader:
    mod_line_i = line["Note Text"]
    mod_line_o = ""
    #    mod_line.replace(chr(10),"%")
    for c in mod_line_i:
        if c == chr(10) or c == chr(124):
            mod_line_o = mod_line_o + " "
        else:
            mod_line_o = mod_line_o + c
    line["Note Text"] = mod_line_o
    writer.writerow(line)

    lines_converted = lines_converted + 1

f_input.close()
f_out.close()

from time import gmtime, strftime
print ("|    End:             ", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print ("|    Lines processed: ", lines_converted)
print ("|    Errors:          ", errors)
print ("|                                                                |")
print ("|----------------------------------------------------------------|")
