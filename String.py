def makeAnagram(a, b):
    a = list(a)
    b = list(b)
    count = 0
    for i in a:
        if i in b:
            if a.count(i) < b.count(i):
                count += b.count(i) - a.count(i)
                while (a.count(i) != b.count(i)):
                    b.remove(i)

        else:
            count += 1

    for i in b:
        if i in a:
            if a.count(i) > b.count(i):
                count += a.count(i) - b.count(i)
                while (a.count(i) != b.count(i)):
                    a.remove(i)
        else:
            count = count + 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()