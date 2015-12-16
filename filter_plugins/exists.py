import os.path

def file_exists(arg):
    return os.path.isfile(arg)

def dir_exists(arg):
    return os.path.isdir(arg)

class FilterModule(object):
    def filters(self):
        return {'file_exists': file_exists,
                'dir_exists': dir_exists}
