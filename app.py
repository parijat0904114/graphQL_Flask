from flask import Flask, request
import json
from graphene import ObjectType, String, Argument, Schema, NonNull, Int, Field

app = Flask(__name__)


class Student(ObjectType):
    id = NonNull(Int)
    name  = String()
    email = String()

# array of objects
student_array = [
    Student(id = 1, name="Parijat", email="parijat2009@gmail.com"),
    Student(id = 2, name="Prashun", email="prashun@gmail.com"),
    Student(id = 3, name="Purohit", email="purohit@gmail.com")
]

class Query (ObjectType):

    student_details = Field(Student, id = Argument(Int))

    def resolve_student_details(self, info, id):

        # return the book which matches the id given
        for s in student_array:
            if (s.id == id):
                selected = s

        return selected


StudentSchema = Schema(query=Query)

@app.route('/student/<int:id>')
def get_student_by_id(id):
    query = """
        {
            studentDetails (id: %d )
            {
            id, name
            }
        }
    """%(id)
    result = StudentSchema.execute(query)
    return (result.data['studentDetails'])

if __name__=="__main__":
    app.run(debug=True)