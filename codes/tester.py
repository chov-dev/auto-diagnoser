import datetime
import subprocess
import configparser
import os

config = configparser.ConfigParser()

configName = "selfDiagnose"

if (os.path.isfile("자가진단설정파일(삭제 시 문제 발생).ini")):
    print("정보 저장됨. (비밀번호 변경을 위해선 프로그램이 설치된 경로에 위치한 자가진단설정파일(삭제 시 문제 발생).ini파일을 수정하거나 삭제하십시오)")


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
subprocess.call(['Python', "codes/macro_auto_self_dignose.py"])
