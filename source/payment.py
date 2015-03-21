#import tmp_params
import datetime

"""
    expected format

"""

PAYMENT_FIELDS_LEN = 6

class Payment:
    """
        Defines payment transaction object.
        Contains payment details - price, target, payer, date, etc.
        <Payment> object controls only its content type matching, according
        to limitations in __init__. It doesn't support any other checks.
    """
    
    
    
    def __init__(self, fields):
        """
            Takes for input list <fields> of exact size <PAYMENT_FIELDS_LEN>.
            All <fields> elements must match type as shown below.
        """
        
        """
        expected fields order:
        [0] - title     (string)
        [1] - date      (string or datetime.datetime)
        [2] - purpose   (string)
        [3] - price     (integer > 0)
        [4] - payer     (string)
        [5] - comment   (string)
        """
        
        if type(fields) is not list:
            raise Exception("[GAG Exception] <fields> arg is not list")
        if len(fields) != PAYMENT_FIELDS_LEN:
            raise Exception("[GAG Exception] size of <fields> doesn't match PAYMENT_FIELDS_LEN")
        
        # load title string
        self.title   = fields[0]
        if type(self.title) is not str:
            raise Exception("[GAG ASSERT] Title field is not string")

        # load date (string, or datetime object)
        self.date = fields[1]
        if (type(self.date) is not str) and (type(self.date) is not datetime.datetime):
            raise Exception("[GAG ASSERT] Date field is not string nor datetime")
        
        # load purpose string
        self.purpose = fields[2]
        if type(self.purpose) is not str:
            raise Exception("[GAG ASSERT] Purpose field is not string")
        
        # load price
        self.price = fields[3]
        if type(self.price) is not int:
            raise Exception("[GAG ASSERT] Price field is not integer")
        if self.price <= 0:
            raise Exception("[GAG ASSERT] Price is non-positive")
        
        # load payer string
        self.payer   = fields[4]
        if type(self.payer) is not str:
            raise Exception("[GAG ASSERT] Payer field is not string")
        
        # load comment string
        self.comment = fields[5]
        if type(self.comment) is not str:
            raise Exception("[GAG ASSERT] Comment field is not string")
        
        #print "[debug] constructor end"

    def output(self):
        """
            Returns fancy output line for payment.
        """
        
        str_title_len   = 50
        str_date_len    = 40
        str_purpose_len = 30
        str_price_len   = 10
        str_payer_len   = 20
        #str_comment_len =
        
        if len(self.title) > (str_title_len - 2):
            out_title = self.title[:str_title_len - 2] + " |"
        else:
            out_title = self.title + (" " * (str_title_len - len(self.title) - 2)) + " |"
        
        # if date is presented with <datetime> object, then
        # then output it in format %d.%m.%y (31.12.99)
        if type(self.date) is datetime.datetime:
            out_date = " " + datetime.datetime.strftime("%d.%m.%y") + " |"
        # or output as string otherwise
        else:
            if len(self.date) > (str_date_len - 4):
                out_date = " " + self.date[:str_date_len - 4] + " |"
            else:
                out_date = " " + self.date + (" " * (str_date_len - len(self.date) - 4)) + " |"
        
        if len(self.purpose) > (str_purpose_len - 4):
            out_purpose = " " + self.purpose[:str_purpose_len - 4] + " |"
        else:
            out_purpose = " " + self.purpose + (" " * (str_purpose_len - len(self.purpose) - 4)) + " |"
        
        # enormous sums aren't supported (over 9999999 at the moment)
        if len(str(self.price)) > (str_price_len - 4):
            raise Exception
        out_price = (' ' * (str_price_len - len(str(self.price)) - 4) ) + str(self.price) + ' |'
        
        if len(self.payer) > (str_payer_len - 2):
            out_payer = " " + self.payer[:str_payer_len - 2]
        else:
            out_payer = " " + self.payer + (" " * (str_payer_len - len(self.payer) - 2))
        
        out_line = out_title + out_date + out_purpose + out_price + out_payer
        return out_line
        
    def printPayment(self):
        """ Prints payment object using <output> function. """
        print self.output()
    
# end of Payment class
        
        
def sumPaymentsPrice(payments_list):
    sum = 0.0
    for p in payments_list:
        sum += p.price
    return sum
        
        
# get payments methods            
def getPaymentsByPayer(payments, payer_name):
    """ Returns list of payments from <payments> with payer <payer_name> """
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
        
        
        
        