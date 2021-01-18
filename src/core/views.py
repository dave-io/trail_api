from django.shortcuts import render
from django.db import transaction
import uuid

from .models import SDG, Indicator


# Create your views here.


def createSdg(name, description, image):

    try:
        with transaction.atomic():
            sdg = SDG(
                name=name,
                description=description,
                image=image,
            )
            sdg.save()

            return sdg
    except Exception as ex:
        # Log Error
        return ex


def findSdgById(sdgId):
    try:

        sdg = SDG.objects.get(id=sdgId, isDeleted=False)
        return sdg

    except SDG.DoesNotExist:
        return None

    except Exception as ex:
        pass


def getSdgs():
    try:

        sdgs = SDG.objects.filter(isDeleted=False)
        return sdgs

    except SDG.DoesNotExist:
        return None

    except Exception as ex:
        pass


def createSdgIndicator(description, sdgId):

    try:
        sdgIndicator = Indicator(description=description, sdgId=sdgId)
        sdgIndicator.save()
        return sdgIndicator
    except Exception as ex:
        pass


def getSdgIndicatorById(indicatorId):
    try:
        indicator = Indicator.objects.get(
            isDeleted=False, indicatorId=indicatorId)
        return indicator
    except Exception as ex:
        pass


def getSdgIndicators(indicators):
    # [Returns a list of Indicators defined under an SDG]

    try:
        sdgIndicators = Indicator.objects.filter(
            indicators=indicators, isDeleted=False)
        return sdgIndicators
    except Indicator.DoesNotExist:
        return None
    except Exception as ex:
        # Log Error
        return ex
