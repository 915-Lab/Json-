import json


def read_json_file():
    """
    json파일을 읽어들여 딕셔너리 data에 데이터 저장하는 함수
    :return:
    """
    file_path = "data_json/test01.json"  # 상대경로 저장
    with open(file_path, "r") as fp:  # 경로에 해당되는 json파일 열기, 'r' -> 읽기모드, fp 객체생성
        data = json.load(fp)  # data 딕셔너리에 json 데이터 저장
    return data


def data_setting(data):
    """
     data에 있는 데이터중 점수 딕셔너리를 합하여 새로운 딕셔너리 생성함수
    @:param data:
    :return:
    """
    result = dict()
    average = 0
    for key, value in data.items():  # key -> "1","2" / value -> 점수 딕셔너리
        add = 0
        count = 0
        for key2, value2 in value.items():  # key -> "점수 기준들" / value -> 점수(int)
            add = add + value2
            if count < len(value):  # len(딕셔너리) -> 딕셔너리의 key개수 / len(value) == 9
                count = count + 1

            if count == len(value):  # 점수 기준이 9개이므로 add값을 초기화 하기위해 두번째 반복문 break
                break

        add = int(round((add / len(value)) * 20))  # 소수 첫 번째 자리에서 반올림
        result[key] = add
        average = average + add

    result_len = len(result) # 기존 딕셔너리 길이를 저장
    result["average"] = round((average / result_len),2) # 평균값을 구하는식 소수점 두 번째 자리까지 나타냄

    return result


def set_json_file(result):
    """
    파이썬 딕셔너리로 json 파일을 만드는 함수
    @:param result:
    :return:
    """
    result_file_path = "result_data_json/result_data.json"  # json 파일을 만들 경로지정
    with open(result_file_path, "w", encoding="UTF-8") as fp:  # "w" -> 쓰기 모드
        json.dump(result, fp, indent=4)  # indent=4를 이용하여 들여쓰기설정


def run():
    """
    객체생성함수
    1. Json 파일 읽기 및 데이터 딕셔너리에 저장
    2. 딕셔너리 value값 더하기 및 새로운 결과 딕셔너리 생성
    3. 파이썬 딕셔너리 데이터를 Json 파일 데이터로 전환 및 Json 파일에 저장
    :return:
    """
    read = read_json_file()
    data_set = data_setting(read)
    set_json_file(data_set)


if __name__ == "__main__":
    run()
