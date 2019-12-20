def get_row(header, hlen, row_dict, errors):
    row = []
    errfield_mesg = {er['field']: er['message'] for er in errors }
    
    for i in range(0,hlen-1,2):
        error = ""
        header_field = header[i]   
        if header_field in errfield_mesg:
            error = errfield_mesg[header_field]
        if header_field in row_dict:
            row.extend([row_dict[header_field], error])
        else:
            row.extend(["",error])

    return row


def get_rows_to_write(headers, hlen, data, errors_dict, errors_only=True):
    if errors_only:
        return [get_row(headers, hlen, row_dict, errors_dict.get(i,[])) 
                for i, row_dict in enumerate(data) if errors_dict.get(i)]
    else:
        return [get_row(headers, hlen, row_dict, errors_dict.get(i,[]))
                for i, row_dict in enumerate(data)]

