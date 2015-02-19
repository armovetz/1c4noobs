# csv settings
CSV_EOL         = '\n'      # End of line expected in csv file

CSV_DLMTR       = '\t'      # CSV delimiter symbol

CSV_FIELDS_NUMB = 6         # Number of columns in csv table

CSV_HEADER      = "header line"     # header line of csv file will be ignored

CSV_DATE_FORMAT = ""    # if set to empty string - date field treated as string
                        # if set as format string for datetime module - then
                        #     date time will be parsed according to its

# location of csv fields in the table
CSV_F_TITLE     = 0
CSV_F_DATE      = 1
CSV_F_PURPOSE   = 2
CSV_F_PRICE     = 3
CSV_F_PAYER     = 4
CSV_F_COMMENT   = 5