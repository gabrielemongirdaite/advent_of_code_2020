import time
card_public_key = 10705932
door_public_key = 12301431

def loop_size(public_key, subject_number):
    value = 1
    loop = 0
    while value != public_key:
        value = (value * subject_number) % 20201227
        loop += 1
    return loop


def encryption_key(loop, subject_number):
    value = 1
    for i in range(loop):
        value = (value * subject_number) % 20201227
    return value

start_time = time.time()
door_loop = loop_size(door_public_key, 7)
encryption = encryption_key(door_loop, card_public_key)

print('1st part answer: ', encryption)
print("--- %s seconds for 1st part---" % (time.time() - start_time))