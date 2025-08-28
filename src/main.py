# 1. 초기 사용자 목록 생성
# 초기 사용자 목록 - 딕셔너리 형태, 사용자의 정보에는 이름, 생년월일, 아이디, 비밀번호, 역할이 포함
# 역할: viewer, editor, admin
# 이름: 문자열
# 생년월일: YYYY-MM-DD 형식의 문자열
# 아이디: 문자열, 고유해야 함
# 비밀번호: 문자열, 최소 8자 이상, 대문자, 소문자, 숫자, 특수문자 포함
# 사용자 정보는 딕셔너리로 관리
users = {
    'user1': {'name': 'Alice', 'dob': '1990-01-01', 'password': 'Password1!', 'role': 'viewer'},
    'user2': {'name': 'Bob', 'dob': '1985-05-12', 'password': 'SecurePass2@', 'role': 'editor'},
    'admin': {'name': 'Charlie', 'dob': '1970-07-23', 'password': 'AdminPass3#', 'role': 'admin'}
}

# 프로그램 실행 시 전체 사용자 목록을 출력
def print_users():
    print("Current Users:")
    for user_id, info in users.items():
        print(f"ID: {user_id}, Name: {info['name']}, DOB: {info['dob']}, Role: {info['role']}")
    print()

# 2. 회원가입 기능
# 새로 사용자 추가 시 사용자로부터 정보 입력받기
# 입력된 생년월일 유효 날짜 확인
# 중복된 아이디 검사
# 비밀번호 보안조건 설정 및 유효성 검사
def is_valid_dob(dob):
    from datetime import datetime
    try:
        datetime.strptime(dob, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def is_strong_password(password):
    import re
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[\W_]', password)):
        return True
    return False

def sign_up():
    user_id = input("Enter new user ID: ")
    if user_id in users:
        print("Error: User ID already exists.")
        return
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    if not is_valid_dob(dob):
        print("Error: Invalid date of birth format.")
        return
    password = input("Enter your password: ")
    if not is_strong_password(password):
        print("Error: Password does not meet security requirements.")
        return
    role = input("Enter your role (viewer/editor/admin): ")
    if role not in ['viewer', 'editor', 'admin']:
        print("Error: Invalid role.")
        return
    users[user_id] = {'name': name, 'dob': dob, 'password': password, 'role': role}
    print("User registered successfully.")

# 3. 로그인 기능
# 사용자로부터 아이디와 비밀번호 입력받기
# 입력된 아이디가 존재하는지 확인
# 비밀번호가 일치하는지 확인
# 로그인 성공 시 환영 메시지 출력 및 역할에 따른 기능
# 로그인 실패 시 오류 메시지 출력

def login():
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")
    if user_id in users and users[user_id]['password'] == password:
        print(f"Welcome, {users[user_id]['name']}! You are logged in as {users[user_id]['role']}.")
        return user_id
    else:
        print("Error: Invalid user ID or password.")
        return None

# 4. 역할에 따른 기능 설정
# viewer: 내 정보 수정, 회원 탈퇴(본인)
def view_user_info(user_id):
    user = users[user_id]
    print(f"User Info - ID: {user_id}, Name: {user['name']}, DOB: {user['dob']}, Role: {user['role']}")

def edit_user_info(user_id):
    name = input("Enter new name (leave blank to keep current): ")
    dob = input("Enter new date of birth (YYYY-MM-DD, leave blank to keep current): ")
    password = input("Enter new password (leave blank to keep current): ")
    
    if name:
        users[user_id]['name'] = name
    if dob:
        if is_valid_dob(dob):
            users[user_id]['dob'] = dob
        else:
            print("Error: Invalid date of birth format. Keeping current DOB.")
    if password:
        if is_strong_password(password):
            users[user_id]['password'] = password
        else:
            print("Error: Password does not meet security requirements. Keeping current password.")
    
    print("User information updated.")

# editor: 모든 사용자 정보 수정, 회원 탈퇴(본인)
def edit_any_user_info():
    target_id = input("Enter the user ID to edit: ")
    if target_id in users:
        edit_user_info(target_id)
    else:
        print("Error: User ID does not exist.")
def delete_own_account(user_id):
    confirm = input("Are you sure you want to delete your account? (yes/no): ")
    if confirm.lower() == 'yes':
        del users[user_id]
        print("Your account has been deleted.")
        return True
    return False
def delete_any_account():
    target_id = input("Enter the user ID to delete: ")
    if target_id in users:
        confirm = input(f"Are you sure you want to delete the account of {target_id}? (yes/no): ")
        if confirm.lower() == 'yes':
            del users[target_id]
            print(f"Account {target_id} has been deleted.")
        else:
            print("Account deletion cancelled.")
    else:
        print("Error: User ID does not exist.")

# admin: 모든 사용자 정보 수정, 회원 탈퇴(모든 사용자)
def admin_actions(user_id):
    while True:
        action = input("Admin Actions: [1] Edit User [2] Delete User [3] Logout: ")
        if action == '1':
            edit_any_user_info()
        elif action == '2':
            delete_any_account()
        elif action == '3':
            print("Logging out from admin actions.")
            break
        else:
            print("Invalid action. Please try again.")

# 5. 사용자 정보 추가, 수정, 삭제 기능
# 실행 종료 후, 전체 사용자 목록 구조 항시 출력

# 메인 프로그램 루프
def main():
    print_users()
    while True:
        action = input("Choose an action: [1] Sign Up [2] Login [3] Exit: ")
        if action == '1':
            sign_up()
            print_users()
        elif action == '2':
            user_id = login()
            if user_id:
                role = users[user_id]['role']
                if role == 'viewer':
                    while True:
                        viewer_action = input("Viewer Actions: [1] View Info [2] Edit Info [3] Delete Account [4] Logout: ")
                        if viewer_action == '1':
                            view_user_info(user_id)
                        elif viewer_action == '2':
                            edit_user_info(user_id)
                        elif viewer_action == '3':
                            if delete_own_account(user_id):
                                break
                        elif viewer_action == '4':
                            print("Logging out.")
                            break
                        else:
                            print("Invalid action. Please try again.")
                elif role == 'editor':
                    while True:
                        editor_action = input("Editor Actions: [1] View Info [2] Edit Info [3] Delete Account [4] Logout: ")
                        if editor_action == '1':
                            view_user_info(user_id)
                        elif editor_action == '2':
                            edit_user_info(user_id)
                        elif editor_action == '3':
                            if delete_own_account(user_id):
                                break
                        elif editor_action == '4':
                            print("Logging out.")
                            break
                        else:
                            print("Invalid action. Please try again.")
                elif role == 'admin':
                    admin_actions(user_id)
        elif action == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please try again.")


if __name__ == "__main__":
    main()