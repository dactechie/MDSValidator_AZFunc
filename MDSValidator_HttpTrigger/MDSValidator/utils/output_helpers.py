def get_row(header, hlen, row_dict, errors):
    row = {}
    errfield_mesg = {er['field']: er['message'] for er in errors }
    
    for h in header:
       row[h] = row_dict[h]
       row[f"error_{h}"] = errfield_mesg.get(h, "")

    return row


def get_vresult_rows(headers, hlen, data, errors_dict, errors_only=False):
    if errors_only:
        return [get_row(headers, hlen, row_dict, errors_dict.get(i,[])) 
                for i, row_dict in enumerate(data) if errors_dict.get(i)]
    else:
        return [get_row(headers, hlen, row_dict, errors_dict.get(i,[]))
                for i, row_dict in enumerate(data)]

