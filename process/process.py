class Maximum:
    
    def __init__(self, rout_matrix, start, end):
        self.rout_matrix = rout_matrix
        self.start = start
        self.end = end
        #sorted(matrix, key=lambda rout: rout["value"], reverse=True)


    def __get_available_routes(self, rout_lyric):
        sub_routes = []
        for rout in self.rout_matrix:
            if rout["from"] == rout_lyric and rout["value"] > 0:
                sub_routes.append(rout)

        return sub_routes

    def __delete_a_channel(self, rout_from, rout_to):
        for rout in self.rout_matrix:
            if rout["from"] == rout_from and rout["to"] == rout_to:
                self.rout_matrix.remove(rout)
    
    def __get_better_rout(self, available_routes):
        return sorted(available_routes, key=lambda rout: rout["value"], reverse=True)[0]

    def __do_rout(self):
        sub_routes = self.__get_available_routes(self.start)
        print(self.__get_better_rout(sub_routes))

    def resolve(self):
        self.__do_rout()
