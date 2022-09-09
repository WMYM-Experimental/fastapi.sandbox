import email
from enum import Enum
from fastapi import Body, Query, Path
from fastapi import FastAPI
from pydantic import Field
from pydantic import EmailStr, PaymentCardNumber, FilePath
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()

# Models


class EyeColor(Enum):
    brown = "brown"
    blue = "blue"
    green = "green"


class Person(BaseModel):
    name: str = Field(
        ...,
        example="Wmym",
        min_length=2,
        max_length=10)
    age: int = Field(
        ...,
        example=18,
        ge=18,
        le=100
    )
    is_married: Optional[bool] = Field(
        default=False
    )
    eyes_color: Optional[EyeColor] = Field(
        default="brown",
        example="brown"
    )
    email: Optional[EmailStr] = Field(
        default=None,
        example="***@***.com"
    )
    card_number: Optional[PaymentCardNumber] = Field(
        default=None,
        example="1234-1234-1234-1234"
    )


class Location(BaseModel):
    city: str
    country: str


@ app.get("/")
def home():
    return {"world": "mundo"}

# python logic is still useful


@ app.get("/tweet/{tweet_id}")
def tweet(tweet_id: int):
    if tweet_id % 2 == 0:
        return {"tweet_id": "divisible by 2"}
    return {"tweet_id": "Not divisible by 2"}

# request and response Body


@ app.post("/person/new")
def new_person(person: Person = Body(...)):
    return {person}

# Query parameters


@ app.get("/person/details")
def person_details(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=10,
        title="Name",
        description="Name of the person"
    ),
    age: str = Query(
        ...,
        title="Age",
        description="Age of the person"),
):
    return {name: age}


# path parameters

@ app.get("/person/details/{id}")
def person_details(
    id: int = Path(
        ...,
        gt=0,
        le=100,
        title="ID",
        description="ID of the person"
    )
):
    return {id: "id exists"}


# Validiations request body

@ app.post("/person/new_post/{id}")
def update_person(
    id: int = Path(
        ...,
        gt=0,
        le=100,
        title="ID",
        description="ID of the person"
    ),
    file: FilePath = Body(
        ...,
        title="File",
        description="File to upload"
    ),
    person: Person = Body(
        ...,
        title="Person",
        description="Person to update"
    )

):
    return {id: person}


# Validations request body with pydantic
@ app.put("/person/update/data/{id}")
def update_person_data(
    id: int = Path(
        ...,
        gt=0,
        le=100,
        title="ID",
        description="ID of the person"
    ),
    person: Person = Body(
        ...,
        title="Person",
        description="Person details"
    ),
    location: Location = Body(
        ...,
        title="Location",
        description="Location details"
    )
):
    result = dict(person)
    result.update(dict(location))
    return {id: result}
