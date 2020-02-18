import os
from chardet import detect
import argparse

def search_dir(dirname):
    result_list = []
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        if os.path.isdir(full_path):
            result_list.extend(search_dir(full_path))
        else:
            result_list.append(full_path)

    return result_list

def get_encoding_type(filepath):
    with open(filepath, "rb") as f: #바이너리값으로 읽음
        rawdata = f.read()

    codec = detect(rawdata)
    return codec["encoding"]

INCLUDE_EXT_LIST = ['.txt', '.smi']

parse = argparse.ArgumentParser()
parse.add_argument("-f", type = str)
parse.add_argument("-e", nargs = "+")#여러개의 경우 이렇게 하면 리스트로 넘어옴
args = parse.parse_args()


if args.f is not None:
    path = args.f
    filelists = search_dir(path)

    if args.e is not None:
         if len(args.e) > 0:
             INCLUDE_EXT_LIST  = [ e.lower() if e[0:1] == "." else ".{}".format(e.lower()) for e in args.e]
        #     for e in args.e:
        #         INCLUDE_EXT_LIST = []
        #         if e[0:1] == ".":#.txt .smi 이런식으로 쓴 경우
        #             INCLUDE_EXT_LIST.append(e)
        #         else:           #txt smi 이런식으로 쓴 경우
        #             INCLUDE_EXT_LIST.append(".", e)
    for file in filelists:
        filename, ext = os.path.splitext(file)
        tempfile = filename + "_tmp" + ext  #aaa_tmp.txt 처럼
        if ext.lower() in INCLUDE_EXT_LIST:
            encoding = get_encoding_type(file)
            if encoding.lower().find("utf") < 0:
                try:
                    with open(file, "r") as read, open(tempfile, "w", encoding="utf-8") as write:
                        write.write(read.read())
                    os.unlink(file)   #원본파일 삭제
                    os.rename(tempfile, file)#임시파일 이름을 원본파일과 같게                  
                    print("{} 파일이 저장되었습니다.".format(file))
                except:
                    pass
                finally:
                    if os.path.exists(tempfile):
                        os.unlink(tempfile) #file을 삭제하는 os 라이브러리 메소드
