name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

#make_dict = zip(name,favorite_animal)
#print make_dict

#convert_make_dict_to_real_dict = dict(make_dict)
#print convert_make_dict_to_real_dict


def make_dict(list1, list2):
  new_dict = {}
  zip_dict = zip(name,favorite_animal)
  new_dict = dict(zip_dict)
  print new_dict
  return new_dict
make_dict(name,favorite_animal)
