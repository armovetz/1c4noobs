#import csv_settings
import csv_settings 
from csv_settings import *
import ambience
from ambience import *
import payment


class Booker:

    def __init__(self, csv_files_list, csv_settings_file):
        self.csv_files = csv_files_list
        
        self._rejected_lines    = []
        self._skipped_lines     = []

        self._parsed_payments   = []
        
        self._accepted_payments = []
        self._rejected_payments = []

        self._parseFiles()
        self.check_code = self._runChecks()

        if self.check_code != []:
            print "[CRITICAL] Booker initialized with errors!"

    def _addPayment(self, csv_line):

        fields = csv_line.split(CSV_DLMTR)
        #print "__[DEBUG]", fields
        if len(fields) != CSV_FIELDS_NUMB:
            print "Len(fields) = ", len(fields)
            print "Fields:"
            print fields
            raise Exception("[GAG Exception] Wrong number of fields")
        
        # set order of fields as expected by Payments constructor
        payment_fields = ["", "", "", 0, "", ""]
        payment_fields[0] = fields[CSV_F_TITLE      ]
        payment_fields[1] = fields[CSV_F_DATE       ]
        payment_fields[2] = fields[CSV_F_PURPOSE    ]
        payment_fields[3] = int(fields[CSV_F_PRICE ])
        payment_fields[4] = fields[CSV_F_PAYER      ]
        payment_fields[5] = (fields[CSV_F_COMMENT    ])[:-len(CSV_EOL)] # cut off EOL symbol
        
        # if all checks passed - add payment fields finally
        p = payment.Payment(payment_fields)
        self._parsed_payments.append(p)

        
    def _parseFiles(self):
        csv_lines = []
        
        # read csv lines from files in <files_list>
        for file_name in self.csv_files:
            payments_file = open(file_name, 'r')
            for line in payments_file:
                csv_lines.append(line)
            payments_file.close()
        
        # run through csv lines and parse them as payment
        for line in csv_lines:
            if line == CSV_EMPTY_LINE:
                continue        # skip empty csv line case
            if line in CSV_SKIP_LINES:      
                self._skipped_lines.append(line) # save skipped csv lines
                continue        
            if line.find(CSV_DLMTR) == -1:
                self._rejected_lines.append(line)
                continue
                #raise Exception("[GAG Exception] No CSV delimiter in line")

            try:
                self._addPayment(line)
            except Exception, e:
                #print Exception
                print e
                self._rejected_lines.append(line)


    def _checkPayment(self, payment):
        """ 
        
        """
        if (payment.title   == "") and (CSV_payment_must_have_title     == True):
            return -11
        if (payment.date    == "") and (CSV_payment_must_have_date      == True):
            return -12
        if (payment.purpose == "") and (CSV_payment_must_have_purpose   == True):
            return -13
        if (payment.payer   == "") and (CSV_payment_must_have_payer     == True):
            return -14
        if (payment.comment == "") and (CSV_payment_must_have_comment   == True):
            return -15
        return 0
    
    def _runChecks(self):
        err_codes = []
        if (not CSV_allow_rejected_lines) and (self._rejected_lines != []):
            err_codes.append(-1)
            print "[CRITICAL] Rejected lines not allowed but present."

        if (not CSV_allow_skipped_lines) and (self._skipped_lines != []):
            err_codes.append(-2)
            print "[CRITICAL] Skipped lines not allowed but present."

        for p in self._parsed_payments:
            if self._checkPayment(p) == 0:
                self._accepted_payments.append(p)
            else:
                self._rejected_payments.append(p)
                
        if (not CSV_allow_rejected_payments) and (self._rejected_payments != []):
            err_codes.append(-3)
            print "[CRITICAL] Rejected payments not allowed but present."

        if (not CSV_allow_no_acc_payments) and (self._accepted_payments == []):
            err_codes.append(-4)
            print "[CRITICAL] Accepted payments must present but not found."
        
        return err_codes

# method to print summary on rejected
        
# methods to filter payments
    def getPaymentsByPayer(self, payer_name):
        """ Returns loaded payments with payer <payer_name> """
        return payment.getPaymentsByPayer(self._accepted_payments, payer_name)
            
    def getPaymentsByPurpose(self, purpose_name):
        """ Returns loaded payments with purpose <purpose_name> """
        return payment.getPaymentsByPurpose(self._accepted_payments, purpose_name)
    
# methods to sum up payments
    def sumPaymentsForPayer(self, payer_name):
        """ Sums up total price of payments by <payer_name> """
        return payment.sumPaymentsPrice(self.getPaymentsByPayer(payer_name))
    
    def sumPaymentsOnPurpose(self, purpose_name):
        """ Sums up total sum of payments on <purpose_name> """
        return payment.sumPaymentsPrice(self.getPaymentsByPurpose(purpose_name))
    
    def sumPaymentsTotal(self):
        """ Sums up price of all payments loaded in Booker """
        return payment.sumPaymentsPrice(self.payments)

# methods for fancy stats print
    def printPaymentsTotal(self):
        """ Prints all payments loaded in Booker """
        for payment in self._accepted_payments:
            payment.printPayment()
    
    def printPaymentsForPayer(self, payer_name):
        """ Prints all payments by <payer_name> """
        print "-- Payments made by [" + payer_name + "]"
        for payment in self.getPaymentsByPayer(payer_name):
            payment.printPayment()
    def printPaymentsOnPurpose(self, purpose_name):
        """ Prints all payments on <purpose_name> """
        print "-- Payments made on [" + purpose_name + "]"
        for payment in self.getPaymentsByPurpose(purpose_name):
            payment.printPayment()
    
    def printPayersOnPurpose(self, purpose_name):
        """ Prints details about each payer spent on <purpose_name> """
        print "-- Payers on [" + purpose_name + "]"
        purp_payments = self.getPaymentsByPurpose(purpose_name)

    #def printAllPayersSummary(self):
    
    
    

# end of Booker class
