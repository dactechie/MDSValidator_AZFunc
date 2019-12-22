import logging
import json
import azure.functions as func
import sys
from .input_file_processor import get_details_from, get_data
from .MDSValidator import MDSDataFileProcessor
from .MDSValidator.utils.InputFileErrors import InputFileError


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
      data = get_data(req)
      filename = req.params.get('name')
      program, start_date, period = get_details_from(filename)

      # TODO put these in an app.ini/app.cfg on Sharepoint which the logic app loads and passes in as query params
      errors_only = False
      open_and_closed_eps = True
      
      result_dicts = MDSDataFileProcessor.exe(data, open_and_closed_eps, 
                                              errors_only, start_date,
                                              program=program, period=period, 
                                              nostrict=False)
      # in dev env only :
      #logging.info(result_dicts)
      results = json.dumps(result_dicts)

      return func.HttpResponse(body=results, 
                               mimetype="application/json", status_code=200)
    except InputFileError as ife:      
      logging.error(ife)
      # Using 201  (not appropriate) to distinguish in the LogicApp between error vs non-error state
      return func.HttpResponse(body=json.dumps({'error': ife.get_msg()}),
                               mimetype="application/json", status_code=201)
    except Exception as e:
      _, _, exc_traceback = sys.exc_info()
      logging.exception(e.with_traceback(exc_traceback))
      return func.HttpResponse(json.dumps({'error':str(e)}), status_code=400 )
