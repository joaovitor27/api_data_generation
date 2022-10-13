from fastapi import FastAPI
import generation

app = FastAPI()


@app.get("/api")
async def root():
    return {"message": "Hello World"}


@app.get("/api/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/generation-people")
async def get_generation_people(number_people: int = 1, sex: str = 'R', age: int = 18, uf_code: str = '',
                                formatting: bool = True, data_only: bool = True) -> {}:
    """
    `Generate people data.`

    The function is called `get_generation_people` and it takes the following arguments:

    * `number_people`: The number of people to generate.
    * `sex`: The sex of the people to generate.
    * `age`: The age of the people to generate.
    * `uf_code`: The UF code of the people to generate.
    * `formatting`: Whether to format the data.
    * `data_only`: Whether to return only the data

    The function returns a dictionary with the key "result" and the value of the result of the function generation_people

    :param number_people: The number of people to generate, defaults to 1
    :type number_people: int (optional)
    :param sex: 'M' for male, 'F' for female, 'R' for random, defaults to R
    :type sex: str (optional)
    :param age: The age of the people to generate, defaults to 18
    :type age: int (optional)
    :param uf_code: The state code, for example, SP, RJ, MG, etc
    :type uf_code: str
    :param formatting: If True, the result will be formatted in a dictionary. If False, the result will be a list, defaults
    to True
    :type formatting: bool (optional)
    :param data_only: If True, the result will be a list of dictionaries, if False, the result will be a list of objects,
    defaults to True, defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the key "result" and the value of the result of the function generation_people.
    """

    result = generation.generation_people(number_people, sex, age, uf_code, formatting, data_only)

    return {"result": result}


