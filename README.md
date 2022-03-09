# 모두의 연구소 AI 해커톤

## 배드민턴 자세 Pose-estimation

+ 목표 : 라켓을 포함한 자세를 취하는 사람의 포즈를 인식

## Quick Start

```Bash
#Train
bash train-run.sh airiss-data/config/simple.yaml

# Inference
python scripts/demo_inference.py \
--cfg airiss-data/config/simple.yaml \
--checkpoint "exp/test-02-simple.yaml/final_DPG.pth" \
--showbox \
--indir data/test \
--save_img \
--outdir data/airiss/test-result

# or

sh test-run.sh

```

## Prerequisite [TBD]

1. data
2. pretrained-model
3. yolo weight

