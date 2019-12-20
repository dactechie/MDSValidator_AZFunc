#from math import ceil
#import xlwings as xw
# from MDSValidator_HttpTrigger.MDSValidator.utils.dates import now_string
# from MDSValidator_HttpTrigger.MDSValidator.logger import logger





# def _process_chunks(ws, data_rows, starter, ender, chunk_size=10):

#     line_num = starter
#     for line_num in range(starter, ender-chunk_size+1, chunk_size):
#         st_row_num = line_num + 2
#         ed_row_num = st_row_num + chunk_size
#         ws.range(f'A{str(st_row_num)}:A{str(ed_row_num)}').value = \
#                     data_rows[line_num:line_num+chunk_size]
#         logger.info(f"end row number : {ed_row_num} " )
    
#     starter = line_num+chunk_size
#     chunk_size = ceil(0.2 * (ender - starter))
#     if chunk_size < 1 : #or ((starter+chunk_size) > (ender - starter)):
#         return
#     logger.debug(f"calling process chunks again start {starter }:: chunksize {chunk_size}")
#     _process_chunks(ws, data_rows, starter, ender, chunk_size)


# def write_data_to_book(data, errors, book_name, errors_only=True) -> str:
#     result_book_name = 'result.xlsx'
#     try:
#         app = xw.App(visible=False)
#         book = app.books.open("./MDSTemplate.xltx")
#         ws = book.sheets['loaded']
#         headers = ws.range('A1:BT1').value # TODO: remove the column hard-coding

#         rows = get_rows_to_write(headers, len(headers), data, errors, errors_only)

#         endval = len(rows)
#         chunk_size = ceil(0.2 * endval) # chunksize 20% 

#         logger.info(f"\t >>> endval {endval}  chunksize {chunk_size} <<< \n")

#         _process_chunks(ws, rows, starter=0, ender=endval, chunk_size=chunk_size)
#         result_book_name = f"{book_name}_{now_string()}.xlsx"

#         logger.info(f"results book name : {result_book_name}")

#         book.save(result_book_name)

#     except Exception as e:
#        logger.exception(e)

#     finally:
#         book.close()
#         app.quit()
#         logger.debug(f" app pid : app.pid")
#         app.kill()
#         return result_book_name

