import requests
# Thực hiện yêu cầu HTTP đến URL ''
response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
# Kiểm tra xem yêu cầu thành công hay không
if response.status_code == 200:
# Nếu yêu cầu thành công, lấy dữ liệu JSON từ phản hồi
    json_data = response.json()
 # In ra màn hình thông tin các bài đăng từ dữ liệu JSON
    print('DANH SÁCH CÁC BÀI POST:')
    for post in json_data:
        print("   -",post['name'])
    print('DANG SÁCH THÔNG TIN CỦA MỖI BÀI POST:')
    for post in json_data:
        print("postId:", post['postId'])
        print("ID:", post['id'])
        print("Tên:", post['name'])
        print("Email:", post['email'])
        print("Nội dung:", post['body'])
        print("==================================")
        if post['id']==3:
            break
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)