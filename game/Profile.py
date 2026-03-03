from enum import StrEnum
from datetime import date
from dateutil.relativedelta import relativedelta

"""Provide the Profile class, and required Enums for the character profiles on the profile screen."""

# Enums provide constant values for comparison, and a single location for the string representaion

# String representations for Blood Types in the profile screen
class BloodType(StrEnum):
    """Bloodtypes for the character profiles"""
    A_POS = "A+"
    A_NEG = "A-"
    B_POS = "B+"
    B_NEG = "B-"
    AB_POS = "AB+"
    AB_NEG = "AB-"
    O_POS = "O+"
    O_NEG = "O-"
    QA_POS = "Qa+"
    ELEC = "Electricity"
    UNKNOWN = "00±"

# Character status representations for the profile screen
class CharacterStatus(StrEnum):
    """Character status for the character profiles. 
    String representation must match the statuses used in the profile icon sprite names"""
    ALIVE = "Alive"
    DEAD = "Dead"
    UNKNOWN = "Unknown"

# Gender representations for the profile screen
class Gender(StrEnum):
    """gender markers for the character profiles. """
    FEMALE = "F"
    MALE = "M"
    NEUTRAL = "N"

# This is all the data represented in the character profile
# The type hinting is not well enforced, but keep to the values in the Enums. 
# If more are needed, define above.
class Profile:
    """Holds the data that is displayed on the Profile screen"""

    # This is used for calculating birthdays, however if we do keep track of the date in game 
    # this reponsibility should be moved elsewhere
    CURRENT_DATE = date.fromisoformat("2050-12-01")
    
    # Class acts as a read-only container for data. 10 arguments is needed here
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-positional-arguments
    # pylint: disable=too-many-arguments
    def __init__(self, name: str, 
                gender: Gender,  
                manifest: str, 
                occupation: str, 
                birthday: date, 
                height: int, 
                weight: int, 
                blood_type: BloodType, 
                status: CharacterStatus = CharacterStatus.ALIVE):
        self.name = name
        self.gender = gender
        self.manifest = manifest
        self.occupation = occupation
        self._birthday = birthday
        self.height = height
        self.weight = weight
        self.blood_type = blood_type
        self.status = status

    @property
    def birthday(self) -> str:
        """Return birthday in 00/00/0000 format"""
        return self._birthday.strftime("%d/%m/%Y")

    @birthday.setter
    def birthday(self, value) -> str:
        self._birthday = value

    @property
    def age(self) -> int:
        """Calculate the number of years between the in game date, and the birthday of a character"""
        return relativedelta(self.CURRENT_DATE, self._birthday).years
