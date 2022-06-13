import re

# Type Prefix http://1005.idv.hk/index.php?page=11&p=

type = {
  "ASV": "21",
  "ATENU": "331",
  "E5T": "331",
  "FACELIFT": "366",
  "AVBWL": "390",
  "V6B": "390",
  "V6P": "390",
  "E6X": "406",
  "V6X": "414"
}

regex = {
  "plate": re.compile("^(([A-Z][A-Z]) ?(\d{3,4}))")
}