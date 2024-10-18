def play_hip_hop_music():
  artist = "lil wayne"
  song = "megaman"
  print("Now playing on station 98.9: [megaman] by [lil wayne]")

def play_r_and_b_music():
  artist = "prince"
  song = "kiss"
  print("Now playing on station 104.1: [kiss] by [prince]")

def play_soul_music():
  artist = "bill withers"
  song = "lean on me"
  print("Now playing on station 202.3: [lean on me] by [bill withers]")

def main():
  print("Please choose a radio station:")
  print("1. Hip Hop Music")
  print("2. R&B Music")
  print("3. Soul Music")

  station = float(input("Enter the station number: "))

  if station == 98.9:
      play_hip_hop_music()
  elif station == 104.1:
      play_r_and_b_music()
  elif station == 202.3:
      play_soul_music()
  else:
      print("There is no station with that frequency.")

if __name__ == "__main__":
  main()