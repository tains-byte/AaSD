from merge import MergeSort
from choice import Choice

def test_choice():
    test_1 = []
    test_2 = [1, 2, 23, 55, 100, 2425, 2949]
    test_3 = [24692, 22599, 21594, 20000, 10009, 10001, 9999, 2332, 23, 1]
    test_4 = [1, 249, 23, 2094, 20000, 1394]
    test_5 = list(range(10**8,10, -10))

    exp_1 = []
    exp_2 = [1, 2, 23, 55, 100, 2425, 2949]
    exp_3 = list(reversed(test_3))
    exp_4 = sorted(test_4)
    exp_5 = sorted(test_5)

    assert Choice(test_1.copy(), len(test_1)) == exp_1, "Empty list"
    assert Choice(test_2.copy(), len(test_2)) == exp_2, "Sorted list"
    assert Choice(test_3.copy(), len(test_3)) == exp_3, "Reversed list"
    assert Choice(test_4.copy(), len(test_4)) == exp_4, "Random list"
    assert Choice(test_5.copy(), len(test_5)) == exp_5, "Big data list"
    print("All tests passed")


def test_merge():
    test_1 = []
    test_2 = [1, 2, 23, 55, 100, 2425, 2949]
    test_3 = [24692, 22599, 21594, 20000, 10009, 10001, 9999, 2332, 23, 1]
    test_4 = [1, 249, 23, 2094, 20000, 1394]
    test_5 = list(range(10**8,10, -10))


    exp_1 = []
    exp_2 = [1, 2, 23, 55, 100, 2425, 2949]
    exp_3 = list(reversed(test_3))
    exp_4 = sorted(test_4)
    exp_5 = sorted(test_5)


    assert MergeSort(test_1.copy()) == exp_1, "Empty list"
    assert MergeSort(test_2.copy()) == exp_2, "Sorted list"
    assert MergeSort(test_3.copy()) == exp_3, "Reversed list"
    assert MergeSort(test_4.copy()) == exp_4, "Random list"
    assert MergeSort(test_5.copy()) == exp_5, "Big data list"
    print("All tests passed")


if __name__ == '__main__':
    
    test_choice()
    test_merge()

