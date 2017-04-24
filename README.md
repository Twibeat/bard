Bard
========
순환신경망(RNN - Recurrent Neural Network)을 이용한 작곡 도우미
midi파일을 입력받아서 비슷한 느낌의 곡의 midi파일을 만들어 줍니다.

### 주요 사용 패키지
keras, QT5(python3), music21


### linux
```
conda create -n keras python=3 keras qt5
pip install music21
```

### mac
```
conda create -n keras python=3 qt5
conda install -c conda-forge keras=2.0.2
conda install theano(theano를 backend로 사용한다면)
pip install music21
```

### toDO
- 원래 QT버전은 임시 데모용, Web에서 사용 가능하도록 만든다.
- core부분 리팩토링


