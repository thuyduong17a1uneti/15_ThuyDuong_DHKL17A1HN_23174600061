'''
Viết chương trình Python để chuyển đổi đối tượng từ điển Python (sắp xếp theo khóa) thành dữ liệu JSON. 
In các thành viên đối tượng với mức thụt lề 4.
'''
import json
python_dict = {
    "name": "Thuy Duong",
    "age": 20,
    "is_student": True,
    "courses": ["Dev M", "design", "Anything is good"],
    "address": {
        "street": "Chuong Trinh St",
        "city": "Hanoi"
    }
}

data = json.dumps(python_dict)
data_dict = json.loads(data)
print(data)
print("My name is", data_dict["name"],data_dict["age"],"tuổi")
