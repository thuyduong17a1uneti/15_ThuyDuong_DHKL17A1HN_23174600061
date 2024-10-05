import xml.dom.minidom
def main():
    doc= xml.dom.minidom.parse("H:/VD_chuong2_PY/BaiTapChuong2/2.3.xml")
    staff_tags=doc.getElementsByTagName("staff")
    for staff in staff_tags:
        staff_id=staff.getAttribute("id")
        name=staff.getElementsByTagName("name")[0].firstChild.data
        salary=staff.getElementsByTagName("salary")[0].firstChild.data
        print(f"staff ID:{staff_id},Name:{name},Salary:{salary}")

if __name__=="__main__":
    main()