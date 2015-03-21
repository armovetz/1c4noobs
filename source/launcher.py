import os
import booker
import csv_settings
import ambience
from ambience import *

print "[launcher] Start "

abs_path_to_tables_dir = r'''C:\RearPatio\1c4noobs\csv_tables'''

table_files_list = [     \
"Adler.csv" ]
#"September.csv",    \
#"October.csv",      \
#"November.csv",     \
#"December.csv",     \
#"January.csv",      \
#"February.csv",     \
#"March.csv"
#]

table_files_paths = []
for table_file in table_files_list:
    table_files_paths.append(os.path.join(abs_path_to_tables_dir, table_file))

#table_files_names_list = [  \
#os.path.join(abs_path_to_tables_dir, "January_utf8.csv") \
#]
#os.path.join(abs_path_to_tables_dir, "February.csv")



my_booker = booker.Booker(table_files_paths, "")

print "__[DEBUG] tables list:"
for table in my_booker.csv_files:
    print "    " + table

print "___[DEBUG] Rejected lines "
for line in my_booker._rejected_lines:
    print line

print "__[DEBUG] rejected lines    = ", len(my_booker._rejected_lines    )
print "__[DEBUG] skipped lines     = ", len(my_booker._skipped_lines     )
print " "
print "__[DEBUG] parsed payments   = ", len(my_booker._parsed_payments   )
print " "
print "__[DEBUG] accepted payments = ", len(my_booker._accepted_payments )
print "__[DEBUG] rejected payments = ", len(my_booker._rejected_payments )
print "__[DEBUG] acc + rej paymnts = ", len(my_booker._accepted_payments ) + len(my_booker._rejected_payments )

#my_booker.printPaymentsTotal()
print "Purposes:"
for purp in AMB_PURPOSES:
    print "-- ", purp, ": ", my_booker.sumPaymentsOnPurpose(purp)

print "Payers:"
for payer in AMB_PAYERS:
    print "-- ", payer, ": ", my_booker.sumPaymentsForPayer(payer)



print "[launcher] Finish "
