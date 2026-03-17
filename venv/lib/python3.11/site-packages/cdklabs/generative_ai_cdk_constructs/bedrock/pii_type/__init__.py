from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ..._jsii import *


@jsii.enum(
    jsii_type="@cdklabs/generative-ai-cdk-constructs.bedrock.PIIType.CanadaSpecific"
)
class CanadaSpecific(enum.Enum):
    '''(experimental) Types of PII specific to Canada.

    :stability: experimental
    '''

    CA_HEALTH_NUMBER = "CA_HEALTH_NUMBER"
    '''(experimental) A Canadian Health Service Number is a 10-digit unique identifier, required for individuals to access healthcare benefits.

    :stability: experimental
    '''
    CA_SOCIAL_INSURANCE_NUMBER = "CA_SOCIAL_INSURANCE_NUMBER"
    '''(experimental) A Canadian Social Insurance Number (SIN) is a nine-digit unique identifier, required for individuals to access government programs and benefits.

    :stability: experimental
    '''


@jsii.enum(jsii_type="@cdklabs/generative-ai-cdk-constructs.bedrock.PIIType.Finance")
class Finance(enum.Enum):
    '''(experimental) Types of PII in the domain of Finance.

    :stability: experimental
    '''

    CREDIT_DEBIT_CARD_CVV = "CREDIT_DEBIT_CARD_CVV"
    '''(experimental) A three-digit card verification code (CVV) that is present on VISA, MasterCard, and Discover credit and debit cards.

    For American Express credit or debit cards,
    the CVV is a four-digit numeric code.

    :stability: experimental
    '''
    CREDIT_DEBIT_CARD_EXPIRY = "CREDIT_DEBIT_CARD_EXPIRY"
    '''(experimental) The expiration date for a credit or debit card.

    This number is usually four digits
    long and is often formatted as month/year or MM/YY. Guardrails recognizes expiration
    dates such as 01/21, 01/2021, and Jan 2021.

    :stability: experimental
    '''
    CREDIT_DEBIT_CARD_NUMBER = "CREDIT_DEBIT_CARD_NUMBER"
    '''(experimental) The number for a credit or debit card.

    These numbers can vary from 13 to 16 digits
    in length.

    :stability: experimental
    '''
    PIN = "PIN"
    '''(experimental) A four-digit personal identification number (PIN) with which you can access your bank account.

    :stability: experimental
    '''
    SWIFT_CODE = "SWIFT_CODE"
    '''(experimental) A SWIFT code is a standard format of Bank Identifier Code (BIC) used to specify a particular bank or branch.

    Banks use these codes for money transfers such as
    international wire transfers. SWIFT codes consist of eight or 11 characters.

    :stability: experimental
    '''
    INTERNATIONAL_BANK_ACCOUNT_NUMBER = "INTERNATIONAL_BANK_ACCOUNT_NUMBER"
    '''(experimental) An International Bank Account Number (IBAN).

    It has specific formats in each country.

    :stability: experimental
    '''


@jsii.enum(jsii_type="@cdklabs/generative-ai-cdk-constructs.bedrock.PIIType.General")
class General(enum.Enum):
    '''(experimental) Types of PII that are general, and not domain-specific.

    :stability: experimental
    '''

    ADDRESS = "ADDRESS"
    '''(experimental) A physical address, such as "100 Main Street, Anytown, USA" or "Suite #12, Building 123".

    An address can include information such as the street, building,
    location, city, state, country, county, zip code, precinct, and neighborhood.

    :stability: experimental
    '''
    AGE = "AGE"
    '''(experimental) An individual's age, including the quantity and unit of time.

    :stability: experimental
    '''
    DRIVER_ID = "DRIVER_ID"
    '''(experimental) The number assigned to a driver's license, which is an official document permitting an individual to operate one or more motorized vehicles on a public road.

    A driver's license number consists of alphanumeric characters.

    :stability: experimental
    '''
    EMAIL = "EMAIL"
    '''(experimental) An email address, such as marymajor@email.com.

    :stability: experimental
    '''
    LICENSE_PLATE = "LICENSE_PLATE"
    '''(experimental) A license plate for a vehicle is issued by the state or country where the vehicle is registered.

    The format for passenger vehicles is typically five
    to eight digits, consisting of upper-case letters and numbers. The format
    varies depending on the location of the issuing state or country.

    :stability: experimental
    '''
    NAME = "NAME"
    '''(experimental) An individual's name.

    This entity type does not include titles, such as Dr.,
    Mr., Mrs., or Miss.

    :stability: experimental
    '''
    PASSWORD = "PASSWORD"
    '''(experimental) An alphanumeric string that is used as a password, such as "*very20special#pass*".

    :stability: experimental
    '''
    PHONE = "PHONE"
    '''(experimental) A phone number.

    This entity type also includes fax and pager numbers.

    :stability: experimental
    '''
    USERNAME = "USERNAME"
    '''(experimental) A user name that identifies an account, such as a login name, screen name, nick name, or handle.

    :stability: experimental
    '''
    VEHICLE_IDENTIFICATION_NUMBER = "VEHICLE_IDENTIFICATION_NUMBER"
    '''(experimental) A Vehicle Identification Number (VIN) uniquely identifies a vehicle.

    VIN
    content and format are defined in the ISO 3779 specification. Each country
    has specific codes and formats for VINs.

    :stability: experimental
    '''


@jsii.enum(
    jsii_type="@cdklabs/generative-ai-cdk-constructs.bedrock.PIIType.InformationTechnology"
)
class InformationTechnology(enum.Enum):
    '''(experimental) Types of PII in the domain of IT (Information Technology).

    :stability: experimental
    '''

    URL = "URL"
    '''(experimental) A web address, such as www.example.com.

    :stability: experimental
    '''
    IP_ADDRESS = "IP_ADDRESS"
    '''(experimental) An IPv4 address, such as 198.51.100.0.

    :stability: experimental
    '''
    MAC_ADDRESS = "MAC_ADDRESS"
    '''(experimental) A media access control (MAC) address assigned to a network interface.

    :stability: experimental
    '''
    AWS_ACCESS_KEY = "AWS_ACCESS_KEY"
    '''(experimental) A unique identifier that's associated with a secret access key.

    You use
    the access key ID and secret access key to sign programmatic AWS requests
    cryptographically.

    :stability: experimental
    '''
    AWS_SECRET_KEY = "AWS_SECRET_KEY"
    '''(experimental) A unique identifier that's associated with a secret access key.

    You use
    the access key ID and secret access key to sign programmatic AWS requests
    cryptographically.

    :stability: experimental
    '''


@jsii.enum(
    jsii_type="@cdklabs/generative-ai-cdk-constructs.bedrock.PIIType.UKSpecific"
)
class UKSpecific(enum.Enum):
    '''(experimental) Types of PII specific to the United Kingdom (UK).

    :stability: experimental
    '''

    UK_NATIONAL_HEALTH_SERVICE_NUMBER = "UK_NATIONAL_HEALTH_SERVICE_NUMBER"
    '''(experimental) A UK National Health Service Number is a 10-17 digit number, such as 485 777 3456.

    :stability: experimental
    '''
    UK_NATIONAL_INSURANCE_NUMBER = "UK_NATIONAL_INSURANCE_NUMBER"
    '''(experimental) A UK National Insurance Number (NINO) provides individuals with access to National Insurance (social security) benefits.

    It is also used for some purposes in the UK
    tax system.

    :stability: experimental
    '''
    UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER = "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER"
    '''(experimental) A UK Unique Taxpayer Reference (UTR) is a 10-digit number that identifies a taxpayer or a business.

    :stability: experimental
    '''


@jsii.enum(
    jsii_type="@cdklabs/generative-ai-cdk-constructs.bedrock.PIIType.USASpecific"
)
class USASpecific(enum.Enum):
    '''(experimental) Types of PII specific to the USA.

    :stability: experimental
    '''

    US_BANK_ACCOUNT_NUMBER = "US_BANK_ACCOUNT_NUMBER"
    '''(experimental) A US bank account number, which is typically 10 to 12 digits long.

    :stability: experimental
    '''
    US_BANK_ROUTING_NUMBER = "US_BANK_ROUTING_NUMBER"
    '''(experimental) A US bank account routing number.

    These are typically nine digits long.

    :stability: experimental
    '''
    US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER = "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER"
    '''(experimental) A US Individual Taxpayer Identification Number (ITIN) is a nine-digit number that starts with a "9" and contain a "7" or "8" as the fourth digit.

    :stability: experimental
    '''
    US_PASSPORT_NUMBER = "US_PASSPORT_NUMBER"
    '''(experimental) A US passport number.

    Passport numbers range from six to nine alphanumeric characters.

    :stability: experimental
    '''
    US_SOCIAL_SECURITY_NUMBER = "US_SOCIAL_SECURITY_NUMBER"
    '''(experimental) A US Social Security Number (SSN) is a nine-digit number that is issued to US citizens, permanent residents, and temporary working residents.

    :stability: experimental
    '''


__all__ = [
    "CanadaSpecific",
    "Finance",
    "General",
    "InformationTechnology",
    "UKSpecific",
    "USASpecific",
]

publication.publish()
