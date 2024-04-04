import pandas as pd
import os

class LoadData():
    # 데이터 로드 클래스 구현
    pass

class AddData():
    # 데이터 추가 함수 구현
    pass

class UpdateData():
    # 데이터 업데이트 함수 구현
    pass

class DeleteData():
    # 데이터 삭제 함수 구현
    pass

class SetOnOff() :
    # 공정별 데이터 조작 가능 여부 권한 조정
    pass

class ViewProcess():
    pass

def load_menu():
    # 메뉴 파일이 위치한 경로1
    menu_f_path = 'menu.txt'
    if os.path.exists(menu_f_path):
        with open(menu_f_path, 'r', encoding='utf-8') as file:
            menu_content = file.read()
        return menu_content
    else:
        return f"e : {menu_f_path}"

def main_menu():
    menu_content = load_menu()  # 메뉴 내용 불러오기
    while True:
        print(menu_content)
        choice = input("명령어 : ")

        if choice == '1':
            add_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            break
        else:
            print("error")
            print(menu_content)

# 아래 함수들(add_data, view_data, update_data, delete_data)은 구현이 필요합니다.

if __name__ == "__main__":
    main_menu()
