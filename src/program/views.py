from django.shortcuts import render
from django.db import transaction

from core.models import Indicator
from .models import Location, Program, Program_Indicator, Program_Sdg

# Create your views here.


def createProgram(name, image, description, code, locations, sdgs):
    """[Create a program]

    Args:
        name ([string]): [description]
        image ([string]): [description]
        description ([string]): [description]
        code ([string]): [description]
        locations ([list]): [description]

    Returns:
        [object]: [program instance]
    """
    try:
        with transaction.atomic():
            program = Program(
                name=name,
                description=description,
                image=image,
                code=code
            )
            program.save()

            createLocations(program, locations)

            createProgramSdg(program, sdgs)

            return program
    except Exception as ex:
        # Log Error
        return ex


def createLocations(program, locations):
    """[Create Locations for a program]

    Args:
        program ([object]): [instance of program]
        locations ([list]): [array list of locations]
    """
    try:
        for location in locations:
            saveLocation = Location(
                program=program,
                name=location
            )
            saveLocation.save()

    except Exception as ex:
        pass


def createProgramSdg(program, sdgs):
    """[Create sdgs for a program]

    Args:
        program ([object]): [program instance]
        sdgs ([list]): [list of sdgs id]

    Returns:
        [list]: [returns list of created sdgs]
    """
    try:
        for sdg in sdgs:
            programSdg = Program_Sdg(
                program=program,
                sdgId=sdg['id']
            )
            programSdg.save()
            createProgramIndicators(programSdg, sdg['indicators'])

    except Exception as ex:
        # log Error
        pass


def createProgramIndicators(programSdg, indicators):
    """[summary]

    Args:
        indicators ([object]): [description]
    """
    try:
        for indicator in indicators:
            programIndicator = Program_Indicator(
                programSdg=programSdg,
                selectedIndicatorId=indicator
            )
            programIndicator.save()

    except Exception as ex:
        # log Error
        pass


def getProgramById(programId):
    """[Returns a Program Object by programId]

    Args:
        programId ([int]): [programId]

    Returns:
        [object]: [program object]
    """
    try:

        program = Program.objects.get(id=programId, isDeleted=False)
        return program

    except Program.DoesNotExist:
        return None
    except Exception as ex:
        # Log Error
        return ex


def getPrograms():
    """[Returns a list of programs]

    Returns:
        [list]: [list of programs]
    """
    try:
        program = Program.objects.filter(isDeleted=False)
        return program

    except Program.DoesNotExist:
        return None

    except Exception as ex:
        # Log Error
        return ex


def getProgramLocation(program):
    """
    Get a list of locations attributed to a program
    """
    try:
        locations = Location.objects.filter(program=program, isDeleted=False)
        return locations
    except Location.DoesNotExist:
        return None
    except Exception as ex:
        # Log Error
        pass


def getprogramSdgs(program):
    """[Returns a list of sdgs selected for a program]

    Args:
        program ([object]): [instance of a program]
    """
    try:

        programSdgs = Program_Sdg.objects.filter(
            program=program, isDeleted=False)
        return programSdgs

    except Program_Sdg.DoesNotExist:
        return None
    except Exception as ex:
        # Log Error
        pass

# def getSdgIndicators(pro):
#     """[Returns a list of Indicators defined under an SDG]

#     Args:
#         sdg ([object]): [Instance of sdg]
#     """

#     try:
#         sdgIndicators = Indicator.objects.filter(sdg=sdg, isDeleted=False)
#         return sdgIndicators
#     except Indicator.DoesNotExist:
#         return None
#     except Exception as ex:
#         #Log Error
#         return ex


def getSelectedSdgIndicators(programSdg):
    """[Returns a list of selected Indicators chosen under an SDG]

    Args:
        programSdg ([object]): [Instance of programSdg]
    """

    try:

        programSdgIndicators = Program_Indicator.objects.filter(
            programSdg=programSdg, isDeleted=False)
        return programSdgIndicators

    except Indicator.DoesNotExist:
        return None
    except Exception as ex:
        # Log Error
        return ex
