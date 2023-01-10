# TestWordle
Fun project testing Wordle

Start the program by running Wordle.py


### Send POST request with json body
POST http://localhost:8080/new_game/


===================================================================
POST http://localhost:8080/guess/
Content-Type: application/json

{
  "word": "crown"

}




===
Server Console
/home/girish/PycharmProjects/TestPythonCode/venv/bin/python /home/girish/PycharmProjects/TestPythonCode/work/Wordle.py 
INFO:     Started server process [102341]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)



Random string of length 5 is: zydfs


================================================

Game response
===================================================

HTTP/1.1 200 OK
date: Tue, 10 Jan 2023 18:26:21 GMT
server: uvicorn
content-length: 143
content-type: application/json

{
  "0": "wrong_position",
  "1": "InCorrect",
  "2": "InCorrect",
  "3": "wrong_position",
  "4": "InCorrect",
  "incorrectly_guessed_letters": [
    "c",
    "r",
    "o",
    "w",
    "n"
  ]
}
Response file saved.
> 2023-01-10T122621.200.json

Response code: 200 (OK); Time: 3ms (3 ms); Content length: 143 bytes (143 B)

