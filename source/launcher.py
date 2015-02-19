import os
import booker

print "[launcher] Start "

abs_path_to_tables_dir = r'''C:\RearPatio\1c4noobs\tables'''

table_files_names_list = [  \
os.path.join(abs_path_to_tables_dir, "January.csv") \
]
#os.path.join(abs_path_to_tables_dir, "February.csv")

   

my_booker = booker.Booker(table_files_names_list, "")

my_booker.printPaymentsTotal()

print "[launcher] Finish "