import sys

def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding='UTF8')
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:   # IOError: 존재하지 않는 파일 열때, OSError: 파일 저장시 파일명이나 파일경로에 문제가 있을 경우
        print(err)
    finally:
        if fh is not None:
            fh.close()
    return lines

def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w", encoding='UTF8')
        for line in lines:
            fh.write(line)
    except (EnvironmentError) as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()

def remove_blank_lines():
    if len(sys.argv) < 2:
        print("Usage: python {0} [file ...]".format(sys.argv[0]))

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)

if __name__ == "__main__":
    remove_blank_lines()
