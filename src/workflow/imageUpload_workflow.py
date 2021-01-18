# import base64
# import uuid
# import json
# from images.views import createImage as CreateImageRecord
# from core.views import getSdgById

# from apiutility.jsonTransformer import transformImageRecord
# from apiutility.errorCodes import ErrorCodes
# from apiutility.views import badRequestResponse, internalServerErrorResponse, successResponse


# def imageUploadURLRouter(request):
#     if request.method == "POST":
#         return _uploadFile(request)


# def _uploadFile(request):
#     # verify if the file to upload is either png or jpg
#     fileToUpload = request.FILES['image']
#     name = fileToUpload.name
#     if not name.lower().endswith(('jpg', 'jpeg', 'png')):
#         return badRequestResponse(ErrorCodes.INVALID_FILE_FORMAT,
#                                   message="File format is invalid")

#     # take the file and store it in a temporary folder
#     fileName = str(uuid.uuid4()) + name
#     tempPath = '' + fileName
#     uploadFile(fileToUpload, tempPath)

#     # create an instance of the Image Model
#     imageRecord = CreateImageRecord(name=fileName,
#                                     sdg=sdg,
#                                     path=fileName)
#     if imageRecord == None:
#         return internalServerErrorResponse(ErrorCodes.IMAGE_RECORD_CREATION_FAILED,
#                                            message="Image file creation failed")

#     # upload image file to SFTP server
#     if not uploadFileToS3(tempPath, fileName):
#         return internalServerErrorResponse(ErrorCodes.IMAGE_UPLOAD_FAILED,
#                                            message="Image file upload failed")

#     return successResponse(message="Successfully uploaded file", body=transformImageRecord(imageRecord))


# def uploadFile(file, tempPath):
#     with open(tempPath, 'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)
#     return True


# def uploadFileToS3(filePath, s3FileName):
#     s3 = boto3.client('s3', aws_access_key_id=ENVVariables.AWS_ACCESS_KEY_ID,
#                       aws_secret_access_key=ENVVariables.AWS_SECRET_KEY)

#     try:
#         s3.upload_file(
#             filePath, ENVVariables.METRIC_ENTRY_AWS_BUCKET_NAME, s3FileName)
#         return True
#     except Exception as e:
#         print('uploadFileToS3@Error')
#         print(e)
#         return False
