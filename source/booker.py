#import csv_settings
import csv_settings 
from csv_settings import *
import ambience
from ambience import *
import payment


class Booker:

    def __init__(self, csv_files_list, csv_settings_file):
        self.csv_files = csv_files_list
        self._payments = []
        
        # load settings from file <csv_settings_file> 
        # import ConfigParser
        # parser = ConfigParser.ConfigParser()
        # parser.read(csv_settings_file)
        
        import csv_settings
        
        self._loadPayments()

    def _loadPayments(self):
        csv_lines = []
        
        # read csv lines from files in <files_list>
        for file_name in self.csv_files:
            payments_file = open(file_name, 'r')
            for line in payments_file:
                csv_lines.append(line)
            payments_file.close()
        
        
        
        # run through csv lines and parse them as payment
        for line in csv_lines:
            if line == ((CSV_DLMTR * (CSV_FIELDS_NUMB - 1)) + CSV_EOL): 
                continue        # skip empty csv line case
            if line == CSV_HEADER:      
                continue        # skip header table line

            if line.find(CSV_DLMTR) == -1:
                raise "No CSV delimiter in line"
    
            fields = line[:-len(CSV_EOL)].split(CSV_DLMTR)
            if len(fields) != CSV_FIELDS_NUMB:
                #print "((CSV_DLMTR * (CSV_FIELDS_NUMB - 1)) + CSV_EOL) <"
                #print ((CSV_DLMTR * (CSV_FIELDS_NUMB - 1)) + CSV_EOL)
                #print ">"
                #print "line = <"
                #print line
                #print ">"
                #print len(fields)
                raise Exception("Wrong number of fields")
            
            # set order of fields as expected by Payments constructor
            payment_fields = []
            payment_fields.append( fields[CSV_F_TITLE      ] )
            payment_fields.append( fields[CSV_F_DATE       ] )
            payment_fields.append( fields[CSV_F_PURPOSE    ] )
            payment_fields.append( fields[CSV_F_PRICE      ] )
            payment_fields.append( fields[CSV_F_PAYER      ] )
            payment_fields.append( fields[CSV_F_COMMENT    ] )
            
            # if all checks passed - add payment fields finally
            #try:
            p = payment.Payment(payment_fields)
            #print p.price
            self._payments.append(p)
            #print 
            #print len(self._payments)
            #except:
            #    raise Exception("Debug exception")
    
    

# methods to filter payments
    def getPaymentsByPayer(self, payer_name):
        """ Returns loaded payments with payer <payer_name> """
        return payment.getPaymentByPayer(self._payments, payer_name)
            
    def getPaymentsByPurpose(self, purpose_name):
        """ Returns loaded payments with purpose <purpose_name> """
        return payment.getPaymentByPurpose(self._payments, purpose_name)
    
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
        for payment in self._payments:
            payment.pprint()
    
    def printPaymentsForPayer(self, payer_name):
        """ Prints all payments by <payer_name> """
        print "-- Payments made by [" + payer_name + "]"
        for payment in self.getPaymentsByPayer(payer_name):
            payment.pprint()
    def printPaymentsOnPurpose(self, purpose_name):
        """ Prints all payments on <purpose_name> """
        print "-- Payments made on [" + purpose_name + "]"
        for payment in self.getPaymentsByPurpose(purpose_name):
            payment.pprint()
    
    def printPayersOnPurpose(self, purpose_name):
        """ Prints details about each payer spent on <purpose_name> """
        print "-- Payers on [" + purpose_name + "]"
        purp_payments = self.getPaymentsByPurpose(purpose_name)

    #def printAllPayersSummary(self):
    
    
    

# end of Booker class
