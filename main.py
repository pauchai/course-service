from fastapi import FastAPI, Request, status, Response
import xmltodict
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/course_info")
def get_course_info(course_no:int):


        data = json.parse('
        "lessons": [
                {
                    "no":  1,

                },
                {
                    "no":  2,
                    
                },
                {
                    "no":  3,
                    
                },
                {
                    "no":  4,
                    
                }                

            ]
        ')
            
            
        
        return Response(content=data, media_type="application/json")

@app.get("/lesson_info")
def get_lesson_info_xml(lesson_no:int):

    with open(f"./data/lessons_meta/lesson{lesson_no}.es.xml", mode="r") as lesson_info:
        data = "\n\r".join(lesson_info.readlines())
        return Response(content=data, media_type="application/xml")


@app.get("/course_info_json")
def get_course_info_json():
    with open("./data/lessons_meta/lesson1.es.xml", mode="r") as xml_file:
        lesson_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
    return lesson_dict


