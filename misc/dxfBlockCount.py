def blockCounter(file):
    with open(file, 'r', encoding="utf-8") as f:
        data = f.read()
        block_record = data.count('BLOCK_RECORD')
        blocks = data.count('BLOCK')
    return blocks-block_record

if __name__ == '__main__':
    file = 'MrP_2022_Ketteler_DXF_V.dxf'
    blocks = blockCounter(file)
    print(blocks)