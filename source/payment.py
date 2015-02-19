#import tmp_params
import datetime

"""
    expected format

"""


class Payment:
    """
        Defines payment transaction object.
        Contains payment details - price, target, payer, date, etc.
    """
    
    
    
    def __init__(self, fields):
        """
            Constructor
        """
        
        """
        expected fields order:
        [0] - title
        [1] - date in format <DD.MM.YY>
        [2] - purpose (from PURPOSES list)
        [3] - price in integer (RUR)
        [4] - payer string (from PAYERS list)
        [5] - comment
        """
        
        #print "[debug] constructor start"
        #print fields
        
        # load details
        self.title   = fields[0]

        #self.date    = datetime.datetime.strptime(fields[1], "%d.%m")
        self.date = fields[1]

        self.purpose = fields[2]

        try:
            self.price   = int(fields[3])
        except:
            raise Exception("Bad price field")
        
        self.payer   = fields[4]
        self.comment = fields[5]
        
        # verify details
        #if self.title == "":
        #    raise Exception("Empty title")
        
        # date
        # purpose
        if self.price < 0:
            raise Exception("Negative price")
        # payer
        
        #print "[debug] constructor end"

    def pprint(self):
        """
            Forms fancy output line for payment and prints it
        """
        
        str_title_len   = 20
        str_date_len    = 10
        str_purpose_len = 15
        str_price_len   = 10
        str_payer_len   = 10
        #str_comment_len =
        
        if len(self.title) > (str_title_len - 2):
            out_title = self.title[:str_title_len - 2] + " |"
        else:
            out_title = self.title + (" " * (str_title_len - len(self.title) - 2)) + " |"
        
        #TBD: out_date = "  " + datetime.datetime.strftime("%d.%m") + "  |"
        if len(self.date) > (str_date_len - 2):
            out_date = self.date[:str_date_len - 2] + " |"
        else:
            out_date = self.date + (" " * (str_date_len - len(self.date) - 2)) + " |"
        
        if len(self.purpose) > (str_purpose_len - 3):
            out_purpose = " " + self.purpose[:str_purpose_len - 3] + " |"
        else:
            out_purpose = " " + self.purpose + (" " * (str_purpose_len - len(self.purpose) - 3)) + " |"
        
        out_price = (' ' * (str_price_len - len(str(self.price)) - 3) ) + str(self.price) + ' |'
        
        if len(self.payer) > (str_payer_len - 1):
            out_payer = " " + self.payer[:str_payer_len - 1]
        else:
            out_payer = " " + self.payer + (" " * (str_payer_len - len(self.payer) - 1))
        
        out_line = out_title + out_date + out_purpose + out_price + out_payer
        
        print out_line
# end of Payment class
        
        
def sumPaymentsPrice(payments_list):
    sum = 0.0
    for p in payments_list:
        sum += p.price
    return sum
        
        
# get payments methods            
def getPaymentsByPayer(payments, payer_name):
    """ Returns payments from <payments> with payer <payer_name> """
    result = []
    for p in payments:
        if p.payer == payer_name:
            result.append(p)
    return result
        
def getPaymentsByPurpose(payments, purpose_name):
    """ Returns payments from <payments> with purpose <purpose_name> """
    result = []
    for p in payments:
        if p.purpose == purpose_name:
            result.append(p)
    return result
        
        
        
        