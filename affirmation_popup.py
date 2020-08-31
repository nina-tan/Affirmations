import os
import sys

affirmations_list = []
with open('affirmation.txt') as f:
    for line in f:
        affirmations_list.append(line)

# automate popup
os.system('osascript ./affirmation_notif.scpt "' + affirmations_list[0] + '"')

# prepare next affirmation
affirmations_list.append(affirmations_list[0])
affirmations_list.remove(affirmations_list[0])
with open('affirmation.txt', '+w') as f:
    for line in affirmations_list:
        f.write(line)
