from Crypto.Hash import SHA256
import sys

def splitFileIntoBlocks(filename, block_size=1024):
    blocks = []

    f = open(filename, "rb") # opening for [r]eading as [b]inary

    block = f.read(block_size)
    while block != b"":
        blocks.append(block)
        block = f.read(1024)

    f.close()
    return blocks

def getHashOfFirstBlock(blocks):
    h = SHA256.new()
    reversed_blocks = list(reversed(blocks))
    h.update(reversed_blocks[0])
    last_hash = h.digest()

    for block in reversed_blocks[1:-1]:
        h = SHA256.new()
        h.update(block + last_hash)
        last_hash = h.digest()

    h = SHA256.new()
    h.update(reversed_blocks[-1] + last_hash)
    
    return h.hexdigest()

if __name__ == "__main__":
    filename = input('Enter file\'s name: ')

    blocks = splitFileIntoBlocks(filename)
    block_hash = getHashOfFirstBlock(blocks)

    print("Final hash value:")
    print(block_hash)