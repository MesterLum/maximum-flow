import time
class Maximum:
    
    def __init__(self, rout_matrix, start, end):
        self.rout_matrix = rout_matrix
        self.start = start
        self.end = end

        self.minimums = 0

    def __rest_minimum_value(self, routs):
        rout_minimum = self.__get_rout_sorted(routs, reverse=False)
        to_rest = rout_minimum["value"]
        self.minimums = self.minimums + rout_minimum["value"]
        for rout in routs:
            # Get index of the rout to rest the minimum
            index = self.rout_matrix.index(rout) 
            
            self.rout_matrix[index]["value"] = self.rout_matrix[index]["value"] - to_rest

        # Finally we will delete the channels
        #self.__delete_channels()

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
                #print("deleted", rout)
    
    def __get_rout_sorted(self, routes, reverse=True):
        return sorted(routes, key=lambda rout: rout["value"], reverse=reverse)[0]

    def __do_rout(self, point, rout = [], before=""):
        sub_routes = self.__get_available_routes(point)
        better = self.__get_rout_sorted(sub_routes)
        rout.append(better)

        if better["to"] == before:
            return {
                "impossible": True,
                "rout": rout
            }
        if better["to"] != self.end:
            return self.__do_rout(better["to"], rout, better["from"])
        else:
            return {
                "impossible": False,
                "rout": rout
            }

    def __print_matrix(self, matrix):
        for sub_matrix in matrix:
            print(sub_matrix)   

        print("\n")
    
    def __print_rout(self, rout):
        for sub_rout in rout:
            print(sub_rout)
        
        print("\n")

    def resolve(self):
        rout = self.__do_rout(self.start, rout = [])
        self.__rest_minimum_value(rout["rout"])

        rout = self.__do_rout(self.start, rout = [])
        #self.__print_rout(rout)
        self.__rest_minimum_value(rout["rout"])

        rout = self.__do_rout(self.start, rout = [])
        #self.__print_rout(rout)
        self.__rest_minimum_value(rout["rout"])

        rout = self.__do_rout(self.start, rout = [])
        #self.__print_rout(rout)
        self.__rest_minimum_value(rout["rout"])

        rout = self.__do_rout(self.start, rout = [])
        print(rout)
        self.__print_rout(rout["rout"])
        self.__rest_minimum_value(rout["rout"])
        rout = self.__do_rout(self.start, rout = [])
        print(rout)
        self.__print_rout(rout["rout"])
        self.__rest_minimum_value(rout["rout"])


        print(self.minimums)
        self.__print_matrix(self.rout_matrix)


        
            
