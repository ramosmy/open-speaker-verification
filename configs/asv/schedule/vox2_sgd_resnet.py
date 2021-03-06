# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(policy='step', step=[8, 14, 17, 20, 22])
# LRReducer = dict(interval=10000, patience=2)
total_epochs = 40
