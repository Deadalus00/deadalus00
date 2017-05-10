class bird(object):
     have_feather=True
     way_of_reproduction="eggs"
     def move(self, dx, dy):
        position=[0,0]
        position[0]=position[0]+dx
        position[1]=position[1]+dy
        return position

class chicken(bird):
    way_of_wove='walk'
    possible_in_kfc=True
    able_to_fly=False

class oriole(bird):
    way_of_move='fly'
    possible_in_kfc=False

summer=chicken()
print(summer.move(5,5))

class human(object):
    laugh='hahaha'
    def show_laugh(self):
        print (self.laugh)
    def laugh_100th(self):
        for i in range(100):
            self.show_laugh()
li_lei=human()
li_lei.laugh_100th()
