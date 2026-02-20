import re
from app.utils.regex_patterns import *

def regex_extract(text: str):
    return {
        "phoneNumbers": re.findall(PHONE, text),
        "bankAccounts": re.findall(ACCOUNT, text),
        "upiIds": re.findall(UPI, text),
        "phishingLinks": re.findall(URL, text),
        "emailAddresses": re.findall(EMAIL, text),
        "caseIds": re.findall(CASE, text),
        "orderNumbers": re.findall(ORDER, text),
        "policyNumbers": re.findall(POLICY, text)
    }