import csv

from .dates import now_string
from ..logger import logger
from .output_helpers import get_rows_to_write

#def get_rows_to_write(headers, hlen, data, errors_dict)
headers = ['ID','First name','Surname','SLK 581','Sex','DOB','Date accuracy indicator','Country of birth','Indigenous status','Preferred language','Postcode (Australian)',
            'Usual accommodation','Client type','Source of referral','Commencement date','End date','Reason for cessation','Treatment delivery setting','Method of use for PDC',
            'Injecting drug use status','Principle drug of concern','ODC1','ODC2','ODC3','ODC4','ODC5',
            'Main treatment type','OTT1','OTT2','OTT3','OTT4','OTT5','Living arrangements','Previous alcohol and other drug treatment received','Mental health']


def write_results_to_csv(data, errors, output_filename):
  
  rows = get_rows_to_write(headers, len(headers), data, errors)
  
  with  open(output_filename, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
  

  return output_filename