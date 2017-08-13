class TempTracker:
    '''
    @see https://www.interviewcake.com/question/python/temperature-tracker
    '''

    def __init__(self):
        '''
        initialize the counter map
        '''
        self.object_map = {}
        self.max = None
        self.min = None
        self.mean = None
        self.mode = None
        self.no_elems = 0

    def insert(self, value):
        print("Inserting %d" % value)
        if self.max:
            self.max = max(self.max, value)
        else:
            self.max = value

        if self.min:
            self.min = min(self.min, value)
        else:
            self.min = value

        if self.mean:
            self.mean = (self.mean * self.no_elems + value) / (self.no_elems + 1)
            self.no_elems += 1
        else:
            self.mean = value
            self.no_elems = 1

        if value in self.object_map:
            self.object_map[value] += 1
        else:
            self.object_map[value] = 1

        if self.mode:
            elem_cnt = self.object_map[value]
            mode_cnt = self.object_map[self.mode]
            if elem_cnt > mode_cnt:
                self.mode = value
        else:
            self.mode = value

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


def main():
    temp_tracker = TempTracker()

    temp_tracker.insert(80)
    print ("Max = %d, Min = %d, Mean = %f, Mode = %d" \
           % (temp_tracker.get_max(), temp_tracker.get_min(), \
              temp_tracker.get_mean(), temp_tracker.get_mode()))
    print ("\n-------------------------------------\n")

    temp_tracker.insert(90)
    print ("Max = %d, Min = %d, Mean = %f, Mode = %d" \
           % (temp_tracker.get_max(), temp_tracker.get_min(), \
              temp_tracker.get_mean(), temp_tracker.get_mode()))
    print ("\n-------------------------------------\n")

    temp_tracker.insert(20)
    print ("Max = %d, Min = %d, Mean = %f, Mode = %d" \
           % (temp_tracker.get_max(), temp_tracker.get_min(), \
              temp_tracker.get_mean(), temp_tracker.get_mode()))
    print ("\n-------------------------------------\n")

    temp_tracker.insert(70)
    print ("Max = %d, Min = %d, Mean = %f, Mode = %d" \
           % (temp_tracker.get_max(), temp_tracker.get_min(), \
              temp_tracker.get_mean(), temp_tracker.get_mode()))
    print ("\n-------------------------------------\n")

    temp_tracker.insert(70)
    print ("Max = %d, Min = %d, Mean = %f, Mode = %d" \
           % (temp_tracker.get_max(), temp_tracker.get_min(), \
              temp_tracker.get_mean(), temp_tracker.get_mode()))
    print ("\n-------------------------------------\n")

    temp_tracker.insert(20)
    print ("Max = %d, Min = %d, Mean = %f, Mode = %d" \
           % (temp_tracker.get_max(), temp_tracker.get_min(), \
              temp_tracker.get_mean(), temp_tracker.get_mode()))
    print ("\n-------------------------------------\n")

    temp_tracker.insert(50)
    print ("Max = %d, Min = %d, Mean = %f, Mode = %d" \
           % (temp_tracker.get_max(), temp_tracker.get_min(), \
              temp_tracker.get_mean(), temp_tracker.get_mode()))
    print ("\n-------------------------------------\n")


if __name__ == '__main__':
    main()
