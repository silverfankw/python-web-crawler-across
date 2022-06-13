import re

# Type Prefix http://1005.idv.hk/index.php?page=11&p=

type = {
  "ATE": "1",
  "AVW": "2",
  "3ASV": "3",
  "ASV": "21",
  "AVBW": "263",
  "AVBE": "264",
  "ATEU": "268",
  "ASU": "274",
  "ATEE": "295",
  "ASB": "296",
  "ASC": "298",
  "ASCU": "304",
  "ATSE": "305",
  "AVBWU": "307",
  "AVC": "308",
  "AVBWS": "313",
  "AAU": "316",
  "ATENU": "331",
  "E5T": "331",
  "E5L": "342",
  "3ATENU": "342",
  "3AVBWU": "344",
  "AMC": "345",
  "ATH": "346",
  "ASUD": "353",
  "AMNE": "361",
  "AMNF": "361",
  "FACELIFT": "366",
  "AVBWL": "390",
  "V6B": "390",
  "V6P": "390",
  "E6T": "396",
  "AVG": "401",
  "AVBML": "405",
  "E6X": "406",
  "V6X": "414"
}

regex = {
  "fleet": re.compile("^..\/index.php\?page=11"),
  "plate": re.compile("^(([A-Z][A-Z]) ?(\d{3,4}))")
}