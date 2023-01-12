import os
import csv
from post import Post

# file path
file_path = "./kylevenv/Chapter12/data.csv"

# Post object save
post_list = []

# data.csv file exists
if os.path.exists(file_path):
    # 게시글 로딩
    # print("loading ...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        # Create post instance
        post = Post(int(data[0]),data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()

# 게시글 쓰기
def write_post():
    """게시글 쓰기 함수"""
    print("\n\n- 게시글 쓰기 -")
    title = input("Please input title\n>>>")
    content = input("Please input content\n>>>")
    # ID
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# Enroll a new board")

# 게시글 목록
def list_post():
    """게시글 목록 함수"""
    print("\n\n - board lists")
    id_list = []
    for post in post_list:
        print("ID :", post.get_id())
        print("TItle :", post.get_title())
        print("View :", post.get_view_count())
        print("")
        id_list.append(post.get_id())
    
    while True:
        print("Q) Please select ID. (If you want to go back to Menu, please input -1)")
        try:
            id = int(input(">>>"))
            if id in id_list:
                board_detail(id)
                break
            elif id == -1:
                break
            else:
                print("There is no ID")
        except ValueError:
            print("Please input Number value")

# 게시글 상세
def board_detail(id):
    """게시글 상세 함수"""
    print("\n\n- board detail")
    print(id)
    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            print("ID :", post.get_id())
            print("TItle :", post.get_title())
            print("Content :", post.get_content())
            print("View :", post.get_view_count())
            target_post = post

    while True:
        print("Q) Edit: 1 Delete: 2 (If you want to go back to Menu, please input -1)")
        try:
            choice = int(input(">>>"))
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
            elif id == -1:
                break
            else:
                print("There is no ID")
        except ValueError:
            print("Please input Number value")

# 게시글 저장
def save_post():
    """ 게시글 저장 함수 """
    f = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("# Successfully Saved")
    print("Close Program")

# 게시글 수정
def update_post(target_post):
    """ 게시글 수정 함수"""
    print("\n\n- Edit board")
    title = input("Input title\n>>>")
    content = input("Input content\n>>>")
    target_post.set_post(target_post.id, target_post.title, target_post.content, target_post.view_count)
    print("# Successfully Updated")

# 게시글 삭제
def delete_post(target_post):
    """ 게시글 삭제 함수"""
    post_list.remove(target_post)
    print("#Successfully Removed")

# 메뉴 출력하기
while True:
    print("\n\n- KYLE BLOG -")
    print("- Please select menu -")
    print("1. Write Board")
    print("2. Board List")
    print("3. Close Program")
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("Please press number")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            save_post()
            break