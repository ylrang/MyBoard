#!/bin/sh
DATE=$(date +%Y%m%d)
# 데이터베이스 백업 압축 파일 생성
/usr/bin/mysqldump --login-path=local django_board|gzip > /home/backup/mysql_db_back_${DATE}.sql.gz
# 변경 방지를 위해 파일의 소유권을 root로 지정
chown root.root /home/backup/mysql_db_back_${DATE}.sql.gz
# root 이외의 계정은 실행만 가능. 수정 불가
chmod 755 /home/backup/mysql_db_back_${DATE}.sql.gz
# 3일 지난 파일 삭제
find /home/backup/ -ctime +3 -exec rm -f {} \;
