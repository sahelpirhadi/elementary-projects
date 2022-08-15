def _unique_list_sample_(sample_list):
    output_list = []
    for items in sample_list:
        if items not in output_list:
            output_list.append(items)
    return output_list
