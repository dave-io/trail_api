from django.http.response import JsonResponse
import json
from apiutility.errorCodes import ErrorCodes
from apiutility.jsonTransformer import transformIndicatorList, transformProgram, transformProgramList, transformProgramSdg_and_Indicator_List
from apiutility.validators import validateKeys, validateThatListIsEmpty, validateThatStringIsEmpty, validateThatStringIsEmptyAndClean
from apiutility.views import badRequestResponse, internalServerErrorResponse, successResponse
from program.views import (createProgram as CreateProgramRecord, getProgramById, getProgramLocation, getPrograms,
                           createProgramSdg as createProgramSdgRecord, getprogramSdgs)


def programRouter(request):
    if request.method == 'POST':
        return createProgram(request)

    if request.method == 'GET':
        return listPrograms(request)


def programSingleRouter(request, programId):
    return listProgramById(request, programId)


def programSdgRouter(request, programId):
    if request.method == 'POST':
        return createProgramSdg(request, programId)

    if request.method == 'GET':
        return listProgramSdgs_and_Indicators(request, programId)


def createProgram(request):

    try:
        body = json.loads(request.body)

        # check if all required fields are present in request payload
        missingKeys = validateKeys(payload=body, requiredKeys=[
                                   'name', 'description', 'image', 'code', "locations"])

        if missingKeys:
            return badRequestResponse(ErrorCodes.MISSING_FIELDS, message=f"The following key(s) are missing in the request payload: {missingKeys}")

        # load the fields from Json
        name = body['name']
        description = body['description']
        image = body['image']
        code = body['code']
        locations = body['locations']
        sdgs = body['sdgs']

        if not validateThatStringIsEmptyAndClean(name):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Program name can neither contain special characters nor be empty")

        if not validateThatStringIsEmpty(description):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Program description can neither contain special characters nor be empty")

        if not validateThatStringIsEmptyAndClean(code):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Program code can neither contain special characters nor be empty")

        if not validateThatListIsEmpty(locations):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Program must contain a list of locations")

        if not validateThatListIsEmpty(sdgs):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Program must contain a list of sdgs")

        program = CreateProgramRecord(
            name, image, description, code, locations, sdgs)

        if program is None:
            return internalServerErrorResponse(errorCode=ErrorCodes.PROGRAM_CREATION_FAILED, message="Program failed to create", data={})
        else:
            return successResponse(message="successfully created program", body=transformProgram(program, getProgramLocation(program), getprogramSdgs(program)))
    except Exception as ex:

        # Log Exception
        pass


def listPrograms(request):
    try:
        programs = getPrograms()

        return successResponse(message="programs fetched successfully", body=transformProgramList(programs))

    except Exception as ex:
        pass


def listProgramById(request, programId):
    try:
        program = getProgramById(programId)
        if program is not None:
            return successResponse(message="program fetched successfully", body=transformProgram(program, program.location_set.all(), program.program_sdg_set.all()))
        else:
            return successResponse(message="program does not exist", body={})
    except Exception as ex:
        pass


def createProgramSdg(request, programId):
    try:
        body = json.loads(request.body)

        sdgs = body['sdgs']

        if not validateThatListIsEmpty(sdgs):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Program must contain a list of sdgs (ids)")

        program = getProgramById(programId)

        if program is None:
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Program does not exist")

        programSdg = createProgramSdgRecord(program, sdgs)

        if programSdg is None:
            return badRequestResponse(errorCode=ErrorCodes.PROGRAM_SDG_CREATION_FAILED, message="program sdgs creation failed")

        return successResponse(message="successfully created sdgs for program", body=[])

    except Exception as ex:
        pass


def listProgramSdgs_and_Indicators(request, programId):
    try:

        program = getProgramById(programId)

        if program is None:
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Program does not exist")

        programSgds = getprogramSdgs(program)

        return successResponse(message="program sdgs and indicators fetched successfully", body=transformProgramSdg_and_Indicator_List(programSgds))

    except Exception as ex:
        pass
