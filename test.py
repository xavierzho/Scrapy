import os

# for parent, _, filenames in os.walk('book-img'):
#     for filename in filenames:
#         src = os.path.join(parent, filename)
#         dst = os.path.join(parent, filename.split('-')[-1].strip('0'))
#         os.rename(src, dst)


with open('README.md', 'a') as f:
    for i in range(1, 307):
        f.write(f'![{i}](book-img/{i}.jpg)\n')
