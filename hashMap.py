class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    #creates an array the size of array_size and assigns each value in the array to none
    self.array = [None for item in range(array_size)]

    #hash code creation method count collisions uses number of collisions to caculate the hash code
def hash(self, key, count_collisions=0):
    #key.encode() method that converts string into corresonding bytes
    key_bytes = key.encode()
    #sums up total of key_bytes to create our hash code
    hash_code = sum(key_bytes)
    return hash_code + count_collisions
#transforms hash_code into useful indicies
def compressor(self, hash_code):
    return hash_code % self.array_size

def assign(self, key, value):
    #creates a index in the array for our value
    array_index = self.compressor(self.hash(key))   
    #saves the value into the array
    current_array_value = self.array[array_index]
    #used to handle collisions checks if there is alread an array value at the index if there isn't value is added
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
    #if the key value we are entering into are the same we overrite the value for the key updating it
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return
    number_collisions = 1
    #while the array key is not equal to the key we are trying to enter
    while current_array_value[0] != key:
      #we create a new hash_code using number_collisions  
      new_hash_code = self.hash(key, number_collisions)
      #we create a new index by compressing the new_hash_code
      new_array_index = self.compressor(new_hash_code)
      #if the array value at that index in none we enter our data
      if self.array[new_array_index] == None:
        self.array[new_array_index] = [key, value]
        return
      #if the array index at that value equals the key we overwrite that data  
      if self.array[new_array_index] == key:
        self.array[new_array_index] = [key, value]
        return
      #if there is already data at that key and it does not equal our new array index we created we incrememnt the $ of collisions  
      if self.array[new_array_index] != key:
        number_collisions += 1
#reuturns the value of the array at this keys index
def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]
    #if our return value is none we return none
    if possible_return_value == None:
      return None
    #if our return value key == key we are looking for return the value of said key  
    if possible_return_value[0] == key:
      return possible_return_value[1]
    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return
#code to view hash_map in action
#hash_map = HashMap(20)
#hash_map.assign("gneiss", "metamorphic")
#print(hash_map.retrieve("gneiss"))