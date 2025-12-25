def locate_card(cards, query):
     low = 0 
     high = len(cards) - 1
     l = len(cards)
     while (low <= high):
          mid = (low+high) // 2
          middle_num = cards[mid]
          if (query == middle_num):
               return mid
          elif (query < middle_num):
               low = mid + 1
          elif (query > middle_num):
               high = mid -1
     return -1
if __name__ == "__main__":
    cards = [13, 11, 10, 7, 4, 3, 1, 0]
    query = 7
    result = locate_card(cards, query)
    print(f"Card {query} is at position: {result}")
               
