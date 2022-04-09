from colossalai.amp import AMP_TYPE

SEQ_LENGTH = 2048
BATCH_SIZE = 8
NUM_EPOCHS = 1
# WARMUP_EPOCHS = 1

parallel = dict(
    tensor=dict(mode="3d", size=8),
)

model = dict(
    type="palm_8b",
    # use_grad_checkpoint=True,
    # use_act_offload=False,
)

fp16 = dict(mode=AMP_TYPE.NAIVE)

clip_grad_norm = 1.0
