# South East London (SEL) Long COVID Programme, 2024.

import sys, csv, re

codes = [{"code":"191970005","system":"snomedct"},{"code":"275472008","system":"snomedct"},{"code":"280943007","system":"snomedct"},{"code":"231517009","system":"snomedct"},{"code":"231517009","system":"snomedct"},{"code":"191956005","system":"snomedct"},{"code":"231517009","system":"snomedct"},{"code":"231517009","system":"snomedct"},{"code":"191977008","system":"snomedct"},{"code":"191966002","system":"snomedct"},{"code":"31297008","system":"snomedct"},{"code":"191973007","system":"snomedct"},{"code":"191975000","system":"snomedct"},{"code":"71787009","system":"snomedct"},{"code":"191977008","system":"snomedct"},{"code":"191953002","system":"snomedct"},{"code":"191956005","system":"snomedct"},{"code":"191957001","system":"snomedct"},{"code":"191965003","system":"snomedct"},{"code":"191966002","system":"snomedct"},{"code":"238967004","system":"snomedct"},{"code":"30693006","system":"snomedct"},{"code":"191981008","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["psychogenic-anxiety-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["psychogenic-anxiety-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["psychogenic-anxiety-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
