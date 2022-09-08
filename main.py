from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"world": "mundo"}


@app.get("/tweet/{tweet_id}")
def tweet(tweet_id: int):
    if tweet_id % 2 == 0:
        return {"tweet_id": "divisible by 2"}
    return {"tweet_id": "Not divisible by 2"}
