import os
import sys
import shutil

def change_file_ext():
    if len(sys.argv) < 2:
        print("Usage: python {0} filename.old_ext 'new_ext'".format(sys.argv[0]))
        sys.exit()

    name = os.path.splitext(sys.argv[1])[0] + "." +  sys.argv[2]
    print("os.path.splitext(sys.argv[1]): ", os.path.splitext(sys.argv[1]))
    print("name: ", name)

    try:
        # shutil.copyfile(원파일명, 새파일명): 원본파일 내용을 신규파일에다 그대로 복사
        shutil.copyfile(sys.argv[1], name)
    except OSError as err:
        print(err)

if __name__ == "__main__":
    change_file_ext()