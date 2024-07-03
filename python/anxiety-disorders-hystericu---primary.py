# South East London (SEL) Long COVID Programme, 2024.

import sys, csv, re

codes = [{"code":"197480006","system":"snomedct"},{"code":"44376007","system":"snomedct"},{"code":"44376007","system":"snomedct"},{"code":"44376007","system":"snomedct"},{"code":"44037003","system":"snomedct"},{"code":"44037003","system":"snomedct"},{"code":"44376007","system":"snomedct"},{"code":"88902008","system":"snomedct"},{"code":"191713008","system":"snomedct"},{"code":"191714002","system":"snomedct"},{"code":"191714002","system":"snomedct"},{"code":"71802006","system":"snomedct"},{"code":"44037003","system":"snomedct"},{"code":"3586005","system":"snomedct"},{"code":"44376007","system":"snomedct"},{"code":"95439001","system":"snomedct"},{"code":"71802006","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-disorders-hystericu---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-disorders-hystericu---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-disorders-hystericu---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
