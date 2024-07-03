# South East London (SEL) Long COVID Programme, 2024.

import sys, csv, re

codes = [{"code":"17496003","system":"snomedct"},{"code":"21897009","system":"snomedct"},{"code":"197480006","system":"snomedct"},{"code":"44376007","system":"snomedct"},{"code":"83482000","system":"snomedct"},{"code":"231519007","system":"snomedct"},{"code":"908651000006108","system":"snomedct"},{"code":"417620007","system":"snomedct"},{"code":"185348006","system":"snomedct"},{"code":"231507004","system":"snomedct"},{"code":"11806006","system":"snomedct"},{"code":"231508009","system":"snomedct"},{"code":"231521002","system":"snomedct"},{"code":"30693006","system":"snomedct"},{"code":"191983006","system":"snomedct"},{"code":"21897009","system":"snomedct"},{"code":"191708009","system":"snomedct"},{"code":"191709001","system":"snomedct"},{"code":"191728008","system":"snomedct"},{"code":"102912007","system":"snomedct"},{"code":"1037391000000102","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
