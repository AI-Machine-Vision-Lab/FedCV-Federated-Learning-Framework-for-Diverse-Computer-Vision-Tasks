from ptflops import get_model_complexity_info

from model.segmentation.deeplabV3_plus import DeepLabV3_plus

model = DeepLabV3_plus(pretrained=True)

print('================================================================================')
print('DeepLab V3+, ResNet, 513x513')
print('================================================================================')
flops, params = get_model_complexity_info(model, (3, 513, 513), verbose=True)

print('{:<30}  {:<8}'.format('Computational complexity: ', flops))
print('{:<30}  {:<8}'.format('Number of parameters: ', params))

print('================================================================================')
print('DeepLab V3+, ResNet, 769x769')
print('================================================================================')
flops, params = get_model_complexity_info(model, (3, 769, 769), verbose=True)

print('{:<30}  {:<8}'.format('Computational complexity: ', flops))
print('{:<30}  {:<8}'.format('Number of parameters: ', params))
