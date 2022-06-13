import re

# Type Prefix http://1005.idv.hk/index.php?page=11&p=

type = {
  "ATE": "1",
  "AVW": "2",
  "ASV": "21",
  "AVBE": "264",
  "ASU": "274",
  "ATSE": "305",
  "AVBWU": "307",
  "ATENU": "331",
  "E5T": "331",
  "3ATENU": "342",
  "ASUD": "353",
  "AMNE": "361",
  "AMNF": "361",
  "FACELIFT": "366",
  "AVBWL": "390",
  "V6B": "390",
  "V6P": "390",
  "E6X": "406",
  "V6X": "414"
}

regex = {
  "fleet": re.compile("^..\/index.php\?page=11"),
  "plate": re.compile("^(([A-Z][A-Z]) ?(\d{3,4}))")
}