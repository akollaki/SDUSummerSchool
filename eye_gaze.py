# determine if a person is looking at camera
def eye_contact(gaze_vectors, lower, upper):
   for vec in gaze_vectors:
       if all(lower < ele < upper for ele in vec):
           return True
   return False

# continuously read last line of csv file and return if gaze vectors are within bounds
lastRead = 0
def read_csv(filename, lower, upper):
   global lastRead
   path = f"/home/dlinano/OpenFace/build/processed/{filename}.csv"
   while True:
       with open(path) as file:
           if data:
               data = file.readlines()
               lastRow = data[-1].split(',')
               if lastRow[0] != lastRead and lastRow[4] != '0':
                   lastRead = lastRow[0]
                   if eye_contact([[float(lastRow[11]), float(lastRow[12])]], lower, upper):
                       return

if __name__ == '__main__':
   lowerBound = -0.1
   upperBound = 0.1
   try:
       while True: 
           read_csv("output", lowerBound, upperBound)
           # reach here if eye vectors are within lower and upper bounds
   except KeyboardInterrupt:
       print("Program closed")
