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

## "volume_total.csv"
## Function to oopen a file on your local computer with the argument being the file path.
## A default argument of open is mode=r to open the contents of a file with only permission
## to read the file, not write to it or perfomr a different operation. 
## EACH row in our CSV will become a list of strings, with single-quotes around each value.
def read_file():
    # Empty dictionary to count distinct occurences
    d = dict()
    count_of_rides = 0
    case_type = 1
    case_channel = 5

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

            count_of_rides += 1

    for key in list(d.keys()):
        print(key, ':', d[key])

    print(count_of_rides)


def main():
    read_file()


if __name__ == "__main__":
    main()