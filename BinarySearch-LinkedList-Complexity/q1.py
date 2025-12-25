# Find position of a given number in a list of numbers arranged in decreasing order, also need to minimize the number of times we access the elements from the list
def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1
#Default way of writing a main function in Python is __name__ == "__main__"
if __name__ == "__main__":
    cards = [13, 11, 10, 7, 4, 3, 1, 0]
    query = 1
    result = locate_card(cards, query)
    print(f"Card {query} is at position: {result}")
