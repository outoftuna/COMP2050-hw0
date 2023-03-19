""" File name:   dfa.py
    Author:      Ta Viet Thang
    Date:        March 18, 2023 
    Description: This file defines a function which reads in
                 a DFA described in a file and builds an appropriate datastructure.

                 There is also another function which takes this DFA and a word
                 and returns if the word is accepted by the DFA.

                 It should be implemented for Exercise 3 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""


def load_dfa(path_to_dfa_file:str)->object:
    """ This function reads the DFA in the specified file and returns a
        data structure representing it. It is up to you to choose an appropriate
        data structure. The returned DFA will be used by your accepts_word
        function. Consider using a tuple to hold the parts of your DFA, one of which
        might be a dictionary containing the edges.

        We suggest that you return a tuple containing the names of the start
        and accepting states, and a dictionary which represents the edges in
        the DFA.

        (str) -> Object
    """

    edges = dict()
    start = []
    accept = []
    with open(path_to_dfa_file) as file:
        for line in file:
            if line.startswith('initial'):
                start = line.split()[1:]
            elif line.startswith('accepting'):
                accept = line.split()[1:]
            elif line.startswith('transition'):
                content = line.split()[1:]
                if content[0] not in edges.keys():
                    edges[content[0]] = {content[2]: content[1]}
                else: 
                    edges[content[0]][content[2]] = content[1]
    return [(start, accept), edges]


def accepts_word(dfa:object, word:str) -> bool:
    """ This function takes in a DFA (that is produced by your load_dfa function)
        and then returns True if the DFA accepts the given word, and False
        otherwise.

        (Object, str) -> bool
    """

    initial = dfa[0][0]  
    current = initial[0]  
    accepting = dfa[0][1]  
    edges = dfa[1]  

    for character in word:
        try:
            if character in edges[current].keys():
                current = edges[current][character]  
            else:
                return False
        except KeyError:
            return False
    return current in accepting



def assert_test(result, expect, word):
    assert result == expect, f"expected {expect} but got {result} for word {word}"


def test_dfa1():
    print("="*10)
    print("TEST DFA 1")
    path_to_dfa = 'comp2050-hw0/exercise3_dfa/test1.dfa'
    dfa = load_dfa(path_to_dfa)
    words = ["planning", "satisfiability", "search", "reinforcement", "learning"]
    expected = [True] * len(words)
    for i in range(0, len(words)):
        result = accepts_word(dfa, words[i])
        assert_test(result, expected[i],words[i])
    print("PASS ALL TEST1.DFA")
    print("="*10)


def test_dfa2():
    print("="*10)
    print("TEST DFA 2")
    path_to_dfa = 'comp2050-hw0/exercise3_dfa/test2.dfa'
    dfa = load_dfa(path_to_dfa)
    words = ["sang","sing","song","sung"]
    expected = [True] * len(words)
    for i in range(0, len(words)):
        result = accepts_word(dfa, words[i])
        assert_test(result, expected[i],words[i])
    print("PASS ALL TEST2.DFA")
    print("="*10)


def test_dfa3():
    print("="*10)
    print("TEST DFA 3")
    path_to_dfa = 'comp2050-hw0/exercise3_dfa/test3.dfa'
    dfa = load_dfa(path_to_dfa)
    words = ["0", "01", "010", "0101", "01010", "010101", "0101010", "01010101", "010101010", "0101010101"]
    expected = [True] * len(words)
    for i in range(0, len(words)):
        result = accepts_word(dfa, words[i])
        assert_test(result, expected[i],words[i])
    print("PASS ALL TEST3.DFA")
    print("="*10)


def test_dfa4():
    print("="*10)
    print("TEST DFA 4")
    path_to_dfa = 'comp2050-hw0/exercise3_dfa/test4.dfa'
    dfa = load_dfa(path_to_dfa)
    words = ["af", "abcf", "adef", "abcbcf", "adebcf", "abcdef", "abcdebcbcf"]
    expected = [True] * len(words)
    for i in range(0, len(words)):
        result = accepts_word(dfa, words[i])
        assert_test(result, expected[i],words[i])
    print("PASS ALL TEST4.DFA")
    print("="*10)


if __name__ == "__main__":
    test_dfa1()
    test_dfa2() 
    test_dfa3()
    test_dfa4()