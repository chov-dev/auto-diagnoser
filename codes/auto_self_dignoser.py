import datetime
import subprocess
import configparser
import os
hourToDignose = int(input("자가진단을 할 시(오전 6시 30분인 경우 6 입력):"))
minuteToDignose = int(input("자가진단을 할 분(오전 6시 30분인 경우 30 입력):"))

spliter = "------------------------------------\n"

config = configparser.ConfigParser()

configName = "selfDiagnose"

if (os.path.isfile("자가진단설정파일(삭제 시 문제 발생).ini")):
    print(spliter+"비밀번호 저장됨. (비밀번호 변경을 위해선 프로그램이 설치된 경로에 위치한 자가진단설정파일(삭제 시 문제 발생).ini파일을 수정하거나 삭제하십시오)")

else:
    config['DEFAULT']['userName'] = input(
        "이름을 입력하십시오 (예:홍길동):")
    config['DEFAULT']['area'] = input(
        "거주지역을 입력하십시오(서울특별시/부산광역시/대구광역시/인천광역시/광주광역시/대전광역시/울산광역시/세종특별자치시/경기도/강원도/충청북도/충청남도/전라북도/전라남도/경상북도/경상남도/제주자치도):")
    config['DEFAULT']['birthDate'] = input("생년월일을 입력하십시오 (예:050101):")
    config['DEFAULT']['school'] = input(
        "학교명을 입력하십시오 (예:OO중학교):")
    config['DEFAULT']['schoolType'] = input(
        "학교 유형을 입력하십시오 (유치원/초등학교/중학교/고등학교/특수학교):")
    config['DEFAULT']['password'] = input("자가진단 비밀번호를 입력하십시오(예:1234):")
    with open('./자가진단설정파일(삭제 시 문제 발생).ini', "w") as f:
        config.write(f)

now = datetime.datetime.now()
lastDignose = datetime.datetime(
    now.year, now.month, now.day - 1, hourToDignose, minuteToDignose, 0)
while True:
    print(spliter+"자가진단 자동화 프로그램 By Chov.dev\n문의 : gungnaeng@naver.com")
    print(spliter+"자가진단 시각 대기 중 (%d시 %d분)" % (hourToDignose, minuteToDignose))
    while True:
        now = datetime.datetime.now()
        act_time = datetime.datetime(now.year, now.month, now.day,
                                     now.hour, now.minute, now.second)
        if act_time - lastDignose >= datetime.timedelta(days=1):
            subprocess.call(['Python', "codes/macro_auto_self_dignose.py"])
            lastDignose = datetime.datetime(
                now.year, now.month, now.day, hourToDignose, minuteToDignose, 0)
            print(spliter+"자가진단 완료 (시각%s)" % datetime.datetime.now())
            break
