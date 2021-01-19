from django.http.response import JsonResponse
import json
import base64
import uuid
import boto3
from apiutility.errorCodes import ErrorCodes
from apiutility.jsonTransformer import transformIndicatorList, transformSdg, transformSdgList, transformSdgIndicator
from apiutility.validators import validateKeys, validateThatListIsEmpty, validateThatStringIsEmpty, validateThatStringIsEmptyAndClean
from apiutility.views import badRequestResponse, internalServerErrorResponse, successResponse, resourceNotFoundResponse
from core.views import (createSdg as createSdgRecord, findSdgById as findSdgByIdRecord,
                        getSdgs as getSdgsRecord, createSdgIndicator as createSdgIndicatorRecord,
                        getSdgIndicatorById as getSdgIndicatorByIdRecord, getSdgIndicators as getSdgIndicatorsRecord)


def sdgRouter(request):
    if request.method == 'POST':
        return createSDG(request)

    if request.method == 'GET':
        return listSDGs(request)


def singleSdgRouter(request, sdgId):
    return getSdgById(request, sdgId)


def sdgIndicatorsRouter(request):
    if request.method == 'POST':
        return createSdgIndicator(request)

    if request.method == 'GET':
        return getSdgIndicators(request)


def singleSdgIndicatorRouter(request, indicatorId):
    return getSdgIndicatorById(request, indicatorId)


def createSDG(request):

    try:
        body = json.loads(request.body)

        # check if all required fields are present in request payload
        missingKeys = validateKeys(payload=body, requiredKeys=[
                                   'name', 'description', 'image'])

        if missingKeys:
            return badRequestResponse(ErrorCodes.MISSING_FIELDS, message=f"The following key(s) are missing in the request payload: {missingKeys}")

        # load the fields from Json
        name = body['name']
        description = body['description']
        image = body['image']

        if not validateThatStringIsEmptyAndClean(name):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="SDG name can neither contain special characters nor be empty")

        if not validateThatStringIsEmpty(description):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="SDG description can neither contain special characters nor be empty")

        image = request.FILES['image']
        name = image.name
        bucket_name = 'vgg-daniel-test'

        if not name.lower().endswith(('jpg', 'jpeg', 'png')):
            return badRequestResponse(ErrorCodes.INVALID_FILE_FORMAT, message="Image format is invalid")

        # take the file and store it in a temporary folder
        fileName = str(uuid.uuid4()) + name
        tempPath = '' + fileName

        aws_session = boto3.Session(
            aws_access_key_id, aws_secret_access_key)
        s3 = aws_session.resource('s3')
        # s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
        #                   aws_secret_access_key=aws_secret_access_key)

        # # print(tempPath)
        print(s3)

        try:
            response = s3.Bucket(bucket_name).put_object(
                Key='images/%s' % image.name, Body=image)
            # s3.upload_file(bucket_name, '/images', fileName)
            print("Image uploaded")
            return True
        except Exception as ex:
            print(ex)
            return False

        uploadImage(image, tempPath)  # *******key*******

        sdg = createSdgRecord(name, description, image)

        if sdg is None:
            return internalServerErrorResponse(errorCode=ErrorCodes.SDG_CREATION_FAILED, message="Failed to create SDG")
        else:
            return successResponse(message="successfully created your SDG", body=transformSdg(sdg))
    except Exception as ex:

        # Log Exception
        pass


def listSDGs(request):
    try:
        sdgs = getSdgsRecord()

        return successResponse(message="SDGs fetched successfully", body=transformSdgList(sdgs))

    except Exception as ex:
        pass


def getSdgById(request, sdgId):
    try:
        sdg = findSdgByIdRecord(sdgId)
        if sdg is not None:
            return successResponse(message="SDG fetched successfully", body=transformSdg(sdg))
        else:
            return resourceNotFoundResponse(errorCode=ErrorCodes.SDG_ID_NOT_SUPPLIED, message="The requested SDG does not exist")
    except Exception as ex:
        pass


def createSdgIndicator(request):
    try:
        body = json.loads(request.body)
        # check if all required fields are present in request payload
        missingKeys = validateKeys(payload=body, requiredKeys=[
            'description', 'sdgId'])

        if missingKeys:
            return badRequestResponse(ErrorCodes.MISSING_FIELDS, message=f"The following key(s) are missing in the request payload: {missingKeys}")

        indicatorDescription = body['description']
        if not validateThatStringIsEmpty(indicatorDescription):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Indicator description can neither contain special characters nor be empty")

        sdgId = body['sdgId']
        sdg = findSdgByIdRecord(sdgId)

        if sdg is None:
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="Requested SDG does not exist")

        sdgIndicator = createSdgIndicatorRecord(
            description=body['description'], sdgId=body['sdgId'])

        if sdgIndicator is None:
            return badRequestResponse(errorCode=ErrorCodes.SDG_INDICATOR_FAILED, message="Sdg indicator creation failed")

        return successResponse(message="successfully created an indicator for SDG", body=transformSdgIndicator(indicator))

    except Exception as ex:
        pass


def getSdgIndicatorById(request, sdgId, indicatorId):
    try:
        sdg = findSdgByIdRecord(sdgId)
        if sdg is not None:
            indicator = getSdgIndicatorByIdRecord(indicatorId)
            return successResponse(message="Indicator for sdg fetched successfully", body=transformSdgIndicator(indicator))

        else:
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMTERS, message="please provide a valid sdgId", body={})

    except Exception as ex:
        pass


def getSdgIndicators(request):
    try:
        indicators = getSdgIndicatorsRecord()
        return successResponse(message="SDG Indicators fetched successfully", body=transformIndicatorList(indicators))

    except Exception as ex:
        pass


def uploadImage(image, tempPath):
    with open(tempPath, 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)
    return True
