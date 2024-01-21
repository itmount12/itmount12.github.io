# [파이썬] 클래스를 통해 전화번호부 구현하기

학원에서 배운 내용을 토대로 전화번호부 클래스를 생성해 보겠습니다.


**클래스란?** 
    **객체 지향 프로그래밍**의 핵심 개념 중 하나입니다. 객체 지향 프로그래밍은 현실 세계의 개체를 모델링하여 프로그램을 구성하는 시각의 하나로, 코드의 재 사용성과 유지보수 성을 향상시키는 데에 주력합니다. 

    클래스는 특정 종류의 객체를 생성하기 위한 틀이나 설계도로 생각할 수 있습니다. 이는 속성과 메서드로 구성되며, 이를 통해 객체를 생성하고 정의가 가능합니다.

이러한 객체 지향 프로그래밍의 장점:
- 코드의 모듈성:
    - 모듈성이란 코드를 작은 독립적인 부분으로 나누는 원칙을 나타냅니다. 이는 큰 문제를 해결하기 위해 작은 부분으로 나누어 해결하는 것과 관련이 있습니다.
    -객체 지향 프로그래밍에서 클래스와 객체를 사용하면 코드를 모듈화 할수 있습니다. 각 클래스는 특정 기능이나 역할을 담당하며, 이러한 클래스들을 모듈처럼 조합하여 전체 시스템을 구성할 수 있습니다.
    - 모듈성은 코드는 이해하기 쉽게 만들어주고, 특정 부분의 수정이나 개선이 필요할 때에 해당 모듈만 수정할 수 있도록 합니다.
- 유지 보수성:
    - 유지 보수성은 코드를 쉽게 이해하고 수정할 수 있는 능력을 의미합니다. 객체 지향 프로그래밍은 코드를 각각의 클래스로 나누어 정의하고 구조화 함으로써 유지 보수성을 향상시킵니다.
    - 클래스는 특정 기능을 캡슐화 하므로, 해당 기능을 수정하거나 개선할 때에 다른 부분에 영향을 미치지 않도록 해줍니다. 즉 시스템의 특정 부분을 수정할때에 전체 시스템을 이해하지 않아도 됩니다. ( 정형외과 의사는 뼈만 고치니깐 피부과에 신경쓸 필요 없고, 피부과 의사는 피부만 신경쓰니깐 뼈에 신경 쓸 필요 없다. )
- 재사용성:
    - 재사용성은 이미 작성된 코드를 다른 곳에서도 활용할 수 있는 능력을 의미합니다. 객체 지향 프로그래밍은 클래스와 객체를 통해 코드의 재사용성을 높힐 수 있습니다.
    - 클래스를 정의하고 객체를 생성하는 것은 해당 클래스가 제공하는 기능을 여러 곳에서 쉽게 사용할 수 있게 합니다. 이로써 동일 기능을 여러 부분에서 중복해 작성할 필요가 없어집니다.
    - 코드의 재 사용성은 개발 시간을 단축 시키고 버그의 발생 가능성을 줄여 줍니다.

이러한 클래스의 개념을 기반으로 어떻게 클래스를 만들지 고민해 보았습니다.

먼저, 전화번호부 라는 프로그램의 기능과 전화번호부로 생성되는 객체에 대해 생각해 봅시다.

전화번호부 프로그램으로 생성되는 객체: 전화번호부

전화번호부의 속성에 대해 생각해 봅시다: 

전화 번호부의 사전적 의미: 전화 가입자의 전화부를 성명이나 상호 주소 따위와 함께 적어 놓은 책

즉 전화 번호부는 무언가가 적히는 **저장되는**  책 이라는 속성을 가지고 있습니다.

다시 클래스로 들어가서 클래스의 속성과 메소드에 대해 알아봅시다.

1. 속성(attributes):
    - 속성: 클래스의 특징이나 데이터를 나타내는 변수 입니다. 이러한 변수들은 클래스의 상태를 나타냅니다.
    - 속성은 클래스 내부에서 정의되며, 객체가 생성될때 마다 해당 객채의 속성에 대한 메모리가 할당됩니다.
    - 보통 클래스의 속성은 초기화 메서드('\__init__\') 를 사용하여 객체가 생성될 떄 초기 값을 설정합니다.

속성은 클래스의 특징이나 데이터를 나타내는 "변수", 즉 변수라고 하였습니다. 변수를 쓰는 방법은 아는데, 변수를 정확하게 정의하는 것은 어려운 것 같습니다. 변수의 정의를 보겠습니다.

변수: 프로그램에서 데이터를 저장하고 참조하는데 이름이 붙은 **메모리 위치**입니다. 변수는 값이 변할 수 있는 가변적 데이터의 저장에 사용되며, 프로 그램의 실행 동안 여러 값들을 저장하고 조작하는 데 활용됩니다.

즉 클래스의 속성은 이런 개념입니다.

강아지: 강아지의 "이름", 강아지의 "나이", 강아지의 "귀 모양새(쫑긋쫑긋 or 축처짐), 강아지의 "크기"(소형견: 포메, 중형견: 시바견, 대형견:사모예드) etc....

강아지의 이름, 나이, 크기, 귀모양새 는 강아지 마다 다르지만 모두 강아지가 가지고 있는 속성들입니다. 

2.메서드: 메서드는 클래스의 동작이나 기능을 정의하는 함수입니다. 클래스 내부에서 정의되는 함수로, 객체의 행동을 결정합니다. 메서드는 일반적으로 객체의 속성에 접근하거나 조작하는데에 사용됩니다. 메서드를 통해 객체 간의 통신이 이루어지며, 객체의 특정 행동을 수행할 수 있습니다.

*객체를 간략히 요약하면, 데이터와 해당 데이터를 조작하는 함수를 함께 묶어 놓은 것.

앞전에서 배운 자료 구조 중 리스트, 딕셔너리 같은 것들을 생각해 봅시다.

리스트나 딕셔너리는  내부의 요소들을 저장할수 있는 속성과 기능을 가지고 있고, 여기에 값을 추가하거나 인덱싱을 통해 추출하는 .append(), .index() 와 같은 기능을 가지고 있으므로 객체라고 생각할 수 있습니다.

그렇다면 클래스를 정의하자면 ->
1. 클래스의 속성: 특성, 클래스가 가진 고유한 특성 변수
2. 클래스의 메서드: 클래스가 가진 특성을 인자로 가지는 내부 함수
3. 클래스의 객체(인스턴스):  클래스의 속성과 메서드를 가지는 객체, 혹은 클래스의 속성과 메서드로 인해 생성물. 즉 incarnation 된 클래스.

이제 다시 전화번호부를 클래스 화는 과정으로 넘어가서 적어보겠습니다.

1. 전화번호부의 속성: "이름:, 연락처. 주소, 메일 순으로 사람의 정보를 저장하는 기능을 가지고 있음

2. 전화번호부의 기능: 속성의 정보를 1.저장하고, 2.저장 정보를 보여주고,3. 저장 정보를 수정하고, 4, 저장 정보를 삭제하고...
3. 전화번호부의 객체: 개별적인 특성이 1번의 속성과 2번의 기능을 가진 실제적 객체

여기에 기능을 더 생각해 보면, 즐겨찾기를 하는 기능도 있으면 좋을 것 같고, 또 삭제한 것도 마음이 변해서 다시 복원하는 기능, 또 즐겨찾기 한 사람과 사이가 안 좋아졌을 때를 대비해 즐겨찾기를 관리하는 기능, 또 저장된 연락처를 정렬하는 기능 들이 있으면 좋을것 같습니다.

그러면 여기서 또 기능을 추가하기 위해 전화번호부의 속성을 추가하겠습니다. 휴지통의 속성, 즐겨찾기의 속성 ..  이들은 상황에 따라서 가변적인 특성을 가집니다.

그렇다면 다시 전화번호부 클래스 개요를 짜보면,
1. 클래스의 속성:
    - 메인 저장공간: 전화번호부가 저장되는 메인공간
    - 삭제 공간: 삭제한 전화번호가 있는 서브 공간 1
    - 즐겨찾기 공간: 즐겨찾기 된 번호들의 서브 공간 2
2. 클래스의 메소드(동작):
    - 입력된 전화 번호를 저장하는 기능
    - 입력된 정보를 출력하는 기능
    - 입력된 정보를 수정하는 기능
    - 입력된 정보를 검색하는 기능
    - 입력된 정보를 삭제하는 기능
    - 삭제된 정보를 복원하는 기능
    - 입력된 정보를 즐겨찾기 하는 기능
    - 즐겨찾기 된 정보를 관리하는 기능
    - 입력된 정보를 정렬기준에 따라 정렬 하는 기능
    - 입력된 정보를 외부 디렉토리에 저장하고 종료 하는 기능.
3. 클래스의 인스턴스(객체):
    - 어떤 특정한 전화 번호들을 입력 받으면, 1번의 속성과 2번의 메소드로 인해 생성되는 unique 한 데이터. 이 안에는 1번과 2번이 모두 포함 되어 있음.

### 이와 같은 형태로 구상되어집니다.

그러면 지금부터는 이 형태에 맞추어서 클래스를 정의 하겠습니다.


```python
class Phone_book:
    def __init__(self,contact=None,dust_box=None):
        self.contact=contact if contact else []
        self.dust_box=dust_box if dust_box else []
        self.favorites=[]
```

먼저 클래스의 특성들을 정의했습니다. 이 클래스에는 메인 전화부, 휴지통, 즐겨찾기를 저장하는 빈 리스트가 생성자  \__init\__ 에 의해 생성됩니다.

__init__ 는 클래스 내부에서 개별 인스턴스를 생성하고, 이를 초기화 하는 역할을 합니다. 초기화를 해야 다음에 다른 인스턴스를 생성할수 있기 때문에 초기화의 기능도 같이 수행합니다.

## 메인 인터페이스 함수 interpace()


```python
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
```

이 함수는 메인 인터페이스 메서드입니다. 사용자가 객체를 생성한 후,( book1 =Phone_book()) book1.interpace() 메서드를 통해 내부 인터페이스로 진입할 수 있습니다. 이 메서드는 먼저 사용자에게 보일 인터페이스를 프린트해 시각화 하고, 인터페이스에 보이는 각 일련 번호를 입력하면 각각의 다른 기능들을 호출하는 함수입니다. 이 함수는 0을 누르지 않는 이상 계속 반복되는 반복문의(while) 형태로 구성되어 있고, 0을 누르면  viewinR 함수를 호출하고 종료됩니다.(break) 

## 정적 메소드, 데코레이터 함수


```python
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

```

위 함수는 정적 메소드로 지정되었습니다. 정적 메소드란, 인스턴스(개별 특성치) 에 영향을 받지 않는 메소드입니다. 이 함수도 while 반복문으로 수행되고, 0을 누르면 종료가 됩니다. 이 함수가 종료가 되면, interpace() 함수가 while 문의 루프를 받고 있으므로 자동으로 interpace() 메소드로 넘어가게 됩니다. 만약에 0이 아닌 값을 입력하면, 해당하는 메소드를 호출하게 되는 형식의 데코레이터 함수로 지정되었습니다. 이 데코레이터는 interpace() 의 0번을 제외한 모든 숫자 값에 할당되어서 데코레이터로 작용하게 됩니다.

## 연락처 입력함수


```python
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
```

위의 메소드는 연락처를 입력으로 받으면 저장하는 메소드입니다. 입력으로 값들을 받고, 함수 내부의 조건식은 정규 표현식에 의거하여 올바르지 않는 입력들을 예외로 처리하고 메소드를 중단시킵니다. 이렇게 조건에 맞는 입력들은 메소드 내부에서 차원이 2인 딕셔너리로 저장되는데, 이 딕셔너리의 0번 인덱스는 이름을, 1번 인덱스는 연락처, 메일, 주소라는 세부 딕셔너리로 묶고 이 값을 value 로 받게 되어집니다. 이는 추후에 키 값으로 빠른 검색과 수정 메소드를 사용하기 위함입니다. 그리고 마지막으로 이렇게 생성된 딕셔너리는 클래스 내부 속성 리스트 contact 에 저장됩니다.  


```python
import re

class FormatError(Exception):
    def __init__(self,msg="잘못된 형식의 주소입니다."):
        self.msg=msg
        super().__init__(self.msg)
    #상속: 초기화
```

이는 추가적인 코드로 입력값이 정규표현식에 의해 의거되는 포맷과 맞지 않으면 사용자 지정 예외처리를 실행시키는 코드입니다. 클래스 "FormatError"는 모든 예외 클래스의 부모 클래스인 Exception 을 상속받으면서 정의 되었고, 내부 인스턴스를 상속받기 위해 super()를 써서 빌려왔습니다.

#  입력한 연락처 출력 함수


```python
    @page_move
    def print_all(self):
        for idx,all_p in enumerate(self.contact,1):
            print("★"*30)
            print(f"{idx}. 이름:{all_p['이름']}")
            print(f"주소:{all_p['정보']['주소']}")
            print(f"연락처:{all_p['정보']['연락처']}")
            print(f"메일:{all_p['정보']['메일']}")
```

이 메소드는 위의  mak_num 함수에서 input 으로 입력받은 전화 번호 값들을 리스트 내의 딕셔너리화 시킨 값들을 다시 출력하는 함수입니다. 전체 출력된 결과 값들을 보이기 위해 for 문을 사용하였습니다.

이때, 검색된 자료의 가독성을 확보하기 위해 ennumerate() 함수를 사용하여  for 문의 출력 결과에 인덱싱을 1번부터 부여 하였습니다. 또한 리스트 contact 안의 반복되는 객체 all_p는 데이터의 형태가 딕셔너리 이므로, key 값을 통해 내부 인덱싱이 가능하므로 간편하게 [이름], [정보] [주소] 와 같은 형태로 내부 요소를 print() 할수 있도록 하였습니다.

# 연락처 수정 메소드


```python
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
                    self.interpace()
                    break
                else:
                    print("1을 눌러주세요")
            else:
                print(f"수정하려는 이름:{search_name} 과 연락처:{mody_num}가 맞나요? 확인 부탁드립니다.")
                break
```

다음은 연락처를 수정하는 메소드 입니다. 
먼저 이 메소드는 수정할 이름과 수정할 전화번호를 입력 값으로 받습니다. 

그 후 메소드 내부 리스트 name_finder 를 정의합니다. 이 내부 리스트는 리스트 컴프리 헨션으로 내부 요소를 생성하는데, 전화부 리스트 (contact) 안의 '이름' 그리고 '정보''전화번호' 가 입력값과 같은 요소들을  리스트로 내부 요소로 만듭니다.

수정할 이름과 전화번호가 있어서 name_finder 가 생성되었다면, 이를 for 문을 통해 프린트합니다. 이는 사람이 수정할 전화번호가 맞는지 육안으로 확인하기 위한 절차입니다. (동일한 이름의 두 사람이 전화부에 있는 경우를 전제함)

이후 input 함수를 통해 이 전화번호 값을 정말 수정할지 말지를 결정하는 if  문을 작성합니다. 수정할 전화번호가 맞다면 name_finder 의 첫번째 요소를 selected_contact 라는 객체로 정의합니다. 이 객체는 self.contact 의 단일 요소이므로 딕셔터리 타입의 객체 입니다.

이후 수정할 값들을 입력으로 받고, 이를 selected_contact 의 새로운 값들로 업데이트 합니다. 

마지막으로 contact 리스트에 for 문을 enumerate 함수를 활용해 실제 contact 리스트의 값을 업데이트 합니다. contact 는 리스트이므로 내부 요소를 인덱스 번호를 통해 변경할 수 있습니다. 또한 인덱스의 번호는 중복이 없는 고유 값 이므로, seleted_contact의 이름이 같은 전화번호부가 변경되는 불상사를 막을 수 있습니다. 이후 break 문을 작성해 while 루프를 끝내고 inerpace() 메소드로 회귀합니다.

만약 확인을 한 후 수정을 원하지 않는 경우에는 0번을 눌러 interpace() 메소드를 호출하고, 0,1 이외의 값을 누르지 않은 경우에는 루프를 벗어나지 못하고 다시 시작 포인트로 회귀 하게 됩니다.  또 입력한 전화 번호과 이름이 잘못된 경우에는 f-string 으로 입력값들을 표시하고 함수를 종료합니다.

# 연락처 검색 함수


```python
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
```

다음은 연락처를 검색하는 메소드입니다. 연락처 수정 메소드와 같이 찾고자 하는 값을 입력값, 검색된 이름들의 리스트를 리스트 컴프리 헨션으로 생성하고, 이 리스트가 존재한다면 이 값들을 for 문을 통해 print해 번호를 붙여 보이도록 합니다.  이때, list name_finder 내의 객체 nf 는 데이터타입이 딕셔너리이므로, 딕셔너리 내부의 메소드 get을 통해 key 값 '정보' 를 반환하게 됩니다.  

만일 name_finder 함수가 존재하지 않으면 이를 f-스트링으로 표현하여 잘못된 입력임을 사용자에게 고지합니다.

# 리스트 삭제 메소드


```python
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

```

다음은 리스트 내의 전화번호를 삭제하는 메소드입니다.
먼저 삭제할 이름을 입력으로 받고, 삭제할 리스트를 임시로 저장할 리스트를 컴프리헨션으로 표현합니다. 
이 임시 삭제 항목 temp_list 가 존재한다면,
먼저 그 결과를 사용자에게 for 문과 enumerate 함수를 통해 print 하여 시각화합니다.

이 때도 동일한 이름의 사람이 전화번호에 여러 명 저장되어 잇는 경우를 가정하였습니다. for 문으로 시각화된 전화 번호들은 인덱스 번호를 가지게 됩니다. 
그후 real_rid 라는 문자열 객체를 생성하는데, 이 객체는 입력으로 받은 값을 정수화 후 -1 을 한 객체입니다. 이런 복잡한 과정을  수행하는 이유는, 파이선은 0부터 인덱싱을 하기 때문입니다.

temp_list.pop 에서 real_rid 의 값을 가진, 즉 real_rid 번째 값을 pop합니다. 그후 실제 contact 리스트에서는 이 값을 가진 요소를 제거하고, 이를 dust_box 에는 추가하여 휴지통으로 전화번호를 전송하게 됩니다.

# 휴지통 메소드


```python
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
```

다음은 휴지통 내부의 정보들을 복원하는 메소드입니다.
먼저, 이 메소드로 진입하면, 휴지통 내부의 값들을 for 문을 이용해 시각화 합니다. 만일 삭제한 값이 없으면, 휴지통이 비어있다는 문구를 출력하고 메소드를 종료시킵니다.

만일 휴지통이 존재하는 경우, 복원할 전화 번호를 인덱스화 한 값을 입력하는 과정으로 넘어갑니다. 입력한 값이 0이 아니고, 전체 휴지통 리스트 이하의 값을 가진 경우, (이는 인덱스 번호가 아닌 값을 입력했을 경우 오류를 발생하기 위함입니다.)  휴지통에서 해당 값을 pop 하고, 이를 다시 contact 리스트에 append 하여 복원을 시킵니다.

# 즐겨찾기, 즐겨찾기 관리 메소드


```python
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
```

위의 두개 메소드는 휴지통의 메소드와 거의 유사하여 휴지통 메소드의 2개 항목을 클래스화 하고, 이 클래스를 상속하는 방식으로 만들려 하였으나, 클래스 내부에서 클래스를 생성하고 이 클래스에 변수를 지정하는 과정에서 오류가 생겨, 거의 유사한 형태의 메소드로 제작하였습니다.

휴지통 메소드와 즐겨찾기 메소드와의 가장 큰 차이점은 즐져찾기 메소드에서는 임시적 리스트인 restored_contact 의 값이 실제 contact 함수에서 제거되지 않고, 오로지 favorites 리스트에 append 된다는 점입니다. 마찬가지로, 즐겨찾기를 해제하는 경우에도 해제된 요소를 다시 append 하지 않음으로써 전체 contact 내부의 요소에는 어떤 영향도 미치지 않도록 휴지통 메소드의 세부 사항들을 수정하였습니다.

전화번호부 정렬 메소드


```python
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
```

정렬 메소드에서는 정렬 기준을 input 으로 받게 됩니다. 
이름 기준으로 정렬을 원할때에는 n, 주소를 기준으로 원할때는 r,
역순을 원할 때에는 대문자를 입력하면 됩니다.
정렬을 할때는 sorted 함수의 두번쨰 인자값에 람다식을 써 이름, 주소, 그들의 역순으로 정렬하도록 하였습니다.

# 저장된전화 번호를 txt 파일로 저장하는 메소드


```python
 def viewinR(self,result_file="Phone_number.txt"):
        with open(result_file, "w", encoding="utf-8") as file:
            file.write("★" * 30 + "\n")
            for idx, all_p in enumerate(self.contact, 1):
                file.write(f"{idx}. 이름:{all_p['이름']}\n")
                file.write(f"주소:{all_p['정보']['주소']}\n")
                file.write(f"연락처:{all_p['정보']['연락처']}\n")
                file.write(f"메일:{all_p['정보']['메일']}\n")
                file.write("★" * 30 + "\n")
            file.write("♡"*30 +"\n")
            for idx, fav_p in enumerate(self.favorites,1):
                file.write(f"{idx}. 이름:{fav_p['이름']}\n")
                file.write(f"주소:{fav_p['정보']['주소']}\n")
                file.write(f"연락처:{fav_p['정보']['연락처']}\n")
                file.write(f"메일:{fav_p['정보']['메일']}\n")
                file.write("♡" * 30 + "\n")
```

위 메소드는 Phone_number 클래스 내부의 저장된 전화번호를 open 함수를 통해 텍스트 파일로 저장하는 메소드입니다. 
result_file = "Phone_number" 로 파일 이름을 지정하고, "w" 쓰기 모드로 지정하고 with 를 사용해  즐겨찾기와 전화번호부 내부의 요소들을 Phone_number.txt 에 직접 입력합니다. 이 viewinR은 0번을 누르면 실행되는 메소드로, Phone_number 클래스의 저장된 연락처 정보들을 txt 파일로 전환 후 break 문을 통해 interpace() 메소드의 루프를 종료시킵니다.

## 클래스를 모듈화 하기

위의 클래스를 모듈로써 호출하고 싶을때는, py. 형태로 저장합니다.


```python
import sys
import os
```

모듈의 파일의 위치를 시스템 경로에 추가합니다.
sys.path.append(**"모듈의 위치 경로"**)

이후에는 모듈을 import 함수를 통해 임포트 할수 있습니다.

추가적으로 클래스가 어떤 인스턴스를 생성했거나, 모듈안의 어떤 함수가 값을 반환했을 경우에는,

if \__name__ == '__main__':

P1= Phone_number()

을 인스턴스 위에 생성하면 스크립트가 모듈로써 사용 될때 인스턴스가 반환되지 않습니다.


```python

```
