import logging
import azure.functions as func
import os
from datetime import datetime
from .MDSValidator import MDSDataFileProcessor


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    #logging.info(req.form.items())

    logging.info("\n\n\n\n BODY ------------------------------\n\n\n")
    
    barr = req.get_body().decode('utf-8').splitlines() #4 -> n-1
    logging.info(barr)

    #barr[1] = content-type: text/csv ; sdfsdfsdfd ; filename='"sdf"'
    #filename  = barr[1].split(';')[2].split('=')[1]
    #filename = filename.replace('"','')

    filename ="outfile"
    data = barr #barr[4: len(barr)-1]
    
    logging.info(data)
    #os.get __file__

    # input_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
    #               os.path.join( 'MDSValidator', 'input'))
    # filename = os.path.join( input_dir, filename)
    
    # logging.info(f"filename : {filename}, len of barray {len(barr)}")

    # with open(filename, "w") as file:
    #   file.writelines(f"{item}\n" for item in data)

    start_date = datetime(2019,7,1)
    errors_only = False
    all_eps = True
    #data_file = filename #None # uses the latest
    output_data = MDSDataFileProcessor.main(data, all_eps, errors_only, start_date, program='TSS', reporting_period="12", nostrict=False)

     #.encode()
     #"".encode()

    # except ValueError:
    #     pass
    # else:
    #     name = req_body.get('name')

    #if name:
    #HttpResponse(body=None, *, status_code=None, headers=None, mimetype=None, charset=None)
    # with open(output_file, "rb") as file:
    #   file_bytes = file.read()
    #   logging.info(file_bytes)
    #output_data.__str__

    return func.HttpResponse(body=output_data, mimetype='text/csv')
    #else:
    #    return func.HttpResponse(
    #         "Please pass a name on the query string or in the request body",
    #         status_code=400
    #    )
