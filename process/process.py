class Maximum:
    
    def __init__(self, rout_matrix, start, end):
        self.rout_matrix = rout_matrix
        self.start = start
        self.end = end

    def __rest_minimum_value(self, routs):
        rout_minimum = self.__get_rout_sorted(routs, reverse=False)
        for rout in routs:
            # Get index of the rout to rest the minimum
            index = self.rout_matrix.index(rout) 
            self.rout_matrix[index]["value"] = self.rout_matrix[index]["value"] - rout_minimum["value"]

        # Finally we will delete the channels
        self.__delete_channels()

    def __get_available_routes(self, rout_lyric):
        sub_routes = []
        for rout in self.rout_matrix:
            if rout["from"] == rout_lyric and rout["value"] > 0:
                sub_routes.append(rout)

        return sub_routes

    # This method will delete all methods with value 0
    def __delete_channels(self):
        for rout in self.rout_matrix:
            if rout["value"] == 0:
                self.rout_matrix.remove(rout)
                print("deleted", rout)
    
    def __get_rout_sorted(self, routes, reverse=True):
        return sorted(routes, key=lambda rout: rout["value"], reverse=reverse)[0]

    def __do_rout(self, point, rout = []):
        sub_routes = self.__get_available_routes(point)
        better = self.__get_rout_sorted(sub_routes)
        rout.append(better)
        if better["to"] != self.end:
            return self.__do_rout(better["to"], rout)
        else:
            return rout



    def resolve(self):
        first = self.__do_rout(self.start)
        #print
        self.__rest_minimum_value(first)
        for x in self.rout_matrix:
            print(x)
            
