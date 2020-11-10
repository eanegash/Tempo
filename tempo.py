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
#########

import csv
from collections import Counter
from datetime import datetime, timedelta

## "volume_total.csv"
## Function to oopen a file on your local computer with the argument being the file path.
## A default argument of open is mode=r to open the contents of a file with only permission
## to read the file, not write to it or perfomr a different operation. 
## EACH row in our CSV will become a list of strings, with single-quotes around each value.
def read_file():
    # Empty dictionary to count distinct occurences
    d = dict()
    e_d = dict()
    t_issue_sub = dict()

    count_of_rides = 0
    case_type = 1
    case_channel = 5
    tech_issue_subtype = 2 

    #Created date:0, Case Type:1, Subtype:2, Reason:3, Customer reply count:4, Source:5, Ticket ID:6, Agent name:7, Subject:8

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


            #
            if row[case_type] == "Technical Issues":
                if row[tech_issue_subtype] in t_issue_sub:
                    t_issue_sub[row]


            count_of_rides += 1

    ticket_analysis(d, count_of_rides, e_d)

##
## Ticket Analysis 
def ticket_analysis(dic_ticket, count_of_rides, channel_dict):

    print('--------------------------------------')
    print('Case Type:')
    for key in list(dic_ticket.keys()):
        print('|    ', key, ':', dic_ticket[key])
    print('')

    print('--------------------------------------')
    print('Case Channel')
    for key in list(channel_dict.keys()):
        print('|    ', key, ':', channel_dict[key])
    print('')
     
    print('--------------------------------------')
    print('Top 3 Technical Issue Types and Reasons')
    k = Counter(channel_dict)
    # Finding 3 Highes Values
    high = k.most_common(3)
    for i in high:
        print(i[0], ':', i[1])    
    
    print('')
    print('Total:', count_of_rides)


def main():
    read_file()


if __name__ == "__main__":
    main()