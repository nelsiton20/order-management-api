from pydantic import BaseModel
from typing import Any
from peewee import ModelSelect

class ResponseModel(BaseModel):
    model_config = {
        'from_attributes': True
    }

    @classmethod
    def model_validate(cls, obj: Any):
        obj_dict = obj.__dict__ if hasattr(obj, '__dict__') else obj

        # Convertir ModelSelect en listas
        for key, value in obj_dict.items():
            if isinstance(value, ModelSelect):
                obj_dict[key] = list(value)

        return super().model_validate(obj_dict)
