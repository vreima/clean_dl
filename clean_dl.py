# -*- coding: utf-8 -*-

import pathlib, datetime, argparse
from glob import glob

def remove_files(ext, folder):
    p = pathlib.Path(folder)
    files = p.glob(f"*.{ext}")
    count_ok = 0
    count_error = 0
    files_in_use = []
    
    for file in files:
        try:
            file.unlink()
        except PermissionError as p:
            count_error += 1
            files_in_use.append(p.filename)
        except:
            count_error += 1
            raise
        else:
            count_ok += 1
    
    if count_error + count_ok > 0:
        print(f"Unlinked {count_ok} .{ext} files, {count_error} errors.")
    
        if len(files_in_use):
            err_files = [pathlib.Path(f).name for f in files_in_use]
            print(f"-- File{'s' if len(files_in_use) > 1 else ''} {','.join(err_files)} in use.")
        
def remove_directories(pattern, folder):
    p = pathlib.Path(folder)
    dirs = (d for d in p.glob(f".\{pattern}") if d.is_dir())
    print(f"Removing directories matching pattern '{pattern}'.")
    #print([i.name for i in dirs])
    count_ok = 0
    count_error = 0
    
    for path in dirs:
        try:
            rm_dir(path, " ")
        except:
            count_error += 1
            print(f"Error while trying to remove {path.stem}.")
            raise
        else:
            count_ok += 1
            print(f"Removed {path.stem}.")
    print(f"Removed {count_ok} directories, {count_error} errors.")  
            
def rm_dir(path, prefix=""):
    for child in path.iterdir():
        if child.is_dir():
            print(f"{prefix}Removing {child.stem}...")
            rm_dir(child, prefix + " ")
        else:
            print(f"{prefix}Unlinking {child.name}.")
            child.unlink()
            
    path.rmdir()

def main():
    parser = argparse.ArgumentParser(description='Siivoa polku.')
    parser.add_argument('--dir', dest='dir', nargs='+', help='siivottavan kansion polku')
    parser.add_argument('--ext', dest='ext', nargs='+', help='siivottavat tiedostotyypit')
    parser.add_argument('--path', dest='paths', nargs='+', help='siivottavat kansiot')
    args = parser.parse_args()

    this = pathlib.Path(__file__)
    last_modified = datetime.datetime.fromtimestamp(this.stat().st_mtime)

    print(f"{this.name}, modified {last_modified:%d.%m.%Y}")
    
    for path in args.dir:
        print(f"\nCleaning {path}")
        
        for ext in args.ext:
            remove_files(ext, path)
            
        print("")
            
        for pattern in args.paths:
            remove_directories(pattern, path)

    
if __name__ == "__main__":
    main()