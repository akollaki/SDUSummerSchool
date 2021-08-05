# determine if a person is looking at camera
def eye_contact(gaze_vector, lower, upper):
   if all(lower < ele < upper for ele in gaze_vector):
       return True
   return False

# continuously read last line of csv file and return if gaze vectors are within bounds
lastRead = 0
def read_csv(filename, lower, upper):
   global lastRead
   path = f"/home/dlinano/OpenFace/build/processed/{filename}.csv"
   while True:
       with open(path) as file:
           data = file.readlines()
           if data:
               lastRow = data[-1].split(',')
               if lastRow[0] != lastRead and lastRow[4] != '0':
                   lastRead = lastRow[0]
                   try:
                       if eye_contact([float(lastRow[11]), float(lastRow[12])], lower, upper):
                           return
                   except IndexError:
                       print('Caught error')
                       pass

if __name__ == '__main__':
   lowerBound = -0.3
   upperBound = 0.3
   try:
       while True:
           read_csv("output", lowerBound, upperBound)
           print('looking at camera')
           # reach here if eye vectors are within lower and upper bounds
   except KeyboardInterrupt:
       print("Program closed")
