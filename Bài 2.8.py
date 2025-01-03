'''
Viết chương trình Chuyền đổi đối tượng Python sang chuỗi JSON. In ra tất cả các giá trị
'''
import json

if __name__ == "__main__":
    #Đối tượng Python mẫu (dictionary)
    python_object = {
        "name": "Thuy Duong",
        "age": 20,
        "city": "Ha Noi",
        "is_student": False,
        "grades": [95, 89, 78]
    }

    #Chuyển đổi đối tượng Python thành chuỗi JSON và in ra
    json_string = json.dumps(python_object, indent=2)
    print("Chuỗi JSON sau khi chuyển đổi:")
    print(json_string)