# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

class FormatError(Exception):
    def __init__(self,msg="잘못된 형식의 주소입니다."):
        self.msg=msg
        super().__init__(self.msg)
    #상속: 초기화
class Phone_book:
    def __init__(self,contact=None,dust_box=None):
        self.contact=contact if contact else []
        self.dust_box=dust_box if dust_box else []
        self.favorites=[]
    def interpace(self):
        while True:
            print("=" * 35)
            print("연락처 : ", len(self.contact), "명")
            print("=" * 35)
            print("1. 연락처 입력") #clear
            print("2. 연락처 출력") #clear
            print("3. 연락처 수정") #clear
            print("4. 연락처 삭제")
            print("5. 휴지통")
            print("6. 연락처 검색") #clear
            print("7. 즐겨찾기 등록")
            print("8. 즐겨찾기 보기")
            print("9. 정렬")
            print("0. 종료")
            menu = input("메뉴선택: ")

            if menu == '0':
                self.viewinR(result_file="Phone_number.txt")
                print("전화번호부를 사용해 주셔서 감사합니다.")
                break
            elif menu == '1':
                self.make_num()
            elif menu == '2':
                self.print_all()
            elif menu == '3':
                self.modify_contact()
            elif menu == '4':
                self.rid_number()
            elif menu == '5':
                self.dust()
            elif menu == '6':
                self.search()
            elif menu == '7':
                self.save_num()
            elif menu == '8':
                self.favor_lst()
            elif menu == '9':
                self.sort_phone()
    @staticmethod
    def page_move(method):
        def select_page(self):
            while True:
                print("<<< 이전 (0) / >>> 다음 (Enter)")
                key = input('메인화면은 0, 작업을 계속 수행하고 싶으면 아무키나 입력해 주세요')
                if key == "0":
                    print('취소. 초기 메뉴로 돌아갑니다.') #main 화면은 상시 true 이기 때문에 구태여  여기다가 써서 호출할 필요 x
                    break
                else:
                    print('선택하신 페이지로 이동합니다.')
                    method(self)
        return select_page

    @page_move  # 연락처 저장 함수: 1
    def make_num(self):
        name = input("성함:")
        while True:
            phone_number = input("전화번호:")
            if re.match(r'010-\d{4}-\d{4}$',phone_number): #참거짓을 반환하니깐
                break
            else :
                raise FormatError()
        e_mail = input("이메일:")
        while True:
            addr = input("주소:")
            if re.match(r'(\D+시|\D+도|\D+군)\s*\D*',addr):
                 break
            else:
                raise FormatError()
        data = {'이름': name, '정보': {'연락처': phone_number, '메일': e_mail, '주소': addr}}
        self.contact.append(data)
        print('설정이 저장되었습니다. 화면 선택창으로 넘어갑니다.')

    @page_move #연락처 출력
    def print_all(self):
        for idx,all_p in enumerate(self.contact,1):
            print("★"*30)
            print(f"{idx}. 이름:{all_p['이름']}")
            print(f"주소:{all_p['정보']['주소']}")
            print(f"연락처:{all_p['정보']['연락처']}")
            print(f"메일:{all_p['정보']['메일']}")
    @page_move
    def modify_contact(self): #연락처 수정 메소드
        while True:
            search_name = input("수정할 연락처의 이름을 입력하세요: ")
            mody_num = input("수정할 연락처 번호도 입력해 주세요:")

            # 이름을 기준으로 연락처 찾기
                 #저장될 변수:person | self.contact 안에 있는!| 조건: person['이름']이 동일!
            name_finder = [person for person in self.contact if person['이름'] == search_name and person['정보']['연락처']==mody_num ]

            if name_finder:
                print(f"{search_name}로 검색한 결과입니다.")
                #인덱스 번호,찾은 사람 |인덱스화 내장함수, 사람이 볼거니깐 시작지점: 1로!
                for idx, found_person in enumerate(name_finder,start= 1):
                    print(f"{idx}. 연락처:{found_person['정보']['연락처']}")
                #for 문 종료, 찾은사람이 인덱싱 되어 프린트 됨
                mod_key = input("수정을 원하시면 1 번을 눌러주세요, 메인화면으로 돌아가고 싶으시면 0번을 눌러주세요:")
                if mod_key == "1":
                    selected_contact = name_finder[0]
                    #이것 무엇인가? contact 내부의 자료구조 형태를 가진 1개 짜리 리스트
                 #검색된 인덱스 번호의 조건식 -> 0이상,
                    # 수정할 정보 입력
                    new_phone_number = input("새로운 전화번호를 입력하세요: ")
                    new_email = input("새로운 이메일을 입력하세요: ")
                    new_address = input("새로운 주소를 입력하세요: ")

                    # 정보 수정
                    selected_contact['정보']['연락처'] = new_phone_number
                    selected_contact['정보']['메일'] = new_email
                    selected_contact['정보']['주소'] = new_address
                    # 인덱스, 요소  sel.contact 내에서 이름이 일치 -> 큰 데이터 형태는 리스트 이므로 리스트의 인덱스를 통해 데이터 수정!
                    for idx, person in enumerate(self.contact):
                        if person['이름'] == selected_contact['이름']:
                            self.contact[idx] = selected_contact
                            break

                    print("연락처가 수정되었습니다.")
                    break
                elif mod_key =="0" :
                    self.print_menu()
                    break
                else:
                    print("1을 눌러주세요")
            else:
                print(f"수정하려는 이름:{search_name} 과 연락처:{mody_num}가 맞나요? 확인 부탁드립니다.")
                break
    @page_move #연락처 검색 함수 6
    def search(self):
        search = input("이름으로 검색해 주세요:")
        name_finder = [person for person in self.contact if person['이름'] == search]
        if name_finder:
            for idx, nf in enumerate(name_finder,start= 1):
                get_value= nf.get('정보')
                print(f"{idx}. 이름:{search}. 정보:{get_value}")
        else:
            print(f"{search}님은 존재하지 않습니다. 오타를 확인해 보세요")
    @page_move
    def rid_number(self):
        rid = input("삭제할 이름을 입력해 주세요:")
        temp_list = [person for person in self.contact if person['이름'] == rid]
        if temp_list:
            print(f"{rid}로 검색한 결과입니다.")
            for idx, t_list in enumerate(temp_list, 1):
                print(f"{idx}. 연락처:{t_list['정보']['연락처']}")
            real_rid = int(input("삭제할 연락처의 인덱스를 입력해 주세요:")) - 1
            del_contact = temp_list.pop(real_rid)
            self.contact.remove(del_contact)  # 빌려쓰는 변수들
            self.dust_box.append(del_contact)  # 빌려쓰는 변수들
            print("삭제되었습니다.")
        else:
            print(f"{rid}님은 존재하지 않습니다. 오타를 확인해 보세요")

    @page_move
    def dust(self):
        print("휴지통으로 이동합니다.")
        for idx, dust_p in enumerate(self.dust_box, 1):
            print(f"{idx}. 연락처:{dust_p['이름']}-{dust_p['정보']['연락처']}")
        if self.dust_box:
            selected_index = int(input("복원할 연락처의 인덱스 번호를 입력하세요: "))
            if selected_index != 0:
                if 1 <= selected_index <= len(self.dust_box):  # 빌려쓰는 변수들
                    restored_contact = self.dust_box.pop(selected_index - 1)
                    self.contact.append(restored_contact)  # 빌려쓰는 변수들
                    print("연락처가 복원되었습니다.")
                else:
                    print("존재하지 않는 인덱스입니다.")
        else:
            print("휴지통이 비어 있습니다.")
    @page_move
    def save_num(self):
        rid = input("즐겨찾기에 추가할 이름을 입력해 주세요:")
        temp_list = [person for person in self.contact if person['이름'] == rid]
        if temp_list:
            print(f"{rid}로 검색한 결과입니다.")
            for idx, t_list in enumerate(temp_list, 1):
                print(f"{idx}. 연락처:{t_list['정보']['연락처']}")
            real_rid = int(input("추가할 연락처의 인덱스를 입력해 주세요:")) - 1
            del_contact = temp_list.pop(real_rid)
            self.favorites.append(del_contact)  # favorites에 추가
            print("추가되었습니다.")
        else:
            print(f"{rid}님은 존재하지 않습니다. 오타를 확인해 보세요")

    @page_move
    def favor_lst(self):
        print("즐겨찾기로 이동합니다.")
        for idx, dust_p in enumerate(self.favorites, 1):
            print(f"{idx}. 연락처:{dust_p['이름']}-{dust_p['정보']['연락처']}")
        if self.favorites:
            selected_index = int(input("즐겨찾기를 해제할 연락처의 인덱스 번호를 입력하세요: "))
            if selected_index != 0:
                if 1 <= selected_index <= len(self.favorites):
                    restored_contact = self.favorites.pop(selected_index - 1)
                    print("즐겨찾기가 해제되었습니다.")
                else:
                    print("존재하지 않는 인덱스입니다.")
        else:
            print("즐겨찾기 목록이 비었습니다.")
    @page_move   #정렬 메소드
    def sort_phone(self):
        print("이름 기준:n, 주소 기준:r, 역순 입력을 원할 때는 대문자")
        s = input('정렬 기준을 말씀해 주세요: ')
        if s == "n":
            self.contact = sorted(self.contact, key=lambda x: x['이름'])
        elif s == "N":
            self.contact = sorted(self.contact, key=lambda x: x['이름'], reverse=True)
        elif s == "r":
            self.contact = sorted(self.contact, key=lambda x: x['정보']['주소'])
        elif s == "R":
            self.contact = sorted(self.contact, key=lambda x: x['정보']['주소'], reverse=True)
    def viewinR(self,result_file="Phone_number.txt"):
        with open(result_file, "w", encoding="utf-8") as file:
            file.write("★" * 30 + "\n")
            for idx, all_p in enumerate(self.contact, 1):
                file.write(f"{idx}. 이름:{all_p['이름']}\n")
                file.write(f"주소:{all_p['정보']['주소']}\n")
                file.write(f"연락처:{all_p['정보']['연락처']}\n")
                file.write(f"메일:{all_p['정보']['메일']}\n")
                file.write("★" * 30 + "\n")