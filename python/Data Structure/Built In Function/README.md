## q, r = divmod(a, b)

-   a/b = q
-   a%r = r

## b = bin(n)

-   10진수 n을 이진수 b로 변환

## a = int('0bxxx', 2)

-   2진수 xxx를 10진수로 변환

## zip(a, b, c, ...)

-   인자들은 모두 iterable이고, 개수가 동일할 때 사용 가능
-   인자들을 각각의 요소로 나눈 후 순서대로 묶어서 새로운 iterable 생성

## range()

-   range(a) : 0 부터 a-1 까지의 정수 범위를 반환
-   range(a, b) : a 부터 b-1 까지의 정수 범위를 반환
-   range(a, b, c) : c 간격으로 a 부터 b-1 까지 정수 범위를 반환

## sorted( < data > , key = < function > , reverse = < bool >)

-   이터러블한 데이터를 정렬하여 리스트의 타입으로 변환 해주는 파이썬의 내장 함수
-   새롭게 정렬된 목록을 반환 하며, 원래 목록은 영향을 받지 않음
-   stable한 정렬
-   key : 해당 함수를 기준으로 정렬
-   reverse : 기본값은 False로, True이면 역정렬

## 유니코드 관련 함수

-   ord(str) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
-   chr(number) : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 반환

## map(func, list)

-   리스트의 모든 요소를 지정된 함수로 처리
-   원본 리스트를 변경하지 않고 새 리스트를 생성
