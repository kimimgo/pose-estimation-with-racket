# 2022-03-08 18:32:47 질문

1. yolo.pt -> weight 
    module이 없다
    torch.load() no module 'models' : 
    yolo 모델을 load하는데, 왜 torch load 에서 no model 인지?
    
    A : cgf 파일 수정 해야함. => yolov5.cfg 송부해드릴게요!.
    [Conv] => [convolutional]
    yolo s, m, l , x : m l

# model 저장 방법

arch, weight

둘다 저장할 수도 있고 : 둘을 동시에 (압축) 저장
하나만 저장할 수도 있습니다.
    둘을 나누어서 저장을 하죠.
        - weight 만 제공하면 되는경우 wieght만 : yolo
        - 그러면 arch는 어디서 가지고 옵니까?
          - file : yaml, cfg, ...
          - api : ex) torchvision, fastai, 



1. GCP killed     
    gcp instance type 확인
    inference에서 메모리가 ? 아닐듯?
    - demo_inference.py Webcam 관련 구현부 제거
    - Thread worker? GCP VM type 별 thread 제한 있음. 확인.


# GCP 부분 먼저 해결 하시고,

## 학습을 계속 할 여력이 있으신가요?

## data / model 

## data팀에서는 inference 결과에 대한 피드백을 주는 것이 좋아 보입니다.
yolo 개선이 필요한 판단 가능 하겠죠?
inference 하기전에 : (간단한) 이미지 프로세싱
모델 피드백을 줘야 합니다.

## model 팀
yolo 개선
fine-tuning (학습 데이터를 줄이는 단계입니다.)
2개 잡아서 핑퐁 2번 , 학습 2번으로 최고의 모델을 만들어 냅시다!

## (Optional) streamlit 
쉽지만, 큰효과! 
Pose estimation prototype app을 만들어서 test


# inference test 