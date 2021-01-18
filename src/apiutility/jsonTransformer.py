

from apiutility.typeConversions import toUiReadableDateFormat
from core.views import findSdgById, getSdgIndicators, getSdgIndicators
from program.views import getProgramLocation, getSelectedSdgIndicators


def transformProgram(program, locations, programSdgsList):

    loc = []
    if locations is not None:
        for location in locations:
            loc.append(location.name)

    return {
        "id": program.id,
        "name": program.name,
        "description": program.description,
        "code": program.code,
        "image": program.image,
        "locations": loc,
        "sdgs": transformProgramSdg_and_Indicator_List(programSdgsList),
        "created": toUiReadableDateFormat(program.created)
    }


def transformProgramList(programList):
    results = []
    for program in programList:
        results.append(transformProgram(
            program, program.location_set.all(), program.program_sdg_set.all()))
    return results


def transforProgramIndicator(indicator):
    indicatorObj = getIndicator(indicator.selectedIndicatorId)
    return {
        "id": indicator.selectedIndicatorId,
        "description": indicatorObj.description
    }


def transformIndicatorList(indicatorList):
    results = []
    for indicator in indicatorList:
        results.append(transforProgramIndicator(indicator))

    return results


def transformProgramSdg_and_Indicator_List(programSdgsList):
    result = []
    for programSdg in programSdgsList:
        sdg = findSdgById(programSdg.sdgId)
        indicators = transformIndicatorList(
            programSdg.program_indicator_set.all())
        sdgs = {
            "sdgId": programSdg.sdgId,
            "name": sdg.name,
            "indicators": indicators
        }
        result.append(sdgs)
    return result


def transformSdg(sdg):
    return {
        "id": sdg.id,
        "name": sdg.name,
        "description": sdg.description,
        "image": sdg.image
    }


def transformSdgList(sdgList):
    results = []

    for sdg in sdgList:
        results.append(transformSdg(sdg))

    return results


def transformImageRecord(imageRecord):
    return {
        "path": imageRecord.path
    }


def transformSdgIndicator(indicator):
    indicator = getSdgIndicators(indicator.description)
    return {
        "id": indicator.id,
        "description": indicator.description
    }
