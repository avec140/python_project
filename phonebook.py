import pprint
import json

phonebook = {
0: {'Name': 'Kim', 'Phone': '45648733'},
1: {'Name': 'Lee', 'Phone': '89376333'},
2: {'Name': 'Park', 'Phone': '36457818'},
3: {'Name': 'Chung', 'Phone': '76891234'},
4: {'Name': 'Choi', 'Phone': '67451237'}
}

while True:
    print("--------------------------")
    print("1. read")
    print("2. write")
    print("3. delete")
    print("4. exit")
    print("--------------------------")

    intro = int(input())

    if (intro == 1):           #폰북 조회하는 구간
        print("폰북 전체 목록 조회할 경우 : 1번")
        print("폰북 세부 목록 조회할 경우 : 2번")
        intro1 = int(input())
        if(intro1 == 1):
            pprint.pprint(phonebook)
        elif(intro1 == 2):
            print("검색하고 싶은 번호를 입력해주세요")
            search = int(input())
            if search in phonebook:
                contact = phonebook[search]
                print(f"이름: {contact['Name']}, 전화번호: {contact['Phone']}")
            else:
                print("해당 key값에 해당되는 연락처가 없습니다!")
    elif(intro == 2):          #폰북 정보 추가
        print("추가하고 싶은 이름과 전화번호를 입력해주세요.")
        name = input()
        number = input()
        new_index = len(phonebook)
        phonebook[new_index] = {'Name': name, 'Phone': number}
        print(f"이름: {phonebook[new_index]['Name']}, 전화번호: {phonebook[new_index]['Phone']}")

    elif(intro == 3):
        print("삭제하고 싶은 번호를 입력해주세요")
        delete_index = int(input())              #delete_index변수 : phonebook딕셔너리의 값을 삭제하고 싶은 번호 입력
        if delete_index in phonebook:
            del phonebook[delete_index]
            print(f"{delete_index}의 값이 삭제되었습니다.")
        else:
            print("삭제되지 않았습니다. 재시도해보세요!")
        #print(type(delete))

    elif(intro == 4):
        break;