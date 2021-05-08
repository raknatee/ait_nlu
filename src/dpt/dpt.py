class Dpt:
    def __init__(self):
        super().__init__()
        self.data = []
    def add(self,id, head, deprel):
        self.data.append({"id":id,"head":head,"deprel":deprel})

    def __repr__(self)->str:
        _repr = ""
        for item in self.data:
            _repr += f"{item}\n"
        return _repr
    def __str__(self):
        return self.__repr__()
    def __hash__(self):
        return hash(self.__repr__())

class DptFull:
    def __init__(self):
        super().__init__()
        self.data = []
    def add(self,id,word,head,deprel):
        self.data.append({
            'id':id,
            'word':word,
            'head':head,
            'deprel':deprel
        })
    
    def __repr__(self)->str:
        _repr = ""
        for item in self.data:
            _repr += f"{item}\n"
        return _repr
    def __str__(self):
        return self.__repr__()
    

class DptSet:
    @classmethod
    def from_pickle(cls,obj):
        returned = cls()
        returned.data = obj.data
        returned.hash_info = obj.hash_info
        returned.duplication = obj.duplication

        return returned
    def __init__(self,duplication=False):
        self.data = []
        self.hash_info = []
        self.duplication = duplication
    def add(self,obj:Dpt):
        if(not self.duplication):
            if( obj.__hash__() not in self.hash_info):
                self.data.append(obj)
                self.hash_info.append(obj.__hash__())
        if(self.duplication):
            self.data.append(obj)
    def __str__(self):
        string = ""
        for dpt in self.data:
            string+=f"{str(dpt)}\n"
        return string
    def __len__(self):
        return len(self.data)
    def __getitem__(self,key):
        return self.data[key]
        


