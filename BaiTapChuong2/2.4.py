import xml.dom.minidom
def main():
    doc= xml.dom.minidom.parse("H:\VD_chuong2_PY\BaiTapChuong2\2.1.xml to 2.5/2.3.xml")
    print(doc.nodeName)
    print("name card of file")
    print(doc.firstChild.tagName)
    staffs = doc.getElementsByTagName("staff")
    for staff in staffs:
        staff_id = staff.getAttribute("id")
        name = staff.getElementsByTagName("name")[0].firstChild.data
        salary = staff.getElementsByTagName("salary")[0].firstChild.data
        print(f"Staff ID:{staff_id},Name:{name},Salary:{salary}")

if __name__=="__main__":
    main()