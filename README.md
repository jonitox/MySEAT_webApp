# MySEAT_webAPP
>### 좌석관리플랫폼 MySeat
관객이 아닌 관리자의 입장에서 로그인하여 좌석을 마음대로 추가하여 커스터마이징할 수 있고 상영관도 추가 및 제거하며 관리할 수 있도록하는 좌석관리플랫폼을 제공하는 **WEB APPLICATION**   
   
# 개발환경
Flask (Python Web FrameWork)   
MySQL, SQLArchemy (SQL toolkit for python)   
Bootstrap (FE framework)   
Python3   

   
# 기능1 - 사용자 맞춤 상영관 관리  

서비스에 가입한 계정별로 각 계정은 로그인시 각 상영관들을 수정(상영관 추가,삭제)할수 있으며 변경사항을 저장할수 있습니다. 상영관들은 1관,2관.. 과 같은 이름을 가질수 있습니다. 각 상영관은 다시 로그인할 시 마지막으로 저장했던 배치를 불러옵니다. 각 계정의 상영관들의 데이터는 계정정보와 함께 table로 관리하게고 불러올수있게끔 mySQL과 SQLArchemy을 이용하여 구현하였습니다.      
   
# 기능2 - 상영관별 좌석 관리   

상영관별로 좌석을 추가하거나 삭제할수 있습니다. 또 좌석들을 이동시켜 원하는 형태로 배치시킬수 있습니다. 좌석들은 기본적으로 그리드에 맞춰서 배치됩니다.   
또한 좌석별로 좌석명과 같은 별도의 정보를 기재할수 있으며, 각 좌석의 색상을 변경하여 좌석의 등급 등을 나타낼수 있습니다. 각 좌석의 이동은 자바스크립트 interact.js의 오픈소스를 일부 자체 수정하여 구현하였습니다.   
   
# 기능3 - 편의를 위한 기타 기능들   
   
관리자들을 위한 편리한 몇가지 추가 기능들을 구현해놓았습니다. 첫번째로, 사용자는 모든 좌석을 한번에 삭제하여 기존의 상영관을 초기화할 수 있습니다. 두번째로, 상영관을 설정 시, 추천할만한 기본적인 몇가지 좌석 배치들을 불러와서 사용할 수 있습니다. 제공하는 좌석배치 옵션에는 2block 배치, 3block 배치, 콘서트홀 배치 등이 있습니다.  
   

# UI Images   
<img src="/ImageCuts/1.png" width="200px" height="350px" alt="1"></img>
<img src="/ImageCuts/2.png" width="200px" height="350px" alt="2"></img>
<img src="/ImageCuts/3.png" width="250px" height="200px" alt="3"></img>
<img src="/ImageCuts/4.png" width="250px" height="200px" alt="4"></img>   
