
## Class: Cookie using a constructor with arguments self and color. Then it is assigining the color argument to an instance variable called color.
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

## Displaying the colors of both cookie instances
print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())
##` Changing the color of cookie_one to 'yellow'
cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color()) 
