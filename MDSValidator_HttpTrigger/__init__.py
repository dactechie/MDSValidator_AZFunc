import logging
import json
import azure.functions as func
import sys
import urllib.parse
from datetime import datetime
from .MDSValidator import MDSDataFileProcessor
from .MDSValidator.utils.InputFileErrors import InputFilenameFormatError, TooSmallFileError

programs = ['TSS', 'ArcadiaResi', 'ArcadiaDay', 'Althea', 'Mastercare']

def get_details_from(filename):
  filename = urllib.parse.unquote(urllib.parse.unquote(filename))
  filename = filename.split('/')[-1]
  
  if not filename or filename.count('_') != 2 or filename[-4:] != '.csv':
    raise InputFilenameFormatError(filename,"Not a valid file name")

  program, mmyyyy, period = filename[:-4].split('_')
  try:
    if program not in programs:
      raise InputFilenameFormatError(filename,
            f"Not a valid program name.. Valid program names are {programs}.")
    
    if len(mmyyyy) != 6:
      raise InputFilenameFormatError(filename,'Invalid start date part in the filename')
    
    year = int(mmyyyy[2:])
    month = int(mmyyyy[0:2])
    current_year = datetime.now().year
    if not 1 <= month <= 12 or not current_year-2 <=  year <= current_year:
      raise InputFilenameFormatError(filename,'Month/Year not in acceptable range')

    period_start_date = datetime(year,month,1)
    p = int(period)
    if p not in [1, 3, 6, 12]:
      raise InputFilenameFormatError(filename,
            'Period is not valid, should be one of 1,3,6,12.')
      
  except ValueError:
    raise InputFilenameFormatError(filename, 
          'Start date/Period is not valid. Valid examples of MMYYYY: 021998 or 102019' ) 

  return program, period_start_date, p


def get_data(req):
  request_body = req.get_body()
  req_body_len = len(request_body)
  if req_body_len < 500:
    msg = 'Insufficient data. quitting...'
    logging.error(msg)
    raise TooSmallFileError( req_body_len, msg )

  data = request_body.decode('utf-8',errors='ignore').splitlines()

  if len(data) < 2:
    msg = 'Insufficient data. quitting...'
    logging.error(msg)
    raise TooSmallFileError( req_body_len, msg )
    
  return data
    


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
      data = get_data(req)
      filename = req.params.get('name')
      program, start_date, period = get_details_from(filename)

      errors_only = False
      open_and_closed_eps = True
      
      result_dicts = MDSDataFileProcessor.exe(data, open_and_closed_eps, errors_only, start_date,
                                              program=program, period=period, nostrict=False)
      logging.info(result_dicts)

      results = json.dumps(result_dicts)

      return func.HttpResponse(body=results, mimetype="application/json", status_code=200)

    except TooSmallFileError as tsfe:
      msg = f'TooSmallFileError: {tsfe.message} >: {tsfe.expression}'
      logging.error(msg)
      return func.HttpResponse(body=json.dumps({'error': msg}),  mimetype="application/json",
                               status_code=201)

    except InputFilenameFormatError as iffe:
      msg = f'InputFilenameFormatError: {iffe.message} >: {iffe.expression}'
      logging.error(msg)
      return func.HttpResponse(body=json.dumps({'error': msg}), mimetype="application/json",
                              #'\nInvalid filename in query params. Needs to be <program_name>_<start:MMyyyy>_<period>.csv',
                               status_code=201)
    except Exception as e:
      _, _, exc_traceback = sys.exc_info()
      logging.exception(e.with_traceback(exc_traceback))
      return func.HttpResponse(json.dumps({'error':str(e)}), status_code=400 )

      
      # client = pymongo.MongoClient(uri)
      # collection_ref = client["mds_schema"]['json_schema']
      
      
      # myquery = { }

      # mydoc = collection_ref.find(myquery) #.sort([('_id',-1)]).limit(1)
      # result = []
      # for x in mydoc:
      #   result.append(x)
      
      # logging.info(result)

      # return func.HttpResponse(body=json.dumps(result[0]['data']), mimetype="application/json")