import arrow
import os 
import mimetypes 


def datetimeformat(date_str):
    datetime = arrow.get(date_str)
    #formats into real time
    return datetime.humanize()

def file_type(key):
    
    #splits off file_extension (becasue file not stored locally --> returns a tuple (main file name, extension)
    file_name = os.path.splitext(key)
    file_extension = file_name[1]
    try:
        #types_map : tuple containing two dicts. mapping the filename extensions to MIME types. 1st dict non-standard type 2nd dict. standard types
        return mimetypes.types_map[file_extension]
    except KeyError():
        return 'Unknown'
