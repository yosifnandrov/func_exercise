def numJewelsInStones(jewels, stones):
    final = 0
    for jewel in list(jewels):
        final += stones.count(jewel)
    return final


#print(numJewelsInStones("aA","aAAbbbb"))


def find_smaller(arr):
    final = []
    for i in range(len(arr)):
        final.append(sum(map(lambda x: x < arr[i], arr)))
    return final

#print(find_smaller([8,1,2,2,3]))


def simple_math(n):
    n = [int(el) for el in list(str(n))]
    multiply = 1
    sumarry = 0
    for num in n:
        multiply *= num
        sumarry += num
    return multiply - sumarry

#print(simple_math(234))


def restoreString(s, indices):
    combined = list(zip(s, indices))
    new_word = [""] * len(s)
    for letter, index in combined:
        new_word[index] = letter
    return ''.join(new_word)


#print(restoreString("aiohn",[3,1,4,2,0]))




def find_compressed(nums):
    final = []
    for i in range(2, len(nums)+1, 2):
        final.append([nums[i - 1]] * nums[i-2])
    final = [num for row in final for num in row]
    return final

#print(find_compressed([1,2,3,4]))


def decode(encoded,first):
    out = [first]
    for i in range(len(encoded)):
        out.append(out[i] ^ encoded[i])
    return out

#print(decode([1,2,3],1))

def target_array(index,nums):
    target = []
    new = list(zip(index,nums))
    for i,j in new:
        target.insert(j,i)

    return target

#print(target_array([0,1,2,3,4],[0,1,2,2,1]))


some_text ="HOW ARE YOU".split()


final_list = []
for i in range(len(max(some_text,key=len))):
    new_list = []
    for el in some_text:
        if i >= len(el):
            new_list.append(" ")
        else:
            new_list.append(el[i])
    final_list.append(''.join(new_list).rstrip())

#print(final_list)


