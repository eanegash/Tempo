#########
# Use any format(s) you feel is(are) best suited for this exercise, such at ppt, xls, doc, Google, etc. 
# As part of your responsibilities, you routinely track the technical complaint volume and trends. 
# Then recommend and execute on improvement strategies as needed. Using the data provided, please perform an analysis of the following:
# 
# Number of tickets by: 
#   Type
#   Channel
#####
# Percent of overall Technical Issues
#   Week-over-Week Percentage
#####
# Top 3 Technical Issues types and reasons
#   Average interaction count for each
#####
# What are some common trends that you can identify in the technical issue tickets?
# What are some common trends that you can identify about interactions for each technical issue (and do they vary by channel)?
# What would your plan be to address any issues with the trending data that you see?
#
# Created date:0, Case Type:1, Subtype:2, Reason:3, Customer reply count:4, Source:5, Ticket ID:6, Agent name:7, Subject:8
#########

import csv
from collections import Counter
from datetime import date

## "volume_total.csv"
## Open the contents of a file with only permission to read the file, not write to it or perfomr 
## a different operation. EACH row in our CSV will become a list of strings, with single-quotes around each value.
def read_file():
    # Empty dictionary to count distinct occurences
    d = dict()
    e_d = dict()
    t_issue_sub = dict()

    count_of_rides = 0
    create_date = 0
    case_type = 1
    case_channel = 5
    tech_issue_subtype = 2 

    count_of_tech_issues = 0
    ti_dic = dict()

    # “with” statement invokes what Python calls a “context manager” on file. Close file at end of with
    with open('volume_total.csv') as file:
        csv_reader_object = csv.reader(file)
        # Sniffer class has method has header that determines if a header exits. 
        # If the header exists we iterate pass it.
        if csv.Sniffer().has_header:
            next(csv_reader_object)
        # Iterate over each line.
        for row in csv_reader_object:
            #print("CSV row: {0}".format(row))
            # Check if the Case Type is already in dictionary.
            if row[case_type] in d:
                # Increment count of word by 1
                d[row[case_type]] = d[row[case_type]] + 1
            else:
                # Add the word to dictionary with count 1
                d[row[case_type]] = 1

            # Check if the Case Channel is already in dictionary
            # Increment channel count of word by 1
            if row[case_channel] in e_d:
                e_d[row[case_channel]] = e_d[row[case_channel]] + 1
            else:
                e_d[row[case_channel]] = 1

            # Organize Technical Issues by Subtype
            if row[case_type] == "Technical Issues":
                if row[tech_issue_subtype] in ti_dic:
                    ti_dic[row[tech_issue_subtype]] = ti_dic[row[tech_issue_subtype]] + 1
                else:
                    ti_dic[row[tech_issue_subtype]] = 1

                count_of_tech_issues += 1

            count_of_rides += 1
    # Method
    ticket_analysis(d, e_d)
    # Method
    top_three_and_precent(ti_dic, count_of_tech_issues)

    print('Total Number of Tickets:', count_of_rides)
    print('')


## Ticket Analysis : 
## Prints Number of Tickets (Type and Channel)
def ticket_analysis(dic_ticket, channel_dict):

    print('--------------------------------------')
    print('Case Type:')
    for key in list(dic_ticket.keys()):
        print('|    ', key, ':', dic_ticket[key])
    print('')

    print('--------------------------------------')
    print('Case Channel:')
    for key in list(channel_dict.keys()):
        print('|    ', key, ':', channel_dict[key])
    print('')

    print('--------------------------------------')
    # 76:395, 77:886, 56:899, 46:631
    print('Week Over Week Percentage:')
    print('Week 1 Percentage:', round((76/398)*100,2), '%')
    print('Week 2 Percentage:', round((77/886)*100,2), '%')
    print('Week 3 Percentage:', round((56/899)*100,2), '%')
    print('Week 4 Percentage:', round((46/631)*100,2), '%')
    print('')


## Print Percent of Overall Technical Issues (Week-over-Week Percentage)
## Print Top 3 Technical Issue Types and Reasons
def top_three_and_precent(dic, count):

    print('--------------------------------------')
    print('Top 3 Technical Issue Types and Reasons:')
    k = Counter(dic)
    # Finding 3 Highes Values
    high = k.most_common(3)
    for i in high:
        l = float(i[1])
        print(i[0], ':', i[1], 'Elements,',  round(float(l/count)*100,2),'%')

    print('')
    print('Technical Issues Total Count:', count)


def main():
    read_file()

if __name__ == "__main__":
    main()



