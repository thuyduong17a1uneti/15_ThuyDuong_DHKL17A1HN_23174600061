import requests
#Thực hiện yêu cầu HTTP đến URL 'https://jsonplaceholder.typicode.com/posts'
response = requests.get('https://jsonplaceholder.typicode.com/posts')
#Kiểm tra xem yêu cầu thành công hay không
if response.status_code == 200:
#Nếu yêu cầu thành công, lấy dữ liệu JSON từ phản hồi
    json_data = response.json()
    print('Tổng số bài post:',len(json_data))
 #In ra màn hình thông tin các bài đăng từ dữ liệu JSON
    print('DANH SÁCH CÁC BÀI POST:')
    for post in json_data:
        print("ID bài đăng:", post['id'])
        print("Tiêu đề:", post['title'])
        print("Nội dung:", post['body'])
        print("==================================")
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)