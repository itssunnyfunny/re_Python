from pydantic import BaseModel, field_validator, model_validator

class Employee(BaseModel):
    name: str
    department: str
    salary: float

    @field_validator("salary")
    def validate_salary(cls, v):
        if v < 10000:
            raise ValueError("Salary must be greater than 10000")
        return v

    @field_validator("name")
    def validate_name(cls, v):
        if len(v) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return v
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(cls, values):
        if values["password"] != values["confirm_password"]:
            raise ValueError("Passwords do not match")
        return values