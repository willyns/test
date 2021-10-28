def romanToInt(self, s: str) -> int:
  romans = {'I':1, 
          'V':5,
          'X':10,
          'L':50,
          'C':100,
          'D':500,
          'M':1000
         }
  rom_year_list = list(s[::-1])
  res = romans[rom_year_list[0]]
  for i in range(1,len(rom_year_list)):
    if romans[rom_year_list[i]] < romans[rom_year_list[i-1]]:
      res = res - romans[rom_year_list[i]]
    else:
      res = res + romans[rom_year_list[i]]
  return res
        
