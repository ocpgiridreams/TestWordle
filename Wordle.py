from fastapi import FastAPI
import uvicorn
import random
import string
import uuid
import json
from fastapi import Request



app = FastAPI()
cache = {}

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


def  start_game( is_new: bool = False):
        sorted_dict = {}
        cache.clear()
        game_str = get_random_string(5)
        game_id=uuid.uuid1()
        print( game_id)
        cache['game_id'] = game_str
        cache['attempt_count'] = 0
        sorted_dict['status'] = "Game tarted"
        return sorted_dict


def  play_game( guess_str =None,  is_new: bool = False):
    sorted_dict ={}
    if cache['attempt_count'] < 7:
        count = cache['attempt_count'] + 1
        cache['attempt_count'] = count
        game_str = cache['game_id']
        result = {}
        # matching
        res2 = [idx for idx, (x, y) in enumerate(
            zip(game_str, guess_str)) if x == y]

        for elem in res2:
            result[elem] = "correct"
        # Non matching

        incorrectly_guessed_letters = [x for idx, (x, y) in enumerate(
            zip(guess_str, game_str)) if x != y and x in guess_str]
        non_matching = [idx for idx, (x, y) in enumerate(
            zip(guess_str, game_str)) if x != y and x in guess_str]

        # wrong position
        position = [idx for idx, (x, y) in enumerate(
            zip(guess_str, game_str)) if x != y and x in game_str]

        for elem in non_matching:
            result[elem] = "InCorrect"
        common = [x for x in position if x in non_matching]

        print("Wrong_position", common)
        for elem in common:
            result[elem] = "wrong_position"

        myKeys = list(result.keys())
        myKeys.sort()
        sorted_dict = {i: result[i] for i in myKeys}
        sorted_dict['incorrectly_guessed_letters'] = incorrectly_guessed_letters
        # print( sorted_dict)

    else:
        print("Game over")
        sorted_dict['status'] ="Game Over"


    return sorted_dict


@app.get('/')
def read_results():
    results = start_game()
    return results


@app.post("/new_game/")
def read_results():
    results = start_game(is_new =True)
    return results

@app.post("/guess/")
async def get_body( request : Request ):
    postData = await request.body()
    print("Post data ",   postData)
    a = json.loads(postData)
    guess_str = a["word"]
    print("Guess word", guess_str)
    results = play_game( guess_str   )
    return results

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")
