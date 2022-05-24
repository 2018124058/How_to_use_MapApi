# kakao api  
- 하루 300,000 건 무료   
- 참고: https://apis.map.kakao.com/  

# API KEY 발급  
- https://developers.kakao.com/ 에서 개발자 등록, 앱 등록 - 플랫폼 웹으로 선택, 도메인 등록 (ex. http://127.0.0.1:8000)  
- JavaScript 키를 api 키로 사용한다  

# 지도 생성하기  
```
<body>
    <!--지도를 담을 영역-->
    <div id = "basic-map" style = "width:500px; height: 400px;"></div>
    <!--지도 api 불러오기-->
    <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=키 입력"></script>
    
    <!--지도를 생성해 영역에 담기-->
    <script>
        var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
        var options = { //지도를 생성할 때 필요한 기본 옵션
	    center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표-위도, 경도
	    level: 3 //지도의 레벨(확대, 축소 정도)
        };

        var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
    </script>
</body>
```  
- `new kakao.maps.Map(container, options)`로 지도 생성  
    - `container`: 지도를 담을 영역(html element)  
    - `options`  (dict 형태)
        - `center`: 반드시 필요. LatLng의 객체로 위도와 경도 값을 순서대로 주어야 한다  
            `center: new kakao.maps.LatLng(위도, 경도)`  

- 스크롤바로 지도 확대 및 축소 가능  
- 마우스로 지도 위치 이동 가능  

# 관련 라이브러리  
- `clusterer`: 지도 마킹  
- `services`: 장소 검색, 주소-좌표 변환  
- `drawing`: 지도 위에 마커와 그래픽스 객체를 쉽게 그릴 수 있음  

```
<!-- services와 clusterer, drawing 라이브러리 불러오기 -->
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=APIKEY&libraries=services,clusterer,drawing"></script>
```  

# 마커 생성  
```
// 마커 위치 지정
var markerPosition  = new kakao.maps.LatLng(33.450701, 126.570667); 
    
// 마커를 생성
var marker = new kakao.maps.Marker({
    position: markerPosition
});

// 마커가 지도 위에 표시되도록 설정
marker.setMap(map);

// 지도 위의 마커를 제거
marker.setMap(null);      
```

## 마커 여러개 생성  
```
// 마커를 표시할 위치와 title 객체 배열 
var positions = [
    {
        title: '장소1', 
        latlng: new kakao.maps.LatLng(33.450705, 126.570677)
    },
    {
        title: '장소2', 
        latlng: new kakao.maps.LatLng(33.450936, 126.569477)
    },
];

// 마커 이미지의 이미지 주소
var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; // 즐겨찾기 마커
    
for (var i = 0; i < positions.length; i ++) {
    
    // 마커 이미지의 이미지 크기
    var imageSize = new kakao.maps.Size(24, 35); 
    
    // 마커 이미지 생성    
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
    
    // 마커 생성
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
        title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시
        image : markerImage // 마커 이미지 
    });
}
```
## 마커 카테고리 나누기 
카테고리에 따라 다른 마커로 표시하기: 다른 배열에 positions를 저장하여 for문을 쓴다  
```
// 기본 마커 이미지로 표시할 때 
var normal_positions = [
    {
        title: '일반 공연1',  // title은 공연 이름으로 
        latlng: new kakao.maps.LatLng(33.450879, 126.569940)
    },
    {
        title: '일반 공연2', 
        latlng: new kakao.maps.LatLng(33.451393, 126.570738)
    },
];

for (var i = 0; i < normal_positions.length; i ++) {
    // 마커를 생성
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: normal_positions[i].latlng, // 마커를 표시할 위치
        title : normal_positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시
    });
}
```
![마킹 구분한 지도](map_marking.JPG)