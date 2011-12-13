# -*- coding: utf-8 -*-

__name__ = "arquivos"

import os
import string

def split( fn, n ):
    print("splitting file " + fn)
    splited_name = string.split(fn, '.')
    base_name = splited_name[0]
    extension = splited_name[1]

    size = os.path.getsize( fn )
    
    generated_files = []

    with open( fn ) as f:
        files = 0
        while (files * n) < size:
            files += 1
            result = "%s_%03d.%s" % ( base_name, files, extension )
            with open( result , 'w' ) as w:
                generated_files.append(result)
                w.write( f.read(n) )

    return generated_files

def join(fn, files):
    with open(fn, 'w') as f:
        for file in files:
            with open(file) as p:
                f.write(p.read())
            