# csv settings
CSV_EOL         = "\n"      # End of line expected in csv file
CSV_DLMTR       = '\t'      # CSV delimiter symbol
CSV_FIELDS_NUMB = 7         # Number of columns in csv table
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


### empty lines and skip lines
CSV_EMPTY_LINE = (CSV_DLMTR * (CSV_FIELDS_NUMB - 1)) + CSV_EOL
CSV_SKIP_LINES = []

CSV_SKIP_LINES.append("﻿Покупки	дата	назначение	стоимость	покупатель	комментарий	\n")
CSV_SKIP_LINES.append("Покупки	дата	назначение	стоимость	покупатель	комментарий	категория	\n")


# restriction checks
CSV_allow_empty_lines       = True
CSV_allow_rejected_lines    = True
CSV_allow_skipped_lines     = True
CSV_allow_rejected_payments = False
CSV_allow_no_acc_payments   = False

CSV_payment_must_have_title   = False
CSV_payment_must_have_date    = False
CSV_payment_must_have_purpose = False
#CSV_payment_must_have_price  _ has no sense - payment modules checks it itself
CSV_payment_must_have_payer   = True
CSV_payment_must_have_comment = False

