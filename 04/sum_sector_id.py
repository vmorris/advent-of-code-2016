#!/usr/bin/env python3

import string

def tokenize_room(room):
  ''' returns roomname, sectorID, and checksum '''
  _roomname, sid_chksum = room.rsplit('-',1)
  sectorID, checksum = sid_chksum.strip()[:-1].split('[')
  roomname = _roomname.replace('-', '')
  return roomname, sectorID, checksum

def count_letters(word):
  ''' returns a dictionary where key=letter and value=count '''
  letter_freq = {}
  for letter in word:
    if letter not in letter_freq.keys():
      letter_freq[letter] = 1
    else:
      letter_freq[letter] += 1
  return letter_freq

def flip_freq(letter_freq):
  ''' takes a dictionary where key=letter and value=count and flips
      it to return a dictionary where key=count and 
      value=sorted_string_of_letters '''
  count_freq = {}
  for k,v in letter_freq.items():
    if v not in count_freq.keys():
      count_freq[v] = k
    else:
      count_freq[v] = "".join([count_freq[v], k])
  for k,v in count_freq.items():
    count_freq[k] = "".join(sorted(v))
  return count_freq 

def rotate_letter(sid, letter):
  ''' rotate right a letter sid number of times, then return the new letter'''
  alphabet = string.ascii_lowercase
  shifted_value = alphabet.index(letter) + int(sid)
  # modulate over 26 to find new character position
  return alphabet[(shifted_value % 26)]
  

if __name__ == "__main__":

  total_sum = 0
  
  with open('input.txt', 'r') as f:
    for room in f:
      roomname, sectorID, checksum = tokenize_room(room)
      print("----->",roomname)
      letter_frequency = count_letters(roomname)
      count_frequency = flip_freq(letter_frequency)
      count_keys = sorted(count_frequency.keys(), reverse=True)
      most_common = [] # collect all the letters, sorted by frequency and alphabetically
      for k in count_keys:
        most_common.append(count_frequency[k])
      most_common = "".join(most_common)
      print("most common letters:",most_common[:len(checksum)])
      print("checksum:",checksum)
      if checksum == most_common[:len(checksum)]:
        print("  >>  MATCH FOUND  <<")
        total_sum += int(sectorID)

  print(total_sum)
