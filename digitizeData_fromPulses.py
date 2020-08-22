'''
Jeswin Mathew
CSE-3313-001
02-15-2020
'''
#necessary imports needed for numpy, csv for reading the file
#and binascii to convert from binary bits to ASCII
import numpy as np
import csv
import binascii

#getting the corrupted/raw pulses from teh csv file
csvFile = np.genfromtxt('data-communications.csv', delimiter = ',')

#generating pulses 0 and 1 which is uncorrupted
pulse0 = np.ones( 10 )
v_vector = pulse0/np.linalg.norm(pulse0)
pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
w_vector = pulse1/np.linalg.norm(pulse1)


#variable created for storing the first index value
index_zero = [0]

#set of 10 numbers chosen in the encoded message
min_size_pulse = 10

#selecting 8 bits for each character to determine its ASCII value
oneChar_size = 8

#empty string to contain the string's raw numbers 
raw_string = ""

#empty string to contain the processed string
processed_string = ""

#storing the pulses in the csv file in increments of 10 numbers
raw_pulse_count = csvFile.size/min_size_pulse
integer_raw_pulse_count = int(raw_pulse_count)

#variable to store the pulses in the csv file in increments of 8 bits
lettercount = integer_raw_pulse_count/oneChar_size

#Base of the number to which it needs to be converted to
base_value = 2

#index variable created for the bit values
index = 0
index2 = 0

#calculating the bits from the raw pulses from the csv file
message_bits = index_zero * integer_raw_pulse_count  

#converting the letter count into integers
lettercountInt = int(lettercount)

#getting the value of the 8 bit characters
raw_text = index_zero * lettercountInt
count = 1

#looping from first index to last of the raw data with the spaced out set
for increment in range(0,csvFile.size,min_size_pulse):  
  
  #holding the values for the file starting from 0 to end of the csvfile
  values = csvFile[increment:min_size_pulse+increment]
  #val = np.arange(i,i+10)

  #these raw values are the corrupted pulses in the data file
  corrupted_seq_pulse = values

  #finding the inner product of the corrupted value and v vector
  matchzero = np.inner(corrupted_seq_pulse,v_vector)
  absolute_matchzero = abs(matchzero)

  #finding the inner product of the corrupted value and w vector
  matchone = np.inner(corrupted_seq_pulse,w_vector)
  absolute_matchone = abs(matchone)

  #using the Cauchy-Schwarz inequality to see if the first inner product
  #is greater the second, if so assign it the bit to 0 or else to 1
  message_bits[index] = 1 if absolute_matchzero < absolute_matchone else 0
  index+=1

#looping through the total count of the pulses in the corrupted signal 
#and filling it in an array
for a in range(integer_raw_pulse_count):
  raw_string += str(message_bits[a])

#converting from binary to ascii
#data_b2a = binascii.b2a_uu(raw_string)
#print(data_b2a)

#looping through the pulses in increments of 8 bits to 
#convert from binary to ascii
for num in range(0,integer_raw_pulse_count,oneChar_size):
  #converting the raw string into an integer of base 2
  base2 = int(raw_string[num:(oneChar_size+num)],base_value)
  #retrieving the characters after ascii conversion
  raw_text[index2] = chr(base2)
  index2+=1  

#storing the characters into a string and printing it. 
for i in range(lettercountInt):
  processed_string += str(raw_text[i])

#printing processed string to display the encoded message
print(processed_string)
