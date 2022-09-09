from typing import List, Optional
from unittest import result
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Models


class Person(BaseModel):
    name: str
    age: int
    is_married: Optional[bool] = None


class Location(BaseModel):
    city: str
    country: str


@app.get("/")
def home():
    return {"world": "mundo"}

# python logic is still useful


@app.get("/tweet/{tweet_id}")
def tweet(tweet_id: int):
    if tweet_id % 2 == 0:
        return {"tweet_id": "divisible by 2"}
    return {"tweet_id": "Not divisible by 2"}

# request and response Body


@app.post("/person/new")
def new_person(person: Person = Body(...)):
    return {person}

# Query parameters


@app.get("/person/details")
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

@app.get("/person/details/{id}")
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

@app.put("/person/update/{id}")
def update_person(
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
    return result
