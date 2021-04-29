# ==================================================================
# you can easily install it using this coommand 
# pip install browser-history
# ==================================================================

# ==================================================================
#                       importing library
# ==================================================================
import os
import time
from browser_history import get_history
from browser_history.browsers import Firefox
from browser_history.browsers import Brave
from browser_history.browsers import Chrome
from browser_history.browsers import Chromium
from browser_history.browsers import Edge
from browser_history.browsers import Opera
from browser_history.browsers import OperaGX
from browser_history.browsers import Safari
from browser_history.browsers import Vivaldi

# ==================================================================
#              create new folder if does not exists
# ==================================================================
def creating_new_folder(name_of_folder):
    get_current_dir = os.getcwd()
    path = os.path.join(get_current_dir, name_of_folder)
    if os.path.isdir(path):
        print("yes")
    else:
        make_folder = os.mkdir(path)
    return [path]


# ==================================================================
#           Getting the list of Browsers obj into dict
# ==================================================================
def get_list():
    new_list = {}
    try:
        f = Chromium()
        new_list['Chromium'] = f
    except Exception as e:
        print(e)
    return new_list


# ==================================================================
#              getting the history of the browsers
# ==================================================================
def browser_history():
    new_dict = get_list()
    obj_list = []
    print("=======================")
    for key, value in new_dict.items():
        try:
            outputs_his = value.fetch_history()
            outputs_book = value.fetch_bookmarks()
            
            his = outputs_his.histories
            book = outputs_book.bookmarks

            if his:
                path = creating_new_folder("Chromium")[0]
                # his
                full_path_key_csv = os.path.join(path,str(str(key)+"_his.csv"))
                full_path_key_json = os.path.join(path,str(str(key)+"_his.json"))
                time.sleep(2)
                outputs_his.save(full_path_key_csv)
                time.sleep(2)
                outputs_his.save(full_path_key_json)
                # book
                name1 = os.path.join(path, str(str(key)+"_book.csv"))
                name2 = os.path.join(path, str(str(key)+"_book.csv"))
                time.sleep(2)
                book.save(name1)
                time.sleep(2)
                book.save(name2)

            else:
                print("no it does not work")
        except Exception as e:
            print(e)
browser_history()
