
import re

def validateThatStringIsEmptyAndClean(value):
    is_clean = (re.compile(r'[@_!#$%^&*()<>?/\|}{~:]').search(value) == None)
    not_empty = (len(value.strip()) != 0)

    return (is_clean and not_empty)

def validateThatStringIsEmpty(value):
    return (len(value.strip()) > 0)

def validateThatListIsEmpty(value):
    return (len(value) > 0)

def validateKeys(payload, requiredKeys):
    # extract keys from payload
    payloadKeys = list(payload.keys())

    # check if extracted keys is present in requiredKeys
    missingKeys = []
    for key in requiredKeys:
        if key not in payloadKeys:
            missingKeys.append(key)

    return missingKeys