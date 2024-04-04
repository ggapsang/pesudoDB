import pandas as pd
import os

class LoadData():
    # 데이터 로드 클래스 구현
    pass

class AddData():
    # 데이터 추가 함수 구현
    pass

class ViewData():
    # 데이터 조회 함수 구현
    pass

class UpdateData():
    # 데이터 업데이트 함수 구현
    pass

class DeleteData():
    # 데이터 삭제 함수 구현
    pass

class OnOffFlag() :
    # 공정별 데이터 조작 가능 여부 권한 조정
    pass

def load_menu():
    # 메뉴 파일이 위치한 경로1
    menu_file_path = 'menu.txt'
    if os.path.exists(menu_file_path):
        with open(menu_file_path, 'r', encoding='utf-8') as file:
            menu_content = file.read()
        return menu_content
    else:
        return "메뉴 파일을 찾을 수 없습니다."

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
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 아래 함수들(add_data, view_data, update_data, delete_data)은 구현이 필요합니다.

if __name__ == "__main__":
    main_menu()
