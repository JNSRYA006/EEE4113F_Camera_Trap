# Import appropriate packages
import sqlite3
import sys
import time
from datetime import datetime

#sys.path.insert(0,'/home/group10/')
#import RTC_setup

#sys.path.insert(0,'/home/group10/RTC_SDL_DS3231')
#import SDL_DS3231

#ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)

def insert_into_database(file_path_name, file_blob): 
  try:
    conn = sqlite3.connect('images.db')
    print("[INFO] : Successful connection!")
    cur = conn.cursor()
    sql_insert_file_query = '''INSERT INTO images(file_name, file_blob)
      VALUES(?, ?)'''
    cur = conn.cursor()
    cur.execute(sql_insert_file_query, (file_path_name, file_blob, ))
    conn.commit()
    print("[INFO] : The blob for ", file_path_name, " is in the database.") 
    last_updated_entry = cur.lastrowid
    return last_updated_entry
  except sqlite3.Error as e:
    print(e)
  finally:
    if conn:
      conn.close()
    else:
      error = "Oh shucks, something is wrong here."

def read_blob_data(entry_id):
  try:
    conn = sqlite3.connect('images.db')
    cur = conn.cursor()
    print("[INFO] : Connected to SQLite to read_blob_data")
    sql_fetch_blob_query = """SELECT * from images where id = ?"""
    cur.execute(sql_fetch_blob_query, (entry_id,))
    record = cur.fetchall()
    for row in record:
      converted_file_name = row[2]
      photo_binarycode  = row[3]
      # parse out the file name from converted_file_name
      # Windows developers should reverse "/" to "\" to match your file path names 
      last_slash_index = converted_file_name.rfind("/") + 1 
      final_file_name = converted_file_name[last_slash_index:] 
      write_to_file(photo_binarycode, final_file_name)
      print("[DATA] : Image successfully stored on disk. Check the project directory. \n")
    cur.close()
  except sqlite3.Error as error:
    print("[INFO] : Failed to read blob data from sqlite table", error)
  finally:
    if conn:
        conn.close()

def convert_into_binary(file_path):
  with open(file_path, 'rb') as file:
    binary = file.read()
  return binary

def write_to_file(binary_data, file_name):
  with open(file_name, 'wb') as file:
    file.write(binary_data)
  print("[DATA] : The following file has been written to the project directory: ", file_name)

def main():
  file_path_name = "/home/group10/inductor.jpg"
  file_blob = convert_into_binary(file_path_name)
  #print("[INFO] : the last 100 characters of blob = ", file_blob[:100]) 
  last_updated_entry = insert_into_database(file_path_name, file_blob)
  read_blob_data(last_updated_entry)

main()
