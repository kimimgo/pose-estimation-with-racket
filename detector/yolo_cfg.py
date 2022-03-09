from easydict import EasyDict as edict

cfg = edict()
# cfg.CONFIG = 'detector/yolo/cfg/yolov5x_new.cfg'
# cfg.WEIGHTS = 'detector/yolo/data/yolov5x_new.weights'

# cfg.CONFIG = 'detector/yolo/cfg/yolov3-spp.cfg'
# cfg.WEIGHTS = 'detector/yolo/data/yolov3-spp.weights'

# cfg.CONFIG: 'detector/yolo/cfg/yolov5.cfg'
# cfg.WEIGHTS: 'data/airiss/yolo-exp/exp3/weights/best.pt'

cfg.CONFIG = 'detector/yolo/cfg/yolov5.cfg'
cfg.WEIGHTS = 'detector/yolo/data/yolov5x.weights'
cfg.INP_DIM =  608
cfg.NMS_THRES =  0.6
cfg.CONFIDENCE = 0.1
cfg.NUM_CLASSES = 80
