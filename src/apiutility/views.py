
from http import HTTPStatus
from django.http.response import JsonResponse

# Create your views here.


def badRequestResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.BAD_REQUEST, errorCode, message=message, body=body)


def resourceNotFoundResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.NOT_FOUND, errorCode, message=message, body=body)


def internalServerErrorResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.INTERNAL_SERVER_ERROR, errorCode, message=message, body=body)


def errorResponse(httpStatusCode, errorCode, message="", body={}):
    return JsonResponse({'errorCode': errorCode, 'data': body, 'message': message}, status=httpStatusCode, safe=False)


# def getImageFileUpdateFailedErrorPacket(tenantId):
#     return getError(code=ErrorCodes.IMAGE_RECORD_UPDATE_FAILED, tenantId=tenantId,
#                     defaultMessage=DefaultErrorMessages.IMAGE_RECORD_UPDATE_FAILED)


# success responses
def createdResponse(message="", body={}):
    return successResponse(HTTPStatus.CREATED, message=message, body=body)


def successResponse(httpStatusCode=HTTPStatus.OK, message="", body={}):
    return JsonResponse({'data': body, 'message': message}, status=httpStatusCode, safe=False)
