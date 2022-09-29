## 요소 추가

-   append(value) : 요소 마지막에 추가
-   insert(index, value) : 입력한 인덱스에 요소 추가

## 요소 삭제

-   clear() : 모든 요소 삭제
-   pop(index) : 인덱스로 요소 삭제, 삭제한 요소 반환
-   remove(value) : 값으로 검색한 첫번째 요소 삭제
-   del(index1:index2) : 인덱스 또는 범위를 지정하여 요소 삭제

## < list >.sort(key = < function >, reverse = < bool >)

-   리스트에만 사용이 가능한 list 객체의 메소드
-   리스트를 자체를 정렬하고, 반환값은 None
-   stable한 정렬
-   key : 해당 함수를 기준으로 정렬
-   reverse : 기본값은 False로, True이면 역정렬
